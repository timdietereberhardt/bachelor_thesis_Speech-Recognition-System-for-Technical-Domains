#Python Script to analyse the length of each wav file
#If the wav file is over 2 seconds long --> print out the name --> manually edit the wav file
import os
import wave
import contextlib

#Path to the files
data_path = '/Users/tim/Desktop/labeled_own_data'

# Create a list of all audio files in path
label_list = os.listdir(data_path)

#remove DS_Store and background_noises folder Folder in list
label_list.remove('.DS_Store')

#Create a counter
counter = 1
#Set max length to zero
max_length_wav = 0
max_length_noise = 0

#Every label folder
for label in label_list:
    #Path to the files in the folder
    files = [f for f in os.listdir(data_path + '/'+ label) if f.endswith('.wav')]
    #For loop every audio file in folder
    for file in files:
        with contextlib.closing(wave.open(data_path + '/'+ label + '/' + file,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            length = frames / float(rate)

            #Print out the name of the file when the length is over 2 seconds
            if length > 1.85:
                print(counter, " File name:", data_path + '/'+ label + '/' + file)
                print("Length file:", length)
                counter += 1

            #Find the longest wav file and test it in Python Script: Add_noises_to_audio
            if length > max_length_wav and label != '_background_noise_':
                max_length_wav = length
                data_path_max_length_wav = data_path + '/'+ label + '/' + file

            #Find the longest noises wav file and test it in Python Script: Add_noises_to_audio
            if length > max_length_noise and label == '_background_noise_':
                max_length_noise = length
                data_path_max_length_noise = data_path + '/'+ label + '/' + file

print("Max Length:", max_length_wav, "Data Path:", data_path_max_length_wav)
print("Max Length:", max_length_noise, "Noise Data Path:", data_path_max_length_noise)