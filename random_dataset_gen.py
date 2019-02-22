import setting as se
import numpy as np
import logging
from pprint import pprint
from tqdm import tqdm
import random

no_of_samples = 1200


main_input_shape = (no_of_samples,) + se.image_shape
aux_output_shape = (no_of_samples,) + se.aux_output_shape
aux_input_shape = (no_of_samples,) + se.aux_input_shape
main_output_shape = (no_of_samples,) + se.main_output_shape


#create a random distribution for the image data
main_input = np.random.randint(0,255,size=main_input_shape, dtype='int32')


#create a random one hot array for character recognition
aux_output = np.zeros(aux_output_shape, dtype='int32')
for i in range(no_of_samples):
    aux_output[i][0][random.randrange(0,37)] = 1

#create randomized height data
aux_input = np.random.randint(0, 10000, size=aux_input_shape)
#normalize height data
aux_input = aux_input/100

#create random target rel coords data
main_output = np.random.randint(-300,300,size=main_output_shape)
#normalize target data
main_output = main_output/10

np.save('testing/dataset/main_output.npy', main_output)
np.save('testing/dataset/main_input.npy', main_input)
np.save('testing/dataset/aux_input.npy', aux_input)
np.save('testing/dataset/aux_output.npy', aux_output)
