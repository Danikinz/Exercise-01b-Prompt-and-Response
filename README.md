# Exercise-01b-Prompt-and-Response
Exercise for MSCH-C220, 26 August 2021

A demonstration of this exercise is available at [https://youtu.be/O1lcQZpKMRM](https://youtu.be/O1lcQZpKMRM).

This exercise is an opportunity for you to create your (perhaps) first program in Python. The purpose of this exercise is to make sure your python setup is working appropriately and then give you the first step toward completing Project 01.

First, Fork the repository. When that process has completed, make sure that the top of the repository reads [your username]/Exercise-01b-Prompt-and-Response. 

*Edit the LICENSE and replace BL-MSCH-C220-F21 with your full name.* Commit your changes.

Press the green "Code" button and select "Open in GitHub Desktop". Allow the browser to open (or install) GitHub Desktop. Once GitHub Desktop has loaded, you should see a window labeled "Clone a Repository" asking you for a Local Path on your computer where the project should be copied. Choose a location where you will keep the repositories for this class (a C220 folder off your Desktop would be fine). Make sure the Local Path ends with "Exercise-01b-Prompt-and-Response" and then press the "Clone" button. GitHub Desktop will now download a copy of the repository to the location you indicated.

Open Visual Studio Code, and select File->Open. Navigate to the repository folder you just cloned, select the folder, and press "Open".

In the far right (black) panel of the window, you should see five icons. The top one is File Explorer. If that is selected, you should see four files listed: .gitignore, LICENSE, main.py, and README.md.

Open main.py. If you are prompted to install the Python plugin, do so now.

The first three lines in the file (the only lines so far) are probably confusing, but I will explain them as part of my demonstration. You can ignore them for now.

On lines 5 and 6, you will see two variables representing the name and description of a passage: passage_name and passage_text. To fulfill the requirements of this exercise, you will need to utilize the contents of these two variables.

Once the program is run, it should display the following:
```
You are at the West of House
This is an open field west of a white house, with a boarded front door.
What would you like to do? 
```
After the question mark (followed by a space), the program should allow the player to type a response. If the player types "go north", then the program should reply with:
```
Good job!
```
As part of the solution, your program must use the passage_name and passage_text variables. Your program will use the [print()](https://realpython.com/python-print/) and [input()](https://pythonexamples.org/python-input/) functions as well as an [if statement](https://pythonbasics.org/if-statements/). 

Capitalization, punctuation, and spacing are all important, so if you run into trouble, check that you have typed everything correctly.

When you are done writing the program, you will need to test it. If you press the green run arrow in the top right corner of your window, you should see a panel appear at the bottom of the window (labeled Console). After it displays some syntax (related to running the program), the console should run the program.

Test it to make sure everything prints appropriately. Type "go north" to make sure you get the right response. Try typing "Go north" or "Go North". Why do you think it behaved like that?

Save these files and quit Visual Studio Code. In GitHub Desktop, you should now see main.py highlighted. Add a Summary message at the bottom of that panel, and push the "Commit to master" button. On the right side of the top, black panel, you should see a button labeled "Push origin". Press that now.

If you return to and refresh your GitHub repository page, you should now see that your files have been changed (with a new date).

Now edit the README.md file. When you have finished editing, commit your changes, and then turn in the URL of the main repository page (https://github.com/[username]/Exercise-01b-Prompt-and-Response) on Canvas.

The final state of the file should be as follows (replacing my information with yours):
```
# Exercise-01b-Prompt-and-Response
Exercise for MSCH-C220, 26 August 2021

A simple use of python's print() and input() functions and an if statement.

## Implementation
Built using Visual Studio Code and Python 3.9.6

## References
None

## Future Development
None

## Created by 
Danielle Dixon
```
