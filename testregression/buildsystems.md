## Build Systems
The purpose of a Build Systems is to automate the process of generating a software build. But what exactly is a build? According to Wikipedia [“a build is the process of converting source code files into standalone software artifact(s) that can be run on a computer"](https://en.wikipedia.org/wiki/Software_build#:~:text=In%20software%20development%2C%20a%20build,the%20result%20of%20doing%20so.).

The automation process of generating the build can include several different processes, such as: compiling source code into binary, packaging binary code, and running automated tests to detect errors. There is no universal tool that can be used across multiple technologies, some of which specialize in small parts of the process. Here we use one of those general tools, called Gradle.

## Getting Started With Gradle

Gradle is an open source build automation tool, gradle stands out for its extremely versatility. Used by big tech companies, such as Netflix and Linkedin, it uses a Domains Specific Language (DSL) based on Groovy (there is limited support based on Kotlin as well). Gradle has a big list of features, some of these can help you improve your project build performance and dependency management.

## Example Project
In this tutorial we will use the project under the 2-build-gradle/binarysearch folder of the [book's repository](https://github.com/damorim/testing-cin). It's necessary to have a java version installed.

To start a simple project with the gradle, it is necessary to install the tool. As the referring repository already contains the gradlew executable, our job is simpler.

To better understand the commands possible through gradlew, you can run the following command in the binarysearch folder:

```
./gradlew tasks
```
This command will display the list of Gradle execution options as a result.

Looking closely at the options, we see that a Setup option. This would prepare the environment for the development of a new Gradle project. You can test this option in a new directory of your choice. For now, it is only necessary to copy the gradlew executable and the gradle directory (which contains files necessary for the gradle execution) to your test directory.

Once in the new directory, execute the following command:
```
./gradlew init
```

From now on, the tool will guide you through the setup of your project. The first screen provided asks you to choose a type of project to create.

```
Select type of project to generate:
  1: basic
  2: application
  3: library
  4: Gradle plugin
Enter selection (default: basic) [1..4]
```

For our example, we will use an application type project. Then, the language used in the development of the project is requested

```
 Select implementation language:
  1: C++
  2: Groovy
  3: Java
  4: Kotlin
  5: Swift
Enter selection (default: Java) [1..5]
```

In our example, we will use the Java language. Then, the language used in the gradle settings is requested.

```
Select build script DSL:
  1: Groovy
  2: Kotlin
Enter selection (default: Groovy) [1..2]
```
In our example, we will use the Groovy language. Then, we ask for the framework used for the tests, here is an important comment: the gradle also automates tests and the execution of tests in the project! We will explore this during this tutorial.

```
Select test framework:
  1: JUnit 4
  2: TestNG
  3: Spock
  4: JUnit Jupiter
Enter selection (default: JUnit 4) [1..4]
```

In our example, we will use the JUnit 4 framework. Finally, you must provide the name of the project and the source package of your project, both of your choice.

Once this process is finished, your directory will now be filled with a file structure that must be respected during the development of your project, so that the gradle can act effectively. We will highlight two elements created: the build.gradle file, where specifications of the build process are written that will be detailed later, and the src folder, which contains the project classes (main directory), and the test classes (in the test directory). Note that the gradle generated automatic java files to populate these directories. You can modify these files and add others according to the needs of your project.

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