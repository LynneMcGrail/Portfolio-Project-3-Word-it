# Word-It
Word-It is a five letter word guessing game that is based on popular game "Wordle". I chose to base my project off this because I became obsessed with Wordle during lockdowns and love word games. The rules are simply, the user aims to guess a random 5 letter word within six attempts and they will be given colour coded clues as they play as to whether a letter is correct, incorrect, or correct but just in the wrong place. After six attempts, the game will end and the word will be revealed to the user.

The game is a process of elimination, combined with a little luck and logic. It's a great way to test your problem solving ability and a quick game during a coffee break in work! Don't get too competitive now. . .   

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!