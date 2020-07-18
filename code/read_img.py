import dippykit as dip
import numpy as np

path = '../medical_data/mp4_probe_overlayed/extracted_frames/vid1/img0001.jpg'
im = dip.imread(path)

print(im.shape)