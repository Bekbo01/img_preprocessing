# img_preprocessing
## Getting Started
 Noise Detection

SL recognition is a classification task, hence, the data should be divided so that in the resulting sets, the numerical ratio of objects of different classes is the same as in the original population. Such a sample, called a dataset, is needed to train the Machine Learning model to train the system and then use it to solve real-world problems.  The experiment used the dataset alphabet KSL, which consists of 42 letters (figure), which was prepared by 41 classes of datasets (formula), some of them were artificially imposed random noise.

 

Suppose there is dataset A, which consists of 41 KSL letters, each class has 100 frames, and a total of 41 thousand frames are included in the experiment.
А={a_1,a_2,a_3…a_41 },where |A|=41  

Next, random noise N was imposed on classes 3,6,8.

for any  i=3,6,8 ⇒ a_i=a_i+N,where N-noise

A’- is a dataset with superimposed random noiseA^'=a^' |i=3,6,8|


A ̅ – dataset with minus the sets where noise is superimposed

A ̅={a_i  |i≠3,6,8|}

Let's combine the datasets

B=A ̅+A^'

Next, in order to identify frames with noise, we conduct a normalization of dataset B.
B_n=(b_i-b_imin)/(b_imax-b_imin ),i=41

Construct a frequency element for the total dataset Bn

∑_(i=0)^(i=1)▒b_ji ,j=1…41,i+t,где t=  (b_i-b_imin)/(b_imax-b_imin )=0.03

As a result, we get the following histogram, all frames that are above the set threshold contain noise.

 

The proposed method of noise detection allows you to pre-check the presence of noise in the frames when creating a video recording, for real-time gesture recognition systems or detection of noise frames in the finished datasets, which ultimately can ensure the successful operation of any object recognition systems.

Combined-adaptive image pre-processing method

Modern computer technology allows to carry out the automated analysis of various images. This requires, as a rule, the use of methods and algorithms of image preprocessing, their segmentation to select objects on them, and further study of these objects or their identification. However, most of the algorithms used for this require manual image preprocessing. This paper proposes an adapted method of image preprocessing that will use for filtering those or other filters depending on the noise in the input image and depending on the method of object recognition in the image.
Further, to eliminate noise detected frames for systems where objects on the frames are recognized on the basis of segmentation or extraction of the value proposed the following solution: 



{█(T > 0.3,   cn@T≤0,3{█(〖frame〗_WGN,   (M_f+Prewitt) or (W_f+Canny)@〖frame〗_BGN,   M_f+Roberts@others,   Roberts)┤ )┤

For a system where the objects on the frames are recognized by selecting the contour, the solution is as follows:


{█(T > 0.3,   cn@T≤0,3{█(〖frame〗_WGN,   (M_f+AdaptBin) or (W_f+AdaptBin)or(M_f+AdaptBin)@〖frame〗_BGN,   (M_f+AdaptBin) or (W_f+AdaptBin)@others,   ThreshBin)┤ )┤



Thus, the proposed algorithm of image preprocessing for the selection of objects on it does not assume the presence of a priori knowledge about the image, which makes the algorithm universal. This algorithm can be used in research aimed at developing gesture recognition systems for adaptive preprocessing. 


## Installation
### Window Python Installation Guide

1. Downlaod the [Python 3.7.0](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe) from the official website.

	**Remember to check the `Add Python to path` option as shown below**

	![window-installation](https://raw.githubusercontent.com/sunwaytechclub/Python-Installation-Guide/master/pictures/window-install.jpg)

2. Open terminal and make sure you had successfully install Python and had been added to path

	```
	> python --version

	# Make sure the output should be 3.6.* or 3.7.*
	```
Install virtualenv:

```sh
> pip install virtualenv # install virtualenv
> mkdir <Repo name> # create folder
> cd <Repo name> # change directory
> virtualenv env # create virtual enviroment
> env\Scripts\activate # activate virtual env
> git clone https://github.com/Bekbo01/img_preprocessing.git # clone repository
> cd img_preprocessing # got to folder img_preprocessing
> pip install -r requirements.txt # install requirements packages
> ..\env\Scripts\deactivate # deactivate enviroment
```

Renew repository:

```sh
> git pull # pulling repo
> ..\env\Scripts\activate # activate virtual env
> pip install -r requirements.txt # install requirements packages
```
Push repository:
```sh
> git status # check the status of the file
> git add . # adding new changes
> git commit -m "Comment info" # commit changes
> git push origin main # pushing repo
```
