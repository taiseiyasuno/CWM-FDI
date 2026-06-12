import numpy as np
from matplotlib import pyplot as plt
import time
import cv2

# number of filters, KH, KW.
kernel_params = [1, 3, 3] 

# padding, stride
hyperparams= [0, 1]

# FOR IMAGE READS
img = cv2.imread("images/mra19k5tpxhe1.jpeg")

# Resize (comment out if needed)
img = cv2.resize(img, None,fx=0.5, fy=0.5)
in_h, in_w = img.shape[:2]
input = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

num_channels = 3 # this applies to both input and kernel
input_params = [in_h, in_w] # manually adjust (replace variables with numbers) if needed. (N) HW (C) convention is used.
kernel_params = [1,3,3]

# keep in mind that np is row major.
# kernel size (). A convolutional filter will shrink the original dimensions: (H - (filter_size - 1), W - (filter_size - 1))


def convolve(input_params, kernel_params, num_channels, hyperparams):
    filters = kernel_params[1]

    k_h = kernel_params[1]
    k_w = kernel_params[2]
    # kernel = np.zeros(k_h, k_w)

    # comment this out when done testing the kernel
    #kernel_2d = (1/16) * np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]]) # Gaussian blur test
    kernel_2d = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]) # vertical edge detection

    kernel = np.repeat(kernel_2d[:,:,np.newaxis], num_channels, axis=2)

    output = np.zeros((in_h - k_h + 1, in_w - k_w + 1))

    # how many operations are being done in the naive implementation?
    operations = filters * num_channels * np.shape(output)[0] * np.shape(output)[1] * k_h * k_w
    print(f"Number of multiplication + addition operations: {operations}")
    
    time1 = time.perf_counter()
    # naive implementation (without cache utilisation)
    for ff in range(filters): 
        for ch in range(num_channels): 
            for hh in range(np.shape(output)[0]):
                for ww in range(np.shape(output)[1]): 
                    for k_hh in range(k_h):
                        for k_ww in range(k_w): 
                            # the code below doesn't account for multiple filters
                            output[hh, ww] += input[hh + k_hh, ww + k_ww, ch] * kernel[k_hh, k_ww, ch]
    time2 = time.perf_counter()
    return output, (time2 - time1)

# Generate random input (comment out if needed)
# input = np.random.randint(255, size=(in_h, in_w, num_channels))

print(f"Image H: {in_h}, image W: {in_w}")

output, time_taken = convolve(input_params, kernel_params, num_channels,hyperparams)
print(f"Time taken: {time_taken} s")
fig, (ax1, ax2) = plt.subplots(1,2)
ax1.imshow(input)
ax2.imshow(output, cmap=plt.get_cmap('gray'))
plt.show()