from tensorflow.keras.callbacks import TensorBoard

#Training Settings

validation_split = 0.1 # How much of the dataset is reserved for testing # Values range from 0 to 1
batch_size = 100
epochs = 10
verbose = 1
callbacks = [TensorBoard(log_dir='./logs', histogram_freq=0, batch_size=batch_size, write_graph=True)]
random_dataset_loc=['testing/dataset/main_input.npy','testing/dataset/main_output.npy', 'testing/dataset/aux_input.npy','testing/dataset/aux_output.npy']
dataset_loc=['dataset/main_input.npy','dataset/main_output.npy', 'dataset/aux_input.npy','dataset/aux_output.npy']
random_save_dir = ('testing/models')
model_name = 'Haggis_Aero_Img_Rec.h5'
