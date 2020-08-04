Flaky test
================


Unit tests should always have the same results: it will fail or it will pass. In other words, the result should be deterministic. But, sometimes, the same test shows both behaviors, even if there was no change in that unit. These non-deterministic tests are known as Flaky Tests and they are more common than you might think, a Google Engineer says that 16% of their tests have some flakiness.
When the code is passing in the Continuous Integration (CI) system, and a failure occurs, it ends up slowing down or preventing the evolution of the entire pipeline until the fault is found and resolved causing an increase in cost. The problem is that it is difficult to know when a test really failed or when it is Flaky.

## Top causes for flaky tests

A test can be flaky for several reasons, the three most common are:

*   **Async wait**: Every test needs some time to complete. In an asynchronous wait, sometimes the developer uses a **sleep** function to wait for the end of the execution. If the function finishes before this time, the test passes, if it takes more time, it fails. Many flaky tests caused by the async wait can be fixed using **waitFor**. This function, instead of pre-setting a specific amout of time to wait, bounds to the ocurrence of an action, meaning it waits until a certain action takes place. Let's imagine the following test where we send a message and then expect 3 seconds to the message to be sent.
```
click_button "Send"
sleep 3
expect_message_to_be_sent
```
The problem is, sometimes, it takes more than 3 seconds to a message to be sent. When this happens, the test fails.
A way to fix this, is by not specifying a time to the action to happen. The test waits for the message to be sent. This way, the test passes.

```
click_button "Send"
waitFor message_to_be_sent
```

*   **Concurrency**: Just like the async wait problem, other issues related to concurrency also have great impact in causing tests to be flaky. These generally derive from the developer not being mindful of the order in which the operations are being executed by the different threads. This can be settled by adding a synchronization block or making sure the execution order of  threads is being obeyed.
![](../assets/concurrency.jpg)  
In the case presented in this figure, the threads are modifying a shared list. When we try to check if an element of the list is equal to a certain value “x”, depending on which thread modified it last the outcome can be different, causing this code to behave non-deterministically.  

*   **Test Order Dependency**: Sometimes, a test assumes implicit requirements that can't be complied due to some modification made during the execution of a previous test. In this case, the order in which a set of tests is executed plays a role in influencing the occurrence of a certain output. For that reason tests should be independent from each other.

![](../assets/orderDependency.jpg)

As shown in the figure above, when Test 1 for the function isEmpty() is isolated it passes. But when we run Test 2 for insert() before Test 1, Test 1 fails. We added a new value into the list, so it isn’t empty as expected. However, when we run Test 3 for the function remove() after Test 2 and before Test 1, Test 1 passes again. This time, despite having added a new value into the list, we removed it right after, so when Test 1 runs the list is empty again.

Tests can also manifest flakiness due to dependency to other factors, such as network and system time. Using number generators, floating point operations or not dealing well with I/O operations could also lead to flaky behavior.

## Identifying flaky tests

One way to identify these tests is to re-run the tests several times and mark the tests that show contradictory behaviors as “flaky”. However, it's hard to determine how many times you need to re-run a test until it proves to be flaky. It could still happen that your test exhibited a consistent behavior of failure but it was flaky. What some developers do is to set a threshold for the number of executions after which if the test continuosly gives a failure, they would consider to truly exist a bug in the code. 

There are also tools, like [SCOPE](https://scope.dev/), that help to identify these tests in a single run.  

The important thing is to identify the flakiness as soon as possible. Establishing a routine where the system is tested several times helps to identify a flaky earlier, reducing the impact on the development of the project.

## Dealing with flaky tests

Now that we know what a flaky test is and what could cause them, we need to learn how to deal with this type of test.

The approach some teams have to deal with flaky tests is to reject the test that exhibited this behavior, as examining if the issue is with the test or with the code takes time and delays development. Hence the easiest and most straightforward approach is to assume that the test is incorrect and not the code. However, this can’t be the best alternative, because if there is in fact a bug in the code it can escalate to bigger problems by pushing a broken code ahead.

A safe initial approach is to start tagging tests that are flaky. Beyond that, you'll need to investigate the reason why a test showed such behavior and to further analyze the impact caused by this issue. In this case, it's extremely important to collect as much information as possible during the execution of each test: logs, specificities from the environment and memory data from the moment the test was executed, etc. This way it’s easier to reproduce the test that failed and to compare what’s different from the test that passed. As mentioned before, some teams reproduce a failed test countless times, which also helps to evaluate how flaky a test is. Another important piece of information to be considered is when this test started to to flake, since it's usually more complex to find the root problem in tests with older failures.

Once a test is tagged as flaky and data about its execution is collected, you can put this test into quarantine. Its output is disregarded and it shouldn’t be executed in the master pipeline until the issue with it is fixed. Then the assigned developer will start debugging the test, equipped with all the information about in which context this specific test failed and in which it passed. Because most teams set dealing with flaky tests as a high priority, these tests are generally fixed quickly.

## References

1. Qingzhou Luo, Farah Hariri, Lamyaa Eloussi, and Darko Marinov. 2014. An empirical analysis of flaky tests. In Procedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE 2014). Association for Computing Machinery, New York, NY, USA, 643–653. DOI:[https://doi.org/10.1145/2635868.2635920](https://doi.org/10.1145/2635868.2635920)

2. Bryan Lee. 2020. How Can We Peacefully Co-Exist With Flaky Tests?. [Blog] Scope. Available at: <[https://medium.com/scopedev/how-can-we-peacefully-co-exist-with-flaky-tests-3c8f94fba166](https://medium.com/scopedev/how-can-we-peacefully-co-exist-with-flaky-tests-3c8f94fba166)> [Accessed 27 July 2020].

3. John Micco. 2016. Flaky Tests at Google and How We Mitigate Them. [Blog] Testing Blog, Available at: <[https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html)> [Accessed 27 July 2020].

4. August Shi, Wing Lam, Reed Oei, Tao Xie, and Darko Marinov. 2019. iFixFlakies: A Framework for Automatically Fixing Order-Dependent Flaky Tests. In Proceedings of the 27th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE ’19), August 26–30, 2019, Tallinn, Estonia. Association for Computing Machinery, New York, NY, USA, 11 pages. DOI: [https://doi.org/10.1145/3338906.3338925](https://doi.org/10.1145/3338906.3338925)

5. Jonathan Bell, Owolabi Legunsen, Michael Hilton, Lamyaa Eloussi, Tifany Yung, and Darko Marinov. 2018. DeFlaker: Automatically Detecting Flaky
Tests. In Proceedings of ICSE ’18: 40th International Conference on Software Engineering, Gothenburg, Sweden, May 27-June 3, 2018 (ICSE ’18), 12 pages. DOI: [https://doi.org/10.1145/3180155.3180164](https://doi.org/10.1145/3180155.3180164)