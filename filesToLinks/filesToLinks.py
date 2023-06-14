""" 230612mon1704 https://github.com/F3l1p3Tn1

1- To list all files on Terminal and save in "1.txt" file:

Replace "Folder" with your folders names path,
and run the command in terminal:

$ find ~/"Folder"/"Folder" -name '*.html' | grep .html >> 1.txt

Example: 
$ find ~/Documents -name '*.html' | grep .html >> 1.txt


2- Run this Python3 Script to write a list of 
pages as HTML links in "2.html" file:

"""

txt1 = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>LinksHTML</title>\n<link rel="stylesheet" href="style.css">\n</head>\n<body>\n<h1>LinksHTML</h1>\n'

file = "1.txt"
with open(file, 'r') as text:
    txt = text.readlines()

## Separate only .html file names and replace as links:
n = 0
a = '<p><a href="'
b = '">'
c = '</a></p>'
for i in txt:
    if ".html" in i:
        n += 1
        txt1 += (a + i[:-1] + b + "\n" + str(n) + "- " + i[:-1] + c + "\n")
txt1 += '</body>\n</html>'

print(txt1)

## Save in 2.txt:
file = '2.html'
with open(file, 'w') as txt2:
    txt2.write(str(txt1))
