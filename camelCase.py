words=input("enter the string").lower()#get input from user and convert to lower
newword=words.title()#convert first letter of all words to capital
for x in newword:
    final=newword[0].lower()+newword[1:]#convert first letter of string to lowercase
print (final)
