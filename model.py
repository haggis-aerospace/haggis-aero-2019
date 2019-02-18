from keras.layers import Input, Conv2D, Dense, Dropout, Activation, Flatten, MaxPooling2D, concatenate, ELU
from keras.models import Model
import setting


Image_input = Input(shape=setting.image_shape, dtype='float32', name='main_input')

## Inception Block Start

tower_1 = Conv2D(2048, (1, 1), padding='same', activation='relu')(Image_input)
tower_1 = Conv2D(1024, (3, 3), padding='same', activation='relu')(tower_1)

tower_2 = Conv2D(2048, (1, 1), padding='same', activation='relu')(Image_input)
tower_2 = Conv2D(1024, (5, 5), padding='same', activation='relu')(tower_2)

tower_3 = MaxPooling2D((3, 3), strides=(1, 1), padding='same')(Image_input)
tower_3 = Conv2D(1024, (1, 1), padding='same', activation='relu')(tower_3)

Inception_output = concatenate([tower_1, tower_2, tower_3], axis=1)
Flattened_Inception_output = Flatten()(Inception_output)

## Inception Block End
##Convergergence Layer Definination
InceptionHeightConvergence = Dense(512, activation='relu')(Flattened_Inception_output)

## Aux Out Layer
Image_output = Dense(8, activation='softplus', name='Image_output')(InceptionHeightConvergence)

##Height Input Layer Definination
Height_input = Input(shape=(1,), name='aux_input')

##Convergergence Definination
InceptionHeightConverged = concatenate([InceptionHeightConvergence, Height_input])

## Post Inception Dense Block Start
InceptionHeightDenseLayer1 = Dense(32 ,activation = 'relu')(InceptionHeightConverged)
InceptionHeightDenseLayer1 = Dropout(setting.dropoutpercentagelayer1)(InceptionHeightDenseLayer1)

InceptionHeightDenseLayer2 = Dense(32 ,activation = 'relu')(InceptionHeightDenseLayer1)
InceptionHeightDenseLayer2 = Dropout(setting.dropoutpercentagelayer2)(InceptionHeightDenseLayer2)

InceptionHeightDenseLayer3 = Dense(32 ,activation = 'relu')(InceptionHeightDenseLayer2)
InceptionHeightDenseLayer3 = Dropout(setting.dropoutpercentagelayer3)(InceptionHeightDenseLayer3)

InceptionHeightDenseLayer4 = Dense(32 ,activation = 'relu')(InceptionHeightDenseLayer3)
InceptionHeightDenseLayer4 = Dropout(setting.dropoutpercentagelayer4)(InceptionHeightDenseLayer4)
## Post Inception Dense Block End

Rel_coords_out = Dense(2, name='main_output')(InceptionHeightDenseLayer4)
Rel_coords_out_act = ELU(alpha=setting.alpha)(Rel_coords_out) ## ELU is a advanced activation function. Documented in keras.io


model = Model(inputs=[Image_input, Height_input], outputs=[Image_output, Rel_coords_out_act])


model.compile(optimizer=setting.optimizer, loss='binary_crossentropy',
              loss_weights=[1., 0.2])
