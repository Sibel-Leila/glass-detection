# glass-detection

SII - project

We studied the articole: "Seeing Glassware: from Edge Detection to Pose Estimation and Shape Recovery" available at 
	https://pdfs.semanticscholar.org/efcc/2098f7f9637c7db9b9f7ac4c3294578e12ca.pdf

Now we try to implement this algorithm using python

Need to install:
sudo apt install python-pip
pip install opencv-python

Canny edge detector
https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123
1. Noise reduction;
2. Gradient calculation;
3. Non-maximum suppression;
4. Double threshold;
5. Edge Tracking by Hysteresis.


Structured forests for fast edge detection
https://docs.opencv.org/3.4/d0/da5/tutorial_ximgproc_prediction.html

1. Load source color image
2. Convert source image to [0;1] range
3. Run main algorithm
cv::Mat edges(image.size(), image.type());
cv::Ptr<StructuredEdgeDetection> pDollar =
    cv::createStructuredEdgeDetection(modelFilename);
pDollar->detectEdges(image, edges);
4. Show results
if ( outFilename == "" )
{
    cv::namedWindow("edges", 1);
    cv::imshow("edges", edges);
    cv::waitKey(0);
}
else     cv::imwrite(outFilename, 255*edges)


Structured forests
https://github.com/ArtanisCV/StructuredForests
