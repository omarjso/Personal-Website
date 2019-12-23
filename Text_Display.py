import os


display = open("problems/code_template.html", "r")
html = display.read()

Directory = 'problems/ProjectEulerText'

for filename in os.listdir(Directory):
    dot = filename.index(".")
    prb_num = filename[2: dot]
    old_file = open("problems/ProjectEulerText/PE" + prb_num + ".txt", "r")
    new_file = open("problems/ProjectEulerHTML/PE" + prb_num + ".html", "w+")
    new_file.write(html[:675] + old_file.read() + html[675:])
    old_file.close()
    new_file.close()

display.close()

