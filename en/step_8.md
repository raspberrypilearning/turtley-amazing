## Modulo to the rescue

In the previous example, you need a way to keep looping over the list items, so when `i` gets to 9, it will go back around and get the "0th" item from the list again. This is where the modulo operator `%` can help you out.

- Look at the code below: run it and see if you can figure out what is going on. You shoud get `0` to begin with.

  <iframe src="https://trinket.io/embed/python/8fd77a1942" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- Try changing the numbers in the `print` command. There are some examples to try below:

  ```python
  print(17 % 6)
  print(12 % 6)
  print(13 % 6)
  print(6 % 6)
  print(0 % 6)
  print(1 % 6)
  print(8 % 6)
  print(11 % 6)
  ```

- Did you figure it out? The `%` operator prints out the remainder of a division. For example, 15 ÷ 6 is 2 with a remainder of 3. Therefore 15 % 6 would be 3. We can use this operator to help with the problem of running off the end of the list. If the `range` goes above the length of the list, you can just do a `%` of the length of the list.

- Have a look at the example below, and read through the code carefully to make sure you can see how the modulo operator is used.

  <iframe src="https://trinket.io/embed/python/c56b5cb705" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

