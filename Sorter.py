def sort(dir):
    import os
    
    for file in os.listdir(dir):
        file = os.path.splitext(file)
        con_file = "".join(file)
        
        if "installer" in file[0].lower() or "setup" in file[0].lower():
            if file[1] != '':
                print(file)
                
                try:
                    os.rename(dir + "/" + con_file, "C:/Users/jamie/Desktop/Installers" + "/" + con_file)
                except Exception as e:
                    print(f"{file} already exists Error: {e}")
        

        


