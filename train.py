from tkinter import *
import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import ImageTk,Image
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import os


window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Face_Recogniser")
window.iconbitmap("")

img1=ImageTk.PhotoImage(Image.open("images/back3.jpg"))
my_label=Label(image=img1)
my_label.pack()



#dialog_title = 'QUIT'
#dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('1280x720')
window.configure(background='white')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="Student Attendance based on Face Recognition" ,bg="#F0BE2E"  ,fg="black"  ,width=60  ,height=2,font=('times', 15, ' italic bold')) 
message.place(x=300, y=30)

#path = "profile.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(window, image = img)


#panel.pack(side = "left", fill = "y", expand = "no")

#cv_img = cv2.imread("img541.jpg")
#x, y, no_channels = cv_img.shape
#canvas = tk.Canvas(window, width = x, height =y)
#canvas.pack(side="left")
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img)) 
# Add a PhotoImage to the Canvas
#canvas.create_image(0, 0, image=photo, anchor=tk.NW)

#msg = Message(window, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)


def register():
    top = tk.Tk()
    #helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
    top.title("Registration")

    
    #answer = messagebox.askquestion(dialog_title, dialog_text)
 
    #top.configure(background='#CCCCFF')
   
    top.geometry('1280x720')
    top.configure(background='white')

   
    top.grid_rowconfigure(0, weight=1)
    top.grid_columnconfigure(0, weight=1)
    top_frame = Label(top, text='Student Registration',font = ('times', 15, 'italic bold'), bg='#F0BE2E',relief='groove',height=2,width=79)
    top_frame.pack(side='top')
    #message = tk.Label(top, text="Student Registration" ,bg="#F0BE2E"  ,fg="black"  ,width=40  ,height=2,font=('times', 15, 'italic bold')) 
    #message.place(x=300, y=30)

    
    
    lbl = tk.Label(top, text="Enter ID",width=20  ,height=2  ,fg="black"  ,bg="#F0BE2E" ,font=('times', 12, ' bold ') ) 
    lbl.place(x=200, y=100)

    txt = tk.Entry(top,width=20  ,bg="#F0BE2E" ,fg="black",font=('times', 12, ' bold '))
    txt.place(x=500, y=100)

    lbl2 = tk.Label(top, text="Enter Name",width=20  ,fg="black"  ,bg="#F0BE2E"    ,height=2 ,font=('times', 12, ' bold ')) 
    lbl2.place(x=200, y=175)

    txt2 = tk.Entry(top,width=20  ,bg="#F0BE2E"  ,fg="black",font=('times', 12, ' bold ')  )
    txt2.place(x=500, y=175)

    lbl5 = tk.Label(top, text="Enter Mail",width=20  ,fg="black"  ,bg="#F0BE2E",height=2 ,font=('times', 12, ' bold ')) 
    lbl5.place(x=200, y=250)

    txt5 = tk.Entry(top,width=20  ,bg="#F0BE2E"  ,fg="black",font=('times', 12, ' bold ')  )
    txt5.place(x=500, y=250)

    lbl4 = tk.Label(top, text="Enter number",width=20  ,fg="black"  ,bg="#F0BE2E"   ,height=2 ,font=('times', 12, ' bold ')) 
    lbl4.place(x=200, y=325)

    txt4 = tk.Entry(top,width=20  ,bg="#F0BE2E"  ,fg="black",font=('times', 12, ' bold ')  )
    txt4.place(x=500, y=325)

    lbl3 = tk.Label(top, text="Notification : ",width=20  ,fg="black"  ,bg="#F0BE2E"  ,height=2 ,font=('times', 12, ' bold  ')) 
    lbl3.place(x=200, y=400)

    message = tk.Label(top, text="" ,bg="#F0BE2E"  ,fg="black"  ,width=30  ,height=2, font=('times', 12, ' bold ')) 
    message.place(x=500, y=400)

    lbl3 = tk.Label(top, text="Attendance : ",width=20  ,fg="black"  ,bg="#F0BE2E"  ,height=2 ,font=('times', 12, ' bold  ')) 
    lbl3.place(x=200, y=475)

    message2 = tk.Label(top, text="" ,fg="black"   ,bg="#F0BE2E",width=30  ,height=2  ,font=('times', 12, ' bold ')) 
    message2.place(x=500, y=475)

   
    def clear():
        txt.delete(0, 'end')    
        res = ""
        message.configure(text= res)

    def clear2():
        txt2.delete(0, 'end')    
        res = ""
        message.configure(text= res)    
    
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
 
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
 
        return False
    clearButton = tk.Button(top, text="Clear", command=clear  ,fg="black"  ,bg="#F0BE2E"  ,width=20  ,height=2  ,font=('times', 12, ' bold '))
    clearButton.place(x=800, y=100)
    
    clearButton2 = tk.Button(top, text="Clear", command=clear2  ,fg="black"  ,bg="#F0BE2E"  ,width=20  ,height=2 ,font=('times', 12, ' bold '))
    clearButton2.place(x=800, y=175)
 
    def TakeImages():
        
        Id=(txt.get())
        name=(txt2.get())
        mail=(txt5.get())
        pnumber=(txt4.get())
        if(is_number(Id) and name.isalpha() and is_number(pnumber) ):
            cam = cv2.VideoCapture(0) #open webcam wih default id=0
            cam.set(3,700)
            cam.set(4,500)
            harcascadePath = (r"D:\drowsy\python_env\FaceTrain\haarcascade_frontalface_default.xml")
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                    sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite(r"D:\drowsy\python_env\FaceTrain\TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                    cv2.imshow('frame',img)
            #wait for 100 miliseconds 
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
            # break if the sample number is morethan 100
                elif sampleNum>60:
                    break
            cam.release()
            cv2.destroyAllWindows() 
            res = "Images Saved for ID : " + Id +" Name : "+ name
            row = [Id , name, mail, pnumber]
            with open(r'D:\drowsy\python_env\FaceTrain\StudentDetails\StudentDetails.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message.configure(text= res)
        else:
            if(is_number(Id) and is_number(pnumber)):
                res = "Enter Alphabetical Name"
                message.configure(text= res)
            if(name.isalpha()):
                res = "Enter Numeric form"
                message.configure(text= res)
   
    #img2=ImageTk.PhotoImage(Image.open("images/take.png"))
    takeImg =tk.Button(top,command=TakeImages,text="Take images",font=('times', 12, ' bold '),bg="#F0BE2E"  ,fg="black"  ,width=28  ,height=8)
    takeImg.place(x=850, y=350)
    

    go_back=tk.Button(top, text="Back", font=('times', 12, ' bold '),command=top.destroy,bg="#F0BE2E"  ,fg="black",width=20  ,height=2)
    go_back.place(x=500,y=575)
    
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer=cv2.createLBPHFaceRecognizer()
    harcascadePath = (r"D:\drowsy\python_env\FaceTrain\haarcascade_frontalface_default.xml")
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels(r"D:\drowsy\python_env\FaceTrain\TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save(r"D:\drowsy\python_env\FaceTrain\TrainingImageLabel\Trainner.yml")
    res = "Image Trained"#+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read(r"D:\drowsy\python_env\FaceTrain\TrainingImageLabel\Trainner.yml")
    harcascadePath = (r"D:\drowsy\python_env\FaceTrain\haarcascade_frontalface_default.xml")
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv(r'D:\drowsy\python_env\FaceTrain\StudentDetails\StudentDetails.csv')
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','mail','pnumber','Date','Time']
    colnoti_names=['Id','Name','Mail','pnumber']
    attendance = pd.DataFrame(columns = col_names)
    notification=pd.DataFrame(columns=colnoti_names)   
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values 
                bb=df.loc[df['Id'] == Id]['mail'].values
                cc=df.loc[df['Id'] == Id]['pnumber'].values 

                naa=df.loc[df['Id'] != Id]['Name'].values 
                nbb=df.loc[df['Id'] != Id]['mail'].values
                ncc=df.loc[df['Id'] != Id]['pnumber'].values 
                
                tt=str(Id)+"-"+aa 
                attendance.loc[len(attendance)] = [Id,aa,bb,cc,date,timeStamp]
                notification.loc[len(notification)]=[Id,naa,nbb,ncc]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir(r"D:\drowsy\python_env\FaceTrain\ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
       
        
        notification=notification.drop_duplicates(subset=['Id'],keep='first')  
         
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName=r"D:\drowsy\python_env\FaceTrain\Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    fileNames=r"D:\drowsy\python_env\FaceTrain\Notification\Notification_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    print(attendance.id)       
    attendance.to_csv(fileName,index=False)
    notification.to_csv(fileNames,index=False)
    
    cam.release()
    cv2.destroyAllWindows()
    os.system("python dr.py")
    #print(attendance)
    res=attendance
    message2.configure(text= res)

  
lbl3 = tk.Label(window, text="Notification : ",bg="#F0BE2E"  ,fg="black" ,width=20 ,height=2 ,font=('times', 12, ' bold')) 
lbl3.place(x=200, y=450)

message = tk.Label(window, text="" ,bg="#F0BE2E"  ,fg="black"  ,width=30  ,height=2,font=('times', 12, ' bold ')) 
message.place(x=500, y=450)

lbl3 = tk.Label(window, text="Attendance : ",width=20  ,bg="#F0BE2E"  ,fg="black"  ,height=2 ,font=('times', 12, ' bold')) 
lbl3.place(x=200, y=550)

message2 = tk.Label(window, text="" ,bg="#F0BE2E"  ,fg="black",width=30  ,height=2  ,font=('times', 12, ' bold ')) 
message2.place(x=500, y=547)

 
img3=ImageTk.PhotoImage(Image.open("images/train.jpg"))
trainImg = tk.Button(window, text="Train Images", image=img3, command=TrainImages,font=('times', 12, ' bold '))
trainImg.place(x=500, y=150)

img4=ImageTk.PhotoImage(Image.open("images/face.jpg"))
trackImg = tk.Button(window, text="Track Images", image=img4,command=TrackImages,font=('times', 12, ' bold '))
trackImg.place(x=900, y=150)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,bg="#F0BE2E"  ,fg="black"  ,width=20  ,height=3, activebackground = "white" ,font=('times', 12, ' bold '))
quitWindow.place(x=900, y=450)

img5=ImageTk.PhotoImage(Image.open("images/regis3.jpg"))
register_info= tk.Button(window,text="Register",image=img5, command=register,font=('times', 12, ' bold '))
register_info.place(x=110, y=150)

#copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('times', 30, 'italic bold underline'))
#copyWrite.tag_configure("superscript", offset=10)
#copyWrite.insert("insert", "Developed by Ashish","", "TEAM", "superscript")
#copyWrite.configure(state="disabled",fg="red"  )
#copyWrite.pack(side="left")
#copyWrite.place(x=800, y=750)
 
window.mainloop()