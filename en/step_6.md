## Changing colours

The default colour for the pen used by the turtle cursor is black, and the default background colour is white. You can change the colours to make your shapes look even better.

- Look at the code below. It contains three variables called `R`, `G`, and `B`.

  <iframe src="https://trinket.io/embed/python/b964b7d3ce" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

  Variables are a way of storing a value and giving it a name. For instance, there is a variable name `R` with a value of `255`. 

  The following line is commented out in the trinket above, but will be needed if you are using another editor. So if you are not working in Trinket, then remove the `#` symbol, to uncomment the line.
  
  ```python
  screen.colormode(255)
  ```

- Run the code and see what happens. 

- Try changing the values of the three variables, and see what happens. (Note: the maximum value is 255, and after this there will be no effect.) What do you think R, G, and B represent?

--- collapse ---
---
title: Answer
---

`R`, `G` and `B` represent how much red, green, and blue will be used in the colour. Each can have any value from `0` up to `255`.

So to make yellow, you could try the following:
```python
R = 255
G = 255
B = 0
```
--- /collapse ---

[[[generic-theory-simple-colours]]]

  You can change the value of your variables either by setting them to a new value, or by increasing and decreasing them.

-  You can change the colour of the turtle as well. Run the code below to see what happens:

  <iframe src="https://trinket.io/embed/python/ab6732d60e" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Challenge 

Try to complete each of the challenges below.

-  Complete the triangle above with a colour of your choice.
-  Draw a square with sides which are four different shades of red.
-  Draw a cross made of four different colours.

--- hints --- 
--- hint ---

To change a colour, you can just keep adding or subtracting values from the original variables.

--- /hint --- 
--- hint ---

So you could alter colours by doing the following:

```python
R = 255
G = 0
B = 0

turtle.color((R, G, B))
turtle.forward(100)
turtle.right(120)

R -= 20
G += 20
B += 5

turtle.color((R, G, B))
turtle.forward(100)
turtle.right(120)
```

--- /hint ---
--- /hints ---
