# Turtley Amazing

## Is it Art, Maths, or Computer Science?

-   Have a look at the image below. How would you classify this?

![](file:screen1.png)
-   It's a computer generated image, but to make it requires an
    understanding of Art, Maths and Computer Science.
-   Let's see how you too can make images just like this.

## Drawing a line

-   The image above is made up of lines and only lines! To get started,
    you need to know how to draw a line using a little bit of python
    code.
-   Below is an interactive Python environment, in which you can write
    code and then run it to see what happens.

<iframe src="https://trinket.io/embed/python/0d2e8c2dac" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

-   Click on **Run** to see the code working.
-   Now try changing the number in the line `forward(100)`, click on
    **Run** again and see what happens.

## Turning

-   Let's try making the *turtle* turn around.
-   Alter the code above, so that it looks like this:

```python
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
```

-   Now hit run and see what happens.

### Challenge - Try and complete each of the challenges below. If you struggle, then click on the link to see the code.

1.  Draw a square
2.  Draw a triangle
3.  Draw a cross

## Changing colours

-   Look at the code below. It contains three variables called `R`, `G`,
    and `B`.

<iframe src="https://trinket.io/embed/python/b964b7d3ce" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

-   Variables are a way of storing a value, and giving it a name. So for
    instance there is a variable names `R` with a value of `255`. Run
    the code and see what happens. Try changing the values of the three
    variables, and see what happens. (Note - the maximum value is 255,
    and after this there will be no affect.)
-   What do you think R, G and B represent?
-   You can change the colour of the turtle as well. Try copying the
    code below to see what happens.

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

-   So you can change the value of your variables either by setting them
    to a new value, or by increasing and decreasing them.

### Challenge - Try and complete each of the challenges below. If you struggle, then click on the link to see the code.

1.  Draw a square with sides that are 4 different shades of red
2.  Draw a cross made of 4 different colours

## Repetition

-   Read over the code below, then run it to see what it does.

<iframe src="https://trinket.io/embed/python/5222e2013d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

-   A `for` loop repeats instructions a set number of times. In this
    case 8 times.
-   A `for` loop has an associated variable (called `i` here). In this
    example `i` starts from `0` and increases by `1` each time.

### Challenge - Try and complete each of the challenges below. If you struggle, then click on the link to see the code.

-   A spiral can be made by turning a small degree (try `i`) and then
    moving forward a small ammount (how about `i` again). Can you alter
    the `for` loop so that it draws a spial.
-   Adding a few extra lines where you alter the variables `R`, `G`, and
    `B`, would allow you to make a multicoloured spiral. Have a go at
    creating a rainbow spiral.

## Better Spirals

-   Have a go at reading over the code below and guessing what it does.
    Then run it to see if you were correct.

<iframe src="https://trinket.io/embed/python/8f98ccf1fa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

-   The first thing you'll probably notice is that this is going to take
    ages to run. We can speed things up a little though. Add in the
    following line, **before the `for` loop**.

```python
turtle.speed(0)
```

-   Run the code again and it should be a little faster.

