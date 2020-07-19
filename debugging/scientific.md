Scientific Debugging
====================

Often when we encounter unexpected behavior happening in our program depending on how familiar we are with the code, we already know the point that the error is probably happening.

But, and for people who are not so familiar with the code in question, is there not a more systematic way to help them find out where and why the problem is happening?

**Scientific Debugging** is a way that comes very close to the scientific method for explaining things, which is based on observing something, creating a hypothesis to explain what happened, creating tests to prove the hypothesis and finally coming up with an explanation of why that observed happened.

Based on this way of thinking, bringing to the programming context the scientific method works with the following steps:

1. **Observe**. Observe the failure and gather data about what happened.
1. **Hypothesis**. Create an explanation of what happened based on the data collected.
1. **Test**. Create tests to prove or not your explanation of what happened.
1. Repeat from step 1 until you can verify your explanation.

To be clearer:

In the first step, **Observe**, we should save information such as the program entry, which it showed on the screen, if any type of exception happened.

In the second step, **Hypothesis**, we can try to create some explanations of what happened, for example, to suppose if the error occurred on the client or server side of the application.

In the third step **Test** this step is very important because we will try to prove our hypothesis of what happened, through tests such as executing the program by printing the value of variables at certain points in the execution.

