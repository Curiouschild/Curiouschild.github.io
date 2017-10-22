VideoCapture read(Mat frame)
	The methods/functions combine VideoCapture::grab() and VideoCapture::retrieve() in one call. This is the most convenient method for reading video files or capturing data from decode and return the just grabbed frame.
***
generate csv file in Mac terminal 
find *.pgm > at.txt
***
https://github.com/opencv/opencv_contrib

edit brew opencv
	then press E to enter vim editor, move to "-DBUILD_opencv_java=OFF". Press i to enter insert mode and edit it to "-DBUILD_opencv_java=ON". Then press "esc" to quit insert mode. Press :, then wq to save and quit vim.
	
face module


cd ../build //the path of build folder
make -j5
sudo make install

python csv.py //