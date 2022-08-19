import pyttsx3
import wikipedia


engine = pyttsx3.init()

#Voice
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate


def talk_function(text):
    engine.say(text)
    engine.runAndWait()


while True:

    user_input = input("User: ")
    user_input = user_input.lower()

    if user_input == "hello":
        talk_function("Hey!! hello human , I'm Brainy, the Robot. Speed 1 terahertz, memory 1 zigabyte.");

    elif user_input == "when were you created":
        talk_function("I have created last week, by thigshicca, for your service");
        
    elif user_input == "oh nice":
        talk_function("tell me, how can i help you");

    elif user_input == "please do an addition":
       
        talk_function("Please provide me first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 + num2
        print(f'The total is: {total}')
        talk_function(f'The total value is: {total}')

    elif user_input == "please do an subtraction":
       
        talk_function("Please provide me first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 - num2
        print(f'The total is: {total}')
        talk_function(f'The total value is: {total}')

    elif user_input == "please do an Multiplication":
       
        talk_function("Please provide me first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 * num2
        print(f'The total is: {total}')
        talk_function(f'The total value is: {total}')

    elif user_input == "please do an division":
       
        talk_function("Please provide me first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 / num2
        print(f'The total is: {total}')
        talk_function(f'The total value is: {total}')    
    
    elif "who" in user_input:
        data = wikipedia.summary(user_input)
        print(data)
        talk_function(data)

    elif "what" in user_input:
        data = wikipedia.summary(user_input)
        print(data)
        talk_function(data)
        
    elif user_input == "days of the week":
        talk_function('''Sunday
        Monday
        Tuesday
        Wednesday
        Thursday
        Friday
        Saturday''');
           
    elif user_input == "months of the year":
        talk_function('''January 
February 
March 
April
May 
June 
July 
August 
September 
October 
November 
December ''');
        
    elif user_input == "thankyou so much brainy":
        talk_function("it's my pleasure to help you");

    elif user_input == "bye":
        talk_function("byeee.., have a great day!!");       

    else:
        talk_function("I don't understand");