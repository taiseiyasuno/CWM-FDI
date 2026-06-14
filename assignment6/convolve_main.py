import numpy as np
# from matplotlib import pyplot as plt
import sys
import time
import math
import cv2
# for only one CNN layer.

# for windows 
# img = cv2.imread("assignment6/images/Bodleian_Library.jpg")

# for linux
img = cv2.imread("images/Bodleian_Library.jpg")

def do_conv(img, size):
    # Resize (comment out if needed)
    img = cv2.resize(img, (size, size))

    img_h, img_w = img.shape[:2]

    # COLOUR
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # GREYSCALE
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ### SET PARAMETERS
    num_channels = 3 # this applies to both input and kernel. Set to 3 if colour, set to 1 if greyscale. 

    # kernel_params = [k_h, k_w]. A convolutional filter will shrink the original dimensions: (H - (k_h - 1), W - (k_w) - 1)). 
    kernel_params = [3 , 3] 

    # hyperparams = [padding_h, padding_w, stride]
    # Padding is DEPENDENT on the kernel parameter, in accordance with usual practice, but can be set manually. 
    # p_h and p_w count the rows on both top and bottom / columns on left and right. 

    # PADDING CONTROL. manually set p_h and p_w below to 0 if we want to turn off padding or set it manually.
    p_h = kernel_params[0] - 1 
    p_w = kernel_params[1] - 1

    # STRIDE CONTROL. usually, s_h = s_w. 
    s_h = 1
    s_w = 1
    hyperparams = [p_h, p_w, s_h, s_w] 

    # padding the input
    input = np.pad(img, ((math.ceil(p_h/2), math.floor(p_h/2)),(math.ceil(p_h/2),math.floor(p_h/2)),(0,0)),mode="constant",constant_values=0)

    in_h = img_h + p_h
    in_w = img_w + p_w

    input_params = [in_h, in_w] # manually adjust (replace variables with numbers) if needed. (N) HW (C) convention is used.
    # keep in mind that np is row major.

    def convolve_naive1(input_params, kernel_params, num_channels, hyperparams):
        in_h = input_params[0]
        in_w = input_params[1]

        k_h = kernel_params[0]
        k_w = kernel_params[1]

        s_h = hyperparams[2]
        s_w = hyperparams[3]
        # kernel = np.zeros(k_h, k_w)

        # comment this out when done testing the kernel
        #kernel_2d = (1/16) * np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]]) # Gaussian blur test
        kernel_2d = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]) # vertical edge detection

        kernel = np.repeat(kernel_2d[:,:,np.newaxis], num_channels, axis=2)

        output = np.zeros((int((in_h - k_h + s_h)/s_h), int((in_w - k_w + s_w)/s_w)))
        
        time1 = time.perf_counter()

        # naive implementation (without cache utilisation)
        for ch in range(num_channels): 
            for hh in range(np.shape(output)[0]):
                for ww in range(np.shape(output)[1]): 
                    for k_hh in range(k_h):
                        for k_ww in range(k_w): 
                            output[hh, ww] += input[hh * s_h + k_hh, ww * s_w + k_ww, ch] * kernel[k_hh, k_ww, ch]
        
        time2 = time.perf_counter()
        time_diff = time2 - time1
        return output, time_diff

    def convolve_naive2(input_params, kernel_params, num_channels, hyperparams):
        in_h = input_params[0]
        in_w = input_params[1]

        k_h = kernel_params[0]
        k_w = kernel_params[1]

        s_h = hyperparams[2]
        s_w = hyperparams[3]
        # kernel = np.zeros(k_h, k_w)

        # comment this out when done testing the kernel
        #kernel_2d = (1/16) * np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]]) # Gaussian blur test
        kernel_2d = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]) # vertical edge detection

        kernel = np.repeat(kernel_2d[:,:,np.newaxis], num_channels, axis=2)

        output = np.zeros((int((in_h - k_h + s_h)/s_h), int((in_w - k_w + s_w)/s_w)))
        
        time1 = time.perf_counter()

        # naive implementation (with some cache utilisation)
        # kernel is usually small, so should be put in the cache, and shouldn't be indexed every time. 

        for ch in range(num_channels): 
            for hh in range(np.shape(output)[0]):
                hh_s = hh * s_h
                for ww in range(np.shape(output)[1]): 
                    ww_s = ww * s_w
                    running_total = 0
                    for k_hh in range(k_h):
                        for k_ww in range(k_w): 
                            running_total += input[hh_s + k_hh, ww_s + k_ww, ch] * kernel[k_hh, k_ww, ch]
                    output[hh, ww] = running_total
        
        time2 = time.perf_counter()
        time_diff = time2 - time1
        return output, time_diff

    def convolve_naive3(input_params, kernel_params, num_channels, hyperparams):
        in_h = input_params[0]
        in_w = input_params[1]

        k_h = kernel_params[0]
        k_w = kernel_params[1]

        s_h = hyperparams[2]
        s_w = hyperparams[3]
        # kernel = np.zeros(k_h, k_w)

        # comment this out when done testing the kernel
        #kernel_2d = (1/16) * np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]]) # Gaussian blur test
        kernel_2d = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]) # vertical edge detection

        kernel = np.repeat(kernel_2d[:,:,np.newaxis], num_channels, axis=2)

        output = np.zeros((int((in_h - k_h + s_h)/s_h), int((in_w - k_w + s_w)/s_w)))
        
        time1 = time.perf_counter()

        # naive implementation (with some cache utilisation)
        # kernel is usually small, so should be put in the cache, and shouldn't be indexed every time. 

        for ch in range(num_channels): 
            kernel_ch = kernel[:, :, ch]
            input_ch = input[:, :, ch]
            for hh in range(np.shape(output)[0]):
                hh_s = hh * s_h
                for ww in range(np.shape(output)[1]): 
                    ww_s = ww * s_w
                    running_total = 0
                    for k_hh in range(k_h):
                        for k_ww in range(k_w): 
                            running_total += input_ch[hh_s + k_hh, ww_s + k_ww] * kernel_ch[k_hh, k_ww]
                    output[hh, ww] = running_total
        
        time2 = time.perf_counter()
        time_diff = time2 - time1
        return output, time_diff

    # Generate random input (comment out if needed)
    # input = np.random.randint(255, size=(in_h, in_w, num_channels))

    # print(f"Image H: {in_h}, image W: {in_w}")
    output, time_taken = convolve_naive3(input_params, kernel_params, num_channels,hyperparams)

    # how many operations are being done?
    operations = num_channels * np.shape(output)[0] * np.shape(output)[1] * kernel_params[0] * kernel_params[1]
    # print(f"Number of loops needed: {operations}")

    # print(f"Total time taken: {time_taken} s")
    # print(f"Time taken per loop: {(time_taken / operations)*1000000} microseconds")
    # fig, (ax1, ax2) = plt.subplots(1,2)
    # ax1.imshow(input)
    # ax1.title.set_text("Original input")
    # ax2.imshow(output, cmap=plt.get_cmap('gray'))
    # ax2.title.set_text("Convolved output")
    # plt.show()
    return operations, time_taken

# for single repeated trials
repeats = 20
times = np.zeros(repeats)
for i in range(repeats):
    operations, time_taken = do_conv(img, 200)
    times[i] = time_taken
print(f"Number of loops needed: {operations}")
median_times = np.median(times)
min_times = np.min(times)
print(f"Median time taken: {median_times} s")
print(f"Minimum time taken: {min_times} s")
print(f"Median time taken per loop: {median_times/operations} s")
print(f"Time taken per loop, using minimum: {min_times/operations} s")
