import os

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

# MAIN PROGRAM
print_logo()
choice=get_choice()
files,PATH=get_files_and_path()