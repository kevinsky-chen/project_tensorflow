## This program first ensures if the face of a person exists in the given image or not then if it exists, it crops
## the image of the face and saves to the given directory.

## Importing Modules
import cv2
import os
import sys


#################################################################################
__current_path__ = os.getcwd()
__class_path__ = os.path.join(__current_path__, 'myclass', 'my')  # 找到模組的位置
__lib_path__ = os.path.join(os.path.dirname(os.getcwd()), 'lib')
__pic_path__ = os.path.dirname(os.getcwd())
sys.path.append(__lib_path__)  # 增加環境變量
print(__current_path__)
print(__lib_path__)

################################################################################
##Make changes to these lines for getting the desired results.

## DIRECTORY of the images
__in_path__ = os.path.join(os.path.dirname(os.getcwd()), "src", "img", "Calm")
# directory = "D:\Projects\Python\venv\tensorflow/my/src/img/Happy"
sys.path.append(__in_path__)  # 增加環境變量
## directory where the images to be saved:
__out_path__ = os.path.join(os.path.dirname(os.getcwd()), "output", "img", "calm")
# f_directory = "D:/Projects/Python/venv/tensorflow/my/output/img/happy"
sys.path.append(__out_path__)  # 增加環境變量

path_dict = { 'image': os.path.join(__current_path__, 'src', 'image'),
              'video': os.path.join(__current_path__, 'src', 'video'),
              'file': os.path.join(__current_path__, 'src', 'file'),
              'lib': os.path.join(__lib_path__)
              }
j = 0
def facecrop(image):
    ## Crops the face of a person from any image!

    ## OpenCV XML FILE for Frontal Facial Detection using HAAR CASCADES.
    facedata = path_dict['lib']+os.path.sep+"haarcascade_frontalface_alt.xml"
    # print(facedata)
    cascade = cv2.CascadeClassifier(facedata)

    ## Reading the given Image with OpenCV
    img = cv2.imread(image)



    miniframe = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # miniframe = cv2.resize(miniframe, minisize)


    faces = cascade.detectMultiScale(miniframe, 1.1, 4)

    global j
    j += 1
    for f in faces:
        print("in")
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        sub_face = img[y:y+h, x:x+w]

        # f_name = image.split('/')
        # print(f_name)
        # f_name = f_name[-1]

        ## Change here the Desired directory.
        print(__out_path__ + os.path.sep + str(j))
        cv2.imwrite(__out_path__ + os.path.sep + str(j) + ".jpg", sub_face)
        print("Writing: ")



if __name__ == '__main__':
    images = os.listdir(__in_path__)
    i = 0
    
    for img in images:
        # print(img)
        file = __in_path__ + os.path.sep + img
        # print(file)
        # print(i)
        facecrop(file)
        i += 1
