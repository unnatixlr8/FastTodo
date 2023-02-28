# FAST-TODO APP

A Todo app made using FastAPI. It supports CRUD operations on the SQLite DB.
It supports User Creation, Password Hashing, JWT Token Generation and Authorization.


## Steps to run

 1. Clone the repo
 2. Create a Python virtual environment using `python3 -m venv fastvenv`
 3. Activate your virtual environment to run the program using `source fastvenv/bin/activate`
 4. Install dependencies using `pip3 install -r requirements.txt`
 5. Start the server with `uvicorn main:app --reload`
 6. Open localhost:8000 on the Web Browser.
 

## Create User

 1. Click on `/user` Create api and click `Try it out`.
 2. Give a username and a password and Press Execute.
 3. User will be created

## Login and Authorize

 1. Click on Authorize button on the homepage.
 2. Login with the newly created user created above.
 3. It should successfully login to use the other locked apis.

# CRUD Operations

You can perform the crud operations on the db only after logging in.

## Create a Todo

 1. Click on the `/todo ` Create api. 
 2. Type in your todo and press execute.
 3. Your todo will be saved with your user_id.

## View the todos

 1. Click on the `/todo` All api.
 2. It will list all the todos created the logged in user.

## Delete the todos

 1. Click on the `/todo`Delete api.
 2. Pass in the todo_id and press execute.
 3. It will get deleted.

## Update the todos

 1. Click on the `/todo`Update api.
 2. Pass in the todo_id and pass the new todo content.
 3. It will get updated.

