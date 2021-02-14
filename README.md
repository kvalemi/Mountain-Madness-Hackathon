# Project Theme

### Name: **Louis Locator**

### Author: Kaveh Alemi

### Theme:

In the book "_Nineteen Eighty-Four: A Novel_" by George Orwell, there is a significant emphasis on big government spying on its citizens. One of the technologies this government uses is spy cameras that identify and track people. 

This technology is purely engineered by the big government to track HUMANS. But, what happens when dogs/canines suddenly become revolutionary and want to overthrow the government? How will the government track dogs to keep them on a tight leash (pun intended)? Well, they no longer have to worry because I've created a prototype for this exact use case. 

**Louis Locator** is a prototype of a dog identification that can be used to track dogs in static images, batch image containers, and live feeds from security/spy cameras. Given that I only had 24 hours to engineer this system, I only made it a binary classifier, where it can identify if my dog, named Louis, is either located in or not located in an image, a batch of images, or camera live feed.

<br />
<br />

# Project Description

The heart of this project is the deep learning model I trained that does classification on images. This model does binary classification on the following two labels: "Louis" and "Not Louis". The label "Louis" corresponds to my dog Louis located in the image, and "Not Louis" corresponds to my dog Louis not being located in the picture.

The deep learning model I used is a pre-structured Keras Convolutional Neural Network (CNN) called MobileNet V2. This is a lightweight CNN that efficiently trains on smaller datasets and does not require a lot of computational power. I trained this model on about 400 pictures split evenly between images of my dog, which I took, and photos of other dogs that I obtained from online.

After I trained the model, I then built a simple interface, where a user can interact with **Louis Locator** in three ways:

1) **Single Image Processing**: Locates Louis in a single image.

2) **Batch Image Processing**: Locates in a batch of images.

3) **Live Feed Processing**: In real-time, it locates Louis in the feed of a camera system configured to the localhost.

<br />

For each of these three interfaces, the application will take as input an image(s) and run the image(s) through the CNN model, which then outputs a binary outcome. The result is simply printed in the terminal. 

See below for a system design diagram:

![](/Diagram/System%20Design.jpg)

<br />
<br />

# Project Demo

1) **Demo of single image processing:** Run the following commands to classify a single image as containing Louis or not.

- In terminal type `Python3 Louis_Locator.py`

- When prompted input 0

- When prompted input the directory of the image, like `./Dataset/Test/Easy_Louis.jpeg`

<br />

![](/Demo%20Files/Single%20Image%20Demo.png)

<br />

Some more graphical examples of single image processing:
(note: Take a look at `./Notebooks/Testing Notebook.ipynb` to see the testing code)

**Louis (easy classification):**

![](/Examples/1.png)

<br />

**Louis (medium classification):**

![](/Examples/2.png)

<br />

**Louis (hard classification):**

![](/Examples/3.png)

<br />

**Not Louis (easy classification):**

![](/Examples/4.png)

<br />

**Not Louis (medium classification):**

![](/Examples/5.png)

<br />

**Not Louis (hard classification):**

![](/Examples/6.png)

<br />

2) **Demo of batch image processing:** Run the following commands to classify a batch of images.

- In terminal type `Python3 Louis_Locator.py`

- When prompted input 1

- When prompted input the directory of the batch of images, like `./Dataset/Test`

<br />

![](/Demo%20Files/Batch%20Demo.png)

<br />

3) **Demo of live feed processing**: I don't have a fast enough computer to do real-time image processing and classification. If you do, feel free to try it out. You might have to play around with your system settings a bit to ensure that either terminal or python has permissions to access your webcam.

<br />
<br />

# How to Build the Project:

1) Install Python 3

2) Install the following Python dependancies with a package manager (e.g. pip or anaconda):

  - logging
  - sys
  - time
  - tensorflow
  - cv2
  - os
  - numpy

3) Run the following command in a terminal in your local directory: `Python3 Louis_Locater.py`

4) Follow walkthrough from demo to interact with the app. Use test images in `./Dataset/Test` to play around witht he application.

<br />
<br />


# Project Extras

This project can easily be extrapolated to do binary classification on any dog with some very minor changes. Follow these steps:

<br />

1) Change the following directory names:

- `./Dataset/Louis` --> `./Dataset/(your dogs name)`

- `./Dataset/Not_Louis` --> `./Dataset/Not_(your dogs name)`


2) Import pictures of your dog, from all angles into `./Dataset/(your dogs name)`
(I recommend 200 pictures for a good classifier)


3) Import pictures of other dogs into `./Dataset/Not_(your dogs name)` 
(you can images from a dataset called _Stanford Dog Images Dataset_)


4) Run the following training script to automatically train the classifier: `training_script.py`


5) In the source code of `Louis_Locator.py` change any reference from "Louis" to your dogs name, so that the applications outputs the correct label






