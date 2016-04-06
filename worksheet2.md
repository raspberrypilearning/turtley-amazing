# Turtley Amazing Part 2

Take your Python turtle skills to the next level. 

## Better Spirals

1. Have a go at reading over the code below and guessing what it does. Then run it to see if you were correct.

  <iframe src="https://trinket.io/embed/python/8f98ccf1fa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

1. The first thing you'll probably notice is that this is going to take ages to run. We can speed things up a bit, though. Add in the following line, before the `for` loop.

  ```python
  turtle.speed(0)
  ```

1. Run the code again: it should be a little faster.
1. Our code has made a multicoloured spiral, by changing the `R`, `G`, and `B` variables. The colours are a little one-dimensional, though. Can you do a better job?

## Loopy colours

To get more interesting colours, you could write lots of colours in a long list, and then keep changing the colour of the turtle according to the colour of the list. You can create lists in Python, using square brackets `[ ]`

Below is an example of a list of RGB colours:

```python
colours = [(85, 211, 136), (197, 196, 126), (235, 233, 166), (25, 135, 222), (211, 64, 159), (159, 165, 106), (178, 160, 125), (36, 192, 70), (231, 184, 204), (63, 203, 219)]
```

1. This next bit gets a bit complicated. Have a look at the code below, then run it to see what happens.

  <iframe src="https://trinket.io/embed/python/d58123d315" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

  The line `turtle.color(colours[i])` is telling the program to choose the "ith" item in the list. Remember that `i` starts from 0 and goes up to 9.
  
1. What if you want a longer line? Try changing the number of loops in the `for` loop to `range(20)` and see what happens. Do you get an error?

## Modulo to the rescue
In the above example, you need a way to keep looping over the list items, so when `i` gets to 9, it will go back around and get the "0th" item from the list again. This is where the modulo operator `%` can help you out.

1. Look at the code below: run it and see if you can figure out what is going on.

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

1. Did you figure it out? The `%` operator prints out the remainder of a division. 15 ÷ 6 for instance is 2 with a remainder of 3. Therefore 15 % 6 would be 3. We can use this operator to help with the problem of running off the end of the list. If the `range` goes above the length of the list, you can just do a `%` of the length of the list.

1. Have a look at the example below, and read through the code carefully to make sure you can see how the modulo operator is used.

  <iframe src="https://trinket.io/embed/python/c56b5cb705" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Enormous lists

You can now have a go at creating a list of colours that's a little longer than before. To do this you can use a `while` loop. Unlike a `for` loop, a while loop keeps running until a specific condition has been met.

1. Look at the code below. The `while` loop is used to gradually increase the value of `G`, until it reaches 255. Each time, the colours are added to the list.

  <iframe src="https://trinket.io/embed/python/cfb2a665a8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

1. Can you add in two more `while` loops to add more colours? The next loop should gradually decrease `R` until it reaches 0. The final one should then increase `B` until it reaches 255. Have a go, but if you get stuck, all will be revealed in the last section.

## Putting it all together

You can now use the while loops along with the spiral code to make a really pretty spiral. Have a look at the code below, and make sure you understand what it is doing. Try playing with the value of the variables in the loops, to see what effect this has on the output.

  <iframe src="https://trinket.io/embed/python/91a1daf84e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## What Next?

- Learn how to use `functions` to [draw snowflakes](https://www.raspberrypi.org/learning/turtle-snowflakes/) using turtle. 
- Create interactive stories using `lists` in Python with the [Storytime](https://www.raspberrypi.org/learning/storytime/) resource. 
- Take your first steps [controlling physical objects](https://www.raspberrypi.org/learning/getting-started-with-gpio-zero) with Python and a Raspberry Pi. 
