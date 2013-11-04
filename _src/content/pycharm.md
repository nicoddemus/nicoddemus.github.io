Title: Things that surprised me in PyCharm
Date: 2013-10-26 22:03
Category: Python
tags: python, script
Summary: Quick overview of a command-line application framework
status: draft

# Things that surprised me in PyCharm #

I have been an [Eclipse](eclipse.org) user for years now, using it to
write mostly Python (with [PyDev](pydev.org)) and C++ (with [CDT](http://www.eclipse.org/cdt/)). 
Recently I heard about [PyCharm](http://www.jetbrains.com/pycharm/)
and its new free community edition from a good friend of mine. He, also a long time Eclipse user,
was giving it a lot of praise so I decided to give PyCharm a try, at least while working
at home.

So far, I have been loving it so much that I have even made the switch to using at work. :)

Below I describe some of the things that surprised me in a very good way
while using PyCharm. 

## Disclaimer ##

I don't intend in no way to bash Eclipse or PyDev, have been using it in years and it is great. 

Also, keep in mind that this is my personal experience. Your mileage may vary. :)

## Diff view while committing ##

In Eclipse, when you commit you're shown a list of the files being commited 
in the commit dialog. You can double-click on any of them to obtain a side-by-side
view of any of the changes:

(pic)

While side-by-side diff is always good, It doesn't have syntax highlighting, making it a 
little harder to see the code (no big deal thought). Now, if you see something you like to
change in the code (a mispelled word, missing documentation you would like to add, etc.), too bad:
you have to close everything (including the commit dialog with your nice commit message), go
find the offending code and change it, and start again from scratch.

PyCharm has the same feature, with two improvements: syntax highlighting and it is **writable**.
While syntax highlighting it is nice, I can't stress enough how awesome is being able to see a code
and be able to modify it on spot. 

(pic)

As another side bonus, if you for any reason close the commit dialog, it remembers the commit 
message you wrote already the next time you try to commit.

## Tooltips regarding obsolete code and improvements ##

PyCharm can inform you about obsolete constructs and suggest improvements in the code. 

For instance, I had code like this:

```python
with nested(open(fn1) as f1, open(fn2) as f2):
    <snip>
```

PyCharm was displaying a lamp right next to the `with` keyword:

(pic)

I'm using Python 2.7, and in fact you should use the new syntax for nested context managers, but alas
I had to support old versions of python for that code, so `nested` stayed.

I that PyCharm warned me about that was pretty cool. :)

# Points #

* Tasks connection + creating branches for tasks
* Quick Documentation
* Fast
* Commit options: check todos, auto imports, etc.

