import os

ProjectEuler = 'ProjectEulerText/'


for filename in os.listdir(ProjectEuler):
    if "EularProject" in filename and "." in filename:
        cutting_end = filename.index(".")
        os.rename("ProjectEulerText/" + filename, "ProjectEulerText/" + "PE" + filename[12: cutting_end] + ".txt")
        



