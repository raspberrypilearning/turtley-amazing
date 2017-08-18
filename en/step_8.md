## Better spirals

- Have a go at reading over the code below and guessing what it does. Then run it to see if you were correct.

  <iframe src="https://trinket.io/embed/python/8f98ccf1fa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- The first thing you'll probably notice is that this is going to take ages to run. We can speed things up a bit, though. Add in the following line, before the `for` loop:

  ```python
  turtle.speed(0)
  ```

- Run the code again: it should be a little faster.
- Our code has made a multicoloured spiral by changing the `R`, `G`, and `B` variables. The colours are a little one-dimensional, though. Can you do a better job?

