#### Test Selection and Prioritization

Testing can take a large part of the development time and be expensive to create and execute, so It's also a job of to the developers to choose which tests should be done first and which method could used to test a specific part of your code. With a good skill on test selection a developer can assure quality software and cut the costs associated with the testing phase. 

###### Test Case Selection

Testing every case of a specific software can be really impractical since even for small parts of a program the number of possible inputs can be enormous. For this reason we should choose very carefully which cases to use while testing our applications and always trying to achieve the fault detection. 

There are three approaches we could use for choosing test cases for a program, are those: 

1. Random selection.
   * Using simple random test cases we can acquire an effective test and keep a low cost of execution.
1. Coverage-based selection.
   * Using few test cases that aim for maximize test coverage we can make sure every line of code has been executed as least once.
1. Similarity-based selection.
   * Using distinct tests even in a lower quantity we can increase the chance of catching an error. 

Using this heuristics we can make tests that and fast to build and execute but still maintaining a high level of fault detection. 

###### Regression Test Selection

Regression testing selection is the process of choosing which of the tests created for our application will be executed for this purpose. Our goal is to choose a small amount of the already existing scenarios but still serving the purpose for retesting the already existing features. Choosing which tests to use during our regression tests is a process that should involve finding the application's most affected pieces by the change and also test cases for critical parts of the program.

This process can be executed following three techniques:

1. Coverage technique.
   * Chooses the tests based on how they cover the modified portion of the code.
1. Minimisation technique.
   * Uses the least amount of tests necessary to cover the modified part of the code.
1. Safe technique.
   * Executes the most tests possible that inputs different data to the modified method.

###### Test Prioritization
 
Regression test is performed alongside software development to guarantee that new changes don’t affect the behavior of unchanged code. Having a good test-case suite that covers the software as a whole can be challenging and costly, as you can have a large suite and running all of them may take a while.

Test prioritization is a technique for ordering test case suites aiming to remove repetition and waste of time when trying to expose software failures and faults.

Some aspects should be considered for test-case prioritization:
  * Run frequency 
  * Probability of failure, risk and user visibility
  * The priority of requirements in stakeholders documentation
  * Past history of complex code break

Using these criteria, we can list some prioritization techniques:

1. Based on the fault detection percentage.
   * Rating the fault detection on each test, for each run, how many times it has detected a fault or not.
1. Using faulty severity.
   * The priority is based on the requirements of faulty severity, which means the number of times the fault can occur. For defining the weight of each, the following criteria can be used:
    * Business value measure
    * Project change volatility
    * Complexity
    * Fault proneness of requirement
1. Prioritization for regression testing.
   * For regression tests we can use different techniques for prioritizing tests, here are some of them:
    2. No prioritization
        * For this process you can consider not take any technique (not prioritizing the testing order and using an “untreated” test suite). The success of this approach depends on the manner in which the suite was built.
    2. Random prioritization
        * Randomly sorting test cases.
    2. Optimal prioritization
        * Determine which test exposes which fault and order them trying to cover the maximum number of fault as possible.
    2. Total branch coverage prioritization
        * Getting the number of decision branches that a test case can cover and sorting them by the total number of branches decreasingly.
    2. Additional branch coverage prioritization
        * This process is very similar to total branch coverage, but here the test cases are chosen iteratively to generate the best branch coverage in the next step. In the end, you might end with some tests that cannot add additional branch coverage, those can be selected in any order using another prioritization technique.
    2. Total statement coverage prioritization
        * The same process as total branch coverage, but statements are counted instead of branches.
    2. Additional statement coverage prioritization
        * The same process as additional branch coverage, but statements are counted instead of branches.
    2. Total fault-exposing-potential prioritization
        * Statement and branch prioritization may mask a fact about test cases and fault, the ability of a fault be exposed can depend on the probability of that fault cause a failure to the program. Total fault-exposing potential uses mutation analyses, calculating a mutation score for each pair of test cases and statements and summing all values to define a test case prioritization order.
    2. Additional fault-exposing-potential prioritization
        * Same approach as Total fault-exposing-potential, but after choosing a test case, the process lower the points for other test cases that cover the same statements.

###### References
 - [Testomat Guideline for Test Prioritization and Test Selection](https://itea3.org/project/workpackage/document/download/6194/Booklet%20v1.2%20-%20Guideline%20for%20Test%20Prioritization%20and%20Test%20Selection.pdf)
 - [Gregg Rothermel, Ronal H. Untch, Chengyun Chu, Mary Jean Harrold, “Test Case Prioritization: An Empirical Study, UK”, Proceedings of the International Conference on Software Maintenance, Oxford, September 1999](http://cse.unl.edu/~grother/papers/icsm99.pdf)
 - [Ahlam Ansaria, Anam Khanb, Alisha Khanc, Konain Mukadam, “Optimized Regression Test using Test Case Prioritization”, 7th International Conference on Communication, Computing and Virtualization 2016](https://core.ac.uk/download/pdf/82192235.pdf)
 - [Professional QA Regretion Test Selection](https://www.professionalqa.com/regression-test-selection)
 - [Professional QA Test Prioritization](https://www.professionalqa.com/test-prioritization)

