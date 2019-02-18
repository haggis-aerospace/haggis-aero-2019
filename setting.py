from keras import optimizers


camera_index = 0
image_shape = (3280, 2464, 3) # image size

#tower settings
#tower 1
#no of units
tower1unitsl1=2048
tower1unitsl2=1024
tower1unitsl3=512
#activation
tower1activationl1='relu'
tower1activationl2='relu'
tower1activationl3='relu'
#dropout percentage
dropoutpercentagetower1=0.3

#tower 2
#no of units
tower2unitsl1=2048
tower2unitsl2=1024
tower2unitsl3=512
#activation
tower2activationl1='relu'
tower2activationl2='relu'
tower2activationl3='relu'
#dropout percentage
dropoutpercentagetower2=0.5


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
