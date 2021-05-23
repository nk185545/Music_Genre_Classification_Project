from django.shortcuts import render
import os
import glob
import numpy as np
from keras.models import load_model
import librosa
import pickle
from .forms import MusicForm
model = load_model("music_generation_classification_model.h5")
lenc = pickle.load(open("labelencoder.p",'rb'))
def index(request) :
    return render(request,"index.html")

def aboutproject(request) :
    return render(request,"aboutproject.html")

def cappredictor(request):
    return render(request,'cappredictor.html')

def feature_extractor(file_name):
    audio,sample_rate = librosa.load(file_name ,res_type ='kaiser_fast')
    mfccs_features = librosa.feature.mfcc(y=audio,sr=sample_rate,n_mfcc =40)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    return mfccs_scaled_features

def predictCaption(request) :
    if request.method == 'POST':
        up_files = glob.glob('static/uploads/*')
        for x in up_files:
            os.remove(x)

        musicObj = MusicForm(request.POST, request.FILES)
        if musicObj.is_valid():
            f = request.FILES['file']

            with open('static/uploads/' + f.name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            aud_path = 'static/uploads/'+str(f)
            audname= str(f)
            audurl="static/uploads/"+audname
            print(audurl)
            filename = audurl
            audio, sample_rate = librosa.load(filename, res_type='kaiser_fast')
            mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
            print(mfccs_features)
            mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)
            mfccs_scaled_features = mfccs_scaled_features.reshape(1, -1)
            predicted_label = model.predict_classes(mfccs_scaled_features)
            print(predicted_label)
            prediction_class = lenc.inverse_transform(predicted_label)
            prediction_class = "Music Genre Is :- "+str(prediction_class[0])

        return render(request, "cappredictor.html",{"audurl":audurl,"predictedMusicType":prediction_class})
    else:
        musicObj = MusicForm()
        return render(request, "cappredictor.html")