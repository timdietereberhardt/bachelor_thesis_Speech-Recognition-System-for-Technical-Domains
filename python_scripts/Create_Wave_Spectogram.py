#Create a wave diagram and a spectogram from a speech recording
from pylab import *
import wave
import librosa   #for audio processing
import numpy as np
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

def show_wave_n_spec(speech):

    #Create wave diagram
    samples, sample_rate = librosa.load(speech, sr=8000)

    #Samples and sample_rate must have the same dimensions --> reduce dimension of samples to 16000
    samples = librosa.resample(samples,len(samples),8000)

    #Get Frame_Rate
    spf = wave.open(speech, 'r')
    frame_rate = spf.getframerate()

    #Change x,y number fontsize
    matplotlib.rc('xtick', labelsize=20)
    matplotlib.rc('ytick', labelsize=20)



    #Plot wave diagram
    fig = plt.figure(figsize=(14, 8))
    ax1 = fig.add_subplot(211)
    ax1.set_title('Wellenform und Spektogramm von '+speech, fontsize=22)
    ax1.set_xlabel('Zeit in s', fontsize=16)
    ax1.set_ylabel('Amplitude', fontsize=16)
    ax1.plot(np.linspace(0, sample_rate / len(samples), sample_rate), samples)

    #plot the spectogram
    subplot(212)
    spectrogram = specgram(samples, Fs=frame_rate, scale_by_freq=True, sides='default')
    plt.xlabel('Zeit in s', fontsize=16)
    plt.ylabel('Frequenz in Hz', fontsize=16)

    #Change x,y number fontsize
    #matplotlib.rc('xtick', labelsize=14)
    #matplotlib.rc('ytick', labelsize=14)

    show()
    spf.close()

#File path
file1='/Users/tim/Desktop/Alert_Labor.wav'
file2='/Users/tim/Desktop/Alert_Noises.wav'
file3='/Users/tim/Desktop/Test.wav'                 #Test file with another voise and word

show_wave_n_spec(file1)
show_wave_n_spec(file2)
show_wave_n_spec(file3)

