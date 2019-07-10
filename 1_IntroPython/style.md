# Python Style Guide

## Why Should You Learn This?

Creating a new habit is always way easier than fixing a bad habit. This also happens in coding style: getting used to create a bad style of your code, then you will have a bad and tiring time explaining that to your co-workers. By following a styling guide, you can make people to easily understand your code, positively improve the quality of the system, and give consistency to your code.

This handbook is a summarized version of the complete [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html). To improve your code for better readibility, please refer to the complete guide.

## Styling Your Code

1. Semicolons (`;`): Do not terminate your lines with semicolons, and do not use semicolons to put two statements on the same line.
2. Maximum line length is 80 characters. Make use of Python’s implicit line joining inside parentheses, brackets and braces. If necessary, you can add an extra pair of parentheses around an expression. For two lines of expressions, use a nested with statement:

```
with very_long_first_expression_function() as spam, \
  very_long_second_expression_function() as beans, \
  third_thing() as eggs:
place_order(eggs, beans, spam, beans)
```

3. Parentheses (`()`) and brackets (`{}`): Do not use parentheses in return statements or conditional statements unless using parentheses for implied line continuation or to indicate a tuple. There should be nothing after the open parenthesis or bracket on the first line.

4. Whitespace. 
   - **Do not use whitespaces when:**
   - Before a comma, semicolon, or colon
   - After open parentheses/bracket  or before closing it
   - Surround passing keyword argument
   - Aligning token indentation
   - **Use it when:**
   - Surrounding operators
5. Quote characters: be consistent with your choice of single or double quotes
6. TODO Comments: A TODO comment begins with the string TODO in all caps and a parenthesized name, e-mail address, or other identifier of the person or issue with the best context about the problem. This is followed by an explanation of what there is to do.
7. Imports should be on separate lines and are put on the top of the lines 

## Naming Rules

Function names, variable names, and filenames should be descriptive. Do not use abbreviations that are ambiguous or unfamiliar to readers outside your project, and do not abbreviate by deleting letters within a word. Always use a `.py` filename extension. Never use dashes.

# Final Words

> BE CONSISTENT.

If you’re editing code, take a few minutes to look at the code around you and determine its style. This will help all the future collaborators and they will thank you for your effort in keeping the code style consistent.
   