import tkinter as tk
from PIL import Image, ImageTk
import time
from tkinter import Frame
from tkinter import Text
from tkinter import Label
from tkinter import BOTH, END, LEFT
from tkinter import messagebox

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def naivebayes():

    path= "https://github.com/NStugard/Intro-to-Machine-Learning/raw/main/spam.csv"
    dataset= pd.read_csv(path)
    dataset["Spam"]= dataset["Category"].apply(lambda x: 1 if x == "spam" else 0)

    x_train, x_test, y_train, y_test= train_test_split(dataset.Message, dataset.Spam, test_size= 0.25)

    vect= CountVectorizer()
    x_count= vect.fit_transform(x_train.values)
    x_count.toarray()

    nb= MultinomialNB()
    nb.fit(x_count, y_train)
    
    test_count= vect.transform(x_test)
    global acc
    acc= nb.score(test_count, y_test)*100

    INPUT= txt.get("1.0", "end-1c")
    mail= []
    mail.append(INPUT)
    mail_count= vect.transform(mail)
    val= nb.predict(mail_count)
    if val == 1:
        return 1
    else:
        return 0

def reset():

    snd.delete("1.0", END)
    sub.delete("1.0", END)
    txt.delete("1.0", END)

def send():

    val= naivebayes()
    if val == 1:
        messagebox.showwarning("Warning", "SPAM MAIL!!\nAccuracy: " + str(acc) + "\nWant to continue?")
    
    reset()    

def compose():

    root= tk.Toplevel()
    root.geometry("700x467")
    root.title("Compose Mail")
    bg_image = Image.open("bgcompose.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
   
    slbl= Label(root, text= "From: xyz@gmail.com", font= ("Helvetica",12))
    slbl.place(x= 5, y= 100)

    global snd, sub
    slbl= Label(root, text= "To:", font= ("Helvetica",12))
    slbl.place(x= 5, y= 150)

    snd= Text(root, height= 1, width= 35, font= ("Helvetica",13))
    snd.place(x= 40, y= 150)

    sublbl= Label(root, text= "Subject:", font= ("Helvetica",12))
    sublbl.place(x= 5, y= 200)

    sub= Text(root, height= 1, width= 31, font= ("Helvetica",13))
    sub.place(x= 75, y= 200)

    lbl= Label(root, text= "Body", font= ("Helvetica",12))
    lbl.place(x= 5, y= 250)

    global txt
    txt= Text(root, height= 6, width= 40, font= ("Helvetica",13))
    txt.place(x= 5, y= 275)

    button_image= Image.open("send.png")
    button_photo= ImageTk.PhotoImage(button_image)
    button= tk.Button(root, image= button_photo, bd= 0, highlightthickness= 0, highlightbackground= "#ffffff", bg= "#ffffff", activebackground= "#ffffff", relief= "flat", font= ("Helvetica", 12), command= lambda: send())
    button.place(x= 25, y= 400)

    button2_image= Image.open("delete.png")
    button2_photo= ImageTk.PhotoImage(button2_image)
    button2= tk.Button(root, image= button2_photo, bd= 0, highlightthickness= 0, highlightbackground= "#ffffff", bg= "#ffffff", activebackground= "#ffffff", relief= "flat", font= ("Helvetica", 12), command= lambda: reset())
    button2.place(x= 175, y= 400)

    button3_image= Image.open("exit.png")
    button3_photo= ImageTk.PhotoImage(button3_image)
    button3= tk.Button(root, image= button3_photo, bd= 0, highlightthickness= 0, highlightbackground= "#ffffff", bg= "#ffffff", activebackground= "#ffffff", relief= "flat", font= ("Helvetica", 12), command= root.destroy)
    button3.place(x= 650, y= 420)

    root.mainloop()

root= tk.Tk()

root.geometry("1000x666")
root.title("Spam Mail Classifier")
bg_image= Image.open("bg.png")
bg_photo= ImageTk.PhotoImage(bg_image)
bg_label= tk.Label(root, image=bg_photo)
bg_label.place(x= 0, y= 0, relwidth= 1, relheight= 1)

button_image= Image.open("comp.png")
button_photo= ImageTk.PhotoImage(button_image)
button= tk.Button(root, image= button_photo, bd= 0, highlightthickness= 0, highlightbackground= "#ffffff", bg= "#ffffff", activebackground= "#ffffff", relief= "flat", command= compose)
button.place(x= 350, y= 450)

def update_time():

    current_time= time.strftime("%H:%M %p")
    current_day= time.strftime("%A")
    time_label.config(text=f"{current_time}\n{current_day}")
    root.after(1000, update_time)

time_label= tk.Label(root, font=("DS-Digital", 20), fg= "black")
time_label.pack(side= tk.RIGHT, anchor= tk.SE, padx= 10, pady= 10)

update_time()
root.mainloop()