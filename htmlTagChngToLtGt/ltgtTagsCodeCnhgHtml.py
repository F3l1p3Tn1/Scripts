"""
Script to replace tags for html:

"<" replace for "&lt"
">" replace for "&gt"

"""

## Copy and Paste HTML code in "text.html" file

## Execute this script in same folder in terminal

file = "text.html"
with open(file, 'r') as text:
        txt = text.read()

txt1 = txt.replace("<","&lt")

txt2 = txt1.replace(">","&gt")

print(txt2)

file = 'result.txt'
with open(file, 'w') as txt3:
    txt3.write(str(txt2))

# https://github.com/F3l1p3Tn1