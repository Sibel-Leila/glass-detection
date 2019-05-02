# importing PIL 
from PIL import Image 
import cv2
import sys
import numpy

print(sys.argv[0]);

def canny():
	# read the image
	img = cv2.imread(sys.argv[1])

	# conver to gray scale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# we found on of the best algorithms to detect the edges named: Canny
	# documentation: https://docs.opencv.org/3.1.0/da/d22/tutorial_py_canny.html
	edges = cv2.Canny(gray, 35, 50)

def print_image(edges):
	# print the image
	A = numpy.squeeze(numpy.asarray(edges))
	img = Image.fromarray(A)
	img.save(sys.argv[2])


def edgeDetection():
	# structured forests and fast edge detection

	# 1. Load source color image
	img = cv2.imread(sys.argv[1])

	# 2. Convert source image to [0;1] range
	gray = numpy.divide(img, 255)

	print_image(gray)

	# 3. Run main algorithm
	# cv::Mat edges(image.size(), image.type());
	# cv::Ptr<StructuredEdgeDetection> pDollar =
	#     cv::createStructuredEdgeDetection(modelFilename);
	# pDollar->detectEdges(image, edges);
	# 4. Show results
	# if ( outFilename == "" )
	# {
	#     cv::namedWindow("edges", 1);
	#     cv::imshow("edges", edges);
	#     cv::waitKey(0);
	# }
	# else     cv::imwrite(outFilename, 255*edges)

edgeDetection()