# name of bot : pie

from telegram.ext import *
import numpy as np
import tensorflow.keras as keras
import joblib
from tensorflow.keras.applications.vgg16 import VGG16
import os
from PIL import Image

TOKEN = os.getenv('Token')

label = {0 : 'COVID-19', 1 : 'NORMAL'}

model = joblib.load('xray.pkl')
vggmodel = VGG16(weights = 'imagenet', include_top = False, input_shape = (256, 256, 3))
for i in vggmodel.layers:
    i.trainable = False

def about(update, context) :
    # chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    # last_name = update.message.chat.last_name
    # username = update.message.chat.username
    update.message.reply_text("""
    Hi {}🙂, I'm Pie🤖 - an AI Bot.\nMy boss trained me to detect COVID-19 from CT Scan pictures. Internally my boss has used Deep Hybrid Network to train me😏. You can test my capabilities by uploading CT Scan picture.\n\nFeel free to connect with my boss😊\nLinkedin : {}\nGithub : {}""".format(first_name, r'https://www.linkedin.com/in/ronylpatil', r'https://github.com/ronylpatil'))

def handle_message(update, context) :
    first_name = update.message.chat.first_name
    update.message.reply_text('Hey {}🙂, I\'m Pie🤖 - an AI Bot.\nHope you\'re doing well. My job is to detect Covid-19 by CT-scan. You can upload CT scan picture and detect whether a patient has COVID-19 or not.'.format(first_name))

def handle_photo(update, context) :
    image_file = context.bot.getFile(update.message.photo[-1].file_id)
    image_file.download("image.jpg")
    update.message.reply_text('Model is being loaded!')
    # model = joblib.load(r'E:\DHL Project\CNN Projects\Deep Hybrid Learning Projects\X-ray\xray.pkl')
    # model = joblib.load('xray.pkl')
    # vggmodel = VGG16(weights = 'imagenet', include_top = False, input_shape = (256, 256, 3))
    # for i in vggmodel.layers:
    #     i.trainable = False

    image = Image.open('image.jpg').convert('L')   # convert to grey scale image, mandatory step(vvimp step)
    test_image = image.resize((256, 256))
    test_image = keras.preprocessing.image.img_to_array(test_image)
    test_image = np.concatenate((test_image,) * 3, axis = -1)
    test_image /= 255.0
    test_image = np.expand_dims(test_image, axis=0)
    feature_extractor = vggmodel.predict(test_image)
    features = feature_extractor.reshape(feature_extractor.shape[0], -1)
    update.message.reply_text('You\'re almost there!')
    prediction = model.predict(features)[0]
    final = label[prediction]
    if final == 'COVID-19' :
        update.message.reply_text("""
        I'm sorry to inform you that based on my prediction you're COVID Positive😔. Please consult a doctor as soon as possible.\n\nGet well soon and, wish you a speedy recovery.\n\n🔺Stopping the spread starts with you🔺
✔Wear a mask.
✔Clean your hands.
✔Maintain a safe distance.
✔Get vaccinated.
        """)
    else :
        update.message.reply_text("""
        There is no need to worry. Your're normal but if symptoms appear, consult a doctor as soon as possible.\n\n🔺Stopping the spread starts with you🔺
✔Wear a mask.
✔Clean your hands.
✔Maintain a safe distance.
✔Get vaccinated.
        """)

def help(update, context) :
    update.message.reply_text("""Basic Commands :
/about - About Pie🤖
/linkedin - Linkedin handle of Owner.
/github - Github handle of Owner.""")

def linkedin(update, context) :
    update.message.reply_text('LinkedIn : {}.\nDon\'t forget to follow😁'.format(r'https://www.linkedin.com/in/ronylpatil'))

def github(update, context) :
    update.message.reply_text('Github : {}.\nDon\'t forget to follow😁'.format(r'https://github.com/ronylpatil'))

updater = Updater(TOKEN, use_context = True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('github', github))
dp.add_handler(CommandHandler('linkedin', linkedin))
dp.add_handler(CommandHandler('about', about))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(MessageHandler(Filters.text, handle_message))
dp.add_handler(MessageHandler(Filters.photo, handle_photo))
updater.start_polling()
updater.idle()
