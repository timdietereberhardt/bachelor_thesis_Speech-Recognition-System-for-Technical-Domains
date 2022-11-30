#Create a bar chart with a csv file
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Which data should be used? Warden = True, Own Data = False
Warden = False

if Warden == True:
    #WARDEN DATA
    file_warden='/Users/tim/Desktop/Datenanalyse.csv'
    data = pd.read_csv(file_warden, sep=',', na_values='.')
    labels = data.iloc[1:36,0]
    number = data.iloc[1:36,1]

    #plot with KIT colors
    plt.figure(figsize=(30,5))
    index = np.arange(len(labels))
    plt.bar(index, number,color=(0.25, 0.576, 0.51))
    plt.xlabel('Begriffe', fontsize=16)
    plt.ylabel('Anzahl der Aufnahmen', fontsize=16)
    plt.xticks(index,labels, fontsize=15, rotation=60)
    plt.title('Anzahl der Aufnahmen für jeden Begriff in den Warden Daten V.2', fontsize=26)
    plt.show()

if Warden == False:
    #OWN DATA
    labels = ['background noise', 'pressure alert', 'alert', 'balls screw drive', 'cnc', 'error logs', 'measurement system', 'nc alert', 'reutlingen', 'stop' ]
    number = [152, 82,82,88,85,83,83,83,82,82]
    print(labels)
    print(number)

    #plot with KIT colors
    plt.figure()
    index = np.arange(len(labels))
    plt.bar(index, number,color=(0.25, 0.576, 0.51))
    plt.ylabel('Anzahl der Aufnahmen')
    plt.xticks(index,labels, rotation=60)
    plt.title('Anzahl der Aufnahmen für jeden Begriff in den eigenen Daten', fontsize=10)
    plt.show()
