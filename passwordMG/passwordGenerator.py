import random
import string


def passwordGenerator(length=10,punctuation=True):
    password=''
    punctuationLength=5
    punctuationCount = 0
    for i in range(0,length):
        choice = random.randint(1,100000)
        if choice % 2 == 0:
            letter = chr(random.randint(65,90))
        elif choice % 2 != 0:
            letter =chr(random.randint(97,122))
        punctuationChoice = random.randint(0,31)
        password += letter
        if punctuationChoice % 2 == 0 and punctuationCount < punctuationLength and len(password) < length:
            password += string.punctuation.replace(',','')[punctuationChoice]
            punctuationCount += 1
    return password



def passwordGen(length,username,description):
    password = passwordGenerator(length)
    allClear = 0
    with open('passwordStore.csv','a+') as fwr :
        fwr.seek(0)
        data = fwr.readlines()
        for line in data:
            if password == line.split(',')[1]:
                allClear = 1
                break
        if allClear == 0:
            fwr.write('{},{},{}\n'.format(username,password,description))

if __name__ == '__main__':
    length=25
    username='testName'
    description='test.com'
    passwordCall(length,username,description)