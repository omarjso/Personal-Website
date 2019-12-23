import os 


def insert_header(header, filename, link):
    done_link = False
    for i in range(len(filename) + len(link)): 
        if done_link == False and filename[i: 7 + i] == "</head>":
            filename = filename[:i - 2] + link + filename[i - 2:]
            done_link = True
        if filename[i: 6 + i] == "<body>":
            filename = filename[:i + 7] + header + filename[i + 7:]
    return filename        


dir_path = "/services/http/users/o/omarjamal/problems/ProjectEulerHTML" 
template = "/services/http/users/o/omarjamal/problems/templates/header.html"

"""
for filename in os.listdir(dir_path):
    if "PE" in filename:
        HTML = open((dir_path + '/' + filename), 'r')
        HTML_str = HTML.read()
"""        
template = open(template, "r").read()

link = '\n\t\t<link href="css/headstripe.css" rel="stylesheet">'

file = open("/services/http/users/o/omarjamal/problems/ProjectEulerHTML/PE003.html", "r")
file = file.read()

print(insert_header(template, file, link))



