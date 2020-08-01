Example Project
================

First you have to create a new directory on your computer where the project will be set up. Once in this directory, execute the following command:

```
gradle init
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

In our example, we will use the JUnit 4 framework. Finally, you must provide the name of the project and the source package of your project, both of your choice. We will use gradle_demo as project and source names.

Once this process is finished, your directory will now be filled with a file structure that must be respected during the development of your project, so that the gradle can act effectively. This structure can be seen in the scheme below. We will highlight two elements created: the build.gradle file, where specifications of the build process are written that will be detailed later, and the src folder, which contains the project classes (main directory), and the test classes (in the test directory). Note that the gradle generated automatic java files to populate these directories. You can modify these files and add others according to the needs of your project.

```
.
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
    │   ├── java
    │   │   └── gradle_demo
    │   │       └── App.java
    │   └── resources
    └── test
        ├── java
        │   └── gradle_demo
        │       └── AppTest.java
        └── resources
```
