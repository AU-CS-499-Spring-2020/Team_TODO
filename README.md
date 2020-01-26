# Welcome to Pycket
Pycket (pronounced picket) is the title of our project for CS 499. This will be a Python based application built using the Flask web framework combined with MySQL. While this application is primarily a ticketing/support system, it will also incorporate the functionalities of a web store. 

## Prerequisites
### Install Git
The download for git can be found [here](https://git-scm.com/downloads)

### Install Python
The download for Python can be found [here](https://www.python.org/downloads/) (download and install 3.8.1).

### Setup Git/Github
For setting up git/github, follow the guide found [here](https://www.theodinproject.com/courses/web-development-101/lessons/setting-up-git). You can skip the install section and move directly to the section titled, "Configure Git and Github." Following this section will allow the user to push/pull from our Github using a signed SSH key allowing for more security and ease of use.

You will need to clone our Github repository to your machine. You can accomplish this by:
1. Open a terminal, powershell, or other prompt.
2. Navigate to your desired directory.
3. Use `git clone https://github.com/AU-CS-499-Spring-2020/Team_TODO.git`.

Congrats, you now have a local copy of the repository housed on your own machine.

### Setup a Virtual Environment
Learn about virtual environments [here](https://realpython.com/python-virtual-environments-a-primer/).

Use the following to setup a python virtual environment for our project.
1. Open a terminal, powershell, or other prompt.
2. Navigate to your local repository.
3. Type `python3 -m venv venv` for Unix/MacOS or `python -m venv venv` for Windows machine.
4. Activate the virtual environment using `source venv/bin/.activate` for Unix/MacOS or `venv/Scripts/activate.bat` for Windows.
5. You are now in the virtual environment and your prompt should read `(venv) $`.
6. We now need to install Flask and its dependencies. Type `pip install flask`.
7. Flask is now installed and we are ready to build our flask app.

## Journals
Each team member is to have their own journal. Team members are responsible for maintaining and updating their own journals with whatever project related tasks they worked on that day. Project related tasks include but are not limited to coding, reviewing code, design, team meetings, pair programming, etc. Again, each team member is responsible for maintaining and updating their own journals. 