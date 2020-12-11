# Math flask app
Flask-app to do addition, subtraction, multipliation and division. 

## How to use
To develope this app simply run the `docker-compose up` and you will get the development set-up. Then you can simply change the app on your local machine. The Dockerfile provides a production version of the app.

## Resource Table
|Method | Path | Used to | Parameters | error-codes |
| --- | --- | --- | --- | --- |
| POST | /add | Add two numbers | x:int, y:int | 200 OK, 301 Missing |
| POST | /subtract | Subtract two numbers | x:int, y:int | 200 OK, 301 Missing |
| POST | /multiply | Multiply two numbers | x:int, y:int | 200 OK, 301 Missing |
| POST | /divide | Divide two numbers | x:int, y:int | 200 OK, 301 Missing |
