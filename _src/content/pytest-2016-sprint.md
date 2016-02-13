Title: Pytest 2016 sprint funding
Date: 2016-02-13 
Category: pytest
tags: python, testing, pytest
Summary: Pytest 2016 sprint funding, how it will be and what to expect
status: draft


# Pytest Sprint 2016

In June [pytest](https://github.com/pytest-dev/pytest) core developers and users are gathering in Freiburg, Germany for
a [sprint](http://pytest.org/latest/announce/sprint2016.html). This is being
funded by a [indiegogo campaign](https://www.indiegogo.com/projects/python-testing-sprint-mid-2016#), so
if you are a pytest user or your company heavily relies on pytest, please consider 
making a donation!

# Back in 2013 
 
I was really excited when I first discovered pytest. I wrote a post
titled *pytest: best thing since sliced bread* in our company blog, highlighting the features I 
liked best. Our blog is not public, but I will post some of its 
contents here:
  
* **assertEqual?** no more. You just use plain asserts, and assertion rewrite
 means that special output in failed assertions can be done, for example
 by showing a context diff if a string comparison fails. 

* **Test finding**: The test runner automatically finds and runs tests just like 
  we expect it, including xUnit style tests. 
  Also, it supports using simple functions instead of having to subclass some test base class.
  This was a problem back then, so we wrote our own test runner.

* **Code Coverage**: Back then our own test runner implemented code coverage.

* **Parallel Support**: Again our test runner implemented this. This was a major
  need for us as we have thousands of tests so running them sequentially is not
  an option.

* **skip and xfail** built-in decorators.

* `--pastebin` parameter. Very useful to share errors with others, better
  than pasting a messy traceback in Skype (still used for communication to this day). 
  This is an underrated core plugin in my opinion. :)

* **Fixtures**, which is one of the killer pytest feature.
  The automatic dependency injection really shines in promoting code re-use
  between tests.
     
* **Plugins**: all features are implemented in terms of plugins, 
  and this is another pytest killer feature as the 
  [plugin ecosystem](http://plugincompat.herokuapp.com) is huge.
  
  
# Adopting
  
py.test was so feature-rich that we decided to ditch our test runner. It was
argued that even if you wanted to write only xUnit-style tests and leave
more advanced features (like fixtures) alone, being able to write plain asserts
was enough reason to replace our runner.
  
It was only two years later that we could finally adopt py.test 
for all projects. While initially there were concerns now even the initial 
nay-sayers are praising py.test.

It took us this long because:
 
* It was not a full-time thing, it was something one team member or another
  (mostly me) spending some free extra time on.
* We needed support for running Qt tests, so I wrote [pytest-qt](https://github.com/pytest-dev/pytest-qt).
* There were several tests with problems when running under xdist. This happened
  because our custom runner parallized tests by *file*, while xdist parallizes
  *all* tests. When xdist was brought in several tests presented concurrency
  issues within tests on the same file, as they never ran in parallel before.
  
But the adoption is complete and we couldn't be happier with it. We are also
migrating from xUnit tests to fixture based ones as time allows.  

# Now

It's been two years since I became a [pytest](https://github.com/pytest-dev/pytest)
core developer. I try to be very active in the community and contribute with
PRs whenever I can. Really happy to be able to work on and use such a great tool.



  
 
