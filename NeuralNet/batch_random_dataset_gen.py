import setting as se
import numpy as np
import logging
from pprint import pprint
from tqdm import tqdm
import random
import gc
import train_set
import logging

#setup logging
logging.basicConfig(filename='testing/logs/batch_rand_gen_logs.log',level=logging.DEBUG)
logging.info('logging initialized')
#enable garbage collection
gc.enable()

#initizaling globals
total_no_of_samples = train_set.total_no_of_samples
batch_size = train_set.batch_size
no_of_batches = int(total_no_of_samples/batch_size)

main_input_shape = (batch_size,) + se.image_shape
aux_output_shape = (batch_size,) + se.aux_output_shape
aux_input_shape = (batch_size,) + se.aux_input_shape
main_output_shape = (batch_size,) + se.main_output_shape
logging.info('globals initialized')

#create a random distribution for the image data
def main_input_create(batch_no):
    main_input = np.random.randint(0,255,size=main_input_shape)
    main_input = main_input/255 #normalize dataset
    np.save('testing/dataset/main_input_{}.npy'.format(batch_no), main_input)
    return main_input

#create a random one hot array for character recognition
def aux_output_create(batch_no):
    aux_output = np.zeros(aux_output_shape, dtype='int32')
    for i in range(batch_size):
        aux_output[i][random.randrange(0,37)] = 1
    np.save('testing/dataset/aux_output_{}.npy'.format(batch_no), aux_output)
    return aux_output

#create randomized height data
def aux_input_create(batch_no):
    aux_input = np.random.randint(0, 10000, size=aux_input_shape)
    #normalize height data
    aux_input = aux_input/100
    np.save('testing/dataset/aux_input_{}.npy'.format(batch_no), aux_input)
    return aux_input

#create random target rel coords data
def main_output_create(batch_no):
    main_output = np.random.randint(-300,300,size=main_output_shape)
    #normalize target data
    main_output = main_output/10
    np.save('testing/dataset/main_output_{}.npy'.format(batch_no), main_output)
    return main_output

if __name__ == '__main__':
    try:
        for batch_no in tqdm(range(no_of_batches)):
            #running through dataset generation functions
            main_input_create(batch_no)
            main_output_create(batch_no)
            aux_input_create(batch_no)
            aux_output_create(batch_no)
            logging.info('pass {} complete. starting garbage collection'.format(batch_no))
            gc.collect()
        logging.info('program complete')
        pprint('execution complete')
    except Exception as e:
        logging.debug(e)
