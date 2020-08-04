# How Good Are your Tests?

```
A good test has a high probability of finding an undiscovered error;
A good test is not redundant;
```

## What is test adequacy?

to do

## Adequacy criterion

to do

## Characteristics of the good test suite

### Fast

A fast test suite will provide feedback much earlier, making the development process more efficient. When a test suite is very slow, people tend not to run it completely before integration.

### Complete

Test coverage is a great quality indicator of your tests, with greater coverage, bigger are the chances of catching bugs. A test suite with a high test coverage, aims to measure the effectiveness of tests against the tested requirements, determining whether the existing test cases are covering the requirements being tested.

### Maintainable

It should be possible to have easy manipulation in the test suite. You must be able to add, modify or delete tests without having a negative impact on the system. Organization is essential for the presence of this characteristic. As the system evolves, tests need to keep up with these developments, both in terms of change and the utility of the test.

### Isolated

The tests must be independent of each other, that is, they must be executed without impacting other subsequent tests. The increase in the execution time of each test can increase, since the environment will be recreated. This time is justified by the fact of gaining independence between tests, allowing them to be run in any order and in parallel, thus decreasing the total execution time of the test suite.

## Approaches / Techniques

Some approaches / techniques help us to increase the quality of tests. We can quote some of them:

**Structural Testing** is designed according to the internal structure of the system, and therefore allows a more accurate verification of the software's operation. This type of test is developed by analyzing the source code and developing test cases that cover the functionality of the software component.

**Mutation Testing** are tests that test our tests, this approach includes changes to our code creating the mutants and running our tests repeatedly on this “new version” of code.

**Fault-based**

to do
