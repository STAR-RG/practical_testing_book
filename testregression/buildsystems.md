Build Systems
================

The purpose of a Build System is to automate the process of generating a software build. But what exactly is a build? In a simplified way, build is the process that involves compiling the source code of a computer program into binary files that are executed by the computer. At this stage, the build system also handles tasks such as managing project dependencies. After compilation, some projects also test the code using the test classes written by the developers to ensure that the code is ready and correct.

The automation process of generating the build can include several different processes, as we mentioned: compiling source code into binary, packaging binary code, and running automated tests to detect errors. There is no universal tool that can be used across multiple technologies, some of which specialize in small parts of the process. Here we use one of those general tools, called Gradle.

## Getting Started With Gradle

Gradle is an open source build automation tool, gradle stands out for its extremely versatility. Used by big tech companies, such as Netflix and Linkedin, it uses a Domains Specific Language (DSL) based on Groovy (there is limited support based on Kotlin as well). Gradle has a big list of features, some of these can help you improve your project build performance and dependency management.

## Exercise Time!
Now it’s time to create your own project using Gradle as Builder. First, you need to clone [this repository](https://github.com/damorim/testing-cin) on your computer. This repo contains a lot of practical material used in this book. The section that we’ll use is under the 2-build-gradle/binarysearch folder. 

Feel free to create your own Gradle project following this tutorial:  
[Example Project](./gradlesetup.md)

However, we have already made a project available for us to do the analysis. It is a simple design of a Binary Search algorithm in an array with some test cases.

## The Build file
When executing a build through the gradle, the tool will look for instructions on what should be done during it. Each phase, or order, performed is called a task (as we have already shown above) and these tasks are described in the build.gradle file, which is located in the root folder of the repository.

In the file provided, you will find some code to perform a simple build of the project:

```
plugins {
   id 'java'
   id 'application'
}
```

This first line tells the build system what the project's compilation logic should be. As in the above process we specified that the project would be a Java application, the code looks like this.

```
repositories {
   mavenCentral()
}
```

This second line tells Gradle which repository the system should resolve dependencies on.

```
dependencies {
   testImplementation 'junit:junit:4.1', 'org.hamcrest:hamcrest-all:1.3'
}
```
This configuration tells the system some additional dependencies of the project, in this case we specify which test libraries are used for the correct compilation of the code.

```
application {
   mainClassName = 'BinarySearch.java'
}
```

Finally, it is specified which project file the main class is in.

## The project’s code
The project classes, as well as the test classes, are located, by default, below the src directory. The only class of this project is in the main directory and it is a simple Binarysearch algorithm in arrays.

The only test class is found in the test directory and there are some test cases for the algorithm described in the design class. The code is written using the JUnit framework and tests some expected results from certain input cases.

## Compiling the project
Now that you know where the project is, we can move on to the build process. In the root folder, type in the terminal:
```
./gradlew build
```
After a few seconds, Gradle will have configured all the dependencies, compiled the project and applied the tests. The test results can be found in the HTML file found in the new build directory, which is now located in the root folder. Within this new directory are configuration files, temporary files, binaries used in the compilation and the test results (in the reports folder). The index.html file presents, in a very intuitive way, the test results for each package and class of the project. If any test fails, the file will show the entire stack of the failed test execution

## Testing the Code
To improve the display of tests in the terminal, you can also add one more task to your build file. The task code is as follows:

```
tasks.withType(Test) { 
  testLogging {
    exceptionFormat "full"
    events "started", "skipped", "passed", "failed"
    showStandardStreams true
  }
}
```

To execute this new task, we will only run the tests on the project. Running gradlew test, we obtain, in addition to the code compilation logs, the result of the tests execution.

If you don't find that answer, the gradle may not have run the tests. This can happen because the tool exists precisely to avoid rework, so it analyzes the inputs and outputs of each task, if the inputs have not changed, it does not execute the task again, considering that it is up-to-date. If this is the case, just use the command gradle test `--rerun-tasks`, which forces the gradle to run the tasks again.

Now we can see which tests were run and the results of each one. With a versatile tool such as Gradle you can write many different tasks that can help with your specific build automation, like the one above.

## Proposed Exercise
Now that you have finished this section, we suggest to you to create two new test cases for the BinarySearch project: One of them should fail and the other should pass. Then run the build process and analyse the result shown in your terminal.
