sentence=input()
sign=0

for i in sentence:
    
    if i==".":
        i.replace(".",". ")
        sign+=1
    if len(i)>1:
        if "  " in sentence:
            i.replace("  "," ")
        elif "   " in sentence:
            i.replace("   "," ")
        elif "    " in sentence:
            i.replace("    "," ")
        elif "     " in sentence:
            i.replace("     "," ")
        elif "      " in sentence:
            i.replace("      "," ")
    if i.islower():
        if sign==1:
            i=i.lower()

sentence=sentence.capitalize()
print(sentence)
