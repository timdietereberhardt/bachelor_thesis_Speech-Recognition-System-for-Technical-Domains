#Test for Sound Augmentation
#Source:
#https://www.kaggle.com/huseinzol05/sound-augmentation-librosa


#import python packages
from pylab import *
import os
import wave
import librosa   #for audio processing
import numpy as np
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")


#Define the functions for augmentation
#Check the augmentation with wave chart and spectogram
def show_wave_n_spec(samples, sample_rate, file_name):

    #Change x,y number fontsize
    matplotlib.rc('xtick', labelsize=20)
    matplotlib.rc('ytick', labelsize=20)

    #Plot wave diagram
    fig = plt.figure(figsize=(14, 8))
    ax1 = fig.add_subplot(211)
    ax1.set_title('Wellenform und Spektogramm: '+ file_name, fontsize=22)
    ax1.set_xlabel('Zeit in s', fontsize=16)
    ax1.set_ylabel('Amplitude', fontsize=16)
    ax1.plot(np.linspace(0, sample_rate / len(samples), sample_rate), samples)

    #plot the spectogram
    subplot(212)
    spectrogram = specgram(samples, Fs=sample_rate, scale_by_freq=True, sides='default')
    plt.xlabel('Zeit in s', fontsize=16)
    plt.ylabel('Frequenz in Hz', fontsize=16)



    show()

#Func: Get the samples and sample rate for not augmentation data
def normal(label_list, data_src_path, test):
    #Create two empty func output arrays
    all_wave_normal = []
    all_label_normal = []

    #Every label folder
    for label in label_list:

            # Path to the files in the folder
            files = [f for f in os.listdir(data_src_path + '/' + label) if f.endswith('.wav')]

            # For every audio file in folder
            for file in files:
                # Read the audio file, extract samples and sample rate & resample to 8000Hz
                samples, sample_rate = librosa.load(data_src_path + '/' + label + '/' + file, sr=8000)
                samples = librosa.resample(samples, len(samples), 8000, res_type='kaiser_best')

                #Wave and spectogram
                if test:
                    file_name = file + ' (Normal)'
                    show_wave_n_spec(samples, sample_rate, file_name)

                # add the new samples and labels in an arrays
                all_wave_normal.append(samples)
                all_label_normal.append(label)

    return all_wave_normal, all_label_normal


#Func: Change pitch and speed of the audio files, test = bool
def pitch_speed_augmentation(label_list, data_src_path, test):

    #Create two empty func output arrays
    all_wave_pitch_speed = []
    all_label_pitch_speed = []

    #Every label folder
    for label in label_list:

            # Path to the files in the folder
            files = [f for f in os.listdir(data_src_path + '/' + label) if f.endswith('.wav')]

            # For every audio file in folder
            for file in files:
                # Read the audio file, extract samples and sample rate & resample to 8000Hz
                samples, sample_rate = librosa.load(data_src_path + '/' + label + '/' + file, sr=8000)
                samples = librosa.resample(samples, len(samples), 8000, res_type='kaiser_best')

                # Change low and high
                length_change = np.random.uniform(low=0.8, high=1)
                speed_fac = 1.0 / length_change
                print("resample length_change = ", length_change)
                tmp = np.interp(np.arange(0, len(samples), speed_fac), np.arange(0, len(samples)), samples)
                minlen = min(samples.shape[0], tmp.shape[0])
                samples *= 0
                samples[0:minlen] = tmp[0:minlen]


                #Wave and spectogram
                if test:
                    file_name = file + ' (Pitch and Speed)'
                    show_wave_n_spec(samples, sample_rate, file_name)


                #add the new samples and labels in an arrays
                all_wave_pitch_speed.append(samples)
                all_label_pitch_speed.append(label)

    return all_wave_pitch_speed, all_wave_pitch_speed

