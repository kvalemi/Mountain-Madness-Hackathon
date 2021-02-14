## Project Theme

### Name: **Louis Locator**

### Author: Kaveh Alemi

### Theme:

In the book "_Nineteen Eighty-Four: A Novel_" by George Orwell, there is a large emphasis on big government spying on it's citizens. One of the technologies this government uses is spy cameras that identify and track people. 

This technology is purely engineered by big government to track HUMANS. But, what happens when dogs/canines become revolutionary and want to overthrow the government? How will the government track dogs in order to keep them on a tight leash (pun intended). Well they no longer have to worry, because I've created a prototype for this exact use case. 

**Louis Locator** is a prototype identification system used to identify dogs from static images, batch image containers, and live feeds from security/spy cameras. Given that I only had 24 hours to engineer this system, I only made it a binary classifier, where it can identify if my own dog, named Louis, is seen in an image, a batch container of images, or a live feed.

<br />
<br />

## Project Description

The hear of this project is the deep learning model I trained to be able to do classification on framed images. This model does binary classification on the following two labels: "Louis" and "Not Louis". The label "Louis" corresponds to my dog "Louis" being in the framed image, and "Not Louis" corresponds to my dog Louis not being in the picture.

The deep learning model I used is a pre-structured Keras Convolutional Neural Network called MobileNet V2. This is a lightweight CNN that efficiently trains on smaller training datasets, and does not require lots of computational power. I trained this model on about 400 pictures split evenly between pictures of my dog, which I took, and pictures of dogs that I obtained from Kaggle.

After I trained the model, I then built a fairly intuitive interface, where a user can interact with **Louis Locator** in three ways:

1) Single Image Processing: Try and locate Louis in a single image.

2) Batch Image Processing: Try and locate Louis in a batch of images stored in a local directory.

3) Live Feed Processing: In real-time, try and see if Louis is in the frame as inputted by the security camera hooked up to the system.

<br />

For each of these three interfaces, the application will run the framed images through the CNN model and come up with a result. The result is simply printed out to terminal. See below for a system design diagram:

![](/Diagram/System%20Design.jpg)

<br />
<br />

## Project Demo

1) **Demo of single image processing:** Run the following commands to classify single images.

- In terminal type `Python3 Louis_Locator.py`

- When prompted input 0

- When prompted input the directory of the image, like `./Dataset/Test/Easy_Louis.jpeg`

<br />

![](/Demo%20Files/Single%20Image%20Demo.png)

<br />

Some more graphical examples of test images:

- Take a look at `./Notebooks/Testing Notebook.ipynb` to see how I tested each image

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

2) **Demo of batch image processing:** Run the following commands to classify single images.

- In terminal type `Python3 Louis_Locator.py`

- When prompted input 1

- When prompted input the directory of the image, like `./Dataset/Test`

<br />

![](/Demo%20Files/Batch%20Demo.png)

<br />

3) **Demo of live feed processing**: I don't have a fast enough computer to do real-time image processing and classification. If you do, feel free to try it out. You might have to tweak with your system settings a bit to ensure that either terminal or python has permissions to access your webcam.

<br />
<br />

## How to Build the Project:

1) Install (Python 3)

2) Install the following Python dependancies with a package manager:

  - logging
  - sys
  - time
  - tensorflow
  - cv2
  - os
  - numpy

3) Run the following command in your local directory: `Python3 Louis_Locater.py`

4) Follow walkthrough from demo to interact with the app

<br />
<br />


## Project Extras

This project can easily be extrapolated to do binary classification on any dog with very some very minor changes. Follow these steps:

<br />

1) Change the following directory names:

- `./Dataset/Louis` --> `./Dataset/(your dogs name)`

- `./Dataset/Not_Louis` --> `./Dataset/Not_(your dogs name)`


2) Import pictures of your dog, from all angles into `./Dataset/(your dogs name)`


3) Import pictures of other dogs into `./Dataset/Not_(your dogs name)` 

- you can images from a dataset called _Stanford Dog Images Dataset_

4) Run the following training script: `training_script.py`

5) In the source code of `Louis_Locator.py` change any reference from Louis to your dogs name, so that the applications output is labelled correctly






