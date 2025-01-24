######################################
# Image Filter Project Starter Code  #
#                                    #
#           Project STEM             #
#                                    #
#              9/20/19               #
#                                    #
######################################

# Before running any code, please run the following in the shell :
# pip install -r requirement.txt

# importing PIL.Image library and os library
from PIL import Image #from PIL import Image 
import os

# Deletes old created images if they exist
images = ["combinedFilters.jpg","polarized.jpg","cool.jpg","twocolor.jpg","grey.jpg"]
for i in images:
  if os.path.exists(i):
    os.remove(i)

# Adds two blank lines before any output
print("\n\n")
# input for blue(polarize filter)
b_change = int(input("Choose an intensity for the polarizing filter (0 - 100): "))
color_pick = input("Choose a color for the twocolor filter. Red and blue(r), green and red(g) or blue and yellow(b): ")
color_true = False
while color_true == False:
  if color_pick == "r" or color_pick == "g" or color_pick == "b":
    color_true = True
  else:
    print("The color you inputted is invalid. Please enter r(red and blue), g(green and red) or b(blue and yellow).")
    color_pick = input("Choose a color to keep in the twocolor filter (r, g or b): ")

# Opens image - upload a Local File into repl.it
img = Image.open('image.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

########################
#    Example Filter    #
########################
def grey():
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = (r + g + b) // 3
    newg = (r + g + b) // 3
    newb = (r + g + b) // 3
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage


#####################
#    Your Filter    #
#####################

def cool():
  print("Code for cool filter")
 # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = int(float(r) // 1.25)
    newg = int(float(g) // 0.55)
    newb = int(float(b) // 0.6)
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  return newImage

#####################################
#    Your Filters with User Input   #
#####################################

def polarized():
  print("Code for polarized")
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = r + (b_change // 2)
    newg = g
    """
    if g - b_change < 0:
      newg = 0
    else:
      if (g - (b_change / 2)) % 1:
        b_change = b_change - 1
      else:
        newg = (g - (b_change / 2))
    """
    if b - b_change < 0:
      newb = 0
    else:
      newb = b - b_change
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  return newImage

def twocolor():
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    #red and blue
    if color_pick == "r":
      newr = (r)
      newg = (r + g + b) // 4
      newb = (r + g + b) // 4
    #green and red
    elif color_pick == "g":
      newr = (r + g + b) // 3
      newg = (g)
      newb = (r + g + b) // 3
    # blue and yellow
    elif color_pick == "b":
      newr = (r + g + b) // 3
      newg = (r + g + b) // 3
      newb = (b)
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage


# Creates the four filter images and saves them to our files
a = grey()
a.save("grey.jpg")
b = cool()
b.save("cool.jpg")
c = polarized()
c.save("polarized.jpg")
d = twocolor()
d.save("twocolor.jpg")

# Image filter names for use below
f1 = "cool"
f2 = "polarized"
f3 = "twocolor"

# Apply multiple filters through prompts with the user
answer = input("\nWhich filter do you want me to apply?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
  answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

while answer == "grey" or answer == f1 or answer == f2 or answer == f3:
  if answer == "grey":
   img = grey()
  elif answer == f1:
   img = cool()
  elif answer == f2:
   img = polarized()
  elif answer == f3:
   img = twocolor()
  else:
    break
  print("Filter \"" + answer + "\" applied...")
  answer = input("\nWhich filter do you want me to apply next?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
  while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
    answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
print("Image being created...Done")

# Create the combined filter image and saves it to our files
img.save("combinedFilters.jpg")