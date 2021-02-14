import logging
logging.getLogger('tensorflow').disabled = True
import sys
from time import sleep
import tensorflow as tf
from tensorflow import keras
import cv2
import os
import numpy as np



# simple loading animation for adding cool retro effect
def loading_animation():

	print('\n')

	for i in range(21):
		sys.stdout.write('\r')
		sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
		sys.stdout.flush()
		sleep(0.1)   

	print('\n')



# function to transform the normal image to a parsable image
def apply_image_trans(img):

	# standard image normalization/optimization
    img_size = 224
    final_image = cv2.resize(img, (img_size, img_size))
    final_image = np.expand_dims(final_image, axis = 0)
    final_image = final_image/255.0
    
    return final_image



# Function for interpreting the model sigmoid output
def interpret_sigmoid(dir, sigmoid):

	# sigmoid less than 0.5 means the classifier has spotted Louis
	if(sigmoid < 0.50):
		print('\nLouis Has Been Spotted In The Following Image: ', str(dir))
		return 1

	# sigmoid less than 0.5 means the classifier has not spotted Louis
	else:
		print('\nLouis Not Spotted In The Following Image: ', str(dir))
		return 0



# collect user input 1: What mode does the user want the application to be in
def user_input_collection_1():

	print('\nEnter The Code For Which Tracker Function to Initiate. Options Are Seen Below')

	print('\n\tPress 0 To Look For Louis in A Single Image')
	print('\tPress 1 To Look For Louis in Many Images')
	print('\tPress 2 To Look For Louis in A Security Camera Live Feed')

	user_input_1 = input('\nYour Choice: ')

	return int(user_input_1)



# Perform processing and classification on a single image
def single_image_processing():

	# read in directory of single image
	print('\nEnter The Directory Of The Image Below')
	user_input_2 = input('\nImage Directory: ')

	try:

		# read in the image
		frame = cv2.imread(user_input_2)

	except:

		# exception case
		print('\nDirectory Not Found. Exiting.')
		sys.exit(1)

	# load model
	model = keras.models.load_model('./Model/Fitted_Model.h5')

	# apply image transformations
	final_image = apply_image_trans(frame)

	print('\n---')
	# do classification on transformed image
	interpret_sigmoid(user_input_2, model.predict(final_image))
	print('\n---')


	print('\nSingle Image Processing Finished.')



# Perform processing and classification on a batch of images
def batch_image_processing():

	# read in directory of batch of images
	print('\nEnter the Local Directory of Image Batch')
	user_input_3 = input('\nBatch Image Directory: ')

	# read in the model
	model = keras.models.load_model('./Model/Fitted_Model.h5')

	# loop through the images located in the directory
	for filename in os.listdir(user_input_3):

		try:

			# read in individual images
			rel_path = os.path.join(user_input_3, filename)
			img = cv2.imread(rel_path)

			# apply image transformations
			final_image = apply_image_trans(img)

			# do classification on the transformed image
			interpret_sigmoid(rel_path, model.predict(final_image))

			print('\n---\n')

		except Exception as e:

			# exception case for any errors
			print('Unable To Read The Following Image: ' + str(filename))
			pass



# Perform image processing and classification on Real-Time Camera Live Feed
# note: if system has multiple cameras hooked up, then you might have to fiddle
#		around with the cam_id variable to located the correct camera
def real_time_processing():

	cam_id = 0
	print('\nConnected to Camera ID: ', str(cam_id))
	print('\nPress 0 to End Live Feed Processing')

	model = keras.models.load_model('./Model/Fitted_Model.h5')

	# define camera feed
	capture = cv2.VideoCapture(cam_id)

	# perform infinite reads of the camera feed
	while True:

		try:

			# capture the frame
			ret, img = capture.read()

			# transform the frame
			final_image = apply_image_trans(img)

			# call the image classifier
			ret_status = interpret_sigmoid('live feed', model.predict(final_image))

			# if Louis was spotted then save the feed
			if(ret_status):
				cv2.imwrite('./Live_Feed_Results', (cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)))

		except Exception as e:

			# exception case for errors
			print('** Something Failed **')
			break

		# break out of loop when 0 is pressed
		if cv2.waitKey(0):
			break



# main function
def main():

	print('\nInitiating Louis Locator 1.0...')
	
	# load the animation
	loading_animation()

	# collect application type from the user
	user_input_1 = user_input_collection_1()

	# load the animation
	loading_animation()

	# begin correct application type
	if(user_input_1 == 0):
		single_image_processing()
	elif(user_input_1 == 1):
		batch_image_processing()
	elif(user_input_1 == 2):
		real_time_processing()
	else:
		print('\nWrong Input. Exiting.')
		exit()


	print('\nExiting Louis Locator.\n')



if __name__ == "__main__":
	main()