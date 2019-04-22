
import numpy as np
from tqdm import tqdm
import time


#custom shuffle method for dataset
def shuffle(mx, ax, my, ay):
    print('Begining Shuffle Process')
    shuffler = range(len(mx)) # I can't come up with a better variable name
    shuffler = np.asarray(shuffler, dtype='int32')
    smx = []
    sax = []
    smy = []
    say = []
    np.random.shuffle(shuffler)
    for _ in tqdm(range(len(shuffler))):
        i = shuffler[_]
        smx.append(mx[i])
        sax.append(ax[i])
        smy.append(my[i])
        say.append(ay[i])
    print('Shuffle Process complete.')
    print('Returning to root Program')
    return smx, sax, smy, say
