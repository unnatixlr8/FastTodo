# FAST-TODO APP

A Todo app made using FastAPI. It supports CRUD operations on the SQLite DB.
It supports User Creation, Password Hashing, JWT Token Generation and Authorization.

![Screenshot 2023-02-28 at 6 18 35 PM](https://user-images.githubusercontent.com/20882958/221864869-cb88467f-0c56-44ae-8893-9752ac9550dd.png)

![Screenshot 2023-02-28 at 6 44 08 PM](https://user-images.githubusercontent.com/20882958/221865012-3f48a201-7a59-427c-ad4a-0e6c9ffbbe99.png)

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

![Screenshot 2023-02-28 at 6 23 06 PM](https://user-images.githubusercontent.com/20882958/221865286-b4af13fc-96dc-43a3-9320-53901e79f0fe.png)

## Login and Authorize

 1. Click on Authorize button on the homepage.
 2. Login with the newly created user created above.
 3. It should successfully login to use the other locked apis.

![Screenshot 2023-02-28 at 6 23 54 PM](https://user-images.githubusercontent.com/20882958/221865407-69c659d6-e874-4da8-89a1-1fc65f65c4f3.png)

![Screenshot 2023-02-28 at 6 24 13 PM](https://user-images.githubusercontent.com/20882958/221865421-0465e1e2-bb01-4dc7-b8e7-8e45da30cd67.png)

# CRUD Operations

You can perform the crud operations on the db only after logging in.

## Create a Todo

 1. Click on the `/todo ` Create api. 
 2. Type in your todo and press execute.
 3. Your todo will be saved with your user_id.
 
 ![Screenshot 2023-02-28 at 6 29 58 PM](https://user-images.githubusercontent.com/20882958/221865843-54e98684-abba-47fc-864d-ed4ff5dab3a1.png)

## View the todos

 1. Click on the `/todo` All api.
 2. It will list all the todos created the logged in user.
 
 ![Screenshot 2023-02-28 at 6 30 20 PM](https://user-images.githubusercontent.com/20882958/221865945-742f8aa8-b226-4f9a-aa39-8e54c3c91c8b.png)

## Delete the todos

 1. Click on the `/todo`Delete api.
 2. Pass in the todo_id and press execute.
 3. It will get deleted.
 
 ![Screenshot 2023-02-28 at 6 37 53 PM](https://user-images.githubusercontent.com/20882958/221866017-af268e98-3731-4b6f-b242-c4286f0acc16.png)

## Update the todos

 1. Click on the `/todo`Update api.
 2. Pass in the todo_id and pass the new todo content.
 3. It will get updated.
 
 ![Screenshot 2023-02-28 at 6 39 29 PM](https://user-images.githubusercontent.com/20882958/221866144-9e08a110-6552-482f-8503-63b26ed1ace4.png)

