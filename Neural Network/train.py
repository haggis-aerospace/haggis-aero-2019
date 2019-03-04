import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
from tensorflow import keras
import setting
from tqdm import tqdm
import numpy as np
import Miscfunc
import subprocess
import train_set
import gc
from keras.preprocessing.image import ImageDataGenerator


def load_random_trainingdata():
    main_input = np.load(train_set.random_dataset_loc[0])
    main_output = np.load(train_set.random_dataset_loc[1])
    aux_input = np.load(train_set.random_dataset_loc[2])
    aux_output =  np.load(train_set.random_dataset_loc[3])
    return main_input, aux_input, main_output, aux_output

def load_trainingdata():
    main_input = np.load(train_set.dataset_loc[0])
    main_output = np.load(train_set.dataset_loc[1])
    aux_input = np.load(train_set.dataset_loc[2])
    aux_output =  np.load(train_set.dataset_loc[3])
    return main_input, aux_input, main_output, aux_output

#check is training data exists
if os.path.isfile(train_set.dataset_loc[0]):
    #load training data
    main_input, aux_input, main_output, aux_output = load_trainingdata()
elif os.path.isfile(train_set.random_dataset_loc[0]):
    #load random training data
    main_input, aux_input, main_output, aux_output = load_random_trainingdata()
else:
    subprocess.call(['python3', 'random_dataset_gen.py'])
    #load random training data
    main_input, aux_input, main_output, aux_output = load_random_trainingdata()

#Shuffle dataset
main_input, aux_input, main_output, aux_output = Miscfunc.shuffle(main_input, aux_input, main_output, aux_output)

#normalize image data
for _ in tqdm(range(len(main_input))):
    main_input[_].astype('float32')
    main_input[_] = main_input[_] / 255

#Split the data into training set and validation set
val_main_input = main_input[:int(len(main_input)*train_set.validation_split)]
val_aux_input = aux_input[:int(len(main_input)*train_set.validation_split)]
val_main_output = main_output[:int(len(main_input)*train_set.validation_split)]
val_aux_output = aux_output[:int(len(main_input)*train_set.validation_split)]

train_main_input = main_input[int(len(main_input)*train_set.validation_split):]
train_aux_input = aux_input[int(len(main_input)*train_set.validation_split):]
train_main_output = main_output[int(len(main_input)*train_set.validation_split):]
train_aux_output = aux_output[int(len(main_input)*train_set.validation_split):]



#main training Process
## TODO write code to check if a NN save exists and load it in.


#import the computation graph into the training session
## TODO write code to not import the computation graph in the event of contuining a training session
import model

model.model.fit([train_main_input, train_aux_input], [train_aux_output, train_main_output],
          batch_size=train_set.batch_size,
          epochs=train_set.epochs,
          validation_data=([val_main_input,val_aux_input], [val_aux_output,val_main_output]),
          shuffle=False,
          callbacks=train_set.callbacks)

# Save model and weights
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)
model_path = os.path.join(train_set.random_save_dir, train_set.model_name)
model.model.save(model_path)
print('Saved trained model at %s ' % model_path)

# Score trained model.
scores = model.model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])
