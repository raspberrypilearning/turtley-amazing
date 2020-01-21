## Repetition

Repeating lines of code is one of the fastest ways to get something done. Quite often in computer science, it makes more sense to repeat lines of code rather than write out another set of instructions. For example, the square you created earlier uses the same two instructions four times. Rather than writing them out four times, you could write them out once but add an instruction to repeat them.

In Python there are two types of loops that you are likely to use: a `while` loop and a `for` loop. If you want a section of code to repeat forever, or until a condition is set, then a `while` loop might be best. If you want to loop for a set number of times, then a `for` loop is preferable. 

- Here, we have used a `while True` loop. This means that the code inside the loop (i.e. the code which is indented) will repeat forever. You can try it in Trinket to see what it does, but remember it will loop **forever**!

  ```python
  from turtle import Turtle, Screen
    
  turtle = Turtle()
  
  while True:
      turtle.forward(1)
      turtle.right(1)
  ```

  This type of loop is not going to be very useful for drawing shapes with Turtle where you want to be more precise. 

- In this example, a `for` loop has been used. Press **Run** to see what happens.   
  
  <iframe src="https://trinket.io/embed/python/b89b6f5457" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

  A `for` loop repeats instructions a set number of times, in this case 8 times. A `for` loop has an associated variable (called `i` here). In this example, `i` starts from `0` and increases by `1` each time. Let's apply this to the code to draw a square:

  ```python
  from turtle import Turtle, Screen
    
  turtle = Turtle()
  
  for i in range(4):
      turtle.forward(100)
      turtle.right(90)
  ```

- Copy and paste this code into the Trinket editor above and run it. The turtle has been asked to repeat two instructions four times to make a square.

- Once you have created one shape using a loop, you can repeat the shape again and again by putting it inside another loop. This is a great way to draw spirals. Adapt your code by making it look like this:

  ```python
  from turtle import Turtle, Screen
    
  turtle = Turtle()
  
  for i in range(30):
      for i in range(4):
          turtle.forward(100)
          turtle.right(90)
      turtle.right(25)
  ```
  
  A spiral can be made by turning a small degree and then moving forward a small amount. The section of code for making a square is inside another `for` loop that repeats it 30 times, each time turning the cursor 25 degress to make a pleasing spiral shape.  
  
### Challenge

Try to complete each of the challenges below.

- Can you alter the `for` loop so that it draws a more interesting spiral using one of the shapes you made earlier, like a triangle or circle?

- Adding a few extra lines where you alter the variables `R`, `G`, and `B` would allow you to make a multicoloured spiral. Have a go at creating a rainbow spiral.

--- hints --- 
--- hint ---

Just like in the previous exercise, you can add to or subtract from the `R`, `G`, and `B` variables.

--- /hint --- 
--- hint ---

Just alter the variables within the `for` loop:

```python
from turtle import Turtle, Screen
    
turtle = Turtle()
screen = Screen()

R = 255
G = 0
B = 124

for i in range(30):
    turtle.color((R, G, B))
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
        ##ADD SOMETHING HERE
    turtle.right(25)
```

--- /hint --- 
--- hint ---

Try this to get started:

```python
from turtle import Turtle, Screen
    
turtle = Turtle()
screen = Screen()

R = 255
G = 0
B = 124

for i in range(30):
    turtle.color((R, G, B))
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
        R -= 1
        G += 1
    turtle.right(25)
```

--- /hint --- 
--- /hints ---
