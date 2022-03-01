import random

words = ["What is Ansible? How can it be usefull in DevOps?",
"What is Terraform? How can it be usefull in DevOps?",
"What is Vagrant? How can it be usefull in DevOps?",
"What is Centron? How can it be usefull in DevOps?",
"What is GitLab? What is GitLab runner? How can it be usefull in DevOps?",
"What is VMWare? What is VSphere? How can it be usefull in DevOps?",
"What is Kubernetes? How can it be usefull in DevOps?",
"What is the difference between a container and a virtual machine? ",
"What is puppet? How can it be usefull in DevOps?",
"What is chef? How can it be usefull in DevOps?",
"What is Salt? How can it be usefull in DevOps?",
"What is Proxmox? How can it be usefull in DevOps?",
"What is OpenStack? How can it be usefull in DevOps?",
"What is GitHub actions? How can it be usefull in DevOps?",
"What is Salesforce? How can it be usefull in DevOps?",
"What is Service now? How can it be usefull in DevOps?",
"What is GLPI? How can it be usefull in DevOps?",
"What is slack? How can it be usefull in DevOps?",
"What is Azure DevOps? How can it be usefull in DevOps?",
"What is Subversion? How can it be usefull in DevOps?",
"What is Grafana? How can it be usefull in DevOps?",
"What is Heroku? How can it be usefull in DevOps?",
"What is Jenkins? How can it be usefull in DevOps?",
"What is SonarQube? How can it be usefull in DevOps?",
"What is PaaS (Platform as a service)? How can it be usefull in DevOps? Give some examples.",
"What is SaaS (Software as a service)? How can it be usefull in DevOps? Give some examples.",
"What is IaaS (Infrastructure as a service)? How can it be usefull in DevOps? Give some examples.",
"What is Slack ? How can it be usefull in DevOps?",
"What is Maven? How can it be usefull in DevOps?",
"What is Gradle? How can it be usefull in DevOps?",
"What is Selenium? How can it be usefull in DevOps?",
"What is NPM (for Node JS)? How can it be usefull in DevOps?",
"What is nuget? How can it be usefull in DevOps?",
"What is JFROG? How can it be usefull in DevOps?",
"What is Azure Functions? How can it be usefull in DevOps?",
"Is bash usefull in DevOps? How ?",
"Is PowerShell usefull in DevOps ?",
"What is Ruby? How can it be usefull in DevOps?",
"What is the difference between public cloud and private cloud? ",
"What is the best devops tool ? Do you think this exists?",
"Name at least 3 cloud providers , differences from each other?",
"Are containers recommended to be used in production? how is it possible?"]

firstquestion = random.randint(0, 41)
secondquestion = firstquestion

while secondquestion == firstquestion:
    secondquestion = random.randint(0, 41)

thirdquestion = firstquestion

while thirdquestion == firstquestion or thirdquestion == secondquestion:
    thirdquestion = random.randint(0, 41)

print("Firstquestion :")
print(words[firstquestion])
print("Secondquestion :")
print(words[secondquestion])
print("Thirdquestion :")
print(words[thirdquestion])

# input file
fin = open("data.txt", "rt")
# output file to write the result to
fout = open("index.php", "wt")
# for each line in the input file
for line in fin:
    fout.write(
        line.replace("question1", words[firstquestion])
        .replace("question2", words[secondquestion])
        .replace("question3", words[thirdquestion])
    )

# close input and output files
fin.close()
fout.close()
