from keras import optimizers


camera_index = 0
image_shape = (480, 640, 3)
alpha = 1.2 ## Rel_coords_out_act layer's activation function parameter in model.py
dropoutpercentagelayer1 = 0.4 ## Dropout percentage in the Post Inception Block's layer 1 in model.py
dropoutpercentagelayer2 = 0.4 ## Dropout percentage in the Post Inception Block's layer 2 in model.py
dropoutpercentagelayer3 = 0.4 ## Dropout percentage in the Post Inception Block's layer 3 in model.py
dropoutpercentagelayer4 = 0.4 ## Dropout percentage in the Post Inception Block's layer 4 in model.py



#optimizer parameters

learning_rate = 0.01
beta_1 = 0.9
beta_2 = 0.999
epsilon = None
decay = 0.0001
amsgrad = False
optimizer=optimizers.Adam(lr=learning_rate, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, decay=decay, amsgrad=amsgrad) ## optimizer for model in model.py
