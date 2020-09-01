import os 
import shutil 

os.chdir('/home/nopc/Desktop/Github-Clones/Rename-Rep/Formal Language and Theory Of Automation')

for f in os.listdir():
    if (len(f.split('_'))) > 4 :
        list_for_name = f.split('_')
        word =''
        for index in range (4,):
            word = word + list_for_name[index] 
        print(word)


