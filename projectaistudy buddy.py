#AI study buddy(rule based chat assistant in python):
#objective: to create a conversational AI assistat using pythons core logic tsriing matching,function,dic and loops:

import datetime
import time
name = input("hello! enter your name")
presentHour = datetime.datetime.now().hour
if  12<= presentHour <=11:
    print("good morning",name)
elif 12 <= presentHour <=16 :  
    print("good afternoon",name)
elif 17<= presentHour <=20:
    print("good evening",name)
else:
    print("good night",name)    
print("hello! welcome to your ArJa")
print("you can ask me asic quetions,type 'bye' to exit from bot")
responses = {          #creating a memory chatbot using dictionary of respponses:
    "hello" :"Hi,welcome to ArJa.How can I help you",
    "how are you" :"I am fine.Thank you",
    "who are you" :"I am smart AI ChatBot",
    "motivate me" :"I am here to help you! what's up ? what are you working on or trying to achive?",
    "happy" :"thats great! what's making you happy today",
    "what is functions in python" :"functions are blocks of reuasble code that peform a specific task and helps to organize your code make it more readable,you define a function using 'def' keyword",
}
#method/function to get ans of chatbot:

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "Data has not stored yet , Im still yet learning mode,i will learn it soon"
    
#take user input:

while True:

    userInput=input("please ask your question :")
    reply = getResponseOfBot(userInput)
    print("ArJa Response:",reply)

    if "bye" in userInput.lower():
        print("bye have a great day")
        break



