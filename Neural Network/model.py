from tensorflow import keras as keras
from keras.layers import Input, Conv2D, Dense, Dropout, Activation, Flatten, MaxPooling2D, concatenate, ELU
from keras.models import Model
import setting
from keras import optimizers

from keras.utils import plot_model



Image_input = Input(shape=setting.image_shape, dtype='float32', name='main_input')

## Inception Block Start

tower_1 = Conv2D(setting.tower1unitsl1, (1, 1), padding='same', activation=setting.tower1activationl1)(Image_input)
tower_3 = MaxPooling2D((3, 3), strides=(1, 1), padding='same')(tower_1)
tower_1 = Conv2D(setting.tower1unitsl2, (3, 3), padding='same', activation=setting.tower1activationl2)(tower_1)
tower_1 = Dropout(setting.dropoutpercentagetower1)(tower_1)
tower_1 = Conv2D(setting.tower1unitsl3, (2, 2), padding='same', activation=setting.tower1activationl3)(tower_1)

tower_2 = Conv2D(setting.tower2unitsl1, (7, 7), padding='same', activation=setting.tower2activationl1)(Image_input)
tower_2 = Dropout(setting.dropoutpercentagetower1)(tower_2)
tower_2 = Conv2D(setting.tower2unitsl2, (5, 5), padding='same', activation=setting.tower2activationl2)(tower_2)
tower_2 = Conv2D(setting.tower2unitsl3, (2, 2), padding='same', activation=setting.tower2activationl3)(tower_2)

tower_3 = MaxPooling2D((3, 3), strides=(1, 1), padding='same')(Image_input)
tower_3 = Conv2D(setting.tower3unitsl1, (1, 1), padding='same', activation=setting.tower3activationl1)(tower_3)
tower_3 = Dropout(setting.dropoutpercentagetower3)(tower_3)
tower_3 = Conv2D(setting.tower3unitsl2, (1, 1), padding='same', activation=setting.tower3activationl2)(tower_3)
tower_3 = Conv2D(setting.tower3unitsl3, (1, 1), padding='same', activation=setting.tower3activationl3)(tower_3)

Inception_output = concatenate([tower_1, tower_2, tower_3], axis=1)
Flattened_Inception_output = Flatten()(Inception_output)

## Inception Block End
##Convergergence Layer Definination
InceptionHeightConvergence = Dense(setting.InceptionHeightConvergencenoofunits, activation=setting.InceptionHeightConvergenceactivation)(Flattened_Inception_output)

## Aux Out Layer
Image_output = Dense(1, activation='softplus', name='Image_output')(InceptionHeightConvergence)

##Height Input Layer Definination
Height_input = Input(shape=setting.aux_input_shape, name='aux_input')
Height_Dense = Dense(setting.InceptionHeightConvergencenoofunits, activation = setting.Denselayer1activation)(Height_input)

##Convergergence Definination
InceptionHeightConverged = concatenate([InceptionHeightConvergence, Height_Dense])

## Post Inception Dense Block Start
InceptionHeightDenseLayer1 = Dense(setting.Denselayer1noofunits ,activation = setting.Denselayer1activation)(InceptionHeightConverged)
InceptionHeightDenseLayer1 = Dropout(setting.dropoutpercentagelayer1)(InceptionHeightDenseLayer1)

InceptionHeightDenseLayer2 = Dense(setting.Denselayer2noofunits ,activation = setting.Denselayer2activation)(InceptionHeightDenseLayer1)
InceptionHeightDenseLayer2 = Dropout(setting.dropoutpercentagelayer2)(InceptionHeightDenseLayer2)

InceptionHeightDenseLayer3 = Dense(setting.Denselayer3noofunits ,activation = setting.Denselayer3activation)(InceptionHeightDenseLayer2)
InceptionHeightDenseLayer3 = Dropout(setting.dropoutpercentagelayer3)(InceptionHeightDenseLayer3)

InceptionHeightDenseLayer4 = Dense(setting.Denselayer4noofunits ,activation = setting.Denselayer4activation)(InceptionHeightDenseLayer3)
InceptionHeightDenseLayer4 = Dropout(setting.dropoutpercentagelayer4)(InceptionHeightDenseLayer4)
## Post Inception Dense Block End

Rel_coords_out = Dense(2, name='main_output')(InceptionHeightDenseLayer4)
Rel_coords_out_act = ELU(alpha=setting.alpha)(Rel_coords_out) ## ELU is a advanced activation function. Documented in keras.io


model = Model(inputs=[Image_input, Height_input], outputs=[Image_output, Rel_coords_out_act])

sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(optimizer=sgd, loss='binary_crossentropy',
              loss_weights=[1., 0.2])

plot_model(model, to_file='model.png')
