import os 
import shutil 

os.chdir('/home/nopc/Desktop/Github-Clones/Rename-Rep/Formal Language and Theory Of Automation')

for f in os.listdir():
    if (len(f.split('_'))) > 4 :
        print(f.split('_'))

