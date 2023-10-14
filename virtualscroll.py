import cv2 as cv  #we used the opencv to get our feed and also process our video.
#It is a popular open-source computer vision and machine learning software library that provides
#various tools and functions for image and video processing.After importing cv2, you can use its
#functions and classes to perform a wide range of computer vision tasks, such as loading and
#displaying images, performing image processing operations, object detection, and more.
import cvzone  #wCVzone will use it to writes some tests, and also it will be a helper library for us to get our
               #handtracking on
from cvzone.HandTrackingModule import HandDetector
import pyautogui as gui  #we utilise the pyautogui to scroll up and down through the points we get from
#our hand.PyAutoGUI is a popular cross-platform automation library that allows you to control the mouse,
#keyboard, and take screenshots. It's easy to use and works on Windows, macOS, and Linux.

cap = cv.VideoCapture(0)
hd = HandDetector(detectionCon=0.70)  #initializing hand tracking object.in bracket() we have specify our
                                      #detection confidence that means like how accurate should we detect
                                      #something before we said it is a hand.0.70 i.e.70%.so when we detect
                                      #something which we think is 70% accurate to be hand we said that is a
                                      #hand and we detect it

text = 'AI Virtual Scrolling' #for just writing that we are doing AI Virtual Scrolling project for that we have
                              #initialize the variable i.e. 'text'
while 1:
    ret,img = cap.read()  #we are taking our video frame here in this variable which is image(img)
                          #the (ret) is a boolean value which shows the presence of video or not and then we are
                          #reading that
    cv.rectangle(img,(0,230),(640,250),(0,255,255),-1) #drawn a rectangle which will act as a neutral that means
    #if our hand will come on that rectangle there is no scrolling happening.-1 is the thickness,(0,255,255)
    #is the color,(0,230) is the starting point,(640,250) is the stopping point.
    cvzone.putTextRect(img,text,[130,40],border=2,colorB=(0,255,255),scale=2.5)  #for displaying text variable
    #using cvzone library.Inside ,bracket we first specify our image then second the variable in which we want
    #to put the text and third to show we give the position and the rest are border,background color,scale

    hands,img = hd.findHands(img)  #to ON our hand detection we do hd.findhands() and this takes in the image
                                   #on which we want to detect the hand, and so we gave our webcam feed, and it
                                   #returns to us our hands and the image which is the output we get from the
                                   #function

    if hands:
        bbox = hands[0]['bbox']  #bbox stands for bounding box.If there is hand detected then we want to get
                                 #the bounding box of that hand
                                 #boundind box of that hand(bbox) = that hand at index 0
        x,y,w,h = bbox  #
        lmlist = hands[0]['lmList']
        length,info,img = hd.findDistance(lmlist[4][0:2],lmlist[8][0:2],img)  #to find the distance between the
        #fingers we have used a function hd.findDistance() which takes the landmarks list(lmlist), and at the last
        #we give this function is our image.This function returns us length and also give us the info which we are
        #not going to use and lastly returns our image because we have also given this function image attribute
        # print(length) #printed length to see what it gives us

        #to scroll we have to use our length and also the values we get from our bounding box.So we quickly put
        #this values we get from our bounding box into separate variable

        if length < 20:
            if y > 190:
                gui.press('down')  #we use pyautogui to scroll up and down.press() which is a function
                                   #which takes either to press up or down
            elif y < 180:
                gui.press('up')
                #the complete logic written from line 45 to line 50 is that we first check the distance between
                #these two fingers.So if the distance between these two fingers is less than 20 then that means
                #we have clicked, and also we go ahead to check whether the clicking is our hand up or down,
                #if it is up then we want to scroll up and if it is down we have to scroll down.The distance
                #between the top and the down is 480 which is the screen size of our webcam








    cv.imshow('frame',img)  #this two lines are used to show the video
    cv.waitKey(1) #here we are just taking it each frame per second
