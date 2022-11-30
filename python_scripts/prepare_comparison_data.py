#This code add noises to the test wav files and create a new wav file
#Import the librarys
import librosa
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

#If test == True --> Create wave diagrams of each new wav file
test = True
new_data_path = '/Users/tim/Desktop/comparison_data/'

#Path to the files
data_path = '/Users/tim/Desktop/labeled_test_own_data'
# Create a list of all audio files in path
label_list = os.listdir(data_path)
#remove background_noises folder Folder in list
label_list.remove('_background_noise_')
label_list.remove('.DS_Store')

#Step 2: Add Noises and audio files via the function
noise_path = '/Users/tim/Desktop/labeled_test_own_data/_background_noise_'
# Create a list of all noise files
noise_list = os.listdir(noise_path)
noise_list.remove('.DS_Store')



#Every label folder
for label in label_list:

        #Path to the files in the folder
        files = [f for f in os.listdir(data_path + '/'+ label) if f.endswith('.wav')]

        #For every audio file in folder
        for file in files:
            #Read the audio file, extract samples and sample rate & resample to 8000Hz
            samples_audio, sample_rate_audio = librosa.load(data_path + '/' + label + '/' + file, sr = 8000)
            samples_audio = librosa.resample(samples_audio, len(samples_audio), 8000,res_type='kaiser_best')

            # Pick a random noise file
            noise_id = randint(0, len(noise_list))

            #Test
            noise_name = noise_list[noise_id]


            # Read the noise file, extract samples and sample rate & resample to 8000Hz
            samples_noise, sample_rate_noise = librosa.load(noise_path + '/' + noise_name, sr=8000)
            samples_noise = librosa.resample(samples_noise, len(samples_noise), 8000)
            print(len(samples_noise))

            #Check if the sample_rate of both files is 8000kHz
            if(len(samples_audio)== 8000 and len(samples_noise) == 8000):
                    #Combine the samples from both files
                    combined = samples_audio + samples_noise

                    #Create a new wave file
                    librosa.output.write_wav(new_data_path + label + '/' + file , combined, len(combined), norm=False)

            else:
                print("Error: The two samples haven't the same size", label, file)


#Check the wave form of the new wav files
if test:
    # Every label folder
    for label in label_list:

        # Path to the files in the folder
        files = [f for f in os.listdir(new_data_path + '/' + label) if f.endswith('.wav')]

        # For every audio file in folder
        for file in files:
            # Read the audio file, extract samples and sample rate & resample to 8000Hz

            samples_audio, sample_rate_audio = librosa.load(new_data_path + '/' + label + '/' + file, sr=8000)
            samples_audio = librosa.resample(samples_audio, len(samples_audio), 8000, res_type='kaiser_best')

            # Control via Wave diagram and spectogram, ONLY FOR TESTING NOT FOR ALL FILES!
            # Plot the audio file
            fig = plt.figure(figsize=(14, 8))
            ax1 = fig.add_subplot(211)
            ax1.set_title('Wellenform und Spektogramm von Audio, File: ' + label + '/' + file, fontsize=16)
            ax1.set_xlabel('Zeit in s', fontsize=16)
            ax1.set_ylabel('Amplitude', fontsize=16)
            ax1.plot(np.linspace(0, sample_rate_audio / len(samples_audio), sample_rate_audio), samples_audio)
            # plot the spectogram
            subplot(212)
            spectrogram = specgram(samples_audio, Fs=sample_rate_audio, scale_by_freq=True, sides='default')
            plt.xlabel('Zeit in s', fontsize=16)
            plt.ylabel('Frequenz in Hz', fontsize=16)
            show()



