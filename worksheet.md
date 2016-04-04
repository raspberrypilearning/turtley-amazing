# Turtley Amazing

## Is it Art, Maths, or Computer Science?

Have a look at the image below. How would you classify this?

![](images/screen1.png)

It's a computer generated image, but to make it requires an understanding of Art, Maths and Computer Science. Let's see how you too can make images just like this.

## Drawing a line

The image above is made up of lines and only lines! To get started, you need to know how to draw a line using a little bit of python code. Below is an interactive Python environment, in which you can write code and then run it to see what happens.

  <iframe src="https://trinket.io/embed/python/0d2e8c2dac" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

1. Click on **Run** to see the code working.
1. Now try changing the number in the line `turtle.forward(100)`, click on **Run** again and see what happens.

## Turning

You've used code to draw a line. Good work! Now let's try making the *turtle* turn around. To do this you need to instruct the turtle not only to move forward, but also to turn right or left. 

  <iframe src="https://trinket.io/embed/python/88c91b8dfb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

1. What do you think will happen in the code above? Click on **Run** to see if you were right. 
1. Write the next lines of code to complete a square shape above and press **Run**. Keep trying until you get it right. 

### Challenge
*Try and complete each of the challenges below.*

1.  Draw a rectangle
1.  Draw a triangle
1.  Draw a cross

## Changing colours

1. Look at the code below. It contains three variables called `R`, `G`, and `B`.

  <iframe src="https://trinket.io/embed/python/b964b7d3ce" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

  Variables are a way of storing a value, and giving it a name. For instance there is a variable name `R` with a value of `255`. 

1. Run the code and see what happens. 
1. Try changing the values of the three variables, and see what happens. (Note - the maximum value is 255, and after this there will be no affect.)
1. What do you think R, G and B represent? You can change the colour of the turtle as well. Try copying the code below to see what happens:

  ```python
  from turtle import Turtle, Screen
  
  turtle = Turtle()
  screen = Screen()
  
  screen.bgcolor('blue')
  
  R = 255
  G = 0
  B = 0
  
  turtle.color((R, G, B))
  turtle.forward(100)
  turtle.right(120)
  G = 255
  turtle.color((R, G, B))
  turtle.forward(100)
  turtle.right(120)
  B += 125
  R -= 100
  turtle.color((R, G, B))
  turtle.forward(100)
  ```

1. You can change the value of your variables either by setting them to a new value, or by increasing and decreasing them.

### Challenge 
*Try and complete each of the challenges below. If you struggle, then click on the link to see the code.*

1.  Draw a square with sides that are 4 different shades of red
2.  Draw a cross made of 4 different colours

## Repetition

1. Read over the code below, then run it to see what it does.

  <iframe src="https://trinket.io/embed/python/5222e2013d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

-   A `for` loop repeats instructions a set number of times. In this case 8 times.
-   A `for` loop has an associated variable (called `i` here). In this example `i` starts from `0` and increases by `1` each time.

### Challenge
*Try and complete each of the challenges below. If you struggle, then click on the link to see the code.*

1. A spiral can be made by turning a small degree (try `i`) and then moving forward a small ammount (how about `i` again). Can you alter the `for` loop so that it draws a spial.
1. Adding a few extra lines where you alter the variables `R`, `G`, and `B`, would allow you to make a multicoloured spiral. Have a go at creating a rainbow spiral.

## Better Spirals

1. Have a go at reading over the code below and guessing what it does. Then run it to see if you were correct.

  <iframe src="https://trinket.io/embed/python/8f98ccf1fa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

1. The first thing you'll probably notice is that this is going to take ages to run. We can speed things up a little though. Add in the following line, **before the `for` loop**.

  ```python
  turtle.speed(0)
  ```

1. Run the code again and it should be a little faster.
1. This has made a multicoloured spiral, by changing the `R`, `G`, and `B` variables, but the colours are a little one-dimensional. Can you do a better job?

## Loopy colours

To get more interesting colours, you could write lots of colours in a big long list, and then keep changing the colour of the turtle according to the colour of the list. You can create lists in Python, using square brackets `[ ]`

Below is an example of a list of RGB colours:

```python
colours = [(85, 211, 136), (197, 196, 126), (235, 233, 166), (25, 135, 222), (211, 64, 159), (159, 165, 106), (178, 160, 125), (36, 192, 70), (231, 184, 204), (63, 203, 219)]
```

1. This next bit gets a bit complicated. Have a look at the code below. Run it to see what happens.

  <iframe src="https://trinket.io/embed/python/d58123d315" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

  The line `turtle.color(colours[i])` is telling the program to choose the "ith" item in the list. Remember that `i` starts from 0 and goes upto 9.
  
1. What if you want a longer line? Try changing the number of loops in the `for` loop to `range(20)` and see what happens. Do you get an error?

## Modulo to the rescue
In the above example, you need a way to keep looping over the list items, so when `i` gets to 9, it just goes back around and gets the "0th" item from the list again. This is where the modulo operator `%` can help you out.

1. Look at the code below - run it and see if you can figure out what is going on.

  <iframe src="https://trinket.io/embed/python/8fd77a1942" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

1. Try changing the numbers in the `print`. There are some example to try below

  ```python
  print(12 % 6)
  print(6 % 6)
  print(0 % 6)
  print(13 % 6)
  print(17 % 6)
  print(1 % 6)
  print(8 % 6)
  print(11 % 6)
  ```

1. Did you figure it out. The `%` operator prints out the remainder of a division. 15 ÷ 6 for instance is 2 with a remainder of 3. Therefore 15 % 6 would be 3. We can use this operator to help with the problem of running off the end of the list. If the `range` goes above the length of the list, you can just do a `%` of the length of the list.

1. Have a look at the example below, and read through the code carefully to make sure you can see how the modulo operator is used.

  <iframe src="https://trinket.io/embed/python/c56b5cb705" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Enormous lists

You can now have a go at creating a list of colours that's a little longer than before. To do this you can use a `while` loop. Unlike a `for` loop, a while loop keeps running until a specific condition has been met.

1. Look at the code below. The `while` loop is used to gradually increase the value of `G`, until it reaches 255. Each time, the colours are added to the list.

  <iframe src="https://trinket.io/embed/python/cfb2a665a8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

1. Can you add in two more `while` loops, to add more colours. The next loop should gradually decreast `R` until it reaches 0. The final one should then increase `B` until it reaches 255. Have a go, but if you get stuck, all is revealed in the last section.

## Putting it all together.

You can use the while loops, along with the spiral code, to make a really pretty spiral now. Have a look at the code below, and make sure you understand what it is doing. Try playing with the value of the variables in the loops, to see what effect it has on the output.

  <iframe src="https://trinket.io/embed/python/91a1daf84e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## What next?
- Learn how to use `functions` to [draw snowflakes](https://www.raspberrypi.org/learning/turtle-snowflakes/) using turtle. 
- Create interactive stories using `lists` in Python with the [Storytime](https://www.raspberrypi.org/learning/storytime/) resource. 
- Take your first steps [controlling physical objects](https://www.raspberrypi.org/learning/physical-computing-guide/) with Python and a Raspberry Pi. 
