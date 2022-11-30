#Create a boxplot diagram with a csv file
import matplotlib.pyplot as plt
import pandas as pd


#File path
file='/Users/tim/Desktop/Warden_Daten_Analyse.csv'

#data in numpy data frame
data = pd.read_csv(file, sep=',', na_values='.')
slice = data.iloc[[0, 34],:]

#Create boxplot diagram
bp = slice.boxplot(vert=False)
plt.title('Boxplot Anteile der Begriffe von den Warden Daten')
plt.xlabel('Anteile in %')
#axes = plt.gca()
#axes.set_ylim([0,800])
plt.show()

