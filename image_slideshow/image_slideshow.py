#!/usr/bin/env python
# coding: utf-8

# In[2]:

transition_time = 2


# RUN THIS FIRST (one time installation)
# pip install opencv-python


# In[1]:


import glob
import cv2
import numpy as np
import pandas as pd
import random
import time
import subprocess
import pickle

from PIL import ImageTk, Image

from tkinter import *  
import tkinter
import sys
from PIL import ImageTk,Image
import pathlib


try:
    # Load dataframe from pickled pandas object
    df= pd.read_pickle("PictureLibrary.plk")
except:
    directory = 'C:\\Users\\Kevin\\Documents\\image-slideshow\\pictures\\**/'
    img_types = ('*.png', '*.jpg', '*.jpeg') # not type sensitive
    img_list, img_titles = [], []
    for i in img_types:
        #img_list.extend(list(map(cv2.imread, glob.glob(directory + i, recursive=True))))
        img_titles.extend(list(glob.glob(directory + i, recursive=True)))
        


    # #### Image dimensions

    # In[5]:


    import collections

    column_names = ["Filename", "Width", "Height", "Ratio"]
    df = pd.DataFrame(columns = column_names)
    for title in img_titles:
        try:
            im = Image.open(title)
            width, height = im.size
            ratio = width / height
            df.loc[len(df)] = [title, width, height, ratio]
            
        except:
            print(i)
            img_titles.remove(i)
            
    df["Available"] = 1


    # In[8]:


    # Save dataframe to pickled pandas object
    df.to_pickle("PictureLibrary.plk") # where to save it usually as a .plk


# In[3]:

vert = df[df["Ratio"] < 1.0].reset_index()
hori = df[df["Ratio"] > 1.0].reset_index()
#vert = df[df["Ratio"] == 3/4].reset_index()
#hori = df[df["Ratio"] == 4/3].reset_index()
vert_len = len(vert) - 1
hori_len = len(hori) - 1



# ### Horizontal favored slideshow

# In[6]:


def close(event):
    root.destroy() # if you want to bring it back
    #sys.exit() # if you want to exit the entire thing

def find_image(end_index, df):
    while True:
        i = random.randint(0, end_index)
        if (df["Available"][i] == 1):
            df["Available"][i] = 0
            return Image.open(df["Filename"][i]), df
        if (df["Available"].sum() == 0):
            df["Available"] = 1
    return 0

root = Tk()  
root.bind('<Escape>', close)
root.attributes("-fullscreen", True)
canvas = Canvas(root, width = 1920, height = 1080, highlightthickness=0)  
canvas.configure(background='black')
canvas.pack()  

df["Available"] = 1

