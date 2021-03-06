import os
from datetime import datetime


def print_logo():
    os.system('color E')
    print("""      
       _                        
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.        Alaa Utilty Tool
         :.       .        \       By @azizamari
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
      .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'
    """)
def get_choice():
    print("Pick a functionality by typing it's number")
    print("[1] Beautify mp4 file name")
    print("[2] Add date to file names")
    print("[3] Remove date from file names (reverse [2])")
    choice=1
    while True:
        choice=input('> ')
        if choice in ['1','2','3']:
            break
        else:
            print(f"Invalid choice '{choice}'")
    return int(choice)

def get_files_and_path():
    PATH=''
    while True:
        print('Insert folder path:')
        PATH=input('> ')
        try:
            files=os.listdir(PATH)
            break
        except:
            print(f'invalid path: "{PATH}" try again !!')
    return (files,PATH)

def remove_extension(filesList,extension):
    toBePopped=[]
    for index,file in enumerate(filesList):
        if file.endswith('.'+extension):
            filesList[index]=file[:len(file)-len(extension)-1]
        else:
            toBePopped.append(index)
    counter=0
    for index in toBePopped:
        filesList.pop(index+counter)
        counter-=1
        
def generate_new_name(fileName):
    fileName=fileName.lower()
    for i in range(len(fileName)):
        if fileName[i]==' ':
            fileName=fileName[:i]+'-'+fileName[i+1:]
        elif fileName[i]=='é' or fileName[i]=='è':
            fileName=fileName[:i]+'e'+fileName[i+1:]
        elif fileName[i]=='à':
            fileName=fileName[:i]+'a'+fileName[i+1:]

    i=0
    while i < len(fileName)-1 and len(fileName) >= 2:
        if fileName[i]=='-' and fileName[i+1]==fileName[i]:
            fileName=fileName[:i]+fileName[i+1:]
        else:
            i+=1

    return fileName

def rename_files(filesList,PATH):
    remove_extension(filesList,'mp4')
    count=0
    for file in filesList:
        newName=generate_new_name(file)+'.mp4'
        os.rename(os.path.join(PATH,file+'.mp4'),os.path.join(PATH,newName))
        count+=1
        print(f"DONE {count}/{len(filesList)}: renamed '{file}.mp4' to '{newName}.mp4")
    print(f"Successfully renamed {count} files !!!!!")

def remove_duplicate_dates(filesList,PATH):
    remove_extension(filesList,'mp4')
    count=0
    for file in filesList:
        newName=' '
        stop=False
        try:
            if len(file)<10: raise 
            newName=file[:len(file)-9]+'.mp4'
        except:
            count-=1
            print(f"ERROR: this file '{file}.mp4' caused a problem. Make sure it has a duplicate date.")
            break
        os.rename(os.path.join(PATH,file+'.mp4'),os.path.join(PATH,newName))
        count+=1
        print(f"DONE {count}/{len(filesList)}: renamed '{file}.mp4' to '{newName}.mp4 ")
    print(f"\nSUCCESSFULLY renamed {count} files !!")

def add_dates(filesList,PATH):
    remove_extension(filesList,'mp4')
    count=0
    for file in filesList:
        date=datetime.today().strftime('%Y%m%d')
        newName=file+'_'+date+'.mp4'
        os.rename(os.path.join(PATH,file+'.mp4'),os.path.join(PATH,newName))
        count+=1
        print(f"DONE {count}/{len(filesList)}: renamed '{file}.mp4' to '{newName}.mp4")
    print(f"Successfully renamed {count} files !!!!!")


# MAIN PROGRAM
print_logo()
while True:
    choice=get_choice()
    if choice==1:
        files,PATH=get_files_and_path()
        rename_files(files,PATH)
    elif choice==2:
        files,PATH=get_files_and_path()
        add_dates(files,PATH)
    elif choice==3:
        files,PATH=get_files_and_path()
        remove_duplicate_dates(files,PATH)
    print('\n')