from tensorflow import keras
import setting
from tqdm import tqdm
import numpy as np
import os
import Miscfunc
import subprocess

def load_random_trainingdata():
    main_input = np.load('testing/dataset/main_input.npy')
    main_output = np.load('testing/dataset/main_output.npy')
    aux_input = np.load('testing/dataset/aux_input.npy')
    aux_output =  np.load('testing/dataset/aux_output.npy')
    return main_input, aux_input, main_output, aux_output

def load_trainingdata():
    main_input = np.load('dataset/main_input.npy')
    main_output = np.load('dataset/main_output.npy')
    aux_input = np.load('dataset/aux_input.npy')
    aux_output =  np.load('dataset/aux_output.npy')
    return main_input, aux_input, main_output, aux_output

#check is training data exists
if os.path.isfile('dataset/main_input.npy'):
    #load training data
    main_input, aux_input, main_output, aux_output = load_trainingdata()
elif os.path.isfile('testing/dataset/main_input.npy'):
    #load random training data
    main_input, aux_input, main_output, aux_output = load_random_trainingdata()
else:
    subprocess.call(['python3', 'random_dataset_gen.py'])
    #load random training data
    main_input, aux_input, main_output, aux_output = load_random_trainingdata()

#Shuffle dataset
main_input, aux_input, main_output, aux_output = Miscfunc.shuffle(main_input, aux_input, main_output, aux_output)


#main training Process
## TODO write code to check if a NN save exists and load it in.


#import the computation graph into the training session
## TODO write code to not import the computation graph in the event of contuining a training session
import model
