# PORTFOLIO PROJECT - 3 PYTHON #

# Word-It
## Purpose 
Word-It is a five letter word guessing game that is based on the popular daily online game "Wordle". I chose to base my project off this because I became addicted to Wordle during the pandemic, and have a passion for word games. The rules are simple, the user aims to guess a random 5 letter word within six attempts. They will be given colour coded indicators as they play, highlighting whether a letter is correct, incorrect, or correct but just in the wrong position. After six attempts, if the user has not guessed the answer, the game will end and the word will be revealed to the user. If the user guesses the word within their six attempts, they will get a "YOU WIN" message and can play again, or quit. 

The game is a process of elimination, combined with a little luck and logic. It's a great way to test a user's problem solving ability and a quick game to do during a coffee break in work! Don't get too competitive now...

* [Here is a link to my Github Repo for PP3 Word-It](https://lynnemcgrail.github.io/ - FINISH LINK HERE)
* [Here is a link to my Heroku App - Word-It](https://word-it.herokuapp.com/)

## Final Design 
![Final project image home page](insert amiresponsive png image)

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

