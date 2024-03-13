
# gudlift-registration 


1. Why

    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.


2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 

        **Edit**: Updated Flask in 3.0.0 version (27/02/24) 
        [Versions Flask](https://flask.palletsprojects.com/en/3.0.x/changes/#version-3-0-0) 
        [Doc Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/) 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 

    **Edit**: Use Pipenv instead of virtualenv 
    [Doc Pipenv](https://docs.pipenv.org/) 


3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory. 
    **Edit**: Pipenv 
    1. Enter the project folder and type `pipenv install` to install the packages and create the Pip files. 
    2. Type `pipenv shell` to run the virtual env. 
    3. Entrer dans le dossier du projet `cd Python_Testing` 
    4. Run the Flask project: `flask --app=server.py <--debug> run` 

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser. 

    **Edit: run the server** 
    In Flask 3.0.0, type:    
    `cd Python_Testing`     
    `flask --app server run --debug` 
    to run the server. 


4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login. 

    **Edit: clubs.json** 
    I have modified the number of points of the last club, the errors was not thrown instead. 
    ```json
    {
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": 14
    } 
    ``` 

    **Edit: competitions.json** 
    I have added a competition, in order to test a future date of competition: 
    ```json
        {
            "name": "New Winter",
            "date": "2024-12-22 13:30:00",
            "numberOfPlaces": 15
        }
    ``` 

5. Testing

    You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using. 

    We also like to show how well we're testing, so there's a module called 
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.


    **Edit: run the tests** 
    * Pytest usage: 
    - launch pipenv 
    - enter the folder: `cd Python_Testing` 
    - run the tests: `pytest path/to/test_file.py <-v>`  (`-v` = "verbose") 
    * Coverage usage: 
    To launch the coverage: `pytest --cov=tests/` 

    The coverage indicates only the % of the tests passed with success, not the coverage of the code itself. 


6. Performance 

    This setup uses [Locust](https://docs.locust.io/en/stable/index.html) to test the load performance. 

    To run it: 
    - `locust` 
    - and open the `http://localhost:8089` url to drive the tools. 

    Locust allows to measure the time to run requests. Into the script, indicate the requests to test. 
***
    L'outil Locust va te permettre de mesurer le temps de test requetes. Dans le script locust tu spécifies les requetes que tu veux tester. 
*** 

