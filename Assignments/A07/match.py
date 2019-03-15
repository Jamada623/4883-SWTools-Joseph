from SSIM_PIL import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from PIL import Image, ImageDraw, ImageMath

def mse(imageA, imageB):
	# Calculating the mean square
	# returning the value calculated
	
	image1 = Image.open(imageA)
	image2 = Image.open(imageB)
	err = np.sum(ImageMath.eval("(float(a) - float(b))**2", a = image1, b = image2))
	err /= float(image1.size[0] * image1.size[1])		
	return err

def compare_images(imageA, imageB):
    #finds the ssim value and returens it
    #converts images to greyscale to find the ssim value

	grayA = Image.open(imageA).convert('L')
	grayB = Image.open(imageB).convert('L')
	score= ssim(grayA, grayB)
	
	return score


if __name__=='__main__':
    #takes the arguements read in the creates  dictionary
    #afterwards the dictionary is looped through and the values found are used to calculate
    #the mse and ssim
    args = {}

    for arg in sys.argv[1:]:
        k,v = arg.split('=')
        args[k] = v	

    imname=args['image'].split('/')
    
    mseimage=""
    currentmean=10000000
    counter =0 #check if looping through dictionary appropriate number of times

    # looping through the dictionary
    for images in os.listdir(args['folder']):                    
        # check to avoid running mse on itself
        if(images!=imname):
            meansqe=mse(args['image'],args['folder']+'/'+images) #calculates mse
            counter+=1
            #updates current mse if the value is smaller than the previous
            if(currentmean>meansqe):
                currentmean=meansqe
                #print(currentmean, smeansqe)                
                mseimage=args['folder']+'/'+images

    print (counter)             
    image1=Image.open(args['image'])
    image2=Image.open(mseimage)
    
    #calculating the ssim
    comp = compare_images(args['image'],args['folder']+'/'+images)
    fig = plt.figure("Images")
    plt.suptitle(" MSE: %.2f  SSIM :%.2f" % (currentmean,comp))
    #plt.suptitle("SSIM : %.2f" % (comp))

    #printing out the images and showing the mse and ssim              
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(image1)
    plt.axis("off")            
    
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(image2)
    plt.axis("off")               
    plt.show()	

    sys.exit()








