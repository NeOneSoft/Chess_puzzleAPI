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