#!/usr/bin/env python3

import tensorflow as tf
import infsetting as se
import logging
import gc
import os


#setup logging
logging.basicConfig(filename='testing/logs/inference.log',level=logging.DEBUG)
logging.info('logging initialized')
#enable garbage collection
gc.enable()
logging.info('garbage collection initialized')

model = tf.keras.models.load_model(se.modelloc)

def model_predict(input_vector):
    logging.info('received input vector :')
    output_vector = model.predict(input_vector)
    return output_vector
