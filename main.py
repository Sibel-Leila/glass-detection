# importing PIL 
from PIL import Image 
import cv2
# importing system calls
import sys

def edge_detection(matrix):
	kernel = [[1, 0, -1], [0, 0, 0], [-1, 0, 1]]
	print(kernel)
	print(matrix[0,0])
	print(matrix[0,1])




print(sys.argv[0]);

# # Read the color image 
# img = Image.open(sys.argv[1])

# # # transform the color image to matrix and returns a tuple of (R, G, B) for that pixel
# # rgb = img.load()
# # print rgb[0, 0]

# # # how to get the 
# # r = rgb[0,0][0]
# # g = rgb[0,0][1]
# # b = rgb[0,0][2]
# # print(str(r) + " " + str(g) + " " + str(b))

# # RGB 2 GRAY and conver to matrix
# gray = img.convert('L').load()
# print gray[0,0]
# print gray[0,1]

img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge_detection(gray)