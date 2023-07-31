import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import*
import cvzone

model=YOLO('yolov8s.pt')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)


my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 

count=0

tracker=Tracker()

total_people={}
counter=[]
   
cap= cv2.VideoCapture("people.mp4")
while True:
    success,frame = cap.read()
    if not success:
        break
    count += 1
    frame=cv2.resize(frame,(1020,500))
    results=model.predict(frame)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
    list=[]         
    for index,row in px.iterrows():
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        if 'person' in c:
            list.append([x1,y1,x2,y2])   
    bbox_id=tracker.update(list)
    for bbox in bbox_id:
        x3,y3,x4,y4,id=bbox
        total_people[id]=(x4,y4)
        cv2.rectangle(frame,(x3,y3),(x4,y4),(255,0,255),1)
        cv2.circle(frame,(x4,y4),4,(255,0,0),-1)
        cvzone.putTextRect(frame,f'{id}',(x3,y3),1,2)
        if id in total_people:
            if counter.count(id)==0:  
                counter.append(id)    
    print("Total  number of people in the frame: " + str(len(list)))             
    if success:
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==27:
            break  
    print(len(counter))         
cap.release()
cv2.destroyAllWindows()        
