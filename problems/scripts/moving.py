import os

problems = os.getcwd()


for filename in os.listdir(problems):
    if "PE" in filename and "." in filename:
        os.rename(filename, "ProjectEular/" + filename)
