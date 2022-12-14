# PORTFOLIO PROJECT - 3 PYTHON 

# Word-It

<img src="assets/readme-docs/welcome-to-word-it.png" width=600>
 
Word-It is a five letter word guessing game that is based on the popular daily online game "Wordle". I chose to base my project off this because I became addicted to Wordle during the pandemic, and have a passion for word games.

The game is a process of elimination, combined with a little luck and logical thinking. It's a great way to test a user's problem solving ability and a quick game to do during a coffee break in work! Don't get too competitive now...

## Project Live Links
* [Here is a link to my Github Repo for PP3 Word-It](https://github.com/LynneMcGrail/Portfolio-Project-3-Word-it)
* [Here is a link to my Heroku App - Word-It](https://word-it.herokuapp.com/)

#
## Table of Contents
- [WORD-IT](#word-it)
- [PROJECT LIVE LINKS](#project-live-links)
- [INITIAL IDEA CONCEPT](#initial-idea-concept)
- [HOW TO PLAY](#how-to-play)
- [FEATURES](#features)
- [UX/UI](#uxui)
    * [SITE GOALS](#site-goals)
    * [FIRST TIME VISITOR AND RETURNING VISITOR GOALS](#first-time-visitor-and-returning-visitor-goals)
    * [USER STORIES](#user-stories)
    * [REQUIREMENTS](#requirements)
    * [EXPECTATIONS](#expectations)
- [LOGIC FLOW](#logic-flow)
- [GAME FEATURES](#game-features)
  * [WELCOME START SCREEN](#welcome-start-screen)
  * [MENU](#menu)
  * [INSTRUCTIONS](#instructions)
  * [GAME PLAY](#game-play)
  * [INPUT VALIDATION AND ERROR HANDLING](#input-validation-and-error-handling)
  * [USER GUESS FEEDBACK](#user-guess-feedback)
  * [GAME WON](#game-won)
  * [GAME LOST](#game-lost)
  * [GAME OVER](#game-over)
  * [FUTURE FEATURES](#future-features)
- [CLASSES](#classes)
- [LANGUAGES USED](#languages-used)
- [TESTING](#testing)
  * [PEP8 CI](#pep8-ci)
  * [MANUAL TESTING](#manual-testing)
- [BUGS AND ERRORS](#bugs-and-errors)
  * [SOLVED BUGS](#solved-bugs)
  * [UNSOLVED BUGS](#unsolved-bugs)
- [DEPLOYMENT](#deployment)
  * [HEROKU](#heroku)
  * [HOW TO FORK A REPOSITORY](#how-to-fork-a-repository)
  * [HOW TO CLONE A REPOSITORY](#how-to-clone-a-repository)
  * [HOW TO MAKE A LOCAL CLONE](#how-to-make-a-local-clone)
- [CREDITS AND REFERENCES](#credits-and-references)
  * [CODE](#code)
  * [ACKNOWLEDGEMENTS](#acknowledgements)

### Initial Idea Concept
My idea for this Python project was to replicate the Wordle game, because it is well-known, and if a user has never played it before it is simple to play which is why I included the option for the user to read the game instructions on starting the game. This game `Word-It` has replay ability as the site allows users to play again with a random generator imported into my code so that a different word is retrieved from the database contained in the `words.txt` file, this allows users to challenge themselves. This game functionality and word database is suitable for all ages and skill levels. I chose to use coloured text in my code so that it appealed to users and was clearly indicating their progress, this is further explained below in the `Colorama` section.

### How to Play
- The user has 6 guesses to get a random 5 letter word correct
- After each guess the user is provided with colour-coded letters to tell them if any of the letters they have entered are correct, and in the right letter position;
  - Green tells the user that the letter is correct and in the right position.
  - Yellow tells the user that the letter is in the word but is in the wrong position.
  - Red tells the user that the letter is not in the word. 
- The user must guess carefully, as they only have 6 chances, throughout the gameplay the various colour coded letters are displayed which will help the player disregard certain words, by process of elimination.
- If the user enters the correct word within 6 guesses, they will win the game. 
- If they do not guess the correct word within 6 guesses, the AI will tell the user the word and the user can play again, or quit the game.

### Features
* Interactive game play elements to enhance user experience, the user is asked to enter their username (and validated it is letters and not left blank) and then the AI returns a welcome message and retrieves their name from the data they input.
* Instructions which appear in an ASCII art border like a scroll, again a typical 'game' feature that people would be familiar with from games as kids such as on consoles like nintendo switch etc. or online games.
* The total number of guesses is printed on starting the game
* And as the user guesses, the remaining number of guesses is printed on each input request to the user so that the user can see how many more chances they have to guess the word. 
* Colour indicators that let the user know if any of the letters they entered are correct, green indicates a correct letter and the right position, a yellow letter indicates a correct lettter, but in the wrong position and letters that are not in the word are incorrect and these are printed in red. 
* I wanted to create an app that was easily accessible and user friendly, with options for the user to play again or simply quit on finishing their first game. 
* For `Word-It` to look fun and interactive I not only used colours, but used ASCII borders and text to enhance the users experience and enjoyment. This can be seen on the initial start screen 'Welcome to Word-It' and throughout the gameplay when the user wins; 'You Win', and if the user decides to quit the game 'Goodbye' is printed in ASCII art words.

## UX/UI
This Word-It game was created to show my programming knowledge of Python so far with Code Institute.
### Site Goals
* To showcase my software development skills in Python.
* To create a user experience that was intellectually challenging, engaging and rewarding.
* To create an app that functions well, returns feedback to the user and is easily accessible to all. 
* To entice the user to play the game again.

### First Time Visitor and Returning Visitor Goals
* I want it to be easy for the user to play the game.
* I want the user to be able to easily navigate throughout the instructions and understand the gameplay.
* I want the user to be enticed to play the game again.
* I want the game to select a different word each time the user plays, and will achieve this by using the Python library [random](https://docs.python.org/3/library/random.html?highlight=random#module-random) - `random.choice`, which will select a random word from the words.txt file.

### User Stories  
The user is any person who enjoys word games and likes to test their problem solving skills.

| ID | ROLE | ACTION | GOAL |
|-----------------|:-------------|:---------------:|:---------------:|
| 1 | USER | As a user, I want to guess the word in 6 guesses or less | So I can win Word-It and challenge myself|
| 2 | USER | As a user, I want to navigate the game play easily | So it enhances my user experience|
| 3 | USER | As a user, I want to be able to start the game when I am ready | So I can prepare myself |
| 4 | USER | As a user, I want the choice to load the game instructions if I need them | So I can decide if I need them or not |
| 5 | USER | As a user, I want to see how many letters are correct / incorrect as I play | So I can see how close I am to winning |
| 6 | USER | As a user, I want to be able to play again when the game ends with a new word | So I can challenge myself|
| 7 | USER | As a user, When the game ends, I want the option to quit or play again | So I can choose to leave if I want to|

#
### Requirements 
- Easy to navigate and understand the game play, which is enabled via the instructions menu option
- Keep the user engaged through user experience; the use of Pyfiglet word art, username input and welcome message which addresses the user, guess validation, guess colour coded letter feedback, user's remaining guesses counter throughout the gameplay, game over win / lose, the correct word displayed if the user loses, and giving the user the option to play again or quit - on quitting the game displays a goodbye message.

### Expectations 
- The user will be prompted to enter their username to start the game and the AI will welcome the user and import the data they input as their username.
- The user will have the choice to either initiate game play or read the instructions, this is an option as a returning user will be familiar with how to play and may not want to read the instructions every time.
- I expect that after each guess, the app will provide feedback to the user and let them know which letters are correct (green), correct but in the wrong letter space (yellow) or incorrect and not in the word (red), and should the user not guess the word within the 6 guesses, the game will return the word they were trying to guess.
- Game over - I expect the user to be able to choose to play again, or quit the game, on which if they choose to quit, a "Goodbye" message will be displayed to the user. If they choose to play again, the game will clear and start from the beginning.

## Logic Flow 
### Lucid Chart 
* I used [Lucid Chart](https://www.lucidchart.com/pages/) to create a flow chart in order to visualise the game play, and how each of the stages in the game would execute and from this, I was able to make a plan for the functions that would be required in Python.

  <details>
  <summary>Flow Chart Diagram</summary>

  ![Lucid Chart](assets/readme-docs/Wordit_Flowchart.png)
</details><br>

#
## Game Features
### Welcome Start Screen
* On entering the site, the user is greeted with a welcome message and prompted to input their name to begin.
* The welcome message was created using Pyfiglet which takes ASCII text and renders it in [ASCII art fonts](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)<br>

<img src="assets/readme-docs/welcome-screen.png" width=600>

* The game validates the user input, by ensuring the data entered consists of numbers or letters, they cannot submit blank space. An error message will appear if the data is invalid.

<img src="assets/readme-docs/username-validation.png" width=600>

### Menu 
* Once the username has input their name, the computer will greet them by name.

<img src="assets/readme-docs/menu-options.png" width=600>

* They will then be asked if they would like to play the game or read the instructions by inputting "P" or "I".
* The input can be upper or lower case, the app can handle both inputs by using the function, lower()
* If the user does not input a "P", "p", "I" or an "i" they will get an error message asking them to input a valid option.

<img src="assets/readme-docs/menu-validation.png" width=600>

### Instructions
* If the user inputs "I" or "i", the instructions on how to play the game will be displayed.
* The instructions are simple and contained within a scroll to make it fun and a feature which makes it feel like an old gameboy style game, this was reminiscent from my childhood and created using [ASCII art](https://www.asciiart.eu/art-and-design/borders)
* The game will start below the scroll

<img src="assets/readme-docs/game-instructions.png" width=600>

### Game Play
* When the user selects "P" or "p" from the menu, the game will start. Or had they chosen the instructions, the game will play immediately below the scroll displaying the instructions on how to play the game. 
* The user is told they have 6 chances and are asked to enter a 5 letter word as their first guess.

<img src="assets/readme-docs/menu-play.png" width=600>

### Input Validation and Error Handling
The user's guess is validated to ensure:
  * The guess must be 5 characters in length
  * It must contain all letters and no blank space
  * If the data input is invalid, the user will be given an error message in red writing and asked to input a new guess

<img src="assets/readme-docs/input-validation-error-handling.png" width=600>

### User Guess Feedback 
* When the user inputs a valid guess, their word is printed back to them and centered on the screen.
* A coloured background is applied to each letter to indicate whether a letter is correct, incorrect, or correct but in the wrong letter space (as per the detailed instructions on how to play Word-It). This is achieved using [Colorama](https://pypi.org/project/colorama/)
* Black letters are used against the coloured background to ensure good user accessibility and readability.
* Each time a user inputs their next guess, the previous guess along with the new one are printed in a list format. This helps the user determine, by process of elimination, which letters they have already guessed, and any changes they might make to the order of the letters depending on the feedback colour indicators.
* After each guess they make, their remaining guesses is displayed.

<img src="assets/readme-docs/first-guess.png" width=600><br>

<img src="assets/readme-docs/guesses-remaining.png" width=600>

### Game Won
* If the user guesses the correct word, the game ends and a "You Win" message is displayed.

<img src="assets/readme-docs/game-won.png" width=600>

### Game Lost
* If the player uses all 6 guesses without guessing the correct word, the game will end and the game over message is displayed and the correct word is revealed to the user. 

<img src="assets/readme-docs/game-over.png" width=600>

### Game Over 
* The game over menu appears on completing the game, the user is presented with the option to play again, or quit. 
* The app can handle the input of lowercase or uppercase letters for the user's choice to play - "P" "p" or quit - "Q" "q".
* Error handling will display an error message if the user inputs an invalid option.

<img src="assets/readme-docs/game-over-menu.png" width=600>

* If the user chooses quit, a goodbye message appears and the game is ended using the exit()method.

<img src="assets/readme-docs/quitgame-goodbye.png" width=600>

* If the user chooses to play again, the terminal is cleared using the os.system(clear) method and the game starts again from the beginning.

### Future Features
* To add a leaderboard that stores the data of the user's attempts so when they play again, they can try to beat themselves. 
* The user can choose the length of the word they would like to guess, e.g. 4/5/6 letters.

## Classes
This Word-It consists of two classes
- Game
- WordChecker

The `Game` object allows the game play to flow, handling user input and using this to display data back to the user. The methods which run the game from the welcome screen, to the usernname prompt, menu options, instructions, validating user input guesses, displaying the users answers and updating the status of the game as the user progresses through their turns.

The `WordChecker` object validates the data input by the user with the randomly selected word which the user is trying to guess. This includes validating the user's input and error handling throughout the game, specifically the colour responsive feedback to the user for the game. 

## Languages Used
* The project was written using [PYTHON3](https://en.wikipedia.org/wiki/Python_(programming_language))


## Testing
### PEP8 CI
The `run.py` file has been passed through [PEP8 CI](https://pep8ci.herokuapp.com/). The file was checked with a few errors returned, detailed in unsolved errors below.

<details>
  <summary>run.py</summary>

  ![Run](assets/readme-docs/PEP8CI-wordit.png)
</details><br>

### Manual Testing
Input testing - all user input was tested and validated for error handling throughout the gameplay, and the appropriate feedback was displayed back to the user
* Username input was tested so that the user must enter data containing letters or numbers, and error handling would display an error message and prompt the user to re-enter the data if they tried to enter an empty username consisting of blank space. The strip() method was also implemented to remove any extra whitespace after the user input their data.
Menu options were tested as to whether upper or lower case letters would be accepted. Error handling will display an error message and reiterate the prompt again if the user inputs a letter other than P or I when navigating the menu. 
* Guess input was tested so that the user:
    * Must input a guess of 5 characters in length
    * The guess must contain all letters and no blank space
    * That if the data input is invalid, the AI will feedback an error message in red writing and asked to input a new guess
* Colour coded responsive feedback: was tested that the correct colours were displayed back to the user and it was of good readability with the colour contrasts.
* The user's remaining guesses was displayed after each guess.
* That the game ends if the user guesses the word correctly, especially if before they reach the full allocation of 6 guesses.
* That the game ends if the user does not guess the word correctly, and runs out of guesses. 
* That the game over screen displays, with the option to play again or quit the game.
* That the terminal clears if the user decides to play again, and a goodbye message is displayed if they choose to quit.
* Random word selection was tested that on playing the game again, the computer retrieved a different word from the `words.txt` file
* All of these tests were carried out in my local terminal during development, and the Heroku terminal. 

## Bugs and Errors
### Solved Bugs
#### Automated Errors
Throughout the development of this project, several automated (flake8) errors have been fixed i.e.
* Indentation errors
* Undefined variable name
* Lines of code being too long
* Not enough whitespace between functions
* No new line at end of file
* Invalid syntax errors
* Imported but unused errors
* Imported libraries that were unused, which I removed (e.g. I had installed `Pygame` originally but it was not needed)

#### Colorama Colour Coding Letters
Colorama was used to add the colour coding to each of the letters in the user's guess. So that each time a user makes a guess, the colour coded guess is added to the `guesses_list` so that all their guesses can be printed back to them after each turn. Initially the colours were not printing out and the Colorama encoding was printing out alongside the user's guess, impairing readability. After researching online and using slack for assistance, I found that the colours would only print out as a string (not a list). In order to overcome this problem, I used a `for` loop to print out each string in the `guesses_list` separately. 

#### WordChecker
Originally I had stored the code for the WordChecker function in a separate file, however the cross-checking of the user's letters guessed against the word selected by the random generator was not working. I made some changes and moved the code into the `run.py` file and it worked. So I removed the WordChecker.py file. 

#### Reinstall libraries
`Pyfliglet` and `Colorama` both uninstalled at one point, therefore I had to reinstall them and make sure I had the correct version of each. I then added them back to my `requirements.txt` file.

### Unsolved Bugs
#### Line Length Errors
I fixed all line length errors bar one, on line 79 as this caused a break in the line of text when running the app. So I restored it to the original code and the game is working as expected.

#### Invalid Escape Sequence Error
The error `W605 invalid escape sequence '\ '` is appearing on lines 89, 91, 108 - this is a result of the scroll added to my code to display the game instructions. I researched the error online but unfortunately could not find a fix for it without completely removing it. It does not affect the code running and the app functioning as expected. 

## Technologies Used
### Programmes and Development
- Written and tested in [GitPod](https://gitpod.io/) 
- This project uses [GitHub](https://github.com/) for utilising git version control
- The project was deployed via [Heroku](https://heroku.com/)
- [LucidChart](https://www.lucidchart.com/pages/) was used to create the flow chart for the game
- The Python code was validated using [PEP8 CI Online](https://pep8ci.herokuapp.com/)

## Python Libraries
- [os](https://docs.python.org/3/library/os.html?highlight=os#module-os)<br>
`os.system` is used to clear the terminal when starting a new game.
- [random](https://docs.python.org/3/library/random.html?highlight=random#module-random)<br>
`random.choice` is used to select a random word for the gameplay, from the `words.txt` file.
- [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)<br>
To take ASCII text and render it into ASCII art fonts.
- [colorama](https://pypi.org/project/colorama/)<br>
To colour code the text in the terminal and providing validation feedback to the user.
- [Counter](https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string)<br>
[Library Collections](https://docs.python.org/3/library/collections.html)<br>
These sources on `stackoverflow` and `python.org` helped with the Collections Counter method relating to the occurrences of a character in a string.

# Deployment
## Heroku
The site was deployed via [Heroku](https://dashboard.heroku.com/apps), and the live link can be found here: [Word-It](https://word-it.herokuapp.com/)

Before deploying to Heroku pip3 freeze > requirements.txt was used to add all the dependencies required to the requirements.txt file. This is required for the game to run on Heroku.

The following steps were taken:
1. Create an account and login to [Heroku](https://dashboard.heroku.com/apps).
2. On the homepage click the button `New` in the top right corner and from the drop-down menu select "Create New App".
3. Create a name for your app, making sure it is unique and descriptive. In this case it is `Word-It`
4. Next select your region. I selected `Europe`.
5. Click the `Create App` button.
6. This will create your app in Heroku and take you to the Heroku dashboard.
7. Navigate to the `Settings` tab and scroll down to `Reveal Config Vars`.
8. Create a `Config Var` replace the word `KEY` and enter `PORT`, and then replace the word `VALUE` and enter `8000`, then click the `Add` button.
9. Below `Config Vars` you will find the `Buildpacks` section, click `Add` Buildpack select `Python` and select `save changes`.
10. Repeat `step 9` to add `node.js` and select `save changes`.
11. It is important to make sure the buildpacks are in the correct order with `Python` being at the top and `node.js` on the bottom. If they are not in the correct order, you can click and drag to move them into the correct order.
12. Navigate to the `Deploy` tab on the top left side.
13. Select `Github, connect to github` as the deployment method.
14. Confirm you want to connect to GitHub.
15. Search for the GitHub Repository in the search field and click `connect`.
16. Once your repository is connected to Heroku, scroll to the bottom of the deploy page and click `Enable Automatic Deploys` for automatic deployment. 
17. Alternatively you can manually deploy by selecting a branch to deploy from and clicking `Deploy Branch`.
18. If you choose to `Enable Automatic Deploys`, [Heroku](https://heroku.com/) will build a new version of the app when a change to `GitPod` is pushed to `GitHub`.  
19. Manual deployment allows you to update the app whenever you click `Deploy Branch`. In the case of this project, I chose to `Enable Automatic Deploys` to ensure the code was deployed straight away at each push from `GitPod`.
20. Once the build process is complete (this can take a few seconds) you will then be able to view the live app by clicking on the button `View` below `Your app was successfully deployed`.
21. Click `View` to navigate to the deployed site.

## Version control
These commands were used for version control during project:
* git add `example filename` - to add files before committing
* git commit -m `"example message"` - to commit changes to the local repository
* git push - to push all committed changes to the GitHub repository
* git branch - to see which branch currently working on
* git pull - to pull all code into main branch once the feature branch had been merged and deleted
* git status - to see if the branch currently working on is upto date or if the are any unstaged
* git log --oneline - to see the last commit
* git commit --amend - to amend the most recent commit message

## How to create a branch/Tag of main:
If you need to `BRANCH` off of the main repository:
1. If you have not already, login in to [GitHub](www.github.com) and go to https://github.com/LynneMcGrail/Portfolio-Project-3-Word-it
2. On the left side of the screen underneath the nav links, click the drop down box `Main`
3. Inside the box you will see `Create new branch/tag`
4. Inside the text box, enter the new branch or tag name i.e., `Features`
5. Below the Branches Tags tab, you will see `Create branch: Features from "main"`
6. Click on `Create branch: Features from "main"` and you will be taken to the new branch page you just called `Features`

## How to fork a repository:
If you need to `FORK` a repository:
1. If you have not already, login in to [GitHub](www.github.com) and go to https://github.com/LynneMcGrail/Portfolio-Project-3-Word-it
2. In the top right corner, click `Fork`
3. The next page will be the forked version of https://github.com/LynneMcGrail/Portfolio-Project-3-Word-it but in your own repository

## How to clone a repository:
If you need to make a clone of this repository:
1. Fork the repository https://github.com/LynneMcGrail/Portfolio-Project-3-Word-it using the steps above
2. Above the file list, click `Code` (usually green at the top right of the code window)
3. Choose if you want to clone using HTTPS, SSH or GitHub CLI, then click the copy button to the right
4. Open Git Bash
5. Change the directory to where you want your clone to go (your own github)
6. Type `git clone` and then paste the URL you copied in step 4
7. Press `Enter` to create your clone

## How to make a local clone:
If you need to make a local clone:
1. If you have not already, login in to [GitHub](www.github.com) and go to https://github.com/LynneMcGrail/Portfolio-Project-3-Word-it
2. Under the repository name, above the list of files, click `Code`
3. Here you will have two options, `Clone` or `Download` the repository
4. You should close the repository using HTTPS, clicking on the icon to copy the link
5. At this point, you can launch the `Gitpod workspace` or choose your own directory
5. Open Git Bash
6. Change the current working directory to the new location of where you want the cloned directory to be located
7. Type git clone and then paste the URL you copied in step 4
8. Press Enter, to create your local clone to your chosen directory

#
## CREDITS AND REFERENCES
### Code
* [W3Schools](https://www.w3schools.com/)<br>
For further developing my understanding of `Python functions` and how they can be implemented
* [Stackoverflow](https://stackoverflow.com/questions/27076239/adding-scoring-system-to-a-number-guessing-game-including-play-again)<br>
For a guide on how to implement a `restart game function`
* [Counter](https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string) and [Library Collections](https://docs.python.org/3/library/collections.html)<br>
These sources on `stackoverflow` and `python.org` helped with the `Collections Counter` method relating to the occurrences of a character in a string.
* [Python String Methods](https://www.youtube.com/watch?v=edeJtMXgW_0&ab_channel=Appficial)<br>
For `Python` string methods 
* [ASCII Art Fonts](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)<br>
The `welcome message` , `you win` , and `goodbye` messages were created using `Pyfiglet` which takes ASCII text and renders it in ASCII art fonts.
* [ASCII Art Borders](https://www.asciiart.eu/art-and-design/borders)<br>
The instructions are displayed within a scroll to make it fun and a feature which makes it feel like an old gameboy style game, this was created using `ASCII Art Borders`.
* `Tech with Tim` on [Youtube](https://www.youtube.com/watch?v=u51Zjlnui4Y&ab_channel=TechWithTim) and [GitHub](https://github.com/techwithtim/ColoredTextInPython/blob/main/main.py)<br>
to learn how to import `Colorama` and change the text colour and background colours within the terminal to enable colour coding and validation of the user's guesses.
* [Code Institute: Build a game with Python](https://codeinstitute.net/ie/blog/game-with-python/)<br>
Helpful blog post by Code Institute to aid my development and learning.
* [Geeks for Geeks](https://www.geeksforgeeks.org/python-program-for-word-guessing-game/)<br>
For understanding game play and code examples with explanations to aid my understanding of creating the game in Python.
* [Program Arcade Games](http://programarcadegames.com/python_examples/show_file.php?file=game_class_example.py)<br>
To further my development and understanding of the use of `classes` in `Game` development in Python. No code directly used, but found it a helpful read on how to create games and look at different approaches in Python. 
* [Object Orientated Programming (OOP) in Python](https://realpython.com/python3-object-oriented-programming/)<br>
To understand classes VS instances in developing the Word-It game.


### Acknowledgements
- Code institute for the Mentors and Tutors on the course. Especially our class Facilitator and Mentor [Simen Daehlin](https://github.com/Eventyret) for sharing his expertise and helping us solve our problems to become better software developers.
- My Mentor [Jubril Akolade](https://www.linkedin.com/in/jubrillionaire/) for guiding me in the right direction and helping me establish good coding practice.
- My fellow classmates for their ideas and enthusiasm on our facilitator sessions and masterclasses, and also their support on Slack.
- Stack Overflow for troubleshooting and fixing errors
- The Slack community for tips, advice, quick fixes and kind words. Especially [Chris Williams](https://github.com/Chr15w1986) who helped me solve bugs and gave me great advice for better coding practice.
- My partner and family, for their encouragement, support and patience.