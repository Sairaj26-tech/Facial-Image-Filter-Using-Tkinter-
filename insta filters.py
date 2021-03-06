from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import numpy as np
from PIL import Image
import requests
import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk


import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
girl_hat=cv2.imread('D:/instagram face filter for intership/Filters/girl hat.png')
hat=cv2.imread('D:/instagram face filter for intership/Filters/hat1.png')
glass=cv2.imread('D:/instagram face filter for intership/Filters/glasses.png')
mouth=cv2.imread('D:/instagram face filter for intership/Filters/rainbow.png')
dog=cv2.imread('D:/instagram face filter for intership/Filters/dog.png')
rab=cv2.imread('D:/instagram face filter for intership/Filters/rab.png')
doggy=cv2.imread('D:/instagram face filter for intership/Filters/doggy.png')
roses=cv2.imread('D:/instagram face filter for intership/Filters/roeses.png')
hearts=cv2.imread('D:/instagram face filter for intership/Filters/hearts.png')
teeth=cv2.imread('D:/instagram face filter for intership/Filters/teeth.png')
crown=cv2.imread('D:/instagram face filter for intership/Filters/crown.png')

########################              girl_hat          #######################################

def put_girl_hat(girl_hat, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    girl_hat = cv2.resize(girl_hat, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if girl_hat[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = girl_hat[i][j][k]
    return fc

def girlhat():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_girl_hat(girl_hat, im, x, y, w, h)
        cv2.imshow('Hat & glasses',im)
        if cv2.waitKey(1) == ord('q'):
          break
    
    webcam.release()
    cv2.destroyAllWindows()
#################                      hat                    ############################

def put_hat(hat, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    hat = cv2.resize(hat, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if hat[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = hat[i][j][k]
    return fc

def hat1():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_hat(hat, im, x, y, w, h)
        cv2.imshow('Hat',im)
        if cv2.waitKey(1) == ord('q'):
          break
    
    webcam.release()
    cv2.destroyAllWindows()
#####################################   glass        ###############################################
def put_glass(glass, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    glass = cv2.resize(glass, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if glass[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = glass[i][j][k]
    return fc
def glass_btn():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_glass(glass, im, x, y, w, h)
        cv2.imshow('glasses',im)
        if cv2.waitKey(1) == ord('q'):
          break
    webcam.release()
    cv2.destroyAllWindows()
####################################   dog        ###############################################
def put_dog(dog, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    dog = cv2.resize(dog, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if dog[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = dog[i][j][k]
    return fc
def dog_btn():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_dog(dog, im, x, y, w, h)
        cv2.imshow('dog',im)
        if cv2.waitKey(1) == ord('q'):
          break
    webcam.release()
    cv2.destroyAllWindows()
    
####################################   dog        ###############################################
def put_rab(rab, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    rab = cv2.resize(rab, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if rab[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = rab[i][j][k]
    return fc
def rab_btn():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_rab(rab, im, x, y, w, h)
        cv2.imshow('rab',im)
        if cv2.waitKey(1) == ord('q'):
          break
    webcam.release()
    cv2.destroyAllWindows()
    
####################################   dog        ###############################################
def put_doggy(doggy, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    doggy = cv2.resize(doggy, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if doggy[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = doggy[i][j][k]
    return fc
def doggy_btn():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_doggy(doggy, im, x, y, w, h)
        cv2.imshow('rab',im)
        if cv2.waitKey(1) == ord('q'):
          break
    webcam.release()
    cv2.destroyAllWindows()
    
 ####################################   roses        ###############################################
def put_roses(roses, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    roses = cv2.resize(roses, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if roses[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = roses[i][j][k]
    return fc
def roses_btn():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_roses(roses, im, x, y, w, h)
        cv2.imshow('rab',im)
        if cv2.waitKey(1) == ord('q'):
          break
    webcam.release()
    cv2.destroyAllWindows()   
 
    
 ####################################   hearts        ###############################################
def put_hearts(hearts, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    hearts = cv2.resize(hearts, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if hearts[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = hearts[i][j][k]
    return fc
def hearts_btn():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_hearts(hearts, im, x, y, w, h)
        cv2.imshow('rab',im)
        if cv2.waitKey(1) == ord('q'):
          break
    webcam.release()
    cv2.destroyAllWindows() 
 
####################################   hearts        ###############################################
def put_teeth(teeth, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    teeth = cv2.resize(teeth, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if teeth[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = teeth[i][j][k]
    return fc
def teeth_btn():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_teeth(teeth, im, x, y, w, h)
        cv2.imshow('rab',im)
        if cv2.waitKey(1) == ord('q'):
          break
    webcam.release()
    cv2.destroyAllWindows() 
    
####################################   crown        ###############################################
def put_crown(crown, fc, x, y, w, h):
    face_width = w
    face_height = h

    
    crown = cv2.resize(crown, (int(face_width * 1.5), int(face_height * 1.95)))
   

    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if crown[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = crown[i][j][k]
    return fc
def crown_btn():
    webcam = cv2.VideoCapture(0)
    while True:
        size=4
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)
        for (x, y, w, h) in fl:            
                im = put_crown(crown, im, x, y, w, h)
        cv2.imshow('rab',im)
        if cv2.waitKey(1) == ord('q'):
          break
    webcam.release()
    cv2.destroyAllWindows() 
    
##################################################  weather ################################################

def weather():
    
    root=tk.Tk() 

    WIDTH=620
    HEIGHT=450
    
    
    def get_weather(city):
        weather_key="79de5817a4d223b536ce61a0f630a4b4"
        url='https://api.openweathermap.org/data/2.5/weather'
        params={'appid':weather_key, 'q':city, 'units':'Metric'}
        response=requests.get(url,params=params)
        report=response.json()
        
        label['text']=show_weather_report(report)
    
    
    def show_weather_report(report):
        try:
            city_name= report['name']
            weather_condition= report['weather'][0]['description']
            temp= report['main']['temp']
            output= 'City: %s \nCondition: %s \nTemperature(??C): %s' %(city_name,weather_condition,temp)
        except:
            output='There was a problem while retrieving that information'
        return output
    
    
    canvas=tk.Canvas(root,width=WIDTH,height=HEIGHT)
    canvas.pack()
    
    
    frame=tk.Frame(root,bg='#0B90A9',bd=5)
    frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')
    
    entry=tk.Entry(frame,font=('Courier New Baltic',20))
    entry.place(relheight=1,relwidth=0.7)
    
    btn=tk.Button(frame,text="Get Weather",relief='raised',bg="gray",font=20,command=lambda: get_weather(entry.get()))
    btn.place(relx=0.72,relheight=1,relwidth=0.28)
    
    low_frame=tk.Frame(root,bg='#0B90A9',bd=5)
    low_frame.place(relx=0.5,rely=0.25,relheight=0.65,relwidth=0.75,anchor='n')
    
    bg_color='white'
    label=tk.Label(low_frame,font=('Calibri',20),justify='center',bd=4)
    label.config(font=40,bg=bg_color)
    label.place(relheight=1,relwidth=1)
    
    """ weather_icon=tk.Canvas(label,bg=bg_color,bd=0,highlightthickness=0)
    weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5) """
    
    
    root.mainloop()
#######################################################################################################



    
from PIL import ImageTk,Image
import PIL.ImageTk

def click():
    root = tk.Toplevel()
    root.geometry("1080x720")
    root.resizable(True,False)
    root.title("Image Filters")
    img_bg = ImageTk.PhotoImage(file = "D:/instagram face filter for intership/insta.png")
    tk.Label(root,image = img_bg).pack()
    hatButton = tk.Button(root, text="GIRL HAT", command=girlhat ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    hatButton.place(x=300, y=500)
    hatButton1 = tk.Button(root, text="HAT", command=hat1 ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    hatButton1.place(x=400, y=500)
    glassButton1 = tk.Button(root, text="GLASS", command=glass_btn ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    glassButton1.place(x=500, y=500)
    dogButton1 = tk.Button(root, text="DOG", command=dog_btn ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    dogButton1.place(x=600, y=500)
    rabButton1 = tk.Button(root, text="RABBIT", command=rab_btn ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    rabButton1.place(x=700, y=500)
    doggyButton1 = tk.Button(root, text="DOGGY", command=doggy_btn ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    doggyButton1.place(x=300, y=600)
    rosesButton1 = tk.Button(root, text="ROSES", command=roses_btn ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    rosesButton1.place(x=400, y=600)
    heartsButton1 = tk.Button(root, text="HEARTS", command=hearts_btn ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    heartsButton1.place(x=500, y=600)
    teethButton1 = tk.Button(root, text="TEETH", command=teeth_btn ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    teethButton1.place(x=600, y=600)
    crownButton1 = tk.Button(root, text="CROWN", command=crown_btn ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    crownButton1.place(x=700, y=600)
 
    
 
##################################################################
   
    #root.resizable(True,False)        
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="WEATHER", command=weather)
    root.config(menu=menubar)
    
    root.mainloop()


window = tk.Toplevel()
window.geometry("1080x720") 
window.resizable(True,False)
window.title("Instagram")
img_bg = ImageTk.PhotoImage(file = "D:/instagram face filter for intership/1112297.png")
tk.Label(window,image = img_bg).pack()
b=tk.Button(window,text="filters",command=click,bg="#ea2a2a" ,activebackground = "white",font=("Bradley Hand ITC",36, ' bold '))
b.place(x=900,y=600)




    
    
    
window.mainloop()   
    
    