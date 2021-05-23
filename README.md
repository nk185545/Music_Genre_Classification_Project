# Music_Genre_Classification_Project

This project is about to classify the music genre (Type). Artificial Neural Network is used to train the model.

Dataset Link : https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification

Libraries used :
    
    1) Numpy
    
    2) OS
    
    3) Tensorflow (Keras)
    
    4) PIL
    
    
Tools used :

    1) Jupyter Notebook
    
    2) Pycharm IDE


Framework used :

    1) Django 
    
    
    
**Project Life Cycle :-**

**1) Data Collection (About Data...) :-** 
 
        a) Data is collected from kaggle.
        
        b) Dataset Link : https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification
        
        c) In data/generas_original, there are 10 folders - those contains 10 types of music(audio files- approx 30sec length). Types are : blues, classicial, country, disco, hiphop, jazz,metal, pop, raggae, rock.
                

**2) Data Preprocessing :-**

    a) First of all make a list named "Class", that contains all 10 types of names.
    
    b) After that, read that folder one by one and pick audio files one by one using OS library.
    
    c) Then read audio files using LIBROSA library. Used mfccs feature provided in librosa library and extracted features from the audio files and make the dataset.
    
    d) Now we have to build model, beacuse we have completed preprocessing to our data.
    
    
    
**3) Model Creation(Train our model):-**

        a) First of all, split tha dataset into train and test set. Used labelencoder for dependent feature.
        
        b) Build Artificial Neural Network model by using Tensorflow(keras) library. Created input layers, hidden layers and output layers.
        
        c) Fit and train the data and save the model in format of .h5 file.
        
        d) Now it's time to predict....
        
    
 **4) Prediction :-**
    
        a) First of all, read the audio file using librosa library.
        
        b) Then extract the mfccs feature from that audio file.
        
        c) then predict the value using our model and perform labelencoder inverse transform to get music type.
        
        
 **At last, using Django framework build the front end and integrate our model in frontend.  (Frontend + Backend)**
 
 **Now our project is completely ready.**
 
 
------------------------------------------------------------------------------------------------------------

**Some Glimpses of Our Project :-**

**1) Home Page :---**
![o1](https://user-images.githubusercontent.com/61588604/119258243-7e411a00-bbe6-11eb-8efe-bbd46f4159eb.png)

![o2](https://user-images.githubusercontent.com/61588604/119258248-81d4a100-bbe6-11eb-9f8d-c5c887eeb3e3.png)

---------------------

**2) Predictor Page :---**

![o3](https://user-images.githubusercontent.com/61588604/119258249-8305ce00-bbe6-11eb-85d4-38780b13e3f8.png)

---------------------

**3) About Project Page:---**

![o4](https://user-images.githubusercontent.com/61588604/119258250-8305ce00-bbe6-11eb-9e08-aac50d031d2d.png)


**<<<<<--------------------------------------------------------------------------------------------------------------->>>>>**
 
