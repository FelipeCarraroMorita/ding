# dingsound
An oven timer ding sound function to be called once your code finishes running! (Yes, I'm serious)

## BUT WHY?!
To know when your code finish processing without having to look at the screen.

## Installation
`!pip install dingsound==0.0.3`


## How to use
`import dingsound as d`

There is **only 2 functions** in this package:
1. `d.ding()` for most offline IDE's
2. `d.ding2()` for Google Colab

`d.ding` has a parameter "mute" that is by default false, but if you call the function and it makes no sound (like will happen on PyCharm) try setting it up as True.

Both do in a pratical manner the same stuff! Have fun.
