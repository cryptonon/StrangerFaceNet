from django.shortcuts import render
# from django.shortcuts import redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import csrf_protect
import base64
from PIL import Image
from io import BytesIO
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import json


def index(request):
    return render(request, 'classify/index.html')


@login_required
def home(request):
    return render(request, 'classify/home.html')


@login_required
def about(request):
    return render(request, 'classify/about.html')


@login_required
@csrf_exempt
def predict(request):
    if request.method == "POST" and request.FILES:
        file_object = request.FILES['filePath']
        messages.success(request, 'Classification Completed!')
        # print('Something Happened! REDIRECTING!', type(file_object))

        encoded = base64.b64encode(file_object.read())
        decoded = base64.b64decode(encoded)
        image = Image.open(BytesIO(decoded))
        image_np = np.array(image)
        resized = cv2.resize(image_np, (224, 224))
        normalized = resized / 255.0
        input_image = normalized.reshape(1, 224, 224, 3)
        # print(image_np.shape)
        # print(input_image.shape)

        model_graph = tf.compat.v1.Graph()
        with model_graph.as_default():
            tf_session = tf.compat.v1.Session()
            with tf_session.as_default():
                model = load_model('models/StrangerFaceNet_5024_100.h5')
                prediction = model.predict(input_image)
                idx = prediction.argmax(axis=1)[0]
                prob = (max(prediction[0])*100).round(3)

        with open('models/classes.json', 'r') as f:
            classes = f.read()

        classes = json.loads(classes)

        person = (classes[str(idx)])[1]

        # print(prediction, idx, prob, person)

        context = {'person': person, 'confidence': prob}
        return render(request, 'classify/home.html', context)
    else:
        return render(request, 'classify/home.html')
