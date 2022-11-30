# Bachelor Thesis - Conception of a Recurrent Neural Network based Speech Recognition System for Technical Domains with Comparison to Existing Systems

## Abstract
The aim of the present bachelor thesis was to provide a proof of concept for the own
development of speech recognition systems in the industrial sector. For this purpose nine
keywords were defined which a recurrent neural network should recognize in an
environment full of noises. The neural network was trained, validated and tested with
collected data. To achieve best possible results of the neural network methods like: Data
Augmentation, Dropout, L1/ L2 Regularization, Transfer Learning and Hyperparameter
Optimization methods were used and their influence of the predictions was analyzed. By
these methods a best network architecture could be chosen. In addition to that, a
comparison between systems from providers such as Google and IBM and the
developed network was done. For this purpose, 18 recordings without noise and 18
recordings with noise were used for this comparison. The result is that the own network
performs better than the other systems in both variants of the recordings. To round off
this comparison, these recordings were played to a test person to compare the results
with the results of the technical systems.

Unfortunately, the data cannot be published according to German data protection law.

### data
comparison_data: The test data used for comparing the systems and testing the best model
converted_Warden_data: The Train, Val and Test MFCC Warden data V. 2 in npy format
labeled_own_data: The labeled own data in WAV format, divided into: Train, Val & Test
orginal_data: The original collection of data without labeling
Testdaten_Python_Skripts: For the test of the data augmentation etc. these data were used


### models
final_model: The best model in h5 format
test_Warden_model: The model trained on the Warden for the Transfer Learning Method test.

### notebooks
	1. development NN, LSTM and GRU with the own data
	2. hyperparameter optimization variant 1 & 2
	3. development GRU with Warden data
	4. test of the Transfer Learning Method
	5. test of the best model


### python_scripts
Prior to development, the methods were tested on smaller datasets. The py data includes these tests.

### system_comparison_results
Excel file with the results of the tests of the other systems and the test person.

### test_results
Output of the test of the best model in csv format

### thesis
Digital pdf form of the thesis


#### Required Python libraries:
Keras, TensorFlow, Librosa, Scikit Learn, Numpy, MatPlotLib, os, pylon, json,
pandas, wave, context lib





