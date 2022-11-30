#Test to add noises from a wav file to another wav file
#First extract the samples of both files and add them together
#Import python packages
import librosa  # for audio processing
import os
import random
import matplotlib.pyplot as plt
import numpy as np

from pylab import *
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

import warnings
warnings.filterwarnings("ignore")


#Function to add noises to all files in audio_list, test = true --> Print the wave forms and spectograms
def mix_noises_to_audiofiles(data_src_path, noise_src_path,label_list, test):

    all_wave_with_noises = []
    all_label_with_noises = []

    # Create a list of all noise files
    noise_list = os.listdir(noise_src_path)
    #Remove folder .DS_Store
    noise_list.remove('.DS_Store')

    #Every label folder
    for label in label_list:

        #Path to the files in the folder
        files = [f for f in os.listdir(data_src_path + '/'+ label) if f.endswith('.wav')]

        #For every audio file in folder
        for file in files:
            #Read the audio file, extract samples and sample rate & resample to 8000Hz
            samples_audio, sample_rate_audio = librosa.load(data_src_path + '/' + label + '/' + file, sr = 8000)
            samples_audio = librosa.resample(samples_audio, len(samples_audio), 8000,res_type='kaiser_best')

            # Pick a random noise file
            noise_id = randint(0, len(noise_list))

            #Test
            noise_name = noise_list[noise_id]
            print(noise_name)
            # Read the noise file, extract samples and sample rate & resample to 8000Hz
            samples_noise, sample_rate_noise = librosa.load(noise_src_path + '/' + noise_name, sr=8000)
            samples_noise = librosa.resample(samples_noise, len(samples_noise), 8000)
            print(len(samples_noise))

            #Check if the sample_rate of both files is 8000kHz
            if(len(samples_audio)== 8000 and len(samples_noise) == 8000):
                    #Combine the samples from both files
                    combined = samples_audio + samples_noise

                    if test:
                        #Control via Wave diagram and spectogram, ONLY FOR TESTING NOT FOR ALL FILES!
                        #Plot the audio file
                        fig = plt.figure(figsize=(14, 8))
                        ax1 = fig.add_subplot(211)
                        ax1.set_title('Wellenform und Spektogramm von Audio, File: '+ label + '/' + file , fontsize=16)
                        ax1.set_xlabel('Zeit in s', fontsize=16)
                        ax1.set_ylabel('Amplitude', fontsize=16)
                        ax1.plot(np.linspace(0, sample_rate_audio / len(samples_audio), sample_rate_audio), samples_audio)
                        # plot the spectogram
                        subplot(212)
                        spectrogram = specgram(samples_audio, Fs= sample_rate_audio, scale_by_freq=True, sides='default')
                        plt.xlabel('Zeit in s', fontsize=16)
                        plt.ylabel('Frequenz in Hz', fontsize=16)
                        show()

                        #Plot the noise file
                        fig = plt.figure(figsize=(14, 8))
                        ax1 = fig.add_subplot(211)
                        ax1.set_title('Wellenform und Spektogramm von Noise, File: '+ noise_name, fontsize=16)
                        ax1.set_xlabel('Zeit in s', fontsize=16)
                        ax1.set_ylabel('Amplitude', fontsize=16)
                        ax1.plot(np.linspace(0, sample_rate_noise / len(samples_noise), sample_rate_noise), samples_noise)
                        # plot the spectogram
                        subplot(212)
                        spectrogram = specgram(samples_noise, Fs= sample_rate_noise, scale_by_freq=True, sides='default')
                        plt.xlabel('Zeit in s', fontsize=16)
                        plt.ylabel('Frequenz in Hz', fontsize=16)
                        show()

                        # Plot the new diagram
                        fig = plt.figure(figsize=(14, 8))
                        ax1 = fig.add_subplot(211)
                        ax1.set_title('Wellenform und Spektogramm von Combined Files:' + label + '/' + file + " & " + noise_name, fontsize=16)
                        ax1.set_xlabel('Zeit in s', fontsize=16)
                        ax1.set_ylabel('Amplitude', fontsize=16)
                        ax1.plot(np.linspace(0, sample_rate_audio / len(combined), sample_rate_audio), combined)
                        # plot the spectogram
                        subplot(212)
                        spectrogram = specgram(combined, Fs= sample_rate_audio, scale_by_freq=True, sides='default')
                        plt.xlabel('Zeit in s', fontsize=16)
                        plt.ylabel('Frequenz in Hz', fontsize=16)
                        show()

                        # Print the arrays
                        print("Audio:")
                        print(type(samples_audio))
                        print(samples_audio)
                        print("Noise:")
                        print(type(samples_noise))
                        print(samples_noise)
                        print("Combine:")
                        print(type(combined))
                        print(combined)

                    all_wave_with_noises.append(combined)
                    all_label_with_noises.append(label)

            else:
                print("Error: The two samples haven't the same size")

    return all_wave_with_noises, all_label_with_noises

#Path to the files
data_path = '/Users/tim/Desktop/Test'

# Create a list of all audio files in path
label_list = os.listdir(data_path)

#remove DS_Store and background_noises folder Folder in list
label_list.remove('.DS_Store')
label_list.remove('_background_noise_')

#Step 2: Add Noises and audio files via the function
noise_path = '/Users/tim/Desktop/Test/_background_noise_'
all_wave_with_noises, all_label_with_noises = mix_noises_to_audiofiles(data_path, noise_path,label_list, True)
