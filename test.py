#%%
import scipy.io as sio
import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd
import Make_gif
FILE =sio.loadmat(r"/Users/wangyuning/Desktop/Data-driven Methods in Engineering Mechanics/SM2001_Project/Data generator (Moehlis Model)/moehlis_data_10.mat")
DATA  = FILE["data"]
a_ = DATA[0,:,:].astype("float32")
#%%
import Visualize_fields 
Visualize_fields.visualize_fields(a_,410,510)


# %%
Make_gif.Draw_gif(410,510)
# %%
