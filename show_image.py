import nibabel as nib
import numpy as np
import os
from PIL import Image
import copy


def get_the_3_slice(volume, volume_name, output_path):
    im1 = Image.fromarray(np.uint8(t1[:,:,256//2] * 255) , 'L') # axial
    im2 = Image.fromarray(np.uint8(t1[:,192//2 - 5,:] * 255) , 'L') # cordial
    im3 = Image.fromarray(np.uint8(t1[144//2,:,:] * 255) , 'L') # sag

    im1.save(os.path(output_path, volume_name + '_axial.png'))
    im1.save(os.path(output_path, volume_name + '_cord.png'))
    im1.save(os.path(output_path, volume_name + '_sag.png'))

def get_vis_label(label):
    label_view = copy.deepcopy(label)
    label_view[label_view[0]==1] = 250
    label_view[label_view[1]==1] = 10
    label_view[label_view[2]==1] = 150
    label_view[label_view[3]==1] = 0
    return label_view


if __name__=='__main__':
    pred_path = ""
    pred = nib.load(pred_path)

    pred_data = pred.get_data()

    t1 = np.load('s9t1.npy')
    t2 = np.load('s9t2.npy')
    label = np.load('s9label.npy')


    print()