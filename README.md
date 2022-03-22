# Flappy Bird

This is a remake of an iconic game "Flappy Bird". The project was done for educational purposes only.

![alt text](https://github.com/gugatchitchi/Flappy_Bird/blob/main/images/Screenshot.png?raw=true)

## Description

The game starts with the user input "space" or "upper arrow". These two inputs would be used later for controlling the birds velocity. Pressing one of the key would increase birds velocity by some X number and make the bird go up. As player tries to keep bird on the center pipes start emerging from the right side of the screen and the goal becomes to pass as many pipes as possible. The score is calculated based on how many pipes the bird has passsed.

## Code Structure

### main
main file contains the code which is ran as the program starts. It initiates the pygame and contains the outer loop of the game. This loop is responsible for restarting the game after player has died and waits for a key to be pressed so new round can be started.

### Params
Params file contains all the parameters for the game. For ex: pygame window size, images which are used, gap height of the pipe, etc. All this information is stored in one place, so game could be altered easily: make it faster, slower, harder, easier...

### Logic
Logic file contains all the code responsible for initiating Bird and Pipe classes, drawing everything on the window and carrying out the game. Most important part of that code is game() function which contains the loop responsible for a single round. It moves bird, pipes and checks for collissions. If player lost the game game() returns the score to update the max_score of the player. (max_score is stored in the main file)

### Bird Class
This files stores class responsible for storing all the information about the bird: X and Y variables, Birds velocity as well as functions which change those values. These functions are called from the functions stored in the logic file.

### Pipes Class
This files stores class responsible for storing all the information about pipes: X and Y variables, as functions which change those values. The functions for altering those values are called and list of all the pipes is stored in the logic file


## Dependencies
* Python 3+
* Python libraries: Pygame, Random, Sys
* Windows 10


## Executing program
* Make sure you have installed all the dependencies
* Run the main file using python


## Authors
Guram Tchitchinadze <gugatchitchinadze@gmail.com>


## Acknowledgments
Inspiration for this project was the the blog from geeksforgeeks - <https://www.geeksforgeeks.org/how-to-make-flappy-bird-game-in-pygame/?ref=gcse>
