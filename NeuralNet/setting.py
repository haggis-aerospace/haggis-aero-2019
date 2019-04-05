from tensorflow.keras import optimizers

image_shape = (3,720,960) # image size !! might need to fix shape
aux_output_shape = (37,) # alpha-numeric entries + null in one-hot-array
aux_input_shape=(1,)
main_output_shape=(2,)
#tower settings
#tower 1
#no of units
tower1unitsl1=960
tower1unitsl2=480
tower1unitsl3=140
#activation
tower1activationl1='relu'
tower1activationl2='relu'
tower1activationl3='relu'
#dropout percentage
dropoutpercentagetower1=0.3

#tower 2
#no of units
tower2unitsl1=960
tower2unitsl2=480
tower2unitsl3=140
#activation
tower2activationl1='relu'
tower2activationl2='relu'
tower2activationl3='relu'
#dropout percentage
dropoutpercentagetower2=0.5

#tower 3
#no of units
tower3unitsl1=1024
tower3unitsl2=512
tower3unitsl3=140
#activation
tower3activationl1='relu'
tower3activationl2='relu'
tower3activationl3='relu'
#dropout percentage
dropoutpercentagetower3=0.5

#Inception Height Convergence layer
#units
InceptionHeightConvergencenoofunits=140
#Activation
InceptionHeightConvergenceactivation='relu'

#Post Inception Dense Block
#no of units
Denselayer1noofunits=32
Denselayer2noofunits=32
Denselayer3noofunits=32
Denselayer4noofunits=32
#Activation
Denselayer1activation='relu'
Denselayer2activation='relu'
Denselayer3activation='relu'
Denselayer4activation='relu'


#dropout percentage
dropoutpercentagelayer1 = 0.4 ## Dropout percentage in the Post Inception Block's layer 1 in model.py
dropoutpercentagelayer2 = 0.4 ## Dropout percentage in the Post Inception Block's layer 2 in model.py
dropoutpercentagelayer3 = 0.4 ## Dropout percentage in the Post Inception Block's layer 3 in model.py
dropoutpercentagelayer4 = 0.4 ## Dropout percentage in the Post Inception Block's layer 4 in model.py



alpha = 1.2 ## Rel_coords_out_act layer's activation function parameter in model.py

#optimizer parameters

learning_rate = 0.01
beta_1 = 0.9
beta_2 = 0.999
epsilon = None
decay = 0.0001
amsgrad = True
#optimizer=optimizers.Adam(lr=learning_rate, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, decay=decay, amsgrad=amsgrad) ## optimizer for model in model.py

sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