for _ in np.arange(5000000):
    rand_i = random.randint(1, 16)
    canvas.delete("all")
    #tk_img1 = tk_img2 = tk_img3 = tk_img4 = None

    # Horizontal image is saved for tk_img4, the other 3 will be vertical.
    ###imgV, vert = find_image(vert_len, vert)
    ###img1, hori = find_image(hori_len, hori)
    ###img2, hori = find_image(hori_len, hori)
    ###img3, hori = find_image(hori_len, hori)
    ###img4, hori = find_image(hori_len, hori)
    ###img5, hori = find_image(hori_len, hori)
    

    if (rand_i == 1 or rand_i == 2):
        # FORMATION D 
        img1, hori = find_image(hori_len, hori)
        
        resize_img2 = img1.resize((1440, 1050))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image(260, 15, anchor=NW, image=tk_img2)  

    elif (rand_i == 3 or rand_i == 4):
        # FORMATION H 
        img1, hori = find_image(hori_len, hori)
        img2, hori = find_image(hori_len, hori)
        img3, hori = find_image(hori_len, hori)
    
        resize_img2 = img1.resize((940, 705))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image((1920/2) - (940 + 10), 10, anchor=NW, image=tk_img2) 

        resize_img3 = img2.resize((940, 705))
        tk_img3 = ImageTk.PhotoImage(resize_img3)  
        canvas.create_image((1920/2 + 10), 10, anchor=NW, image=tk_img3)

        resize_img1 = img3.resize((460, 345))
        tk_img1 = ImageTk.PhotoImage(resize_img1)  
        canvas.create_image((1920-460)/2, 10 + 705 + 10, anchor=NW, image=tk_img1) 

    elif (rand_i == 5 or rand_i == 6):
        # FORMATION J
        img1, hori = find_image(hori_len, hori)
        img2, hori = find_image(hori_len, hori)
        img3, hori = find_image(hori_len, hori)
        img4, hori = find_image(hori_len, hori)
    
        resize_img1 = img4.resize((945, 525))
        tk_img1 = ImageTk.PhotoImage(resize_img1)  
        canvas.create_image(0, 0, anchor=NW, image=tk_img1)  

        resize_img2 = img1.resize((945, 525))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image(0, 525 + 20, anchor=NW, image=tk_img2) 

        resize_img3 = img2.resize((945, 525))
        tk_img3 = ImageTk.PhotoImage(resize_img3) 
        canvas.create_image(945 + 20, 0, anchor=NW, image=tk_img3) 

        resize_img4 = img3.resize((945, 525))
        tk_img4 = ImageTk.PhotoImage(resize_img4) 
        canvas.create_image(945 + 20, 525 + 20, anchor=NW, image=tk_img4) 

    elif (rand_i == 7 or rand_i == 8):
        # FORMATION K / L
        img1, hori = find_image(hori_len, hori)
        img2, hori = find_image(hori_len, hori)
        img3, hori = find_image(hori_len, hori)
        
        if (rand_i == 7):
            switcher = 1
        elif (rand_i == 8):
            switcher = 0
        else:
            print("Error")
    
        resize_img2 = img1.resize((1197, 898))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image(10 + (1-switcher) * (10 + 693), 91, anchor=NW, image=tk_img2) 

        resize_img3 = img2.resize((693, 520))
        tk_img3 = ImageTk.PhotoImage(resize_img3)  
        canvas.create_image(10 + switcher * (10 + 1197), 10, anchor=NW, image=tk_img3)

        resize_img1 = img3.resize((693, 520))
        tk_img1 = ImageTk.PhotoImage(resize_img1)  
        canvas.create_image(10 + switcher * (10 + 1197), 10 + 520 + 20, anchor=NW, image=tk_img1) 
    
    elif ((rand_i >= 9) and (rand_i <= 16)):
        # FORMATION K / L
        img1, hori = find_image(hori_len, hori)
        img2, hori = find_image(hori_len, hori)
        img3, hori = find_image(hori_len, hori)
        
        if (rand_i % 2 == 0):
            switcher_LR = 1
        else:
            switcher_LR = 0
            
        if (rand_i % 4 <= 1):
            switcher_UD = 1
        else:
            switcher_UD = 0
    
        #big right
        resize_img2 = img1.resize((802, 601))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image(10 + 204 + (1-switcher_LR) * (10 + 700), 10 + (1-switcher_UD) * (10 + 439 + 10), anchor=NW, image=tk_img2) 

        #small right
        resize_img3 = img2.resize((585, 439))
        tk_img3 = ImageTk.PhotoImage(resize_img3)  
        canvas.create_image(10 + (1-switcher_LR) * (10 + 700 + 20), (switcher_UD) * (10 + 601 + 10), anchor=NW, image=tk_img3)

        resize_img1 = img3.resize((585, 439))
        tk_img1 = ImageTk.PhotoImage(resize_img1)  
        canvas.create_image(10 + 585 + 10 + (1-switcher_LR) * (10 + 700 + 20), (switcher_UD) * (10 + 601 + 10), anchor=NW, image=tk_img1) 
        
        #left
        if (rand_i <= 12):
            img4, hori = find_image(hori_len, hori)
            img5, hori = find_image(hori_len, hori)
        
            resize_img4 = img4.resize((700, 525))
            tk_img4 = ImageTk.PhotoImage(resize_img4)  
            canvas.create_image(10 + (switcher_LR) * (585 + 10 + 585 + 10), 10, anchor=NW, image=tk_img4)
            
            resize_img5 = img5.resize((700, 525))
            tk_img5 = ImageTk.PhotoImage(resize_img5)  
            canvas.create_image(10 + (switcher_LR) * (585 + 10 + 585 + 10), 10 + 525 + 10, anchor=NW, image=tk_img5)
        else:
            imgV, vert = find_image(vert_len, vert)
            
            resize_img4 = imgV.resize((700, 934))
            tk_img4 = ImageTk.PhotoImage(resize_img4)  
            canvas.create_image(10 + (switcher_LR) * (585 + 10 + 585 + 10), 73, anchor=NW, image=tk_img4)
        
    root.update()
    time.sleep(transition_time)
    
    
        


root.focus_force()
    
root.mainloop() 


# ### Vertical favored slideshow

# In[9]:


