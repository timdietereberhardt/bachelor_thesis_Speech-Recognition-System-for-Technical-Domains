import matplotlib.pyplot as plt
import librosa.display
import librosa
import sklearn
import numpy as np

data_path = '/Users/tim/Desktop/Alert_Noises.wav'
#Extract samples and sample rate
samples, sample_rate = librosa.load(data_path, sr=8000)

#Samples and sample_rate must have the same dimensions --> reduce dimension of samples to 16000
samples = librosa.resample(samples,len(samples),8000)

#Extract mfcc data from samples
mfcc = librosa.feature.mfcc(samples.astype(float),sr=len(samples))

#Plot a mfcc diagram
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfcc, x_axis='time')
plt.colorbar()
plt.title('MFCC from:'+ data_path)
plt.tight_layout()
plt.show()

print(mfcc)

#Normalization
test_norm = sklearn.preprocessing.normalize(mfcc)
print("Orginal --> Max: ", np.amax(mfcc), "Min: ", np.amin(mfcc))
print("Norm. --> Max: ", np.amax(test_norm), "Min: ", np.amin(test_norm))
print(test_norm)