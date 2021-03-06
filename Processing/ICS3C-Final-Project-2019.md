# ICS3C-Final-Project-2019

## Overview

Each heading below will be as the handin folder for you to hand in your project.

A video walk-through will have to be done after the project is all coded.

Use appropriate and numerous comments throughout your code.

Be sure all variable names are appropriate and self-explanatory.

Copy and paste the instructions for each program into the header of each program. After each instruction, write the word DONE after it after you have ensured it is correct.

Use your own functions where it makes sense for "chunking" your code. See these videos for tutorials on writing your own functions: 
- [Functions Basics - Processing Tutorial](https://www.youtube.com/watch?v=zBo2D3Myo6Q) 
- [Modularity with Functions - Processing Tutorial](https://www.youtube.com/watch?v=j_XyeWg_3EE)

Be sure your program follows these style and variable naming guidelines:

+ <https://github.com/processing/processing/wiki/Style-Guidelines>
+ <http://www.informit.com/articles/article.aspx?p=131025&seqNum=3>

## Program 01 - Bouncing Ball

Write a program where the ball is bouncing around the screen.

Be sure the speed of the ball can be controlled with global variables (`x_speed`, `y_speed`).

Be sure the size of the window can be set with global variables `window_height` and `window_width`. 

(Note: to use variables in the `size()` function you must put `size()` in `settings()`, not `setup()`.)

The background colour of the window is to be set globally with the variable `background_colour`.

The colour of the ball is to be set globally with the variable `ball_colour`.

The size of the ball is to be set gloabally with the variable `ball_size`.

Be sure the program meets the needs addressed in the overview, above.

## Program 02 - Moveable Paddle

Write a program with a moveable paddle on the right side of the screen.

Continue using these global variables as defined above:

+ `window_height`
+ `window_width`
+ `background_colour`

The paddle position is to be controlled with the mouse y position.

The width of the paddle is to be set globally with the variable `paddle_width` and is to be set to 5% of the window width.

The height of the paddle is to be set globally with the variable `paddle_height` and is to be set to 15% of the window height.

The colour of the paddle is to be set globally with the variable `paddle_colour`. Choose any colour you like.

Be sure the program continues to meet the needs addressed in the overview, above.

## Program 03 - Working Paddle

Combine both programs above so you have a working Pong game, with your paddle (on the right) working to bounce the ball and the wall on the left working to also bounce the ball.

Continue using all the global variables mentioned above.

Be sure that no portion of the paddle extends above or below the window.

Be sure the program continues to meet the needs addressed in the overview, above.

## Program 04 - Second Paddle

If you have not already done so, consider the size of the ball (`ball_size`) when it bounces off any of the surfaces.

Add a second paddle, this one on the left side of the screen. This paddle will be controlled by the computer, specifically the ball's y-position.

As above, be sure the paddle does not extend above or below the window.

## Program 05 - Keeping Score

If you have not already done so, be sure the ball does not bounce off the right surface if it misses the paddle.

When the ball passes through the right side, increment a score which is diplayed on the top-left corner.
