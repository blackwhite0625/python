import os
fName="class.txt"
if os.path.isfile(fName):
    fr=open(fName,"r")
    flist = fr.readlines()
    for i in flist:
        print(i.strip())
    fr.close()
else:
    print(fName,"不存在")

fa = open(fName,"a")
fa.write("\n共偉文,87,87")
fa.write("\n周瑜安,23,43")
fa.flush()
fa.close()