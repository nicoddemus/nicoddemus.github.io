Title: Pytest 2016 sprint funding
Date: 2016-02-13 
Category: Python
tags: python, testing
Summary: Pytest 2016 sprint funding, how it will be and what to expect
status: draft
 
When I first discovered [pytest](https://github.com/pytest-dev/pytest), I was
really awed by it. I remember posting about it in our internal blog, under the
title *pytest: best thing since sliced bread*, highlighting the features I 
liked best:
  
* `assertEqual`, `assertSets`, `assertSomething`? No more! 
You just use plain `assert`s statements in your test, and pytest will show
proper interim values for the asserted expressions.

  ```python
  # content of test_assert1.py  
  def f():  
      return 3  
  
  def test_function():  
      assert f() == 4  
  ```

It's been two years since I became a [pytest](https://github.com/pytest-dev/pytest)
core developer. 
