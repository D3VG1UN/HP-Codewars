sentence=input()
sentence=sentence.lower()

alphabet="abcdefghijklmnopqrstuvwxyz"

for i in sentence:
    alphabet=alphabet.replace(i,"")

if len(alphabet)==0:
    print("Pangram found")
else:
    print("Pangram not found")