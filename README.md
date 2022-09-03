# img_preprocessing
## Getting Started
### Noise Detection
<p>
The problem of noise-suppression is caused by one of rather actual and widespread problems in the field of recognition of static and dynamic gestures. Existing noise-suppression mechanisms are traditionally specialized to suppress a certain type of noise, so there are no integral filters suppressing all types of noise. Additive Gaussian and impulse noise models are characterized as the most optimal in terms of their application to sign language recognition tasks. Additive Gaussian noise is characterized by adding values from the corresponding normal distribution with a zero mean to each pixel of the image. Impulse noise is interpreted by replacing part of the pixels in an image with values of a fixed or random value. This noise modification is associated with errors in image transmission, for example.
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
