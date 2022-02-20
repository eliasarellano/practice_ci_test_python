import random

words = ["rambo1","rambo2","rambo3",
        "rambo4","rambo5","rambo6"]

firstquestion = random.randint(0,5)
secondquestion = firstquestion

while secondquestion == firstquestion:
  secondquestion = random.randint(0,5)

thirdquestion = firstquestion

while thirdquestion == firstquestion or thirdquestion == secondquestion:
  thirdquestion = random.randint(0,5)

print("Firstquestion :")
print(words[firstquestion])
print("Secondquestion :")
print(words[secondquestion])
print("Thirdquestion :")
print(words[thirdquestion])

#input file
fin = open("data.txt", "rt")
#output file to write the result to
fout = open("index.html", "wt")
#for each line in the input file
for line in fin:
    fout.write(line.replace('question1', words[firstquestion]).replace('question2', words[secondquestion]).replace('question3', words[thirdquestion]))
#close input and output files
fin.close()
fout.close()
