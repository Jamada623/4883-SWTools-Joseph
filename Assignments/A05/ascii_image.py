import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter


#converts the image to ascii
#colours the images and prints them to the screen
#also creates ascii drawing in command prompt
def img_to_ascii(**kwargs):
    """ 
    The ascii character set we use to replace pixels. 
    The grayscale pixel values are 0-255.
    0 - 25 = '#' (darkest character)
    250-255 = '.' (lightest character)
    """

    #assigning ascii characters
    ascii_chars = [ 'M', 'B', 'X', '0', 'J', '+', '-', '*', ':', ',', '.']
  
    #user input variables
    
    width = kwargs.get('width',200)
    #path = kwargs.get('path',None)
    path = kwargs.get('path')
    output = kwargs.get('output')
    fonttype = kwargs.get('fonttype')  

    #opening and resizing image
    im = Image.open(path)
    im = resize(im,width)
    w,h = im.size
    #print(w,h)

    #im = im.convert("L") # convert to grayscale    
    #font = 20
    font = kwargs.get('font')
    shift = font//3
    counter =0

    # Open a TTF file and specify the font size
    fnt = ImageFont.truetype(fonttype, font)
      

    imlist = list(im.getdata())

    newImg = Image.new ( 'RGBA', (w*font//3,h*font//3), (255,255,255,255))
    drawOnMe = ImageDraw.Draw(newImg)

    #loops through every pixel and replaces it with a coloured ASCII character
    for height in range(h):
        for width in range (w):
            r,g,b=imlist[counter]
            gray = int((r + b + g) / 3)
            char = gray // 25            
            drawOnMe.text((width*font//3+shift,height*font//3+shift), ascii_chars[char], font=fnt, fill=(r,g,b))
            counter+=1
    
    newImg.show()
    newImg.save(output)


    i = 1
    for val in imlist:
        sys.stdout.write(ascii_chars[val // 25])
        i += 1
        if i % width == 0:
            sys.stdout.write("\n")

       
    return i

    

    

def resize(img,width):
    """
    This resizes the img while maintining aspect ratio. Keep in 
    mind that not all images scale to ascii perfectly because of the
    large discrepancy between line height line width (characters are 
    closer together horizontally then vertically)
    """
    
    wpercent = float(width / float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width ,hsize), Image.ANTIALIAS)

    return img



#uses input from command line to process the image
if __name__=='__main__':
    
    if (len(sys.argv) < 4): #if not enough arguements are entered a default is set and ran
        path='input_images/juri.jpg'
        font=10
        fonttype='Ondine.ttf'
        output='output_images/output.jpg'   
        img_to_ascii(path=path,font=font,fonttype=fonttype,output=output)
        sys.exit()
        print ('not enough arguements running default test')         
    if len(sys.argv) == 5:
        path =sys.argv[1]    
        font=int(sys.argv[2])
        fonttype= sys.argv[3]
        output=sys.argv[4]
        img_to_ascii(path=path,font=font,fonttype=fonttype,output=output)
        sys.exit()
   
    
    #path = 'C:/Users/jamal/Documents/SWTOOLS HW/ASCII/input_images/vans-logo.png'
    #path = 'C:/Users/jamal/Documents/SWTOOLS HW/ASCII/input_images/juri.jpg'
    #path = 'C:/Users/jamal/Documents/SWTOOLS HW/ASCII/input_images/xmenvsf.JPG'
    #path = 'C:/Users/jamal/Documents/SWTOOLS HW/ASCII/input_images/dizzy.jpg'
    #path = 'C:/Users/jamal/Documents/SWTOOLS HW/ASCII/input_images/dizzy.jpg'
    #path = 'C:/Users/jamal/Documents/SWTOOLS HW/ASCII/input_images/makoto.jpg'
    #path = 'C:/Users/jamal/Documents/SWTOOLS HW/ASCII/input_images/lady.jpg'
    #path = 'C:/Users/jamal/Documents/SWTOOLS HW/ASCII/input_images/nico.jpg'
    #path = 'C:/Users/jamal/Documents/SWTOOLS HW/ASCII/input_images/misaka.jpg'
    #Ascii = img_to_ascii(path=path,width=200)