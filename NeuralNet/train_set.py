from tensorflow.keras.callbacks import TensorBoard

#Training Settings

total_no_of_samples = 10000

validation_split = 0.1 # How much of the dataset is reserved for testing # Values range from 0 to 1
batch_size = 20
epochs = 10
verbose = 1
callbacks = [TensorBoard(log_dir='./logs', histogram_freq=0, batch_size=batch_size, write_graph=True, write_grads=True)]
random_dataset_loc= 'testing/dataset/'
dataset_loc='dataset/'
random_save_dir = ('testing/models')
save_dir = ('models')
model_name = 'Haggis_Aero_Img_Rec'


randomdata = True
New_model = True
model_load_number = 0