#Func: Change pitch and speed of the audio files, test = bool
def pitch_augmentation(label_list, data_src_path, test):

    #Create two empty func output arrays
    all_wave_pitch = []
    all_label_pitch = []

    #Every label folder
    for label in label_list:

            # Path to the files in the folder
            files = [f for f in os.listdir(data_src_path + '/' + label) if f.endswith('.wav')]

            # For every audio file in folder
            for file in files:
                # Read the audio file, extract samples and sample rate & resample to 8000Hz
                samples, sample_rate = librosa.load(data_src_path + '/' + label + '/' + file, sr=8000)
                samples = librosa.resample(samples, len(samples), 8000, res_type='kaiser_best')

                #Change pitch
                bins_per_octave = 12
                pitch_pm = 2
                pitch_change = pitch_pm * 2 * (np.random.uniform())
                print("pitch_change = ", pitch_change)
                samples = librosa.effects.pitch_shift(samples.astype('float64'),
                                                      sample_rate, n_steps=pitch_change,
                                                      bins_per_octave=bins_per_octave)
                #Wave and spectogram
                if test:
                    file_name = file + ' (Pitch)'
                    show_wave_n_spec(samples, sample_rate, file_name)


                #add the new samples and labels in an arrays
                all_wave_pitch.append(samples)
                all_label_pitch.append(label)

    return all_wave_pitch, all_label_pitch

#Func: Change pitch and speed of the audio files, test = bool
def speed_augmentation(label_list, data_src_path, test):

    #Create two empty func output arrays
    all_wave_speed = []
    all_label_speed = []

    #Every label folder
    for label in label_list:

            # Path to the files in the folder
            files = [f for f in os.listdir(data_src_path + '/' + label) if f.endswith('.wav')]

            # For every audio file in folder
            for file in files:
                # Read the audio file, extract samples and sample rate & resample to 8000Hz
                samples, sample_rate = librosa.load(data_src_path + '/' + label + '/' + file, sr=8000)
                samples = librosa.resample(samples, len(samples), 8000, res_type='kaiser_best')

                #Change pitch
                speed_change = np.random.uniform(low=0.9, high=1.1)
                print("speed_change = ", speed_change)
                tmp = librosa.effects.time_stretch(samples.astype('float64'), speed_change)
                minlen = min(samples.shape[0], tmp.shape[0])
                samples *= 0
                samples[0:minlen] = tmp[0:minlen]

                #Wave and spectogram
                if test:
                    file_name = file + ' (Speed)'
                    show_wave_n_spec(samples, sample_rate, file_name)

                #add the new samples and labels in an arrays
                all_wave_speed.append(samples)
                all_label_speed.append(label)

    return all_wave_speed, all_label_speed

#Func: Amplify values in the audio, test = bool
def amplify_value(label_list, data_src_path, test):

    #Create two empty func output arrays
    all_wave_value = []
    all_label_value = []

    #Every label folder
    for label in label_list:

            # Path to the files in the folder
            files = [f for f in os.listdir(data_src_path + '/' + label) if f.endswith('.wav')]

            # For every audio file in folder
            for file in files:
                # Read the audio file, extract samples and sample rate & resample to 8000Hz
                samples, sample_rate = librosa.load(data_src_path + '/' + label + '/' + file, sr=8000)
                samples = librosa.resample(samples, len(samples), 8000, res_type='kaiser_best')

                #Amplify value
                dyn_change = np.random.uniform(low=1.5, high=3)
                samples = samples * dyn_change
                print(samples[:50])

                # Wave and spectogram
                if test:
                    file_name = file + ' (Amplify value)'
                    show_wave_n_spec(samples, sample_rate, file_name)

                # add the new samples and labels in an arrays
                all_wave_value.append(samples)
                all_label_value.append(label)

    return all_wave_value, all_label_value

#Func: random shifting in the audio, test = bool
def random_shifting(label_list, data_src_path, test):

    #Create two empty func output arrays
    all_wave_shift = []
    all_label_shift = []

    #Every label folder
    for label in label_list:
        # Path to the files in the folder
        files = [f for f in os.listdir(data_src_path + '/' + label) if f.endswith('.wav')]

        # For every audio file in folder
        for file in files:
            # Read the audio file, extract samples and sample rate & resample to 8000Hz
            samples, sample_rate = librosa.load(data_src_path + '/' + label + '/' + file, sr=8000)
            samples = librosa.resample(samples, len(samples), 8000, res_type='kaiser_best')

            #Shift random
            timeshift_fac = 0.2 * 2 * (np.random.uniform() - 0.5)  # up to 20% of length
            print("timeshift_fac = ", timeshift_fac)
            start = int(samples.shape[0] * timeshift_fac)
            print(start)
            if (start > 0):
                samples = np.pad(samples, (start, 0), mode='constant')[0:samples.shape[0]]
            else:
                samples = np.pad(samples, (0, -start), mode='constant')[0:samples.shape[0]]


             # Wave and spectogram
            if test:
                file_name = file + ' (Shifting)'
                show_wave_n_spec(samples, sample_rate, file_name)

            # add the new samples and labels in an arrays
            all_wave_shift.append(samples)
            all_label_shift.append(label)

    return all_wave_shift, all_label_shift

