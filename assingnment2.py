
#simple message 
#Assign a message to a variable  and then print and print that message.
message:str="hello i am jaweriahassan" 
print(message)
#simple message 
#Assign a message to a variable  and then print and print that message.
message2:str="hi who are you"
print(message2)
#personal message
message3:str="what is your name"
print(message3)
#personal message
message4:str=("hello ahmed would you like to learn some python today?")
print(message4)
#name cases
message5:str= "JaWeriaHaSSan"
print(message5.upper())
print(message5.lower())
print(message5.title())
#famous quote
quote:str="words without power is mere philosophy"
name:str="allamaiqbal"
print (f"{name}once said,{quote}".title())
#famous qoute2
quote2:str="hum ko maloom hy janat ki haqeeqat dil ki khawish rakhny ko galib ya khyal acha h "
name2:str="mirza galib"
print(f"{name2}once said,{quote2}.".title())
#stripping names 
message6:str="   jaweria hassan"
print(f"{message6}".lstrip())
message7:str="jaweria hassan       "
print(f"{message7}".rstrip())
message8:str="      jaweriahassan      "
print(f"{message8}".strip())
#variable sum
a=5
b=10
c=15
sum=a+b+c
print(f"the sum o a b and c is :{sum}")
#variable spread
a=10
b=5
sum=a+b
print(f" the sum of a b c is :{sum}")
#favourite color
favouritecolor:str="blue"
print(favouritecolor)
newcolor:str="black"
print(f"{newcolor}")
#pet name
petname1:str="cat"
print(f"{petname1}")
petname2:str="dog"
print(f"{petname2}")
#observing name eror
#name4:str="jwera"
#print("name4")
#correctname:str="jaweria"
#print(correctname)
#reassigning score
score:int=100
print(score)
score=99
print(99)
#city nme
cityname:str="lahore"
print(cityname)
#title case text
text:str="pythonprogramming"
print(text.title())
#lower case coversion 
lowercase:str= "PythOnProgramMing"
print(lowercase.lower())
#upper case conversion 
uppercase:str="pythonprogramming"
print(uppercase.upper())
#current temperature 
temperataure:int=25
currenttemperature:int=100
print(f"{temperataure}",f"{currenttemperature}".title())
#ptining a poem 
poem:str="hold fast to dreams for if dreams die life is a broken-winged bird that cannot fly"
print(poem)