#love calculator
print("welcome user")
name1=input("enter the name1")
name2=input("enter the name2")
low_name1=name1.lower()
low_name2=name2.lower()
name=low_name1+low_name2
t=name.count('t')
r=name.count("r")
u=name.count('u')
e=name.count("e")
true=t+r+u+e

l=name.count('l')
o=name.count("o")
v=name.count('v')
e=name.count("e")
love=l+o+v+e

score=int(str(true)+str(love))
if (score<100)or(score>80):
    print(f"your love score is {score}.you got together")
elif(score>50) and (score<79):
    print(f'You go all right. Your score is {score}') 
else:
    print('Your score is {score}')       