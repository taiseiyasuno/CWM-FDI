import numpy as np
# from matplotlib import pyplot as plt
import sys
import math
import cv2
# for only one CNN layer.


# k is kernel size (k x k), s is stride along both axes (s = s_h = s_w)
def do_conv(size, num_channels, k, padding, s):
    # Image set
    # for windows 
    # img = cv2.imread("assignment6/images/Bodleian_Library.jpg")
    # for linux
    img = cv2.imread("images/Bodleian_Library.jpg")

    # Resize (comment out if needed)
    img = cv2.resize(img, (size, size))
    img_h, img_w = img.shape[:2]

    # Channels
    if num_channels == 3: 
        #COLOUR
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif num_channels == 1:
        #GREYSCALE
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        raise ValueError('number of channels must be 3 or 1')
    
    # PADDING CONTROL. 
    # Padding is DEPENDENT on the kernel parameter, in accordance with usual practice, but can be set manually. 
    # p counts the rows on both top and bottom / columns on left and right. 
    if padding == 1:
        p = k - 1 
    else:
        p = 0
        input = img
    
    if num_channels == 3:
        input = np.pad(img, ((math.ceil(p/2), math.floor(p/2)),(math.ceil(p/2),math.floor(p/2)),(0,0)),mode="constant",constant_values=0)
    else:
        input = np.pad(img, ((math.ceil(p/2), math.floor(p/2)),(math.ceil(p/2),math.floor(p/2))),mode="constant",constant_values=0)
    
    in_h = img_h + p
    in_w = img_w + p
    
    # just ascending integers
    kernel = np.arange(0, k * k).reshape(k,k)
    if num_channels == 3:
        kernel = np.repeat(kernel[:,:,np.newaxis], num_channels, axis=2)
    
    output = np.zeros((int((in_h - k + s)/s), int((in_w - k + s)/s)))
    
    if num_channels == 3:
        for ch in range(num_channels):
            kernel_ch = kernel[:, :, ch]
            input_ch = input[:, :, ch]
            for hh in range(np.shape(output)[0]):
                hh_s = hh * s
                for ww in range(np.shape(output)[1]): 
                    ww_s = ww * s
                    running_total = 0
                    for k_hh in range(k):
                        for k_ww in range(k): 
                            running_total += input_ch[hh_s + k_hh, ww_s + k_ww] * kernel_ch[k_hh, k_ww]
                    output[hh, ww] = running_total
    else:
        for hh in range(np.shape(output)[0]):
            hh_s = hh * s
            for ww in range(np.shape(output)[1]): 
                ww_s = ww * s
                running_total = 0
                for k_hh in range(k):
                    for k_ww in range(k): 
                        running_total += input[hh_s + k_hh, ww_s + k_ww] * kernel[k_hh, k_ww]
                output[hh, ww] = running_total
    


if __name__ == "__main__":
    # size, num_channels, k, padding, s: replace everything apart from independent variable (argv[1]) with default values
    do_conv(200, 3 , 3, int(sys.argv[1]), 1)