'''
transition_time = 2

def close(event):
    root.destroy() # if you want to bring it back
    #sys.exit() # if you want to exit the entire thing

def find_image(end_index, df):
    while True:
        i = random.randint(0, end_index)
        if (df["Available"][i] == 1):
            df["Available"][i] = 0
            return Image.open(df["Filename"][i]), df
        if (df["Available"].sum() == 0):
            df["Available"] = 1
    return 0

root = Tk()  
root.bind('<Escape>', close)
root.attributes("-fullscreen", True)
canvas = Canvas(root, width = 1920, height = 1080, highlightthickness=0)  
canvas.configure(background='black')
canvas.pack()  

df["Available"] = 1

for _ in np.arange(5000000):
    rand_i = random.randint(1, 8)
    canvas.delete("all")
    #tk_img1 = tk_img2 = tk_img3 = tk_img4 = None

    # Horizontal image is saved for tk_img4, the other 3 will be vertical.
    ###imgH, hori = find_image(hori_len, hori)
    ###img1, vert = find_image(vert_len, vert)
    ###img2, vert = find_image(vert_len, vert)
    ###img3, vert = find_image(vert_len, vert)
    

    if (rand_i == 1):
        # FORMATION A
        imgH, hori = find_image(hori_len, hori)
        img1, vert = find_image(vert_len, vert)
    
        resize_img1 = img1.resize((688, 917))
        tk_img1 = ImageTk.PhotoImage(resize_img1)  
        canvas.create_image(0, (1080-917)/2, anchor=NW, image=tk_img1)  

        resize_img2 = imgH.resize((1223, 917))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image(917*3/4+10, (1080-917)/2, anchor=NW, image=tk_img2) 

    elif (rand_i == 2):
        # FORMATION A
        imgH, hori = find_image(hori_len, hori)
        img1, vert = find_image(vert_len, vert)
    
        resize_img1 = imgH.resize((1223, 917))
        tk_img1 = ImageTk.PhotoImage(resize_img1)  
        canvas.create_image(0, (1080-917)/2, anchor=NW, image=tk_img1)  

        resize_img2 = img1.resize((688, 917))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image(917*4/3+10, (1080-917)/2, anchor=NW, image=tk_img2) 

    elif (rand_i == 3):
        # FORMATION B
        imgH, hori = find_image(hori_len, hori)
        img1, vert = find_image(vert_len, vert)
        img2, vert = find_image(vert_len, vert)
        img3, vert = find_image(vert_len, vert)
    
        resize_img1 = imgH.resize((560, 420))
        tk_img1 = ImageTk.PhotoImage(resize_img1)  
        canvas.create_image((1920-560)/2, 0, anchor=NW, image=tk_img1)  

        resize_img2 = img1.resize((488, 650))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image((1920/2) - (488/2 + 488 + 30), 430, anchor=NW, image=tk_img2) 

        resize_img3 = img2.resize((488, 650))
        tk_img3 = ImageTk.PhotoImage(resize_img3) 
        canvas.create_image((1920/2) - (488/2), 430, anchor=NW, image=tk_img3) 

        resize_img4 = img3.resize((488, 650))
        tk_img4 = ImageTk.PhotoImage(resize_img4) 
        canvas.create_image((1920/2) - (488/2 - 488 - 30), 430, anchor=NW, image=tk_img4) 

    elif (rand_i == 4):
        # FORMATION C 
        imgH, hori = find_image(hori_len, hori)
        img1, vert = find_image(vert_len, vert)
        img2, vert = find_image(vert_len, vert)
    
        resize_img2 = img1.resize((488, 650))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image((1920/2) - (488 + 40), 0, anchor=NW, image=tk_img2) 

        resize_img3 = img2.resize((488, 650))
        tk_img3 = ImageTk.PhotoImage(resize_img3)  
        canvas.create_image((1920/2 + 40), 0, anchor=NW, image=tk_img3)

        resize_img1 = imgH.resize((560, 420))
        tk_img1 = ImageTk.PhotoImage(resize_img1)  
        canvas.create_image((1920-560)/2, 660, anchor=NW, image=tk_img1) 

    elif (rand_i == 5):
        # FORMATION D 
        imgH, hori = find_image(hori_len, hori)
        
        resize_img2 = imgH.resize((1440, 1050))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image(260, 15, anchor=NW, image=tk_img2) 

    elif (rand_i == 6):
        # FORMATION E 
        img1, vert = find_image(vert_len, vert)
        img2, vert = find_image(vert_len, vert)
        
        resize_img2 = img2.resize((795, 1060))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image((1920/2) - 795 - 50, 15, anchor=NW, image=tk_img2) 

        resize_img1 = img1.resize((795, 1060))
        tk_img1 = ImageTk.PhotoImage(resize_img1) 
        canvas.create_image((1920)/2 + 50, 15, anchor=NW, image=tk_img1) 

    elif (rand_i == 7 or rand_i == 8):
        # FORMATION G
        img1, vert = find_image(vert_len, vert)
        img2, vert = find_image(vert_len, vert)
        img3, vert = find_image(vert_len, vert)
        
        x = random.randint(0, 1)
        y = random.randint(0, 1)

        resize_img1 = img3.resize((560, 747))
        tk_img1 = ImageTk.PhotoImage(resize_img1)  
        canvas.create_image((1920/2) - (560/2), 10 + np.abs(x - y) * (1080 - 747) / 2 + (1-y) * (1-x) * (1060 - 747), anchor=NW, image=tk_img1) 

        resize_img2 = img1.resize((660, 880))
        tk_img2 = ImageTk.PhotoImage(resize_img2)  
        canvas.create_image((1920/2) - (560/2 + 660 + 10), y * (1080 - 880 + 10), anchor=NW, image=tk_img2) 

        resize_img3 = img2.resize((660, 880))
        tk_img3 = ImageTk.PhotoImage(resize_img3)  
        canvas.create_image((1920/2) + (560/2 + 10), x * (1080 - 880 + 10), anchor=NW, image=tk_img3) 
        
    root.update()
    time.sleep(transition_time)
    
    
        


root.focus_force()
    
root.mainloop() 
    
  ''' 


