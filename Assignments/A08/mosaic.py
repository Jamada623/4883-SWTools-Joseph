import os, random, sys
from PIL import Image 
import imghdr 
import numpy as np   

  
def getAverageRGB(image): 
  """ 
  Returns the r,g,b values for the read in image 
  """
  # get image as numpy array 
  im = np.array(image)  
  
  w,h,d = im.shape
  # get average 
  return tuple(np.average(im.reshape(w*h, d), axis=0)) 
  
def splitImage(image, size): 
  """ 
  Creates a list of the image split up by the read in size  
  """
  W, H = image.size[0], image.size[1] 
  m, n = size 
  w, h = int(W/n), int(H/m) 

  # image list 
  imgs = [] 
  
  for j in range(m): 
    for i in range(n): 
      
      imgs.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h))) 
  return imgs 
  
def getImages(imageDir): 
  """ 
  given a directory of images, return a list of Images 
  """
  files = os.listdir(imageDir) 
  images = [] 
  for file in files: 
    filePath =os.path.join(imageDir, file)
     
    try: 
       
      fp = open(filePath, "rb") 
      im = Image.open(fp).convert('RGB') 
      images.append(im)        
      im.load()       
      fp.close()  
    except:        
      print("Invalid image: %s" % (filePath,)) 
  return images  
  
def Compare(input_avg, avgs): 
  """ 
  compares images and returns the best match based on RGB value distance 
  """
  
  # input image average 
  avg = input_avg 
    
  # get the closest RGB value to input, based on x/y/z distance 
  index = 0
  min_index = 0
  min_dist = float("inf") 
  for val in avgs: 
    dist = ((val[0] - avg[0])*(val[0] - avg[0]) +
            (val[1] - avg[1])*(val[1] - avg[1]) +
            (val[2] - avg[2])*(val[2] - avg[2])) 
    if dist < min_dist: 
      min_dist = dist 
      min_index = index 
    index += 1
  
  return min_index 
  
  
def createImageGrid(images, dims): 
  """ 
  creates a grid of images.  
  """
  m, n = dims 
  
  # sanity check 
  assert m*n == len(images) 
  
  
  width = max([img.size[0] for img in images]) 
  height = max([img.size[1] for img in images]) 
  
  # create output image 
  grid_img = Image.new('RGB', (n*width, m*height)) 
    
  # paste images to new picture
  for index in range(len(images)): 
    row = int(index/n) 
    col = index - n*row 
    grid_img.paste(images[index], (col*width, row*height)) 
      
  return grid_img 
  
  
def createMosaic(target_image, input_images, grid_size): 
  
  # split target image  
  target_images = splitImage(target_image, grid_size)    
   
  output_images = [] 
  
  # calculate input image averages 
  avgs = [] 
  for img in input_images: 
    avgs.append(getAverageRGB(img)) 
  
  for img in target_images: 
    # target sub-image average 
    avg = getAverageRGB(img) 
    # find match index 
    match_index = Compare(avg, avgs) 
    output_images.append(input_images[match_index])       
  
  # draw mosaic to image 
  mosaic_image = createImageGrid(output_images, grid_size) 
  
  # return mosaic 
  return mosaic_image 
  
 
if __name__ == '__main__':  

  argd = {}
  mosaicimg=""
  inputfile=""
  imagefolder=""
  imsize=1
    # loops through arguments to get folder and image paths
  for arg in sys.argv[1:]:
      k,v = arg.split('=')
      if(k=="input_file"):
          inputfile=v
      elif(k=="input_folder"):
          imagefolder=v
      elif(k=="size"):
          imsize=v
      elif(k=="output_folder"):
          mosaicimg=v               
      argd[k] = v   
   
  
  # target image 
  input_image = Image.open(inputfile) 
  
  # input images  
  image_folder = getImages(imagefolder) 
  
  # check for folder of images    
  if image_folder == []: 
      print('No input images found in %s. Exiting.' % (imagefolder, )) 
      exit() 
  
  # determine size of each chunk 
  grid_size = (int(imsize), int(imsize))        

  resize_input = True    

  input_image.show()  
  # resizing input 
  if resize_input: 
     
    # for given grid size, compute max dims w,h of tiles 
    dims = (int(input_image.size[0]/grid_size[1]),  
            int(input_image.size[1]/grid_size[0]))  
     
    # resize 
    for img in image_folder: 
      img.thumbnail(dims) 
  
  # create photomosaic 
  mosaic_image = createMosaic(input_image, image_folder, grid_size) 

  #create the output folder and saves the image
  
  directory = mosaicimg
  #make output folder 
  try:  
    os.mkdir(mosaicimg)
  except OSError:  
    print ("Creation of the directory %s failed" % directory)
  else:  
    print ("Successfully created the directory %s " % directory)
  
  # naming file and displaying image
  filename = os.path.basename(inputfile) # get only filename if image is read with a path. 
  name,ext = filename.split('.')
  newname = name+'_mosaic'  
  mosaic_image.save('./'+directory+'/' +newname + '.PNG') 
  mosaic_image.show()
  




