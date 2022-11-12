from tkinter import *
import torch
import time
import json
import requests


def Blynk(V,value):
    token="pwy5OAsSnkfonFciS4xCzS-sOo2LFSWw"
    read ="https://blynk.cloud/external/api/update?token="+token+"&"+V+"="+value
    read =requests.request("GET",read)
    
def function_gui():
    global colour
    win= Tk()
    win.geometry("600x600")
    canvas=Canvas(win, width=600, height=600)
    canvas.pack()
    canvas.create_line(125,0,125,250, fill="black", width=250)
    canvas.create_line(250,475,0,475, fill="black", width=250)
    canvas.create_line(475,0,475,250, fill="black", width=250)
    canvas.create_line(350,475,600,475, fill="black", width=250)
    canvas.create_line(250,246,350,246, fill="white", width=5)
    canvas.create_line(246,250,246,350, fill="white", width=5)
    canvas.create_line(250,354,350,354, fill="white", width=5)
    canvas.create_line(354,250,354,350, fill="white", width=5)

    canvas.create_line(300,0,300,48, fill="white", width=5)
    canvas.create_line(300,100,300,148, fill="white", width=5)
    canvas.create_line(300,200,300,248, fill="white", width=5)

    canvas.create_line(300,352,300,400, fill="white", width=5)
    canvas.create_line(300,452,300,500, fill="white", width=5)
    canvas.create_line(300,552,300,600, fill="white", width=5)

    canvas.create_line(0,300,48,300, fill="white", width=5)
    canvas.create_line(100,300,148,300, fill="white", width=5)
    canvas.create_line(200,300,248,300, fill="white", width=5)

    canvas.create_line(352,300,400,300, fill="white", width=5)
    canvas.create_line(452,300,500,300, fill="white", width=5)
    canvas.create_line(552,300,600,300, fill="white", width=5)
    l1=canvas.create_oval(355,255,370,270, fill=colour[3])
    l2=canvas.create_oval(330,355,345,370, fill=colour[0])
    l3=canvas.create_oval(230,330,245,345, fill=colour[1])
    l4=canvas.create_oval(255,230,270,245, fill=colour[2])
    #canvas.update(l4,'green')


    canvas.create_text(300, 50, text="Lane 1", fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(300, 550, text="Lane 3", fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(470, 300, text="Lane 2", fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(120, 300, text="Lane 4", fill="black", font=('Helvetica 15 bold'))



def model():
    global colour
    path_yolov5=r'C:\Users\Chaitanya\Downloads\HallothonColab\Hallothon\yolov5-master'

    model = torch.hub.load(r''+path_yolov5,'custom',path=r''+path_yolov5+r'\best.pt', source='local')
    img = '14.jpg'
    img2='download.jpg'
    img1='truck1.jpg'
    img3='bike(1).jpeg'
    results = model(img)
    a=str(results)
    a=a.split()

    b=[0,0,0,0,0]

    sum1=[0,0,0,0]
    colour=['red','red','red','red']

    for i in range(3,len(a)):
        if a[i]=='Speed:':
            break
        else:
            if a[i]=='Bike':
                b[0]=a[i-1]
                sum1[0]+=int(b[0])
            elif a[i]=='Car':
                b[1]=a[i-1]
                sum1[0]+=int(b[1])*2
            elif a[i]=='Bus':
                b[2]=a[i-1]
                sum1[0]+=int(b[2])*3
            elif a[i]=='Truck':
                b[3]=a[i-1]
                sum1[0]+=int(b[3])*4
            elif a[i]=='Ambulance':
                 b[4]=a[i-1]
    print(b)


    a=""
    results = model(img1)
    a=str(results)
    a=a.split()

    b1=[0,0,0,0,0]



    for i in range(3,len(a)):
        if a[i]=='Speed:':
            break
        else:
            if a[i]=='Bike':
                b1[0]=a[i-1]
                sum1[1]+=int(b1[0])
            elif a[i]=='Car':
                b1[1]=a[i-1]
                sum1[1]+=int(b1[1])*2
            elif a[i]=='Bus':
                b1[2]=a[i-1]
                sum1[1]+=int(b1[2])*3
            elif a[i]=='Truck':
                b1[3]=a[i-1]
                sum1[1]+=int(b1[3])*4
            elif a[i]=='Ambulance':
                 b1[4]=a[i-1]
    print(b1)

    a=""

    results = model(img2)
    a=str(results)
    a=a.split()

    b2=[0,0,0,0,0]



    for i in range(3,len(a)):
        if a[i]=='Speed:':
            break
        else:
            if a[i]=='Bike':
                b2[0]=a[i-1]
                sum1[2]+=int(b2[0])
            elif a[i]=='Car':
                b2[1]=a[i-1]
                sum1[2]+=int(b2[1])*2
            elif a[i]=='Bus':
                b2[2]=a[i-1]
                sum1[2]+=int(b2[2])*3
            elif a[i]=='Truck':
                b2[3]=a[i-1]
                sum1[2]+=int(b2[3])*4
            elif a[i]=='Ambulance':
                 b2[4]=a[i-1]

    print(b2)

    a=""

    results = model(img3)
    a=str(results)
    a=a.split()

    b3=[0,0,0,0,0]



    for i in range(3,len(a)):
        if a[i]=='Speed:':
            break
        else:
            if a[i]=='Bike':
                b3[0]=a[i-1]
                sum1[3]+=int(b3[0])
            elif a[i]=='Car':
                b3[1]=a[i-1]
                sum1[3]+=int(b3[1])*2
            elif a[i]=='Bus':
                b3[2]=a[i-1]
                sum1[3]+=int(b3[2])*3
            elif a[i]=='Truck':
                b3[3]=a[i-1]
                sum1[3]+=int(b3[3])*4
            elif a[i]=='Ambulance':
                 b3[4]=a[i-1]

    print(b3)
    print(sum1)
    for i in range (0,4):
        if(sum1[i]==max(sum1)):
            colour[i]='green'




    Blynk("v0",str(sum1[0]))
    Blynk("v1",str(sum1[1]))
    Blynk("v2",str(sum1[2]))
    Blynk("v3",str(sum1[3]))


    #min1=min(sum1)
    #print(min1)


    if (int(b[4])>0):
        colour=['red','red','red','red']
        colour[0]='green'
    elif int(b1[4])>0:
        colour=['red','red','red','red']
        colour[1]='green'
    elif int(b2[4])>0:
        colour=['red','red','red','red']
        colour[2]='green'
    elif int(b3[4])>0:
        colour=['red','red','red','red']
        colour[3]='green'
    print(colour)      
    function_gui()
    
    #colour=['red','red','red','red']
    
    #function_gui()
model()

