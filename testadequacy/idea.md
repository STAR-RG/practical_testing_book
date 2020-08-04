# How Good Are your Tests?

```
A good test has a high probability of finding an undiscovered error;
A good test is not redundant;
```

## What is test adequacy?

A major problem with software testing is  evaluating and selecting test cases. This section presents basic approaches to the selection of test cases and the corresponding suitability criteria.
Ideally, we would like a "suitable" test set to be the one that guarantees the correctness of the product. Unfortunately, this goal is not achievable, in practice, we accept criteria that identify inadequacies in test sets.

Now, let’s dive into an example. If the specification describes a different treatment in two cases, but the test set does not check whether the two cases are in fact treated differently, we can conclude that the test set is inadequate to avoid flaws in the program logic. If there is no test in the test suite that executes a specific program instruction, we can conclude in the same way that the test suite is inadequate to avoid failures in that instruction. 


## Adequacy criterion

I bet you are thinking if you can at least use some criteria to choose the approach that suits you better. Well, we can use a whole set of adequacy criteria, each based on some source of information about the program and imposes a set of obligations that an “ideal” set of test cases must satisfy. If a test suite does not meet any criteria, the obligation that has not been fulfilled can provide some useful information on how to improve the test suite. If a set of test cases meets all obligations according to all criteria, we still don't know for sure whether it is a well-designed and effective set of tests, but we do have at least some evidence of its scope.


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

**Fault-based** testing uses test data designed to demonstrate the absence of a set of pre-specified faults; typically, frequently occurring faults. For example, to demonstrate that the software handles or avoids divide by zero correctly, the test data would include zero.

