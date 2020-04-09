#Homework 8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.interpolate import interp2d
#mathworks 2d spline interpolation (For matlab)
batman = mpimg.imread('batman.jpg')
n_rows = batman.shape[0]
n_cols = batman.shape[1]
def upscale(image, resize_y, resize_x):
    resizedImg = np.zeros(shape=(resize_x, resize_y, 3))

    for i in range(3): #red, green, blue
        currentImg = image[...,i]
        x = np.linspace(0, 1, currentImg.shape[1])
        y = np.linspace(0, 1, currentImg.shape[0])
        X, Y = np.meshgrid(x, y)
        Z = currentImg

        x2 = np.linspace(0, 1, resizedImg.shape[1])
        y2 = np.linspace(0, 1, resizedImg.shape[0])
        f = interp2d(x, y, Z, kind='cubic')
        Z2 = f(x2, y2)
        Z2 = Z2-np.min(Z2)
        Z2 = Z2/np.max(Z2)
        resizedImg[...,i] = Z2

    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(batman)

    X2, Y2 = np.meshgrid(x2, y2)
    ax[1].imshow(resizedImg)


upscale(batman, 2472, 1540)
plt.show()
upscale(batman, 154, 96)
plt.show()
upscale(batman, 618, 500)
plt.show()