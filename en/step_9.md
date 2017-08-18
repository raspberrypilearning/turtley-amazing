## Loopy colours

To get more interesting colours, you could write lots of colours in a long list, and then keep changing the colour of the turtle according to the colour of the list. You can create lists in Python, using square brackets `[ ]`.

Below is an example of a list of RGB colours:

```python
colours = [(85, 211, 136), (197, 196, 126), (235, 233, 166), (25, 135, 222), (211, 64, 159), (159, 165, 106), (178, 160, 125), (36, 192, 70), (231, 184, 204), (63, 203, 219)]
```

- This next bit gets a bit complicated. Have a look at the code below, then run it to see what happens.

  <iframe src="https://trinket.io/embed/python/d58123d315" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

  The line `turtle.color(colours[i])` is telling the program to choose the "`i`th" item in the list. Remember that `i` starts from 0 and goes up to 9.
  
- What if you want a longer line? Try changing the number of loops in the `for` loop to `range(20)` and see what happens. Do you get an error?

