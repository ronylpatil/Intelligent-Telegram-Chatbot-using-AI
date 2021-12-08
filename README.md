# Intelligent Telegram Chatbot using AI

##### Profile Visits : 
![Visitors](https://visitor-badge.glitch.me/badge?page_id=ronylpatil.Intelligent-Telegram-Chatbot-using-AI&left_color=lightgrey&right_color=yellow&left_text=visitors) 

<p align="center">
  <img class="center" src ="https://d2vrvpw63099lz.cloudfront.net/introducing-corona-chatbot/header.png" alt="Drawing" style="width: 1300px; height: 400px">
</p>

<b>Description : </b>Built an Intelligent Telegram Chatbot using AI to detect Covid-19 from X-ray pictures. Internally __Deep Hybrid Learning Technique__ is being used to detect Covid-19 from MRI's or CT Scan Images. In this project, I have combined best of the both world's, one is traditional Machine Learning and another is Deep Learning to create a solution that works amazingly well especially when we have a limited training dataset. Here I used __VGG16 Pre-trained Network__ for extracting useful features of image dataset and finally used __XGBOOST__ for classifying the images.

 Actually XGBoost is optimized version of gradient boosting and it is a much evolved version of random forest, actually XGBoost optimize speed 
                       and possibly accuracy. Suppose we don't have millions or thousands of images that required for deep learning then I found 
                       that the accuracy that I got with tens of images with __XGBoost__ is far superior to what we would get with deep learning. 
                       So anytime if we work with limited data, always think about XGBoost as first option and if it doesn't work great then of 
                       course try deep learning. I am sure that sometime deep learning will not be enough if we have limited data. We can also 
                       engineer our own feature extractor but here I'm going to use __VGG16 pretrained architecture__ which make it easy for us to extract these 
                       features without defining alot of code.
                       
At the end these fusion trained 
                       on __1000 MRI's or CT scans__ images __(500 each COVID-19 & NORMAL)__ and finally achieved __98.32% accuracy__ and it took only __21.89 seconds__ to 
                       train this model. This fusion learning __reduce the training time__ of our model, in general deep larning
                       it usually takes a lot of time for training a model, but this hybrid technique reduced the training
                       time and at the same time gave __very good accuracy.__
Finally integrate trained model with __Telegram Bot-Pie.__

<b>Dataset Source : https://www.kaggle.com/fusicfenta/chest-xray-for-covid19-detection</b>

<b>Folder Structure : </b>
```
                    X-ray       --> main folder
                      ----| train      
                          ----| COVID-19
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                              ----| img4.jpg
                          ----| NORMAL
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                              ----| img4.jpg

                      ----| test
                          ----| COVID-19
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                              ----| img4.jpg
                          ----| NORMAL
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                              ----| img4.jpg 
```

<b>Network Architecture : </b>
<p align="center">
  <img class="center" src ="/main/vgg.png" alt="Drawing" style="width: 900px; height: 500px">
</p>

<b>Confusion Matrix : </b>
<p align="center">
  <img class="center" src ="/main/confusion matrix.png" alt="Drawing" style="width: 500px; height: 400px">
</p>

<b>Classification Report : </b>
<p align="center">
  <img class="center" src ="/main/classification report.png" alt="Drawing" style="width: 400px; height: 170px">
</p>

<b>Sample Output : </b>

https://user-images.githubusercontent.com/63307564/145012220-780c329f-2d0c-411e-a592-af0bea269792.mp4

<!-- ![Made with love in India](https://madewithlove.now.sh/in?heart=true&template=for-the-badge) -->
<br>

© 2021 Ronil Patil<br>
[![Website](https://img.shields.io/badge/Made%20with-%E2%9D%A4-important?style=for-the-badge&url=https://www.linkedin.com/in/ronylpatil/)](https://www.linkedin.com/in/ronylpatil/)
