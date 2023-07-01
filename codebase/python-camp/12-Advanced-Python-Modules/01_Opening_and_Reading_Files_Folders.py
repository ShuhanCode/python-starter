import os
import shutil
import send2trash

# f = open('practice.txt', 'w+')
# f.write('This is a test string')
# f.close()

# result  = os.getcwd()
# print(result)

# result = os.listdir()
# print(result)



# shutil.move('/Users/rfnoc/Documents/python-ex/practice.txt', os.getcwd())   

# send2trash.send2trash('practice.txt')  

for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
    
