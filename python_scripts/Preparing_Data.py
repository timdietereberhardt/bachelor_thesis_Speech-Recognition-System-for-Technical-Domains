#Test for prepocess the data for a neural network
#Python packages for preparing the data
from pylab import *
import librosa   #for audio processing
import os
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()



label_list = os.listdir('/Users/tim/Desktop/Test')
#remove DS_Store Folder in list
label_list.remove('.DS_Store')
#Path to the files
audio_path = '/Users/tim/Desktop/Test'

print("Label List:")
print(label_list)

all_wave = []
all_label = []

#for loop for every label in the label_list
for label in label_list:
    #Path to the files in the folder
    waves = [f for f in os.listdir(audio_path + '/'+ label) if f.endswith('.wav')]
    #Create the samples & sample rate for every wav file in the folder
    for wav in waves:
        samples, sample_rate = librosa.load(audio_path + '/' + label + '/' + wav, sr = 8000)
        samples = librosa.resample(samples, len(samples), 8000,res_type='kaiser_best')
        print(type(samples))
        print(type(sample_rate))

        #Check if the sample_rate is 8000kHz
        if(len(samples)== 8000) :
            #Safe the samples in an array (all_wave) with a connection to the label (all_label)
            all_wave.append(samples)
            all_label.append(label)

        else:
            print("Error", audio_path + '/' + label + '/' + wav, "has not the sample_rate 8000; Sample_Rate:",len(samples))


#Convert output labels in integer
y=le.fit_transform(all_label)
classes= list(le.classes_)

#Convert integer labels in vector
y=np_utils.to_categorical(y, num_classes=len(label))
all_wave = np.array(all_wave).reshape(-1,8000,1)

#Print out all the types and sizes of the output variables
print('\n''\n',"Input")
print("Type:" , type(all_wave), "Shape:", np.shape(all_wave))
print(all_wave, '\n''\n')
print("Output")
print("Type:" , type(y), "Shape:", np.shape(y))
print(y, '\n''\n')
print("Samples letzte Aufnahme:")
print("Type:" , type(samples), "Shape:", np.shape(samples))
print(samples, '\n''\n')
print("Sample_Rate letzte Aufnahme:")
print("Type:" , type(sample_rate), "Shape:", np.shape(sample_rate))
print(sample_rate)
