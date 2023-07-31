## Extrai do texto a data: dia/mes/ano(4digitos) para ano4+mes+dia 
## Exemplo: 31/07/2023 => 20230731
date = ''
pl = 0 # position line
pc = 0 # position caractere
p = 0
r = 0 # repeat
txt2 = ''
file = "1.txt"
with open(file, 'r') as text:
    txt1 = text.readlines()
print(txt1)
for l in txt1:
    pl +=1
    for c in l:
        pc += 1
        if '/' == c:
            if r < 1:
                #print('L:', pl, 'C:', pc, 'r:', r, ' ', ' |', l, end='')
                p = pc
                date += l[p+3:p+7]
                date += l[p+0:p+2]
                date += l[p-3:p-1]
                #print(date) 

                txt2 += date + ' '

                date = ''
                p = 0
            r += 1 
            if r > 1:
                r = 0
    txt2 += '\n'       
    pc = 0
print(txt2)
file = '2.txt'
with open(file, 'w') as txt:
    txt.write(str(txt2))

'''
31/01/1900
0123456789
'''