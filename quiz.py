from getpass import getpass
import json
import requests
import time
import base64
import random
import os


url = "https://cae-bootstore.herokuapp.com"
endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"
endpoint_question = "/question/all"

def login_user(user_name, password):
    
    auth_string=user_name+':'+password
    
    headers = {
        'Authorization': "Basic "+base64.b64encode(auth_string.encode()).decode()
    }

    user_data=requests.get(
        url + endpoint_login,
        headers = headers
    )
    return user_data.json()
    




def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text


def login(email):
    password=input("Password: ")
    user=login_user(email, password)
    return user

def register():
    os.system('cls')
    print("Registration:")
    email=input("Email: ")
    first_name=input("First Name: ")
    last_name=input("Last Name: ")
    password=input("Password: ")
    
    user_dict={
        "email":email,
        "first_name":first_name,
        "last_name":last_name,
        "password":password,
        "status": "user"
    }

    if email == "marco.a.vazquez@icloud.com":
        user_dict["status"] = "admin"

    return register_user(user_dict)

def main():
    while True:
        os.system('cls')
        print("Welcome to the Quizbowl")
        email = input("To Login type your 'email'\nto Register type 'register': ")
        if email == 'register':
            success_register = register()
            if success_register:
                print("You have successfully registered")
                os.system('cls') 
                continue
            else:
                print("There was an error please try again")
                time.sleep(2)
                continue
        elif email.lower() == "quit":
            os.system('cls')
            print("Goodbye")
            break
        else:
            try:
                login(email)
            except:
                print("Invalid Username/Password Combo")
                os.system('clear')
                continue

        if email == "marco.a.vazquez@icloud.com":
            os.system('cls')
            print (
"""Admin Options:
1. Create Question
2. Edit Question
3. Delete Question
4. View My Questions
5. Take Quiz
            """)
            while True:
                option = input("Enter Option: ")
                if option == "1":
                    create_question()
                    break
                elif option == "2":
                    edit_question()
                    break
                elif option == "3":
                    delete_question()
                    break
                elif option == "4":
                    view_questions()
                    break
                elif option == "5":
                    start_quiz()
                    break
                else:
                    print("Invalid option, please try again")
        else:
            print("Welcome User")
            answer = input("Would you like to start the quiz or quit? 'start to start' or 'quit to quit': ")
            if answer.lower().strip() == "quit":
                break
            elif answer.lower().strip() == "start":
                start_quiz() 

def create_question():
    question = input("What is your Question? ")
    answer = input("What is the Answer? ")
    new_question = {"question": question,
                    "answer": answer
                   }

def edit_question():
    os.system('cls')
    while True:
        ans = input("What Number Question would you like to Edit? 'Quit' to quit: ")
        if ans.lower().strip() == 'quit':
            break
        # elif dic[qestion_number] == int(ans):
            pass # edit qestion
        else:
            print('Invalid input, plesase try again')

def delete_question():
    os.system('cls')
    while True:
        ans = input("What Number Question would you like to Delete? 'Quit' to quit: ")
        if ans.lower().strip() == 'quit':
            break
        # elif dic[qestion_number] == int(ans):
            pass # delete qestion
        else:
            print('Invalid input, please try again')

def view_questions():
    os.system('cls')
    while True:
        questions = requests.get(url+endpoint_question)
        question_number = 0
        for question in questions.json()['questions']:
            print(f'Question #{question_number+1}')
            print(f"Question ID: {question['id']}")
            print(f"Question: {question['question']}")
            print(f"Answer: {question['answer']}\n")
            question_number += 1
        answer = input("Quit to quit: ")
        if answer.lower().strip() == 'quit':
            break
        else:
            print("Invalid input, please try again")
    
    

def start_quiz():
    total_correct = 0
    question_number = 0
    while question_number < 2:
        os.system('cls')
        questions = requests.get(url+endpoint_question)
        print(questions.json()['questions'][question_number]["question"])
        answer = input("Enter your answer: ")
        if answer.lower().strip() == questions.json()['questions'][question_number]["answer"]:
            total_correct += 1
            os.system('cls')
            print("That answer is correct! Congrats!")
            time.sleep(2)
        else:
            os.system('cls')
            print("Not even close, try again!")
            time.sleep(2)
        question_number += 1
    os.system('cls')
    print(f"The quiz is now complete, your total is {total_correct} out of 10")
    time.sleep(4)

main()



