System Testing
==============

## Introduction

Traditionally, system testing is done when the software is working as a whole. An iterative life cycle allows system testing to take place much earlier, once well-formed subsets of use-case behavior are implemented. The destination is usually the end-to-end operating elements of the system.

The system test can be considered the "third phase" of the tests, being the first unit or unit test, which tests the smallest units in the system, looking for logic and implementation errors in each module, separately. The second would be the integration test, which aims to detect flaws in the interaction between the units, generally the types of flaws found are sending and receiving data. Remembering that integration with other systems is not part of this phase.
In practice they are executed under conditions similar to those that the user will use. This test checks if the components are compatible, if they interact correctly, if they transfer the right data at the right time, etc.

For this, one of the ways used to simulate the user environment in a quick and practical way, is the automated interface tests.

## Framework

### ROBOT

Robot is considered a framework and not just a test automation tool because it was built to provide all the necessary structure to meet an entire acceptance test automation architecture. It allows to use keyword-driven, data-driven and / or behavior-driven (BDD) approaches. It has an easy-to-use tabular data syntax and allows users to use and create libraries in Python or Java.

Robot Framework is actively supported, with many industry-leading companies using it in their software development, mainly because it can be integrated with virtually any other tool to create powerful and flexible automation solutions. Being open source also means that Robot Framework is free to use without licensing costs. Has easy syntax, using human-readable keywords. The framework has a rich ecosystem around it, consisting of libraries and tools that are developed as separate projects.

#### Main advantages

Having comprehensive documentation makes it easier to work with any tool. The Robot Framework is no exception, and has great documentation on their website. 
Also, After each test run, the Robot Framework provides a clear, concise, and human-readable HTML-test report. These reports are based on XML outputs from the tests. As an all-in-one reporting, it also helps when presenting to other stakeholders within an organization.

Another advantage is how quickly a test can be created, in addition to the possibility of making it extremely succinct when compared to other test frameworks or automation tools of the same category. The example below shows a test that aims to open a web page using the firefox browser: the first version is written using Python and Selenium webdriver, the second using the Robot framework.

 * Python with Selenium WebDriver:
 ```python
def setUp(self):
self.driver = webdriver.Firefox() 
self.driver.implicitly_wait(20)
self.base_url = "https://www.facebook.com/" self.verificationErrors = [] self.accept_next_alert = True Keyword
```
 
 * Python with Selenium Webdriver and Robot Framework:
 ```python
Open Browser https://www.facebook.com/         firefox
```

## CODE STRUCTURE

The structure of the script is simple and can be divided into four sections:

### Settings
This is where you configure the libraries to be used, paths to auxiliary files (page objects, for example), contexts and hooks.

### Variables
List of variables to be used (preferably with description) and definition of the values of some of these variables.

### Test Cases
This is the most important section, because without it your test will not run. This is where the test cases / scenarios are, with or without implementation.

### Keywords

Here you can define keywords or implement the test scenarios described above. All of the above sections are optional, depending on how your code was written, except for **Test Cases**. I advise you to always use them for a better organization of the code. 
The labels below are not mandatory, but they also help with the organization.

### Documentation
This keyword precedes the description of the functionality or test scenario. Be aware, because if the documentation is made in the section **Settings**, it should not be enclosed in square brackets. They are only used within **Test Cases**.

### Tags
A simpler label for the scenario, if you want or need to run only one or a few cases. You can do this by calling the title of the scenarios on the command line, but as they are usually large, tags end up being the best option overall.

### Spaces and Variables
The variables in the Robot are represented by $ {variable}. The Robot has the peculiarity of ignoring a space between words.

$ {variable_name} is equal to $ {variable name}. They are also case insensitive. The arguments are divided into at least two spaces. For example:

* command (two spaces) argument1 (two spaces) argument 2.

Note that the space in “argument 2” is ignored. The assignment sign (=) is also optional. Values can be assigned, either:
* $ {value} value
* $ {value} = value

An important observation to be made is that, being the Robot Framework based on Python, it is worth mentioning that this is an indented language, that is, command blocks are separated by spaces or tabs, forming a mandatory visual indentation. There are no *“open”* and *“close”* symbols, Robot inherits this formatting.


## Hands On: Robot with Selenium2Library
 
> [Selenium2Library](https://robotframework.org/Selenium2Library/Selenium2Library.html) is a web testing library for Robot Framework.

Let's hands on at Colab:

<a href="https://colab.research.google.com/github/damorimRG/practical_testing_book/blob/master/testgranularity/robot.ipynb" target="_blank"> 
    <img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"></a>