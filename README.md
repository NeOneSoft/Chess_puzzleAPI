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

-   5.-Done!!, Now you are ready to use it. Now you can access to  http://0.0.0.0:8000/ for our app. Please read the next section to use it.

- Note: If you want to run unit tests please stop the server and execute the follow command:
```
                            docker-compose run web python manage.py test core
``` 

## Chesspuzzle Travis CI [![Build Status](https://travis-ci.com/NeOneSoft/Chess_puzzleAPI.svg?branch=master)](https://travis-ci.com/NeOneSoft/Chess_puzzleAPI)   