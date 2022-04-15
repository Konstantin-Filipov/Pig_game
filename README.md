 1. General description of the game:
"Pig" is a game played by 2 players. Points for per player are gained when the he/she throws a dice.
For example if player1 throws "6" it means that he has 6 points for now.
Player can throw as many times as he/she wants, so he/she can stack his points.
However when he/she throws "1". His/her turn ends and points that were gained from this turn are reset.
Then is the turn for the next player.
A player can choose to hold his/her hand whenever he/she wants during a turn.
Winner is the player who first reaches 100 points.
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
2. Implementation:
We run the game from Main.py file. This is the "foundation point" which calls another file
in which user passes an argument. Based on the argument the program sets the current game mode(single/multiplayer)
Next file that is run is either singleplayer.py/multiplayer.py.
This is where most of the heavy lifting goes. All of the game logic is in these two files.

- for singleplayer.py:
Here the player is vs the computer.
Setting up bot difficulty is achieved by calling a method("set_bot_level") of instance 'bot'.
This method asks the user for the desired level for the bot to be.
After the input the code sets a randomised number which will represent the times that the bot will throw dice until it decides to hold a hand.
Example:
If the player chooses "normal" level game. It means that bot will throw from 1 to 3 (random int in range (1-3)) times per turn.
Bot's turn itself is an automated one, simply calling roll method of class "Dice" after each player's turn.
If level difficulty is set to "hard". It means that bot will throw from 5 to 8 (random int in range (5-8)) times per turn.

- for multiplayer.py
 player is vs another real player.
 Here the turns are not automated -> each player has to pass arguments to the console in order to make anything during a turn.
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
3. Installations:
- Download the zip containing the game.
- Open cmd/any console with admin privileges.
- You need to check whether you have python package already installed on your PC.
  We do this by checking the current installed python version on the PC by typing:
  "python --version"
- If you don’t have a version of Python on your system, then above command will launch the Microsoft Store and redirect you to the Python application page.
- Download the package.
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
4. Running the game
- Unarchive the downloaded zipped folder.
- Open cmd/any console with admin privileges.
- locate to the game's folder -> example: "cd C:\Users\Public\Desktop\pig_game"
- When You are in the directory. type this -> "python main.py"
- Enjoy!
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
5. To run the complete testsuite
- install coverage:
  open any terminal and type
  "pip install coverage"
- to run all tests, type
  "coverage run -m unittest"
- to run particular test
  "coverage run -m unittest <test_filename>.py"
- to produce report, type:
  "coverage report"
- to generate html file with the report, type:
  "coverage html"
- now navigate to <project_folder>/htmlcov/index.html and open the html file in some browser
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
6. Generate documentation from code
- install pdoc, type in cmd:
  "pip install pdoc"
- to generate the documentation of a file, in cmd, type:
  "pdoc <name_of_module>"
- to save documentation as html under ./doc directory, type in cmd:
  "pdoc <name_of_module> -o ./docs"
  -----------------------------------------------------------------------------------------------------------------------------
  -----------------------------------------------------------------------------------------------------------------------------
  7. Generating UML diagrams from
  - install pylint, in cmd, type:
  pip install pylint
  - Use pyreverse command to create the UML diagram image, in cmd, type:
  pyreverse <name of the file>
  - and then type: dot -Tpng classes.dot -o <output_path_name>
