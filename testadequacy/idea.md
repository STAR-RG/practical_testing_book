# How Good Are your Tests?

This chapter presents approaches to determine how good a test suit is, which is the subject of this section.

## What is test adequacy?

It is the minimum and sufficient criteria required to perform a particular type of testing. Ideally we should like an “adequate” test suite to be one that ensures correctness
of the product. Unfortunately, that goal is not attainable and in practice we settle for criteria that identify inadequacies in test suites.(chechik, 2007).

## Approaches

Some approaches help us to increase the quality of tests using coverage. We want to cover as many requirements as possible, because it will increase the chance to capture faults.

- _Logical coverage_ measures extent to which conditionals are covered. Examples: basic conditions and compound conditions.

- _Dataflow coverage_ measures extent to which data flows are covered. Examples: definitions, uses, def-uses, and def-use paths.

- _Structural coverage_ measures amount of code elements covered by the test suite. For example: statement, line, basic-block, branch, function, etc.

- _Mutation coverage_ measures amount of (injected) faults covered by the test suite.

Our focus in this section is to study and practice Structural Testing and Mutation Testing.

## References

1. [Marsha Chechik, Test Case Selection and Adequacy, 2007](http://www.cs.toronto.edu/~chechik/courses18/csc410/Ch9-10AdequacyAndFunctional.pdf)

2. Marcelo d'Amorim, Coverage test notes