#Func: hpss in the audio, test = bool
def apply_hpss(label_list, data_src_path, test):

    #Create two empty func output arrays
    all_wave_hpss = []
    all_label_hpss = []

    #Every label folder
    for label in label_list:
        # Path to the files in the folder
        files = [f for f in os.listdir(data_src_path + '/' + label) if f.endswith('.wav')]

        # For every audio file in folder
        for file in files:
            # Read the audio file, extract samples and sample rate & resample to 8000Hz
            samples, sample_rate = librosa.load(data_src_path + '/' + label + '/' + file, sr=8000)
            samples = librosa.resample(samples, len(samples), 8000, res_type='kaiser_best')

            #hpss
            samples = librosa.effects.hpss(samples)
            samples = samples[1].tolist()


             # Wave and spectogram
            if test:
                file_name = file + ' (hpss)'
                show_wave_n_spec(samples, sample_rate, file_name)

            # add the new samples and labels in an arrays
            all_wave_hpss.append(samples)
            all_label_hpss.append(label)

    return all_wave_hpss, all_label_hpss


# Func: strech the the audio, test = bool
def strech(label_list, data_src_path, test):
    # Create two empty func output arrays
    all_wave_strech = []
    all_label_strech = []

    # Every label folder
    for label in label_list:
        # Path to the files in the folder
        files = [f for f in os.listdir(data_src_path + '/' + label) if f.endswith('.wav')]

        # For every audio file in folder
        for file in files:
            # Read the audio file, extract samples and sample rate & resample to 8000Hz
            samples, sample_rate = librosa.load(data_src_path + '/' + label + '/' + file, sr=8000)
            samples = librosa.resample(samples, len(samples), 8000, res_type='kaiser_best')

            #Shift the silents
            input_length = len(samples)
            samples = librosa.effects.time_stretch(samples, 1.1)
            if len(samples) > input_length:
                samples = samples[:input_length]
            else:
                samples = np.pad(samples, (0, max(0, input_length - len(samples))), "constant")


            # Wave and spectogram
            if test:
                file_name = file + ' (strech)'
                show_wave_n_spec(samples, sample_rate, file_name)

            # add the new samples and labels in an arrays
            all_wave_strech.append(samples)
            all_label_strech.append(label)

    return all_wave_strech, all_wave_strech

#Path to the files
data_path = '/Users/tim/Desktop/Test'

# Create a list of all audio files in path
label_list = os.listdir(data_path)

#remove DS_Store and background_noises folder Folder in list
label_list.remove('.DS_Store')
label_list.remove('_background_noise_')

#Data without Augmentation
all_wave_normal, all_label_normal = normal(label_list, data_path, False)
print(all_wave_normal[0].shape)

#Call the pitch_speed_augmentation function --> Augmentation Method 1
all_wave_pitch_speed, all_label_pitch_speed = pitch_speed_augmentation(label_list, data_path, False)
print(all_wave_pitch_speed[0].shape)

#Call the pitch_augmentation function --> Augmentation Method 2
all_wave_pitch, all_label_pitch = pitch_augmentation(label_list, data_path, False)
print(all_wave_pitch[0].shape)

#Call the speed_augmentation function --> Augmentation Method 3
all_wave_speed, all_label_speed = speed_augmentation(label_list, data_path, False)
print(all_wave_speed[0].shape)

#Call the amplify_value function --> Augmentation Method 4
all_wave_value, all_label_value = amplify_value(label_list, data_path, False)
print(all_wave_value[0].shape)

#Call the shifting function --> Augmentation Method 5
all_wave_shift, all_label_shift = random_shifting(label_list, data_path, False)
print(all_wave_shift[0].shape)

#Call the shifting function --> Augmentation Method 6
all_wave_strech, all_label_strech = strech(label_list, data_path, False)
print(all_wave_strech[0].shape)

#Call the hpss function --> Augmentation Method 7
all_wave_hpss, all_label_hpss = apply_hpss(label_list, data_path, False)
print(all_wave_hpss[0].shape)
