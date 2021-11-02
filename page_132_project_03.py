"""
Author: Phan Ngoc Linh
Date: 25/09/2021
Problem:
   Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.
Solution:
    ....
"""
infileName = input("Enter the input file name: ")
outFileName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))
inFile = open(infileName,"r")
outFile = open(outFileName,"w")
code = ""
for line in inFile.readlines():
    flag = 0
    if '\n' in line:
        flag = 1
        line = line.strip('\n')
    for ch in line:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > 127:
            cipherValue = distance - (127 - ordValue + 1)
        code += chr(cipherValue)
    if flag == 1:
        code += '\n'
outFile.write(code)
inFile.close()
outFile.close()