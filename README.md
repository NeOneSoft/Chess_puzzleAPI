# ChessPuzzle API

- This application was created based on 8 queens puzzle solution and this document explain you how to use it.

## Use with Docker 

- This instructions assume that you have already install docker and docker compose. If don't, please do it before continue.

-   1.- Download this repository in your local machine.
    
-   2.- Open it with your code editor (PyCharm, VisualStudioCode, etc...).
    
-   3.- On your terminal execute the  follow command (This command build containers, install requirements and make migrations for postgres database instance ):
```
                            docker-compose run web python manage.py migrate
```  
-   4.-To run docker compose execute on your terminal the follow command:
```
                            docker-compose up
```  

-   5.-Done!!, now you are ready to use it. Now you can access to  http://0.0.0.0:8000/ for our app. Please read the next section to use it.

- Note: If you want to run unit tests please stop the server and execute the follow command:
```
                            docker-compose run web python manage.py test core
```

## Use Instructions

- Once executed docker-compose up command and your server is running, open http://0.0.0.0:8000/ in your browser:

-   1- As you can see you will get Page not found (404) and some url patterns, so please follow the next url:
    **http://127.0.0.1:8000/api/v1/**
-   2- Now you are in our API root and you can access to the next endpoint:
    **http://127.0.0.1:8000/api/v1/boards/**
-   3- Now you are in our Board List and you can create your board using the html form with board size/puzzles using values between 8-12(I recommend to start with 8 as original problem).
-   4- Once you create your board, you will get a JSON object with the id and board size.
-   5- To get the detail please follow the next url:
    **http://127.0.0.1:8000/api/v1/boards/1/**
-   6- Our API has an extra action to calculate the solutions of your board (This can take a little while depending on you board size). For this case follow the next url:
    **http://127.0.0.1:8000/api/v1/boards/1/results/**
-   7- Done!!, as you can see you will get a response with found solutions for your board and you can see the positions of each solution on your terminal as well.
     

## Chesspuzzle Travis CI [![Build Status](https://travis-ci.com/NeOneSoft/Chess_puzzleAPI.svg?branch=master)](https://travis-ci.com/NeOneSoft/Chess_puzzleAPI)
-  TravisCI keeps running your unit tests automatically for every change that you make on your repository.

## Chesspuzzle Run Local
- In case you want to run on your machine, take in count the next considerations and instructions:

#### Languages, Frameworks and Libraries: 
- Python3.8 / Django3.0: Used as main language and framework respectively.
- Djangorestframework 3.11: Used to create and manage our API rest, endpoints and database.
- Postgres/SQLite3: Used as databases
- Pytest 6.0: Used to write some unittest and get coverage metrics for our APIrest and application models.

### Modules:
- Boards  

### Local Install instructions:

Before running please follow this steps:

- 1- Create new folder in your selected path(Desktop, Downloads, Documents, etc..)
- 2- Clone this repository and move the unzipped folder to the new folder created previously
- 3- Open your terminal and move it to the path folder created on step 1
- 4- Create a virtual environment using the next command (MacOS):
```
                            python3 -m venv <yourvenvname>
``` 

## Running local Chesspuzzle API  

- 1- Open your cloned repository (located in your new folder created in previous section) using
     your code editor preferred (PyCharm, VisualStudioCode, ...)
- 2- Open your code editor's terminal and use "cd .." command to move one folder back into directory path
- 3- Activate your virtual environment using the next command(MacOS):
```
                            source <yourvenvname>/bin/activate
```
- 4- Once you have activated your virtual environment, return to your cloned repository (this should be one up folder) using "cd <reponame>" command 
- 5- Install all requirements located in requirements.txt file using the next command:
```
                            pip install -r requirements.txt
```
- 6- IMPORTANT: This repo can run with SQLite3 or Postgres (the easiest way is using SQLite3).

-   a) For use SQLite3:
        
        - 1.1 .- Go to Chesspuzzle/settings.py
        - 1.2 .- Comment POSTGRES DockerConfiguration section and Uncomment SQLite3 Local configuration section
        - 1.3 .- Execute 'python3 manage.py makemigrations' command 
        - 1.4 .- Execute 'python3 manage.py migrate' command
       
    b) For use Postgres:
    
        -2.1 .- Make sure that you have all ready installed PGAdmin4 in your machine. If don't, please do it before continue
        -2.2 .- Open PGAdmin4 and create a new database
        -2.3 .- Go to Chesspuzzle/settings.py
        -2.4 .- Comment POSTGRES DockerConfiguration section, Uncomment Postgres Local configuration section and set your NAME, USER AND PASSWORD postgres database
        -2.5 .- Execute 'python3 manage.py makemigrations' command
        -2.6 .- Execute 'python3 manage.py migrate' command

- 7- Done!!! You can run your local server using the nex command (MacOS)
```
                            python3 manage.py runserver
```
- 8- Open your browser at **127.0.0.1:8000**
- 9- Follow the 'Use Instructions' section described before: