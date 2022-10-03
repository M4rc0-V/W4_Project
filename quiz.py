from getpass import getpass
import json
import requests
import time
import base64

url = "https://cae-bootstore.herokuapp.com/"
endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"

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
print(login_user('jimb@eam7.com','123'))

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
    password=getpass("Password: ")
    user=login_user(email, password)
    return user

def register():
    print("Registration:")
    email=input("Email: ")
    first_name=input("First Name: ")
    last_name=input("Last Name: ")
    password=getpass("Password: ")
    
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
        print("Welcome to the Bookstore")
        email = input("Type your email to login or Type `register` to Register")
        if email == 'register':
            success_register = register()
            if success_register:
                print("You have successfully registered")
                continue
            else:
                print("There was an error please try again")
                time.sleep(2)
                continue
        elif email.lower() == "quit":
            print("Goodbye")
            break
        else:
            try:
                login(email)
            except:
                print("Invalid Username/Password Combo")
                time.sleep(2)
                continue

        if email == "marco.a.vazquez@icloud.com":
            print ("Admin")
            print ("""
Admin Options:
1. Create Question
2. Edit Question
3. Delete Question
4. View My Questions
            """)
            option = input("Enter Option")
            if option == "1":
                create_question()
            elif option == "2":
                edit_question()
            elif option == "3":
                delete_question()
            elif option == "4":
                view_questions()
        else:
            print ("User")

def create_question():
    question = input("What is your Question?")
    answer = input("What is your Answer?")
    new_question = {
        "question": question,
        "answer": answer
    }

def edit_question():
    pass

def delete_question():
    pass

def view_questions():
    pass





