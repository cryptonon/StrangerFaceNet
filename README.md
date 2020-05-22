# StrangerFaceNet
A prototype of django based web application capable of recognizing 5 characters of Netflix Original TV Show Stranger Things.

## About the Model
This web app is integrated with a simple Neural Network model that makes use of convolution layers to predict 5 characters of Netflix Original TV Show Stranger Things. This model is capable of predicting five classes/persons:

    Finn Wolfhard (Mike)
    Gaten Matarazzo (Dustin)
    Millie Bobby Brown (Eleven)
    Natalia Dyer (Nancy)
    Noah Schnapp (Will)

This model has been trained on 5024 images (~1005 images per class). These 5024 images included the images of their appearance in Stranger Things as well as their real images. Since the training images had (at least) two different distribution, model's accuracy (with about 1000 validation images) had accuracy of only 80%.

The model has been deployed to a web application using django.
