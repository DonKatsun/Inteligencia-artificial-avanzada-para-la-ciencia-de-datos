# Stream flow and Discharge prediction with Machine Learning \& AI

The use of frameworks to implement artificial intelligence and machine learning has been in a raise for the last years, this tools are capable to ease many process like finantial, marketing, health or cyber-security. In this case we used this tools to predict the values of Stage and Discharge of a river when the measeurement sensors fail. This project it's divided in two parts, the first it's intended to replicate values provided by Kenneth W. Chapman. in a CSV. The second part is to predict values making use of images retrieved from de United States Geological Survey. More than 60,000 images and 40,000 values captured by sensors in the river.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The things you need before running the code.

* Anything to run Jupyter Notebooks
* Python 2.7+
* 160 MB Storage

### Documents

* ```CNN_Regresor-Stage: ``` The implementation of the CNN fited for the Stage data 
* ```CNN_Regresor_Discharge: ``` The implementation of the CNN fited for the Discharge data 
* ```crear_CSV:``` This py file helps to create a CSV with the paths of the downloaded images and the Stage/Discharge data from the 2012_2019_PlatteRiverWeir_features_merged_all.csv file
* ```crear_arreglo:``` This file create a npy file with the resize of the images



## Deployment

* You need to download the images and the 2012_2019_PlatteRiverWeir_features_merged_all.csv file
* Then you run the "crear_CSV" file in the same path of the file "2012_2019_PlatteRiverWeir_features_merged_all" and the images, it will output a csv file
* In the same path of the images and the csv file you just created run the file "crear_arreglo" that will output a npy file, then you can discard the downloaded files
* You can now run both CNN
* If you want to see the variable analysis, the MLPRegressor, the SVR or the RFR you must run "Analisis" file 


### Feedback

* ```Big Data, ```--
* ```Deep Learning, Make the dataset smaller:```
We made the images size 100x100 in a gray scale
* ```NLP, Use a CNN:```
We used a CNN Regresor
* ```Statistics, Implement a Yolo algorith to identify the river:```
We made an I'm red filter to identify the river because implement Yolo takes a lot of time


