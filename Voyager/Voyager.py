

#? Voyager Golden Records
#? Einlesen der WAV-Datei




#? Laden der Benötigten Bibliotheken
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

#?Hier wird die Datei eingelesen und in Zwei unterschiedliche Arrays gespeicher
rate, data = wavfile.read('Voyager Golden Record Encoded Image Data 44_1 kHz.wav')

#?Zerlegen des Array data in die beiden Tonspuren hier channel1
channel1 = data[:, 0]
#?Zerlegen des Array data in die beiden Tonspuren hier channel2
channel2 = data[:, 1]

zeilenlaenge = 734 #Gefundener wert durch suchen

spalten = 512       #Gefundener wert durch suchen

start = 1392322     #Startpunkt in .wav gesucht


#? zuweisen der Variable kreis. Dabei zuscheiden des Arrays auf den Wertebereich [start des bildes : start des bildes+ eine bild länge]

kreis = channel1[start:start+zeilenlaenge*spalten]

bild = kreis.reshape(spalten,zeilenlaenge) #umgeformtes Array zuweisen in die Variable bild

# plt.imshow(bild, cmap = 'gray')            #Bild generieren
# plt.plot(0, 0,label='ohne Korrektur')
# plt.legend()
# plt.show(block = True)                                  #Anzeigen des Bildes

offset = -10

kreishd = channel1[start+offset:start+zeilenlaenge*spalten+215+offset] #Zuweisen neuer Daten und zurechtrücken mit +215


x = signal.resample(kreishd,(zeilenlaenge*spalten)) #Hier werden mehr datenpunkte eingefügt durch erstellen von zwischenwerten
bildhd = x.reshape(spalten,zeilenlaenge) #aus 1D array wird 2D array
""" 
plt.imshow(bildhd, cmap = "gray")
plt.plot(0, 0,label='mit Korrektur')
plt.legend()
plt.show(block = True)                                  #Anzeigen des Bildes
"""

#? Zoomen auf den Streifen links im bild


# plt.imshow(bildhd[121:150:2,5:145], cmap = 'gray')
# plt.plot(0, 0,label='Zoom')
# plt.legend()
# plt.show(block = True) 


# plt.imshow(bildhd[200:220:2,0:150], cmap = 'gray', aspect = 'auto')
# plt.show(block = True) 


#? Sytaxerklärung [Startbereich zeile : Endbereich zeile : Wahl jede zweite Zeile, Startbereich spalte : Endbereich spalte]
#!Temp Test
testkreis = kreishd[600:]

startseq = bildhd[121:150:2,18:155].mean(axis=0)
startseq1 = bildhd[120:149:2,18:155].mean(axis=0)
startseq2 = bildhd[120:150,18:155].mean(axis=0)
# plt.plot(startseq2,label = 'startseq2')
# plt.plot(startseq1,label = 'startseq1')
# plt.plot(startseq,label = 'startseq')
# plt.legend()
# plt.show(block = True) 
#Cross Correlation
corr_sig = signal.correlate(kreishd, startseq)
corr_sig1 = signal.correlate(kreishd, startseq1)
corr_sig2 = signal.correlate(kreishd, startseq2)
corr_test = signal.correlate(testkreis, startseq)

# plt.plot(corr_sig[:5000],label = 'corr_sig')
# plt.plot(corr_sig1[:5000],label = 'corr_sig1')
# plt.plot(corr_sig2[:5000],label = 'corr_sig2')
# plt.legend()
# plt.show()

# fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
# fig.suptitle('Cross Correlatet Signal')

# ax1.plot(corr_sig[:5000])
# ax1.set_label('corr_sig')
# ax2.plot(corr_sig1[:5000])
# ax2.set_label('corr_sig1')
# ax3.plot(corr_sig2[:5000])
# ax3.set_label('corr_sig2')
# fig.tight_layout(pad=0.5)
# plt.show(block = True) 
# Die zeilenanfänge sind nun immer die Peaks.

zeilenstart = signal.find_peaks(corr_sig, 0.6e9,distance = 200)
zeilenstart = zeilenstart[0]
zeilenstart1 = signal.find_peaks(corr_sig1, 6e8,distance = 200)
zeilenstart1 = zeilenstart[0]
zeilenstart2 = signal.find_peaks(corr_sig2, 6e8,distance = 200)
zeilenstart2 = zeilenstart[0]
zeilenstarttest = signal.find_peaks(corr_test,0.6e9,distance = 200)
zeilenstarttest = zeilenstarttest[0]
print(len(zeilenstart))
print(zeilenstart.dtype)
print(zeilenstart2)

#plt.plot(zeilenstart)
#plt.plot(zeilenstart1)
#plt.plot(zeilenstart2)
#plt.show(block = True) 
""" 
y=0
startpointssortiert = []
for x in zeilenstart[0]:
    temp = x-y
    if(temp>500):
        startpointssortiert.append(x)
    y = x
print(startpointssortiert) 
"""

kreisstraight = testkreis
testmest = []
y = 0
for zeilenstart in zeilenstart:
    testmest.append(signal.resample(kreisstraight[y:zeilenstart],1000))
    y= zeilenstart

plt.imshow(testmest,aspect = 'auto',cmap='gray')
plt.show(block = True) 

