import setting as se
import numpy as np
import logging
from pprint import pprint
from tqdm import tqdm

no_of_samples = 10000


main_input_shape = se.image_shape + (no_of_samples,)
aux_output_shape = se.aux_input_shape + (no_of_samples,)
aux_input_shape = se.aux_input_shape + (no_of_samples,)
main_output_shape = se.main_output_shape + (no_of_samples,)


#create a random distribution for the image data
main_input = np.random.random(main_input_shape)
