#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import distance as dst
import matplotlib.pyplot as plt
import os
import speech_recognition as sr

from pathlib import Path
#
#
#
class Speech:
    def __init__(self):
        self.original = []
        self.recognized = []
        self.similarity = []

        
    def read_original(self, inFile) :
        with open(inFile) as f :
            content = f.readlines()
            
        for c in content :
            self.original.append(c)

            
    def conv_audio(self, inDir) :
        '''
        https://realpython.com/python-speech-recognition/#author
        '''
        self.recognized = []
        
        trx = os.listdir(inDir)
        trx.sort()
        
        r = sr.Recognizer()
        
        count = 1
        for filename in trx :
            wav_file = inDir + "/" + filename
            track = sr.AudioFile(wav_file)
            #
            with track as source :
                audio = r.record(source)
                print("requesting track", count)
                self.recognized.append(r.recognize_google(audio))
                print("processed track", count)
            count += 1
            
        
    def comp_string(self) :
        ''' 
        https://pypi.org/project/Distance/
        '''
        self.similarity = []
        
        for i in range(len(self.original)) :
            src = self.original[i].split()
            trgt = self.recognized[i].split()
            self.similarity.append(dst.levenshtein(src, trgt))


# In[ ]:


if __name__ == '__main__':
    s = Speech()
    s.read_original("original.txt")
    #
    s.conv_audio("08-English-male")
    s.comp_string()
    eng_m = s.similarity
    #
    s.conv_audio("03-English-Female")
    s.comp_string()
    eng_f = s.similarity
    #
    s.conv_audio("08-Persian-male")
    s.comp_string()
    per_m = s.similarity
    
    data = [eng_m, eng_f]
    fig1, ax1 = plt.subplots()
    ax1.set_title("Male vs. Female")
    ax1.boxplot(data, labels = ["Male", "Female"])
    ax1.set_ylabel("Data")
    #
    data = [eng_m, per_m]
    fig2, ax2 = plt.subplots()
    ax2.set_title("English vs. Persian")
    ax2.boxplot(data, labels = ["English", "Persian"])
    ax2.set_ylabel("Data")
    #    
    plt.show()
    
    print("DONE!")

