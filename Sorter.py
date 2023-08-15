def sort(dir=None):
    import os
    
        
    if dir == None:
        dir = input("Input Directort (desktop for Desktop, downloads for Downloads): ")
        dir = dir.lower()

    if dir == "desktop":
        dir = os.path.expanduser("~/Desktop")
    
    elif dir == "downloads":
        dir = os.path.expanduser("~/Downloads")
        
        
    installers = os.path.expanduser("~/Desktop/Installers")
    
    
    count = 0
    for file in os.listdir(dir):
        file = os.path.splitext(file)
        con_file = "".join(file)
        
        if "installer" in file[0].lower() or "setup" in file[0].lower():
            if file[1] != '':
                print(file)
                count += 1
                
                try:
                    os.rename(dir + "/" + con_file, installers + "/" + con_file)
                except Exception as e:
                    print(f"{file} already exists Error: {e}")

    print("Number of files terminated: ", count)    
    

        
