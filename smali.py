import re
smali = open ("d:/a","r")
text = smali.readlines()
smali.close()
for line in text:
    if line.find(".line")!=-1:
        text.remove(line)

save = open ("d:/c","w")
save.writelines(text)
save.close()
