
Hands On: Git Bisect
====================

 1. What's Git Bisect?
 2. How it works?
 3. References

## What is Git Bisect?
According to [git documentation page](https://git-scm.com/docs/git-bisect) the ``git bisect`` command:

> ... uses a binary algorithm to find which commit in your project's history introduced a bug.

Thus a motivation for using it is that a bug was introduced after some code was commited/pushed and someone needs to find it and fix it. Of course it's possible to do this manually but with ``git bisect`` this task is much more easy.

## How it works?
A common scenario in software development is when someone commits a code (probably without testing or executing automated tests locally) and it adds something that breaks the application (or even the automated tests). It's also common to spend some time searching for what add that broken code to the repository. Usually developers do this effort getting back to a commit where the application was working well and go commit by commit running tests to check which one broke the application. This approach works but it can take some time. To obtain better results, ``git bisect`` is recommended in this scenario.

[![](http://img.youtube.com/vi/D7JJnLFOn4A/0.jpg)](http://www.youtube.com/watch?v=D7JJnLFOn4A "Git Bisect Tutorial")

(Click on image to open this video tutorial)

## References

 - [Git documentation](https://git-scm.com/docs)
