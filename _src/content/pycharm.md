Title: Things that surprised me in PyCharm
Date: 2013-10-26 22:03
Category: Python
tags: python, script
Summary: Quick overview of a command-line application framework
status: draft

I have been an [Eclipse](eclipse.org) user for years now, using it to
write mostly Python (with [PyDev](pydev.org)) and C++ (with [CDT](http://www.eclipse.org/cdt/)). 
Recently I heard about [PyCharm](http://www.jetbrains.com/pycharm/)
and its new free community edition from a good friend of mine, [Igor](https://github.com/itghisi). He, also a long time Eclipse user,
was giving it a lot of praise so I decided to give PyCharm a try, at least while working
at home.

So far, I have been loving it so much that I have even made the switch to using at work. :)

Below I describe some of the things that surprised me in a very good way
while using PyCharm. 

**Disclaimer**

I don't intend in no way to bash Eclipse or PyDev, have been using it in years and it is great. 

Also, keep in mind that this is my personal experience. Your mileage may vary. :)

# Diff view while committing #

In Eclipse, when you commit you're shown a list of the files being committed
in the commit dialog. You can double-click on any of them to obtain a side-by-side
view of any of the changes:

![eclipse-commit-diff]({filename}static/pycharm/eclipse-commit-diff.png)

Now, if you see something you like to change in the code (a misspelled word like the above, missing documentation
you would like to add, etc.), too bad: you have to close everything
(including the commit dialog with your nice commit message), go find the offending code and change it,
and start again from scratch.

PyCharm has the same feature, but your changes are **editable**. I can't stress enough how awesome is being able to
modify it on spot.

![pycharm-commit-diff]({filename}static/pycharm/pycharm-commit-diff.png)

I can fix the typo above easily during the commit process.

As another side bonus, if you for any reason close the commit dialog, it remembers the commit 
message you wrote already the next time you try to commit.

# Commit-Time Checks #

Still during commit, we have several options that can be executed before the actual commit, like
"Optimizing Imports" (sort and remove unused), check for TODOs in the change-set, among others:

![commit]({filename}static/pycharm/commit.png)

One interesting bit is the "Perform code analysis" option...

# Inspect Code #

You can ask PyCharm to perform a "Code Inspection" in a single file, directory, or entire projects. It will look for problems
and improvements in your code without actually executing it. As explained in the previous section, this can also be
done automatically on changed files during commit.

Here's the results of an inspection in a single file:

![inspection]({filename}static/pycharm/inspection.png)

For some of the inspection results, you can also apply a suggested fix. For instance, from
"Function call can be replaced with set literal" we can select the option to fix that:

![inspection-2]({filename}static/pycharm/inspection-2.png)

PyCharm will then change this:

```python
    extensions = set(['.avi', '.mp4', '.mpg', '.mkv'])
```

into this, automatically:

```python
    extensions = {'.avi', '.mp4', '.mpg', '.mkv'}
```

You can disable any inspection you like, including on a per-project basis if wanted.

# Refactoring #

I was trying to rename a module and couldn't find the option on the menu... F2 also didn't work.

Then I glanced at the "Refactoring/Rename" sub-menu of the file and thought... *could it be?*. Yes!
When you rename a module, PyCharm will ask if you would like to also fix all related imports
for you automatically. *Bliss*

There is a lot of other refactoring options, but I haven't had the chance to try them
yet.

# Tooltips regarding obsolete code and improvements #

PyCharm can inform you about obsolete constructs and suggest improvements in the code. 

For instance, I had code like this:

```python
with nested(open(filename1), open(filename2)) as (f1, f2):
    <snip>
```

PyCharm was displaying `nested` in strike-out:

![nested-obsolete]({filename}static/pycharm/nested-obsolete.png)

I'm using Python 2.7, and in fact you should use the new syntax for nested context managers, but alas
I have to support old versions of python in that code, so `nested` stays.

The fact that PyCharm warned me about that was pretty cool. :)


# Tasks + Feature Branches #

Like Eclipse (with Mylin), PyCharm also supports a task based workflow (including task-sensitive contexts).

PyCharm however comes out of the box with a ton of connectors available 
(GitHub, Mantis, Jira, Bugzilla, etc). Also, when you start working a task, it asks if
you would like to create a new feature branch for that task, with configurable
branch name.

![nested-obsolete]({filename}static/pycharm/task-branch.png)

This avoids having to manually create a branch, which is a little tedious (having
the task id on hand, choosing a name, etc).

Bonus points.

# Fast #

I noticed that PyCharm scans source for code completion much faster than Eclipse,
and without interrupting your work. It is really frustrating when you try to save 
a file and Eclipse stops you from doing so because it is executing a background task...

# Quick Documentation #

When you have the cursor over a function/method/class whatever, you have the option to view "Quick Documentation".
See it in action:

![quick-doc]({filename}static/pycharm/quick-doc.png)

As you can see, it renders the docstring of the method in a nice looking format, plus it infers the parameter types
from code usage... so even if the function doesn't have a docstring, you still get this:

![quick-doc-2]({filename}static/pycharm/quick-doc-2.png)

Very nice!

# Docutils Support #

PyCharm includes first-class support for docutils, making it easy to re-generate the documentation directly from the IDE.

On the plus side, it also includes a very nice ReST editor (much better than Eclipse IMHO):

![rst]({filename}static/pycharm/rst.png)


# Sane Plugin System #

In my experience, installing plugins in Eclipse is a pain:

* It is hard to find where you are suppose to go (tip: *Help/Install New Software...*);
* You don't have a single index, so you have to find the plugin on the web;
* The dependency system sometimes fails horribly and I end-up not being able to install
  the plugin I wanted (several people at work also experience this and in the end give up);

PyCharm plugin experience was **much** smoother.

First, it is located where you would expect it: It is an item on "Settings":

![plugins]({filename}static/pycharm/plugins.png)

You can easily browse for plugins directly from there:

![plugins-browse]({filename}static/pycharm/plugins-browse.png)

I quickly installed a Markdown editor (as nice as ReST's), a pastebin plugin so that I can quickly create pastes directly
from selected text, and CodeGlance, which gives a nice code overview similar to that of SublimeText. :)

# Wrapping Up #

That's it so far. I tried to list everything that I would show to my friends
as "look how cool this is". I have been using PyCharm for very little time,
so if I find more interesting things worth of another post I will write a
continuation. :)