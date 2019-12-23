import os


ProjectEuler = 'ProjectEulerHTML/'


for filename in os.listdir(ProjectEuler):
    if "PE" in filename and "." in filename:
        cutting_end = filename.index(".")
        file_number = filename[2: cutting_end]
        if len(file_number) < 3:
            file_number = "0" * (3 - len(file_number)) + file_number  
            os.rename("ProjectEulerHTML/" + filename, 
                    "ProjectEulerHTML/" + "PE" + file_number + ".html")

