# PORTFOLIO PROJECT - 3 PYTHON #

# Word-It
## Purpose 
Word-It is a five letter word guessing game that is based on the popular daily online game "Wordle". I chose to base my project off this because I became addicted to Wordle during the pandemic, and have a passion for word games. The rules are simple, the user aims to guess a random 5 letter word within six attempts. They will be given colour coded indicators as they play, highlighting whether a letter is correct, incorrect, or correct but just in the wrong position. After six attempts, if the user has not guessed the answer, the game will end and the word will be revealed to the user. If the user guesses the word within their six attempts, they will get a "YOU WIN" message and can play again, or quit. 

The game is a process of elimination, combined with a little luck and logic. It's a great way to test a user's problem solving ability and a quick game to do during a coffee break in work! Don't get too competitive now...

* [Here is a link to my Github Repo for PP3 Word-It](https://lynnemcgrail.github.io/ - FINISH LINK HERE)
* [Here is a link to my Heroku App - Word-It](https://word-it.herokuapp.com/)

## Final Design 
![Final project image home page](insert amiresponsive png image)

## Initial Idea Concept
My idea for this Python project was to replicate the Wordle game, because it is well-known, and if a user has never played it before it is simple to play which is why I included the option for the user to read the game instructions on starting the game. My game Word-It has replay ability as the site allows users to play again with a random generator imported into my code so that a different word is retrieved from the database contained in the words.txt file, this allows users to challenge themselves. This game functionality and word database is suitable for all ages and skill levels. I chose to use coloured text in my code so that it appealed to users and was clearly indicating their progress, this is further explained below in the 'Colour' section. [insert link to Colorama]

#### The features I wanted to include:
* Interactive game play elements to enhance user experience, the user is asked for their username and then the AI returns a welcome message and retrieves their name from the data they input.
* The total number of guesses is printed on starting the game
* And as the user guesses, the remaining number of guesses is printed on each input request to the user so that the user can see how many more chances they have to guess the word. 
* Colour indicators that let the user know if any of the letters they entered are correct, green indicates a correct letter and the right position, a yellow letter indicates a correct lettter, but in the wrong position and letters that are not in the word are incorrect and these are printed in red. 
* I wanted to create an app that was easily accessible and user friendly, with options for the user to play again or simply quit on finishing their first game. 
* For Word-It to look fun and interactive I not only used colours, but used ASCII borders and text to enhance the users experience and enjoyment. This can be seen on the initial start screen 'Welcome to Word-It' and throughout the gameplay when the user wins; 'You Win', and if the user decides to quit the game 'Goodbye' is printed in ASCII art words.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

