# importing PIL 
from PIL import Image 
import cv2
import sys
import numpy

def edge_detection(matrix):
	# kernel used is:
	# kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

	n, m = gray.shape

	print(m)
	print(n)

	edge = numpy.zeros((n, m))

	for i in range(0, n):
		for j in range(0, m):
			if j == 0:
				edge[i, j] = 8 * matrix[i, j] - matrix[i, (j+1)]
			elif j == m - 1:
				edge[i, j] = - matrix[i, (j-1)] + 8 * matrix[i, j]
			elif j > 0 and j < m - 1:
				edge[i, j] = - matrix[i, (j-1)] + 8 * matrix[i, j] - matrix[i, (j+1)]

	img = Image.fromarray(edge, 'L')
	img.save('my.png')


print(sys.argv[0]);

# read the image
img = cv2.imread(sys.argv[1])

# conver to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge_detection(gray)
