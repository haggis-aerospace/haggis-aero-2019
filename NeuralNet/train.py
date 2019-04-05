import os
#os.environ["CUDA_VISIBLE_DEVICES"]="-1"
from tensorflow import keras
import setting
from tqdm import tqdm
import numpy as np
import Miscfunc
import subprocess
import train_set
import gc
from keras.preprocessing.image import ImageDataGenerator
gc.enable()


def load_trainingdata(work_dir, number):
    main_input = np.load(work_dir+'main_input_{}.npy'.format(number))
    main_output = np.load(work_dir+'main_output_{}.npy'.format(number))
    aux_input = np.load(work_dir+'aux_input_{}.npy'.format(number))
    aux_output =  np.load(work_dir+'aux_output_{}.npy'.format(number))
    return main_input, aux_input, main_output, aux_output

def model_save(dir, batch_no):
    if not os.path.isdir(dir):
        os.makedirs(dir)
    model_path = os.path.join(dir, train_set.model_name + '_batch_no_{}'.format(batch_no) + '.h5')
    model.model.save(model_path)
    print('Saved trained model at %s ' % model_path)


if train_set.randomdata:
    work_dir = train_set.random_dataset_loc
else:
    work_dir = train_set.dataset_loc

if train_set.New_model:
    print('Starting Fresh!')
    import model
    print('Model graph loaded')

else:
    print('Loading model: ',train_set.model_name, train_set.model_load_number)
    model_path = os.path.join(dir, train_set.model_name + '_batch_no_{}'.format(train_set.model_load_number) + '.h5')
    model = load_model(model_path)

total_no_of_samples = train_set.total_no_of_samples
batch_size = train_set.batch_size
no_of_batches = int(total_no_of_samples/batch_size)



if __name__ == '__main__':
    try:
        for batch_no in range(no_of_batches):
            #load training data
            main_input, aux_input, main_output, aux_output = load_trainingdata(work_dir, batch_no)

            #Shuffle dataset
            main_input, aux_input, main_output, aux_output = Miscfunc.shuffle(main_input, aux_input, main_output, aux_output)

            val_main_input = main_input[:int(len(main_input)*train_set.validation_split)]
            val_aux_input = aux_input[:int(len(main_input)*train_set.validation_split)]
            val_main_output = main_output[:int(len(main_input)*train_set.validation_split)]
            val_aux_output = aux_output[:int(len(main_input)*train_set.validation_split)]

            train_main_input = main_input[int(len(main_input)*train_set.validation_split):]
            train_aux_input = aux_input[int(len(main_input)*train_set.validation_split):]
            train_main_output = main_output[int(len(main_input)*train_set.validation_split):]
            train_aux_output = aux_output[int(len(main_input)*train_set.validation_split):]
            model.model.fit([train_main_input, train_aux_input], [train_aux_output, train_main_output],
                      batch_size=train_set.batch_size,
                      epochs=train_set.epochs,
                      validation_data=([val_main_input,val_aux_input], [val_aux_output,val_main_output]),
                      shuffle=False,
                      callbacks=train_set.callbacks)
            model_save('testing/models', batch_no)

# Score trained model.
        scores = model.model.evaluate([val_main_input,val_aux_input], [val_aux_output,val_main_output], verbose=1)
        print('Test loss:', scores[0])
        print('Test accuracy:', scores[1])

    except Exception as e:
        logging.debug(e)
