# git-bisect

It is common to make changes on a repository that introduces a bug. And sometimes this bug goes unnoticed for a while, but when it's detected not always is simple to find the root cause.

If you are using git as your version-control system, the `bisect` command may help you on this matter. As specified by the documentation, it uses binary search to find the commit that introduced a bug.

<iframe width="560" height="315" src="https://www.youtube.com/embed/D7JJnLFOn4A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Hands-On

Now let's try using git-bisect by ourselves on a repository:

<a href="https://colab.research.google.com/github/damorimRG/practical_testing_book/blob/master/debugging/gitbisect.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"></a>

## Execution Flowchart

We can better visualize the execution of a git-bisect operation in the following flowchart:

![Flowchart](../assets/git_bisect/git_bisect_flowchart.png)

## Automating

Using git-bisect may be a tiresome task when using it if a wide range of commits. Thankfully there is a subcommand of git-bisect that allow us to automate this process.

To use it we need an executable that checks the condition on the repository and terminates with exit code `0` if the current commit is a god commit, or terminates with any other exit code if the commit is a bad one. Given that, we can run the following command replacing `$EXEC` and `$ARGS` with the appropriate values:

```bash
git bisect run $EXEC $ARGS
```

### Practice

You can try to automate the git-bisect operation that we've run in the _Hands-On_ section using the `run` subcommand. Notice that we don't need to print anything in the console.

## Final Thoughts

git-bisect makes it easier to find a bug among a list of affected commits. The process can be run manually or in an automated way by using a command that will classify the commits for you. Sometimes is as simple as invoking one of the tests of the project's suite and other times a more complex script needs to be written. Either way, it is more practical to use it than search by ourselves in a huge list of commits.
