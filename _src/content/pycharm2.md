Title: Things that surprised me in PyCharm (part 2)
Date: 2013-10-26 22:03
Category: Python
tags: python, ide
Summary: More cool things in PyCharm
status: draft

Draft for a new post about PyCharm

# Points #

(igor)

* Refactoring

    * If you move a module inside your project, imports are automatically updated
    * Smart: i.e.: when you do an Extract Method, pycharm search for other pieces of code in the same module where the extracted method could be used (like a DRY inspection)

* Inspection

    * More rich code inspection: some type checking, uninitialized variables, method may be static...

* Git Integration

    - When creating a branch for your project, pycharm asks if you want to create a branch with the same name for projects in your workspace, and keep them in sync
    - The branch menu shows local and remote branches. Operations (merge, checkout, create) are easily accessible. Other minor but cool tricks like a pop up asking if you want to delete a branch after a merge operation.

* Debugger

    - When you Run a script in debug mode, Eclipse asks if you want to switch to "Debugger view". This is a pain.
      PyCharm just shows a simple Debug dock with all debug functions easily accessible.
      It has also the options "Run to Cursor" and "Show Execution Point", which I think Eclipse hasn't.