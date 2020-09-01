import os 
import shutil 

os.chdir('/home/nopc/Desktop/Github-Clones/Rename-Rep/Database Mangement Sysems')

for f in os.listdir():
    if (len(f.split('_'))) > 4 :
        list_for_name = f.split('_')
        word_for_rename =''
        original_constraint = ''
        for index in range (4):
            if (list_for_name[0]=='FALLSEM2020-21'):
                original_constraint = original_constraint +  list_for_name[index]+ '_' 
        for index in range (4,len(list_for_name)):
            if (index == len(list_for_name)-1):
                word_for_rename = word_for_rename +list_for_name[index]
            else :
                word_for_rename = word_for_rename+list_for_name[index] + '_'  
        merged_original_words = original_constraint + word_for_rename
        # print(type(original_constraint))
        if (original_constraint == ''):
            print('The Script Has Already Worked , Thank You')
        else :
            os.rename(merged_original_words, word_for_rename)


