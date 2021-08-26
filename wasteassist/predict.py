import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import models
import matplotlib.pyplot as plt
import numpy as np
from wasteassist.params import *
from google.cloud import storage
import os

# class Model():
def initialise_model():
    resnet = tensorflow.keras.applications.resnet_v2.ResNet152V2(
        include_top=False, weights='imagenet', input_shape=(256, 256, 3))
    resnet.trainable = False
    inputs = tensorflow.keras.Input(shape=(256, 256, 3))
    # We make sure that the base_model is running in inference mode here,
    # by passing `training=False`. This is important for fine-tuning, as you will
    # learn in a few paragraphs.
    x = resnet(inputs, training=False)
    # Convert features of shape `base_model.output_shape[1:]` to vectors
    x = tensorflow.keras.layers.GlobalAveragePooling2D()(x)
    outputs = tensorflow.keras.layers.Dense(7, activation='softmax')(x)
    model = tensorflow.keras.Model(inputs, outputs)
    return model

def download_model(model="resnet", bucket=BUCKET_NAME):
    client = storage.Client().bucket(bucket)
    if model == 'resnet':
        subdir = 'resnet_checkpoint'
        storage_location = 'models/{}/{}'.format(model,subdir)
        command = f"gsutil -m cp -r gs://{bucket}/{storage_location} ."
        os.system(command)
        return subdir
    else:
        pass #for other models
        # subdir = ''
        # blob = client.blob(storage_location)
        # blob.download_to_filename('model.joblib')
        # print("=> pipeline downloaded from storage")
        # model = joblib.load('model.joblib')
        # return model

def compile_model(model):
    '''return a compiled model suited for the task'''

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics='accuracy')
    return model

def predict(img, model):
    classes = {'cardboard': 0,
                'compost': 1,
                'glass': 2,
                'metal': 3,
                'paper': 4,
                'plastic': 5,
                'trash': 6}
    classes = dict((v, k) for k, v in classes.items())
    test = tensorflow.keras.preprocessing.image.smart_resize(
        img, (256,256), interpolation='bilinear'
    )
    # test = tensorflow.keras.preprocessing.image.load_img(
    #     img_path, grayscale=False, color_mode="rgb", target_size=(256,256), interpolation="nearest"
    # )
    # test_arr = tensorflow.keras.preprocessing.image.img_to_array(test)
    test_arr = test * 1./255
    test_arr = np.array([test_arr])  # Convert single image to a batch.
    # predictions = model.predict(input_arr)
    result = model.predict(test_arr)
    class_ = np.argmax(result)
    pred = classes[class_]
    return pred

def build_model():
    CHECKPOINT_PATH = download_model(bucket=BUCKET_NAME)
    resnet = initialise_model()
    resnet = compile_model(resnet)
    resnet.load_weights(CHECKPOINT_PATH)
    return resnet

if __name__ == '__main__':
    CHECKPOINT_PATH = download_model(bucket=BUCKET_NAME)
    resnet = initialise_model()
    resnet = compile_model(resnet)
    resnet.load_weights(CHECKPOINT_PATH)
    # prediction = predict(img_path)
