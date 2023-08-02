# People detection and Counting using YOLO and CNN

This repository contains the code for a people counting and detection project. 

## Introduction

The project involves using YOLOv8 to count the number of people in a video and another custom model to detect the number of people in each frame of the video. The data generated from this process is used to create a dataset, which, in turn, is used to train and test a Convolutional Neural Network (CNN) model.

## Requirements

- Python3 (version 3.10.2)
- TensorFlow (Deep Learning Framework)
- NumPy 
- OpenCV

## Details

### Model 1
The initial model employs YOLOv8, a state-of-the-art object detection algorithm, to perform real-time detection and counting of individuals within a predefined region of interest. Additionally, a tracking mechanism is integrated to precisely monitor the spatial movement and positions of each detected person within the frame.

- The initial phase encompasses the importation of the YOLO and OpenCV libraries.
- The video stream is ingested through OpenCV, and individual frames are extracted from the video stream.
- The YOLO model is then executed on each frame to perform object detection.
- In the subsequent stage, a tracking mechanism is employed, resulting in bounding boxes being delineated around 
  each detected individual to facilitate their spatial monitoring and positional determination within the frame. 
- A unique identifier is assigned to each person, enabling their distinct monitoring throughout the video.
- Ultimately, the count of individuals is obtained by aggregating their unique identifiers into a list, and the 
  length of this list is printed, reflecting the total count of detected persons.

### Model 2
The subsequent model leverages the capabilities of OpenCV to extract a dataset from the same video source by capturing individual images from each frame. These captured images constitute the dataset that will be used for further analysis. Next, a Convolutional Neural Network (CNN) model is utilized to conduct accuracy testing on this dataset. The CNN model, being a deep learning algorithm specialized for image analysis, will be employed to assess and evaluate the performance of the dataset in terms of its predictive accuracy for the task at hand.

- The initial stage involves data preparation from the video using OpenCV.
- Frames are captured and stored in a CSV file, which is subsequently linked to the drive.
- The images in the dataset are labeled with the corresponding number of people in each frame, achieved through cvlib.
- The dataset is then split into training and testing subsets, and a CNN model is applied to evaluate its accuracy.

## Scope
The enhanced crowd counting project can find practical applications in various domains. In retail settings and events, it can enable data-driven decision-making and enhance operational efficiency. Additionally, the system can be employed for public security purposes, helping in crowd management and surveillance.



