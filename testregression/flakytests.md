Flaky test
================


Unit tests should always have the same results: it will fail or it will pass. In other words, the result is deterministic. But, sometimes, the same test shows both behaviors, even if there was no change in that unit. These non-deterministic tests are known as Flaky Tests and they are more common than you might think, a Google Engineer says that 16% of their tests has some flakiness.
When the code is passing in the Continuous Integration (CI) system, and a failure occurs, it ends up slowing down or preventing the evolution of the entire pipeline until the fault is found and resolved causing an increase in cost. The problem is that it is difficult to know when a test really failed or when it is Flaky.

## Identifying flaky tests


One way to identify these tests is to re-run the tests several times and mark the tests that show contradictory behaviors as “flaky”. However, it's hard to determine how many times you need to re-run a test until it proves to be flaky. It could still happen that your test exhibited a consistent behavior of failure but it was flaky. What some developers do is set a treshold for the number of executions after which if the test continuosly gives a failure, they would consider to truly exist a bug in the code. 

There are also tools, like [SCOPE](https://scope.dev/), that help to identify these tests in a single run.  

The important thing is to identify the flakiness as soon as possible. Establishing a routine where the system is tested several times helps to identify a flaky earlier, reducing the impact on the development of the project.

## Top causes for flaky tests

A test can be flaky for several reasons, the three most commons are:

*   Async wait: Every test needs some time to complete. In an asynchronous wait, sometimes the developer uses a **sleep** function to wait for the end of the execution. If the function finishes before this time, the test passes, if it take more time, it fails. Many flaky tests caused by the async wait can be fixed using **waitFor**. This function, instead of pre-setting a specific amout of time to wait, bounds to the ocurrence of an action, meaning it waits until a certain action takes place.
*   Concurrency: Just like the async wait problem, other issues related to concurrency also have great impact in causing tests to flake. These generally derive from the developer not being mindful of the order in which the operations are being executed by the different threads. This can be settled by adding a synchronization block or making sure the execution order of  threads is being obeyed.
*   Test Order Dependency: Another cause to flakiness is when a test T1 needs a test T2 to **have** been executed before it or a test T3 to **haven't** been executed before it. Sometimes, a test assumes implicit requirements that can't be complied due to some altercation made during the execution of a previous test. In this case, the order in which a set of tests is executed plays a role in influencing the occurrence of a certain output. For that reason tests should be independent from other each other.

Tests can also manifest flakiness due to dependency to other factors, such as network and system time. Using number generators, floating point operations or not dealing well with I/O operations could also lead to flaky behavior.

## Dealing with flaky tests
Now that we know what a flaky test is and what could cause them, we need to learn how to deal with this type of tests.

The approach some teams have to deal with flaky tests is to reject the test that exhibited this behavior, as examining if the issue is with the test or with the code takes time and delays development. Hence the easiest and most straightforward approach is to assume that the test is incorrect and not the code. However, this can’t be the best alternative, because if there is in fact a bug in the code it can escalate to bigger problems by pushing a broken code ahead.

A safe initial approach is to start tagging tests that are flaky. Beyond that, you'll need investigate the reason why a test showed such behavior and to further analyze the impact caused by this issue. In this case, it's extremely important to collect as much information as possible during the execution of each test: logs, specificities from the environment and memory data from the moment the test was executed, etc. This way it’s easier to reproduce the test that failed and to compare what’s different from the test that passed. As mentioned before, some teams reproduce a failed test countless times, which also helps to evaluate how flaky a test is. Another important piece of information to be considered is when this test started to to flake, since it's usually more complex to find the root problem in tests with older failures.

Once a test is tagged as flaky and data about its execution is collected, you can put this test into quarantine. Its output is disregarded and it shouldn’t be executed in the master pipeline until the issue with it is fixed. Then the assigned developer will start debugging the test, equipped with all the information about in which context this specific test failed and in which it passed. Because most teams set dealing with flaky tests as a high priority, these tests are generally fixed quickly.

## References

1. [https://docs.gitlab.com/ee/development/testing_guide/flaky_tests.html](https://docs.gitlab.com/ee/development/testing_guide/flaky_tests.html)
2. [https://talkingabouttesting.com/2017/01/04/a-importancia-de-lidar-com-testes-flaky/](https://talkingabouttesting.com/2017/01/04/a-importancia-de-lidar-com-testes-flaky/)
3. [https://talkingabouttesting.com/tag/flaky-tests/](https://talkingabouttesting.com/tag/flaky-tests/)
4. [https://whatis.techtarget.com/definition/flaky-test](https://whatis.techtarget.com/definition/flaky-test)
5. [https://medium.com/hackernoon/flaky-tests-a-war-that-never-ends-9aa32fdef359](https://medium.com/hackernoon/flaky-tests-a-war-that-never-ends-9aa32fdef359)
7. [https://engineering.salesforce.com/flaky-tests-and-how-to-avoid-them-25b84b756f60](https://engineering.salesforce.com/flaky-tests-and-how-to-avoid-them-25b84b756f60)
8. [https://medium.com/monsterculture/reproduce-flaky-tests-b8b42306d23f](https://medium.com/monsterculture/reproduce-flaky-tests-b8b42306d23f)
9. [https://engsoftmoderna.info/cap8.html](https://engsoftmoderna.info/cap8.html)
10. [https://imasters.com.br/desenvolvimento/qa-ci-flaky-tests-e-confiabilidade-para-devs](https://imasters.com.br/desenvolvimento/qa-ci-flaky-tests-e-confiabilidade-para-devs)
11. [https://medium.com/scopedev/how-can-we-peacefully-co-exist-with-flaky-tests-3c8f94fba166](https://medium.com/scopedev/how-can-we-peacefully-co-exist-with-flaky-tests-3c8f94fba166)
12. [https://arxiv.org/pdf/1907.01466.pdf](https://arxiv.org/pdf/1907.01466.pdf)
13. [https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html)