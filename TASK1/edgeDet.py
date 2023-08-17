import cv2
import numpy as np

image = cv2.imread("Duck.jpeg")

denoised_image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

denoised_image_gray=cv2.cvtColor(denoised_image,cv2.COLOR_BGR2GRAY)

#Getting The edges using Canny Edge Detection
edges=cv2.Canny(denoised_image,32,40)

edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_32F)

#Enhancing Details Using Sobel Convolution Mask
sobel=cv2.Sobel(denoised_image_gray,cv2.CV_32FC1,1,1,3)
sobel=cv2.bilateralFilter(sobel,d=3,sigmaColor=75,sigmaSpace=75)

#Adding Both Images with alpha value 0.64
alpha=0.64
superimposed_image = cv2.addWeighted(sobel, 1 -alpha,edges, alpha, 0)

#Modifying the output for saving the file
superimposed_image = np.clip(superimposed_image * 255, 0, 255) # proper [0..255] range
superimposed_image = superimposed_image.astype(np.uint8)  # safe conversion


#Original Image
cv2.imshow("image",image)

#Sketched Image
cv2.imshow("FINAL",superimposed_image)

#Saving the cool duck Image to machine
cv2.imwrite("Sketched_Thug.png",superimposed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
