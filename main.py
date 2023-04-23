import os
from time import sleep
from PIL import Image, ImageFilter

# modified picture files
os.mkdir('png_photos')  # PNG
os.mkdir('size200_img')  # sizes
os.mkdir('size400_img')
os.mkdir('size600_img')
os.mkdir('rotated_img')  # rotating the image
os.mkdir('black_white_img')  # black and white
os.mkdir('blurred_img')  # blurred
os.mkdir('emboss_img')  # emboss

# setting images into objects to call later
img1 = 'pic1.jpeg'
img2 = 'pic2.jpeg'
img3 = 'pic3.jpeg'
img4 = 'pic4.jpeg'
img5 = 'pic5.jpeg'
img6 = 'pic6.jpeg'
img7 = 'pic7.jpeg'
img8 = 'pic8.jpeg'
img9 = 'pic9.jpeg'
img10 = 'pic10.jpeg'

# setting the sizes
size_200 = (200, 200)
size_400 = (400, 400)
size_600 = (600, 600)

# jpeg to png function


def transform(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg'):
            if x == f:
                i = Image.open(f)
                fn, fext = os.path.splitext(f)
                i.save('png_photos/{}.png'.format(fn))
                i.show()
# changing the size function


def size(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg'):
            if x == f:
                if choice2 == "200":
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.thumbnail(size_200)
                    i.save('size200_img/{}_200{}'.format(fn, fext))
                    i.show()
                elif choice2 == "400":
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.thumbnail(size_400)
                    i.save('size400_img/{}_400{}'.format(fn, fext))
                    i.show()
                elif choice2 == "600":
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.thumbnail(size_600)
                    i.save('size600_img/{}_600{}'.format(fn, fext))
                    i.show()
# rotating the pictures to what the user chooses


def rotate(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg'):
            if x == f:
                i = Image.open(f)
                fn, fext = os.path.splitext(f)
                y = int(input("Please type in desired length to rotate: "))
                i.rotate(y).save('rotated_img/{}_rotated{}'.format(fn, fext))
                i.show()
# this is for the black and white photo


def color(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg'):
            if x == f:
                i = Image.open(f)
                fn, fext = os.path.splitext(f)
                i.convert(mode='L').save(
                    'black_white_img/{}_black_and_white{}'.format(fn, fext))
# this blurs the image


def blur(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg'):
            if x == f:
                i = Image.open(f)
                b = int(input("Enter the amount of blur you want: "))
                fn, fext = os.path.splitext(f)
                i.filter(ImageFilter.GaussianBlur(b)).save(
                    'blurred_img/{}_blurred{}'.format(fn, fext))
# the emboss filter


def emboss(x):
    for f in os.listdir('.'):
        if f.endswith('.jpeg'):
            if x == f:
                i = Image.open(f)
                fn, fext = os.path.splitext(f)
                i.filter(ImageFilter.EMBOSS()).save(
                    'emboss_img/{}_emboss{}'.format(fn, fext))


def empty():
    for f in os.listdir('png_photos'):  # empties and deletes the png folder
        os.remove('png_photos/'+f)
    os.removedirs('png_photos')
    for f in os.listdir('size200_img'):  # empties and deletes size folders
        os.remove('size200_img/'+f)
    os.removedirs('size200_img')
    for f in os.listdir('size400_img'):
        os.remove('size400_img/'+f)
    os.removedirs('size400_img')
    for f in os.listdir('size600_img'):
        os.remove('size600_img/'+f)
    os.removedirs('size600_img')
    for f in os.listdir('rotated_img'):  # empties and deletes rotated images folder
        os.remove('rotated_img/'+f)
    os.removedirs('rotated_img')
    for f in os.listdir('black_white_img'):  # empties black and white folder
        os.remove('black_white_img/'+f)
    os.removedirs('black_white_img')
    for f in os.listdir('blurred_img'):  # empties blurred folder
        os.remove('blurred_img/'+f)
    os.removedirs('blurred_img')
    for f in os.listdir('emboss_img'):  # empties emboss folder
        os.remove('emboss_img/'+f)
    os.removedirs('emboss_img')


choice = input("""
      Welcome to the Image Manipulater. In here there are 10 random images that you can manipulate.
      
      Type in a number between 1 to 10 to select a photo to manipulate, or type in "quit" to exit. 
      """)

if choice.isdigit():
    if ("1" in choice) or ("2" in choice) or ("3" in choice) or ("4" in choice) or ("5" in choice) or ("6" in choice) or ("7" in choice) or ("8" in choice) or ("9" in choice) or ("10" in choice):
        choice1 = str(input("""
            Would you like to convert the image into a png instead of jpeg? \n Yes or No
            """))
        if choice1 == "yes":
            transform(locals()["img" + choice])

        choice2 = str(input("""An additional feature is the ability to modify the picture's size. To resize to 200, please input "200". To resize to 400, please input "400". To resize to 600, please input "600". If you prefer not to change the size, please input "no".
"""))
        if choice2 != "no":
            size(locals()["img" + choice])

        choice3 = str(input("""
            You have the option to rotate the image. Are you interested in rotating it?
            If yes just enter in "yes", if no enter "no"
             """))
        if choice3 == "yes":
            rotate(locals()["img" + choice])

        choice4 = str(input("""
            Do you want to convert the image to black and white? Please answer with either "yes" or "no." 
            """))
        if choice4 == "yes":
            color(locals()["img" + choice])

        choice5 = str(input("""
            Would you like to apply a blur effect to the picture? Please respond with either "yes" or "no"
            """))
        if choice5 == "yes":
            blur(locals()["img" + choice])

        choice6 = str(input("""
            Would you like to apply the emboss filter to the image? yes or no: 
            """))
        if choice6 == "yes":
            emboss(locals()["img" + choice])

    final = input("""
      Would you like to quit? |Yes Or No| (Remember before quiting check the folders to see your manipulated images)
              """)

    if final == "yes":
        sleep(0.5)
        for f in os.listdir('png_photos'): # empties and deletes png folder
            os.remove('png_photos/'+f)
        os.removedirs('png_photos')
        for f in os.listdir('size200_img'): # empties and deletes size folders
            os.remove('size200_img/'+f)
        os.removedirs('size200_img')
        for f in os.listdir('size400_img'):
            os.remove('size400_img/'+f)
        os.removedirs('size400_img')
        for f in os.listdir('size600_img'):
            os.remove('size600_img/'+f)
        os.removedirs('size600_img')
        for f in os.listdir('rotated_img'): # empties and deletes rotated images folder
            os.remove('rotated_img/'+f)
        os.removedirs('rotated_img')
        for f in os.listdir('black_white_img'): # empties black and white folder
            os.remove('black_white_img/'+f)
        os.removedirs('black_white_img')
        for f in os.listdir('blurred_img'): # empties blurred folder
            os.remove('blurred_img/'+f)
        os.removedirs('blurred_img')
        for f in os.listdir('emboss_img'): # empties emboss folder
            os.remove('emboss_img/'+f)
        os.removedirs('emboss_img')
        quit()

    elif final == "no":
        choice = input("Choose a new image by picking between 1-10:")

    else:
        print("I'm sorry, the value you entered does not match any of the picture options. Please choose a number between 1 and 10 for picture selection.")
        choice = input()

elif choice == "quit":
    print("Thanks for trying the image manipulater")
    sleep(0.5)
    empty
    quit()

else:
    print("Sorry, that doesn't seem to be one of the choices for a picture! Please input a valid number, it has to be between 1-10.")
