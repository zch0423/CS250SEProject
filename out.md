# 1 this is title
## Description

The short texts we provide aren't descriptive. Often, they only repeat the name of the module.

https://search.maven.org/artifact/org.junit.jupiter/junit-jupiter shows

![image](https://user-images.githubusercontent.com/2319838/78581543-4afdc900-7834-11ea-9c75-b0058f61a85a.png)

https://package-search.jetbrains.com/search?query=junit shows

![image](https://user-images.githubusercontent.com/2319838/78578225-7fbb5180-782f-11ea-96ec-9f53e47dda9c.png)

## Deliverables

- [ ] Improve short descriptions of each module/artifact/package in such a way, that its purpose is clear, i.e. don't repeat the information that the name already carries.




# 2 this is title
If child and parent have same uniqueId, things go wrong. An assertion could help engine writers to find that more quickly. 



# 3 this is title
## Overview

The `@TestFactory` annotation is only supported on instance methods.  However, factories are often merely functions.  The limitation of the annotation means that test factories cannot be written with convenient function or property syntax of non-Java JVM languages.

For example, in Kotlin I'd like to do the following, with the Minutest test library:

```java
@TestFactory
val tests = junitTests {
    test("a test") { ... }
    ...
}
```

In this code, _tests_ is compiled to a static getter.  But because `@TestFactory` is not supported on `static` methods, I have to write a lot of boilerplate code to achieve the same result.

Please allow `@TestFactory` to be used on `static` methods.



# 4 this is title
the button in he JUnit eclipse view that says rerun failed first does nothing different than the one right next to it (rerun)
please either remove or preferably fix its functionality
## Steps to reproduce

run tests that fail
click rerun failed first no change in order

## Context

 - Used versions (Jupiter/Vintage/Platform):
 - Build Tool/IDE: eclipse 2019-03 and previous

## Deliverables




# 5 this is title
We are wanting to experiment with parallel test threads to speed up execution.
We are using a custom Extension in our e2e test suite.

These e2e tests are mostly read only tests with a few that modify db state.

The annotation takes the name of the client we are testing against.
The Extension is then responsible for making sure everything related to the client is prepared and in the base state.

It then uses the ParameterResolver feature to passes testing objects into each test method that automatically talk to the client based on the annotation.

Within the Extension we know if the helpers request modify state or are read only.

We would like to be able to extend our existing extension to be able to dynamic add ResourceLocks on a per test bases.






# 6 this is title
## Proposal

The current proposal is to introduce the following:
- `@ScenarioTest`: class-level annotation used to denote that a test class contains steps that make up a single scenario test.
- `@Step`: method-level annotation used to denote that a test method is a single _step_ within the scenario test.

The `@Step` annotation will need to provide an attribute that can be used to declare the next step within the scenario test. Steps will then be ordered according to the resulting dependency graph and executed in exactly that order. 

For example, a scenario test could look similar to the following:

``` java
@ScenarioTest
class WebSecurityScenarioTest {

    @Step(next = "login")
    void visitPageRequiringAuthorizationWhileNotLoggedIn() {
        // attempt to visit page which requires that a user is logged in
        // assert user is redirected to login page
    }

    @Step(next = "visitSecondPageRequiringAuthorizationWhileLoggedIn")
    void login() {
        // submit login form with valid credentials
        // assert user is redirected back to previous page requiring authorization
    }

    @Step(next = "logout")
    void visitSecondPageRequiringAuthorizationWhileLoggedIn() {
        // visit another page which requires that a user is logged in
        // assert user can access page
    }

    @Step(next = END)
    void logout() {
        // visit logout URL
        // assert user has been logged out
    }

}
```

## Related Issues

- #13 
- #419 
- #607 
- #884 




# 7 this is title
There is hardly any _official_ documentation about how to use and add to the JUnit 5 platform.
This might be useful for users of JUnit, for possible contributors of engines and for IDE and tools developrs.

## Deliverables

The follow list is just a first attempt at enumerating useful documents:

- [ ] What is the JUnit Platform all about?
- [ ] How to discover and run platform tests from any engine
- [ ] How to write and test a test engine for the JUnit platform
- [ ] How to enhance platform reporting and tooling

I guess the whole platform topic is too specific for the general JUnit 5 user guide




# 8 this is title
We would like to send a command to the engine to control the execution and stop the progress of pending tests via the interface `org.junit.platform.launcher.Launcher`.



# 9 this is title
I wanted to be able to be able to run unit tests without them being picked up automatically. I.e. I only want to run them from inside a `main()` method. Sormuras came up with a solution to my question [here](https://stackoverflow.com/questions/50110819/launching-junit-jupiter-tests-from-inside-a-main-method), and suggested that I submit a feature request. I propose that specifying a class or method in a `selector` supplied to the `LauncherDiscoveryRequestBuilder` should make the engine pick that class/methods up and run them even if they're not annotated with `@Test`. I.e. it would be an alternative method of telling the engine what to run. 





# 10 this is title
## Overview

As discussed in https://github.com/spring-io/initializr/issues/862, the `TempDirectory` may fail to clean up the temporary directory due to various reasons, but sometimes the user would prefer that the extension not cause the test to fail if certain files or folders within the temporary directory cannot be deleted.

Introducing a configurable clean up mode would help to support such use cases.

## Proposal

Proposal by @marcphilipp:

> I think it should be strict by default in order to catch subtle bugs in the code under test, e.g. an unclosed stream. But changing to a lenient mode via the annotation (sth. like `@TempDir(cleanupMode = LENIENT)`) or a configuration parameter is certainly sth. we can consider for 5.4.1.

## Deliverables

- [ ] Introduce a means to opt out of test failure when the temporary directory cannot be cleaned up automatically.
- [ ] Document in Javadoc.
- [ ] Document in User Guide.
- [ ] Document in Release Notes.




# 11 this is title
I use org.junit.platform 1.6.2 with org.junit.jupiter 5.6.2 and have two classes with integration tests `FooIT` and `TestBarIT`.

This is my configuration:

```java
    @RunWith(JUnitPlatform.class)
    @SelectClasses({ 
            FooIT.class, TestBarIT.class
    })
    @SuiteDisplayName("Suite IT")
    public class SuiteIT { }
```

However, tests in `FooIT` will be ignored if I don't add word `Test` (for example `TestFooIT`). But I don't want to add word `Test` as we have a strict naming convention for tests. 

I think this is the wrong behavior because Test classes are set explicitly - a developer sets list of classes but JUnit filters it. So, who knows better what classes to use - the developer or JUnit?

Can anyone suggest a workaround for a now to make JUnit suite accept classes without `Test` in their names or to configure it use `IT` for class checking?



# 12 this is title
## Background

This issue addresses some of the topics discussed in #112.

## Status Quo

It is currently possible to register extensions _declaratively_ via `@ExtendWith` on types and methods, and #497 will support programmatic extension registration via fields. However...
- Developers cannot _alter the order_ of registered extensions.
- Developers cannot _remove_ a registered extension.
- Developers cannot _insert_ an extension into the list of registered extensions -- for example, at the front or somewhere in the middle.

## Rationale

In order to avoid the introduction of an overly complex declarative model for sorting, appending, prepending, inserting, and removing extensions, we have opted for a programmatic means to achieve all of the above. Providing a programmatic means to achieve these goals frees developers to manage registered extensions as they see fit without any unnecessary restrictions imposed on them by the framework itself.

## Considerations

Such a mechanism could itself be an `Extension` registered declaratively via `@ExtendWith`; however, the current thinking in the team is that there should be one and only one such component registered at any given time. Since this is such a special case which affects all extensions which have been registered declaratively, it is therefore considered best to introduce a new declarative mechanism for registering this single _component_. Similarly, the API for such a component should therefore not extend `Extension` since doing so would allow users to incorrectly register it via `@ExtendWith` (in which case it would simply be silently ignored).

## Proposal

- Introduce an `ExtensionManager` API that receives a list of all registered extensions as input and returns a list of extensions.
- Introduce a `@ManageExtensionsWith` annotation that allows the user to declare a single class reference for an implementation of `ExtensionManager`.

## Related Issues

- #13 
- #416
- #497
- #864 
- #1707 

## Deliverables

- [ ] Introduce a mechanism for programmatic extension management.




# 13 this is title
This is a sample implementation of #1987.

It probably needs a bit of javadoc tidy-up, but before I invested too much time on that I wanted approval/feedback from the core team for the basic concept and the way I've implemented it.

Note that the first commit is shared in common with #2106.



# 14 this is title
Background:
I tried to implement an extension to make it possible measuring the duration of test executions. So I created an extension like the one in the JUnit5 User Guide. Everything seemed fine when I checked the example implementation provided there ("TimingExtension"). **But** there, the duration is just logged. However, I need to include the results in a report created by implementing a custom TestExecutionListener. Looking at the ExtensionContext interface, I thought I could use the instance provided as an argument to the beforeTestExecution/afterTestExecution methods (defined in BeforeTestExecutionCallback and AfterTestExecutionCallback, respectively) to publish entries containing the time a test is started/is finished. But, at a second glance I saw that the report entries has to be consumed by a EngineExecutionListener, which is, in my case, sadly no supertype of TestExecutionListener. So, there seems no easy way to publish those points in time to my own listener. Sadly, I found no documentation for the EngineExecutionListener in the user guide, so I don't expect the reports are internally received and passed further, such that they are also avaible in execution listeneres. So two questions arise:
* A compound value type holding the start time of test execution and the end time of test execution published through my extension for further use in the listener would be a good fit. Sadly, only publishing the string representation of these times seem to be possible. Therefore, the duration of actual test execution, if not published additionally also as a string representation (which would be kinda redundant in my opinion), has to be computed in the listener after first parsing the time points' string representations. Why isn't it simply possible to publish non-string keys?
* How can I publish results from an extension to an execution listener?

Thanks to you in advance for any response.



# 15 this is title
## Overview

Fixes some of the test cases added in https://github.com/junit-team/junit5/issues/981.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [x] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 16 this is title
I would like to leverage existing `ParameterResolver` implementations and use/adapt the type they would resolve in my own `ParameterResolver`.
If possible, I would like to use them in a declarative fashion.

## Use Cases

### Using a `ParameterResolver` result in another `ParameterResolver`

The first use case I have is leveraging the built-in [`@TempDir`](https://junit.org/junit5/docs/current/api/org/junit/jupiter/api/io/TempDir.html) while testing against multiple Gradle versions and different configurations.
We have an extension that works as a `TestTemplate` to run tests against multiple Gradle versions.
Right now, both parameters are injected separately and are setup at the start of the test (`@ParameterizedTest`) or set up (`@BeforeEach`):

```kotlin
@TestTemplate
@ForGradleVersions(["5.1", "5.2"])
internal fun `do thing with GradleRunner`(@TempDir directory: Path, gradleRunner: GradleRunner) {
  // assume GradleRunner sort-of-configured here
  gradleRunner.withProjectDir(directory.toFile())
  // run build with Gradle Runner
}
```

I would like to be able to compose the `ParameterResolver` class that is performing the resolution for `GradleRunner` with the `ParameterResolver` for `@TempDir`'s path.

For example, something like this:

```kotlin
@TestTemplate
@ForGradleVersions(["5.1", "5.2"])
internal fun `do thing with GradleRunner`(gradleRunner: GradleRunner) {
  // gradleRunner.withProjectDir(directory.toFile()) unneeded because @ForGradleVersions extension leverages another tool/extension to bootstrap a project directory
  // now, run build with Gradle Runner
}
```

In this example, the extension would leverage the JUnit Jupiter built-in `@TempDir` `ParameterResolver` to set the `withProjectDir(...)` before the parameter is actually injected.
The other extension lifecycle methods would also be invoked appropriately.

------

Another similar example we have is another `ParameterResolver`-like extension that gets some local Gradle project files and provides the location of it to the test as a `Path`.
Then, in the test setup, the `GradleRunner` is set up wit those files before building.

An example might look like this:

```kotlin
@TestTemplate
@ForGradleVersions(["5.1", "5.2"])
internal fun `do thing with GradleRunner and files`(@TempDir directory: Path, gradleRunner: GradleRunner, @GradleProject(["projects", "only-plugins-block"]) directoryWithProject: Path) {
  // assume GradleRunner sort-of-configured here with version and withPluginClassPath()
  recursivelyCopyDirectory(from = directoryWithProject, to = directory)
  gradleRunner.withProjectDir(directory.toFile())
  // run build with Gradle Runner
}
```

In here, I have multiple `ParameterResolver`s that all get combined in the test (`@ParmaterizedTest`) implementation.
I want to mutate the `GradleRunner` that was passed in with another "modifier" like extension.

Since the `GradleRunner` has a `null` `.getProjectDir()`, then the customization of the directory from the `@GradleProject` resolver can't really do much.

An example of what it might look like with this feature might be:

```kotlin
@TestTemplate
@ForGradleVersions(["5.1", "5.2"])
internal fun `do thing with GradleRunner`(@GradleProject(["projects", "only-plugins-block"]) gradleRunner: GradleRunner) {
  // GradleRunner has full project configured and setup
  // run build with Gradle Runner
}
```

In this example, the `GradleRunner` has the `withProjectDir(...)` configured by the `ParameterResolver` for `@TempDir` and it's `getProjectDir()` mutated by the `ParameterResolver` (or some other extension) that makes use of `@GradleProject`.

### Adapting/converting an existing `ParameterResolver`  result

We have an internal JUnit Jupiter `ParameterResolver` that provisions Docker containers.
We like that is is mostly generic and can be used to create arbitrary Docker containers, networks, and other launch configurations that we can execute against.

For some containers that get used, a user would like to "adapt" the `Container` parameter that gets injected  to a client for whatever service they are starting.

For example, here is an example that provisions a Cassandra Docker container on `localhost` and runs against it:

```kotlin
@ExtendWith(DockerContainerExtension::class)
@Test
internal fun `my test that uses cassandra container`(@DockerContainer(CassandraContainerLaunchConfigurationProducer::class) container: Container) {
  Cluster.builder()
    .withPort(container.bindings.first { it.fromPort == 9042 }.toPort)
    .addContactPoint("localhost")
    .withoutJMXReporting()
    .withoutMetrics()
    .build().use { cluster ->
      cluster.connect().use { session ->
        // create keyspace, tables, etc.
        // run test
      }
    }
}
```

The `Cluster` and `Session` are opened and used to setup some additional resources like tables, keyspace, etc. before being used in test code.
In this example, we are not (at least not yet) composing `ParameterResolver` and performing the set up in the test (`@Test`) or set up (`@BeforeEach`) methods.

Below is an example of what I would like it to (possibly) look like.

```kotlin
@ExtendWith(DockerContainerExtension::class)
@Test
internal fun `my test that uses cassandra container`(@DockerCassandraSession session: Session, @DockerCassandraKeyspace keyspace: String) {
  // do test with cassandra
  // expect cassandra stuff shut down by extension
}
```

In this example, the underlying connection is to a `Container` is abstracted away.
I'm also hoping to resolve multiple parameters here for a single `Container`.
This example does not have multiple `Container`s, but that is most likely a valid use case, too.

## Using Existing Tools

From what I can tell, there is no way to do this with existing tooling. The `ExtensionContext.Store` isn't helpful here because each extension has dependencies which would require ordering.
There is a desire to reduce the amount of parameters that a test needs as input while also not introducing any inheritance.

The way we have been mostly doing it is to put the injection and configuration in a `@BeforeEach` method and then perform the setup in the test.
We would like to, instead, build upon JUnit Jupiter's tools and extension model.

## Related Issues

- #1604 

## Deliverables

Unsure on exact deliverables.

- [ ] ...




# 17 this is title
Feature Request to simplify Parameterized Tests.

I am looking for an easy way to implement Parameterized Tests with multiple arguments.

While I could use `@CsvSource`, I'd appreciate multiple annotations, similar to NUnit's `TestCase`.

Example:

```java
    @ParameterizedTest // still required?
    @Parameter(10, "10000")
    @Parameter(20, "20000")
    @Parameter(30, "30000")
    void calculate(int input, String expected) {
        assertThat(Integer.toString(input*1000)).isEqualTo(expected);
    }
```

Any thoughts on this?



# 18 this is title
Hi.
I´d like to promote JUnit 5 inside my company, do you provide any kind of abstract or open slides that i can use? By chance, do you have kind of abstract or sth. like a onepager/flyer, that i can drop at the right table? 





# 19 this is title
The idea is to be able to define the concrete class which is subject of a given test class. An example could look like the following:

``` java
@TestsFor(Foo.class)
class FooTests {
    // ...
}
```

`@TestsFor` should be a class level annotation. Usage should be optional.

Having such an annotation makes it explicit which class is tested by a test class without having to rely on the test class's name to obtain this information. IDE vendors can use this information to make it possible to unambiguously navigate from a production class to all related test classes. IntelliJ IDEA already provides this feature, but (as far as I know) has to use the class name of a test class to determine all test classes for a test subject.

While in the most cases it is sufficient to use the name of a class to find all related tests, there are some situations where this approach fails or is inaccurate.
- A test class that only tests a subset of some class may conjugate parts of the tested class's name (especially for non-English class names). Contrived example: class under test is named `BuchVersand`, test class is named `BücherWerdenSonntagsNichtVersandtTests`
- The test subject has a name which is part of other unrelated class names. Example: Classes `Condition` and `VisibilityCondition`. In IntelliJ, also the `VisibilityConditionTests` will falsely be shown as test for `Condition` in addition to `ConditionTests`. 

Using a `@TestsFor` annotation could make it clear what the real class under test is for these cases. It could also be used by  reporting tools.

What do you think about this proposal? And especially, what do IDE vendors think about that?




# 20 this is title
Annotation based Assumptions, e.g.
```
@Test
@Assumption(failOnPass=true)
```
So that we don't have to rewrite all the assumeThat's to assertThat's and perhaps more importantly so that all test frameworks (assertj, spring, etc) don't have to implement an assume for everything.



# 21 this is title
The [fallback approach to argument conversion](https://junit.org/junit5/docs/current/user-guide/#writing-tests-parameterized-tests-argument-conversion-implicit-fallback) is a good one, however I'd like to see it extended in two ways:

Firstly, it only considers methods that accept `String`, whereas there are cases where the factory method accepts `CharSequence`. Notably, this includes `java.time.*` and the related ThreeTen projects.

Secondly, the fallback approach can't complete if it finds multiple matching factory methods. This is an issue that [Joda-Convert](https://www.joda.org/joda-convert/) tackles with annotations:

```java
    import org.joda.convert.FromString;
    public class Point {
      @FromString
      public static Point of(String str) {...}
      public static Point ofInverted(String str) {...}
    }
```

(the one annotated with `@FromString` is the one to use for parsing formalized strings in the way JUnit requires).

What I am proposing is that if the fallback mechanism reaches a point where it finds multiple matching factory methods/constructors, it then searches for an annotation with the name `FromString` (not the type `org.joda.convert.FromString` to avoid the dependency) and chooses that one. This would occur at the end of the current lookup process, thus be backwards compatible.

Supporting this approach would instantly make Joda-Time, Joda-Money and ThreeTen-Extra types compatible with JUnit 5, as they all use Joda-Convert.

For completeness, I note that the `ArgumentConverter` interface already allows Joda-Convert to be integrated if desired. Where the approach above enhances this is that it provides a way to integrate the concept of Joda-Convert directly into JUnit 5 *without the need to add the dependency*.




# 22 this is title
## Overview

In #1005, @kcooney introduced a private `MemoizingSupplier` class in `ExtensionValuesStore` that could (eventually) prove useful in multiple scenarios.

See discussion in [commit comments](https://github.com/junit-team/junit5/commit/6316bd090e662bfbce5e46ece7d5a0bcc858f732##commitcomment-23499744).

## Proposal

The following is a proposal for what such a generic `MemoizingSupplier` might look like.

```java
/*
 * Copyright 2015-2017 the original author or authors.
 *
 * All rights reserved. This program and the accompanying materials are
 * made available under the terms of the Eclipse Public License v1.0 which
 * accompanies this distribution and is available at
 *
 * http://www.eclipse.org/legal/epl-v10.html
 */

package org.junit.jupiter.engine.execution;

import static org.junit.platform.commons.meta.API.Usage.Internal;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.function.Supplier;

import org.junit.platform.commons.meta.API;

/**
 * @since 5.0
 */
@API(Internal)
public class MemoizingSupplier<T> implements Supplier<T> {

	private final Supplier<T> delegate;
	private final Lock lock = new ReentrantLock();

	private volatile boolean valueSet = false;
	private volatile T value;

	public static <T> Supplier<T> of(Supplier<T> delegate) {
		return new MemoizingSupplier<>(delegate);
	}

	private MemoizingSupplier(Supplier<T> delegate) {
		this.delegate = delegate;
	}

	@Override
	public T get() {
		if (!this.valueSet) {
			this.lock.lock();
			try {
				if (!this.valueSet) {
					this.value = this.delegate.get();
					this.valueSet = true;
				}
			}
			finally {
				this.lock.unlock();
			}
		}
		return this.value;
	}

}
```

## Deliverables

- [ ] If the need arises, move `MemoizingSupplier` to a top-level class or hide it behind a factory method in a utility in `junit-platform-commons`.




# 23 this is title
Seems to be feature we wanted?

https://github.com/junit-team/junit5/blob/master/junit-platform-commons/src/main/java/org/junit/platform/commons/util/AnnotationUtils.java#L217-L219

This use case triggered the question:

https://github.com/junit-pioneer/junit-pioneer/pull/133/files#diff-e173b19bdf682fe079028644b4dccc43R168-R171

## Deliverables

- [ ] Working as intended?
- [ ] Bug?




# 24 this is title
I just got bitten by the (IMHO counter-intuitive) behavior of `@TempDir`: When using it in multiple places, each injection point gets the **same** directory injected. That is, the following does not do what one would intuitively expect:

```java
void test(@TempDir File source, @TempDir File target) {
    ...
}
```

Both `source` and `target` point to the same directory!

Of course, you can work around this:

```java
void test(@TempDir File tempDir) {
    File source = new File(tempDir, "source");
    File target = new File(tempDir, "target");
    ...
}
```

But this feels unnecessarily complex for this, IMHO, rather common use case.

If, on the other hand, injecting the same temporary directory in multiple places is _really_ what is desired, one can even imagine the following API to still support that use case:

```java
@TempDir("id") Path samePath;

void test(@TempDir("id") File sameDir) {
    ...
}
```

## Deliverables

- [ ] An update to `TemporaryDirectory` which sets up (and tears down) a new temporary directory at each injection point.




# 25 this is title
## Status Quo

Using JUnit 5 annotations and mechanisms one can do a lot of things that are syntactically possible but don't make sense. For example, one can annotate a method with both `@Test` and `@BeforeEach`.

## Proposal

Introduce a mechanism where JUnit itself but also other parties can register rules that will be checked during discovery time, e.g.:

- `AmbiguousAnnotationsRule`
- `DuplicateExtensionsRule`
- `ProhibitNestedTestsRule` (in case a project wants to forbid this style of testing)

Those rules should be listable and configurable from the launcher API: Error, Warning, Off

Rules could work on different level, e.g whole test plan, engine, package, class, method, etc.

## Related Issues

- #242 



# 26 this is title
After #406 has been resolved we should consider determining line number information for dynamic tests in JUnit Jupiter as described there. For that we need to measure the performance impact and take an informed decision. We could also make this an opt-in feature via a configuration parameter.




# 27 this is title
## Overview
related to https://github.com/pytest-dev/pytest/issues/7662

> It looks like pytest (and Junit) just takes the system time from OS, and save it to test report.
Unfortunately, this timestamp doesn't have any timezone information, Our CI system will treat this timestamp as a UTC time, even the timestamp is actually from another time zone.

<!-- Please describe your changes here and list any open questions you might have. -->

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [ ] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [ ] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 28 this is title
## Overview

This change updates the JUnit Vintage Test Engine to read the parallel configuration parameters, and if parallel execution is enabled, creates a thread pool for executing the test descriptors concurrently. The approach for configuring the thread pool emulates the logic used by the Jupiter Test Engine.

I tested this with the Maven Surefire plugin with the following configuration:

    ...
		<dependency>
		    <groupId>junit</groupId>
		    <artifactId>junit</artifactId>
		    <scope>test</scope>
		</dependency>
	</dependencies>
    ...
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <configuration>
                    <parallel>classes</parallel>
                    <threadCount>4</threadCount>
                </configuration>
                <dependencies>
                    <dependency>
                        <groupId>org.junit.vintage</groupId>
                        <artifactId>junit-vintage-engine</artifactId>
                        <version>5.8.0-SNAPSHOT</version>
                    </dependency>
                </dependencies>
            </plugin>
	</plugins>
    </build>
...

Setting `parallel` to both `classes` and `all` behave as expected.

### Open Questions

* It was not clear to me how the Maven Surefire plugin interfaces with the JUnit vintage engine. I enabled concurrency for top-level `TestDescriptor` instances. The unit test I created only tests parallelism enabled and parallelism disabled.
* ~Also, should I update the user guide and release notes within the scope of this PR?~ I included the user guide and release notes changes in this PR. If they should be separate, please let me know.

Issue: #2229

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [x] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 29 this is title

Would be possible add a chart about the comparison about performance between JUnit 4 vs 5?



# 30 this is title
https://github.com/junit-team/junit5/blob/040037dfb08a0e61b7cb9e485196b0ba3758e756/junit-vintage-engine/src/module/org.junit.vintage.engine/module-info.java#L19

JUnit 4 mandates Hamcrest to be available at runtime and Hamcrest 2.2 (or earlier) claimed `org.hamcrest` as its stable module name.

https://github.com/hamcrest/JavaHamcrest/blob/5dd6a622c73daf716c6e8f33efa712be8dbb42ed/hamcrest/hamcrest.gradle#L16



# 31 this is title
Thanks for adding TempDirectory to JUnit 5.4.0-M1. This will make migration from JUnit 4 easier in my projects :-)


One point looks wrong to me though:
A `@TempDir` constructor parameter is treated like a parameter of a `@BeforeAll` method, ie its value is shared between all tests. See [Javadoc of TempDirectory](https://junit.org/junit5/docs/5.4.0-M1/api/org/junit/jupiter/api/support/io/TempDirectory.html):
> The temporary directory will be shared by all tests in a class when the annotation is present on a parameter of a @BeforeAll method or the test class constructor. Otherwise, e.g. when only used on test or @BeforeEach or @AfterEach methods, each test will use its own temporary directory.

I would expect a `@TempDir` constructor parameter to be treated like parameter of a `@BeforeEach` method, ie a new value for each test.


I'm not sure about the finer points of parameter resolving in JUnit, so maybe the current behavior is as intended. Reasons why I think a `@TempDir` constructor parameter should have a new value for each test:
1. [According to the User Guide](https://junit.org/junit5/docs/5.4.0-M1/user-guide/#writing-tests-test-instance-lifecycle)  "JUnit creates a new instance of each test class before executing each test method"
New instance -> new constructor call -> new value for constructor parameter (my expectation)
2. `@BeforeAll` = by default a static method = global state
`@BeforeEach` = instance method = single test state
constructor = instance bound = single test state
3. I normally want a clean temp directory for each test. Sometimes a shared temp directory might be needed, but it's the exception.
4. Isn't `@TestInstance(Lifecycle.PER_CLASS)` the normal way to share constructor state between all tests?

By the way, the Javadoc is really thorough. Very helpful!



# 32 this is title
## Feature request

The display name of the following is not very readable. Of course the real problem is that Java didn't make `DateTimeFormatter` implement `Format`; otherwise, I believe this would work out of the box.

It would be nice to provide java.time formatting for the display name. Might also be nice to allow custom formatters. 

```java
    @ParameterizedTest( name = "[{index}] {1}  is {2} from now {0}")
    @ArgumentsSource( Instants.class )
    void testIsLockedOn( Instant now, Instant time, Duration duration ) {
        assertThat( lockedRange.isLockedOn( time ) ).isEqualTo( SEC.equals( duration ) );
    }
```





# 33 this is title
Use cases:
- Launcher gives warning if a Specification (e.g. AllTestsSpecification) is not supported, so that user knows that their tests might not be picked up as expected.
- IDE/Launcher switches on features (e.g. Tagging) only if all/some registered engines support it.
- Launcher/IDE won't use features that break backwards compatibility

Potential capabilities to announce:
- Supported specifications
- Tagging
- Engine filters
- Support for opentest4j
- Custom events
- Supported API version (starting with 5.0)?

This feature needs both:
- A way for engines to declare their capabilities
- A way for users of launcher to find out about capabilities




# 34 this is title
This adds support for combining multiple TestTemplate providers
together, in a product style, so that an implementer can use the
benefits of multiple extensions together.

Issue: #1224

## Overview

This is a fix for #1224. I had some free time so I thought I would take a look at how hard it would be. This will almost certainly not work for everyone so I have made it opt-in with a new annotation, @CombineTestTemplates. This will allow those who need this feature to use it, and everything will be normal for others.

Using the Maven test sample as a quick test we get the following test output (happy to hear suggestions for better test names): 
![image](https://user-images.githubusercontent.com/1029558/93200151-f2b1e800-f73e-11ea-8c15-a5c863e1a099.png)

I have not yet had a chance to write test cases but I'm gonna have a crack at that later in the week if this seems interesting.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [x] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 35 this is title
I'm using Junit 5.4.1 and am experiencing a weird issue related to parallelism.

I have a set of Tests that I want to execute in parallel. 4 of these tests are tagged with the tag "main". Which I want to execute using maven. However I only want to execute 2 of them at the same time. Thus I configured jUnit 5 as follows:

`junit.jupiter.execution.parallel.enabled=true
junit.jupiter.execution.parallel.config.strategy=fixed
junit.jupiter.execution.parallel.config.fixed.parallelism=2`

This config works when I invoke the following mvn command:

`mvn test`

However, when i add the parameter to only execute the Tests tagged with main:

`mvn test -Dgroups=main`

ALL of the tests (meaning 4) tagged with "main" are executed in parallel, when only 2 should be executed at the same time. It seems that somehow, the parallelism count is ignored. Unfortunately I can't verify which setting is used by JUnit5 or if this bug is related to mvn surefire or Junit5

## Steps to reproduce

- Create a Test Suite with 5 or more Tests
- Tag 4 of them with a tag (e.g main)
- invoke mvn test -Dgroups=main


## Context

 - Used versions (Jupiter/Vintage/Platform): 5.4.1 Jupiter / no vintage / 1.4.1 platform
 - Build Tool/IDE: maven 3.6 surefire 2.22.1






# 36 this is title
@**Update**: _Now it works exactly like TestNG, which means if A depends on B, and B is disabled, then A is disabled as well_.

Hi everyone,

I am creating a pull request for this feature. It should work similar to TestNG (`@Test(dependsOn = ...)`) but it will not disable the test if some test fails. It just gives methods a priority like `@Order`.

It would be great if someone can give me some advice how to improve it.

Thank you :)



# 37 this is title
## Overview
I'm part of Arquillian team and I've been trying to implement either Arquillian Engine or Arquilian Extension for JUnit 5. Unfortunately, nothing is feasible for now. The Engine is a bigger issue. In case of extension, there is missing only one functionality. 

## Specific problem
One of Arquillian modes is running in-container tests - executing test methods/classes inside of a container (as part of a deployment). Unfortunately, currently there is no way to tell JUnit 5 where the test should be executed or to provide my own runner that would execute the test method either on a client or in a container. I can only skip the test methods or let them run locally.

## Possible solutions

### Custom ExecutableInvoker
The easiest solution would be having an SPI (eg. using service loader) that would load inside of the [TestMethodTestDescriptor](https://github.com/junit-team/junit5/blob/master/junit-jupiter-engine/src/main/java/org/junit/jupiter/engine/descriptor/TestMethodTestDescriptor.java#L60) a custom implementation of the `ExecutableInvoker` class (if none is provided, then the default would be used) and execute the method using the provided invoker.

### Custom runner for test descriptors
The previous solution is easy to do, but has one side effect - the method callbacks would be executed on both sides - on a client and inside of the container (as I would need to simulate everything inside of the container again). An advanced solution would be having a possibility to provide an invoker for every `TestDescriptor` separately.

For more information about my research see this issue: https://github.com/arquillian/arquillian-core/issues/137

## Related Issues

- #157 



# 38 this is title
When using a relative resource path with `@CsvFileSource` — for example, `"test.csv"` as opposed to `"org/exmaple/test.csv"` — the resource is resolved against the runtime type of test class.

This is valid approach until we use inheritance.  If it happens that we have a base class test and subclass located in different packages then, the subclass test fails with cannot find resource. It runs normally if I copy the resource under same package as subclass. Obviously this is not an issue when using full path resources.  

I think that when source file is resolved instead of using runtime class, the class that **declares** the method annotated with `@CsvFileSource` should be used.  

## Steps to reproduce

In order to reproduce we need 2 classes in different packages, let's assume base class Foo.

```java
package org.example.foo;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

public abstract class Foo {
    @ParameterizedTest
    @CsvFileSource(resources = "testEquals.csv",numLinesToSkip = 1)
    public void testEquals( String a, String b ) {
        Assertions.assertEquals(a,b);
    }
}
```

And then if we extend this class with Bar

```java
package org.example.bar;

import org.example.foo.Foo;

public class Bar extends Foo {
}
```

Then the Bar test fails, while being unable to locate resource. However if we place class `Bar` in `org.example.foo` package everything works fine.

## Context

The environment is jupiter-5.4 using gradle-5.4.1 with intelij idea 2019.2



# 39 this is title
## Status Quo

A `static` nested test class is currently treated identical to a top-level test class.

This applies to how it is executed and how it is displayed within the test plan hierarchy in IDEs, reports, etc.

Note that this in contrast to non-static nested test classes (i.e., `@Nested` test classes).

## Proposal

Treat a class (potentially itself a test class) as a _container_ for any `static` nested test classes. The _enclosing_ class could be either top-level or itself a static nested class.

This new treatment would alter where such static nested test classes show up in the test plan's "tree"; however, the manner in which such static nested classes are executed would not change, except that static nested test classes would now be guaranteed to execute after their enclosing test class.

## Further Considerations

Implementing the proposal would affect the SPI proposals for #162, since we would then need to be able to differentiate between static and non-static nested classes.

## Related Issues

- #162 

## Deliverables

- [ ] Decide if we want to implement the proposal.




# 40 this is title
We are migrating to JUnit 5 (from JUnit 4) and using the console launcher in combination with ant like described in https://github.com/junit-team/junit5-samples/blob/master/junit5-jupiter-starter-ant/build.xml

```
<java classpathref="test.classpath" classname="org.junit.platform.console.ConsoleLauncher" fork="true">
    <arg value="--scan-classpath"/>
    <arg line="--reports-dir build/test-report"/>
</java>
```

We cannot use junitlauncher-task because the output supports no @ParameterizedTest and so on.

After running the tests we generate a junitreport (with junitreport ant task) for the test run and a 
unitth report (http://junitth.sourceforge.net/) for the last 100 test runs.

The problem is that the LegacyXmlReportGeneratingListener generates one BIG TEST-nnn.xml for a few hundred test cases. This results in a junitreport without any classes & packages. Just one big list of all tests.
The "OLD" JUnit 4 Ant Task generated a TEST-nnn.xml for each test class. With this, junitreport & unitth can create readable reports. The report generated by LegacyXmlReportGeneratingListener is not readable and useless because it exists of one big "TEST" (it even looses the test class names).

## Steps to reproduce

Run

```
<java classpathref="test.classpath" classname="org.junit.platform.console.ConsoleLauncher" fork="true">
	<arg value="--scan-classpath"/>
	<arg line="--reports-dir build/test-report"/>
</java>
<junitreport todir="build/test-report" tofile="report.xml">
	<fileset dir="build/test-report">
		<include name="*.xml" />
	</fileset>
	<report format="frames" todir="build/test-report" />
</junitreport>
```

with multiple test classes. You just get one big TEST-junit-jupiter.xml instead of a TEST-nnn.xml for each class.

## Context

 - Used versions (Jupiter/Vintage/Platform): 5.5.1
 - Build Tool/IDE: Ant / ConsoleLauncher





# 41 this is title
If a test/lifecycle method has multiple parameters annotated with `@TempDir` or a test class has multiple fields annotated with `@TempDir`, the corresponding test class/method should fail in order to prevent user errors that stem from assuming them to be different directories.

## Deliverables

- [ ] Fail if a test/lifecycle method has multiple parameters annotated with `@TempDir`
- [ ] Fail if a test class has multiple fields annotated with `@TempDir`



# 42 this is title
Now there's no ability to track invocations of Before/After methods with TestExecutionListener, we need it there to be able to link test invocations with all corresponding fixtures and their timings in the reporting tool (Allure). Extensions are not entirely a solution for that, since we want to track events around fixture, one callback on the finish is not enough. And also registering such an extension via annotations everywhere would be quite clumsy.

## Related Issues

- #542



# 43 this is title
## Overview

Hello,

This change adds support for underscores in long numeric literals such as `700_000_000` in `CsvSource` and `CsvFileSource`.

This kind of notation was introduced in Java 1.7 to improve readability of long numbers (https://docs.oracle.com/javase/7/docs/technotes/guides/language/underscores-literals.html).
It is also available in Groovy and Kotlin.

This is the kind of thing that can be done with an `ArgumentConverter`, however it adds a lot of boilerplate code and loose the benefit of better readability / maintability.

Let me know if this is something that you would consider integrating to JUnit-Jupiter.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [x] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 44 this is title
I am working on an extension for tests to be able to react to failed tests or tests that end in exception by including a method annotated with `@OnFailure`.  

My specific high-level "requirement" is to be able to rebuild a Hibernate SessionFactory in these cases.  That method needs access to the SessionFactory to be rebuilt.  Actually it is a SessionFactoryScope class that manages a SessionFactory and exposes it via a ParameterResolver.  E.g.

```
@SessionFactory
public class MyTest {
    @Test
    public void theTest(SessionFactoryScope scope) {
        ...
    }
}
```

If this test fails, I'd like to be able to access the SessionFactoryScope to trigger it to release its SessionFactory and build a new one.  To do that it needs access to the SessionFactoryScope.  I.e.:

```
    @OnFailure
    public void rebuild(SessionFactoryScope scope) {
        ...
    }
```

ATM JUnit / Jupiter does not (AFAICS) allow access to registered ParameterResolvers nor any way to invoke such "extension methods" with resolved parameter arguments.

Seems like a generally useful feature.



# 45 this is title
could you please add a way to configure the number  of threads running @ParameterizedTest like testng dataproviderthreadcount



# 46 this is title
# Print all available properties

The `ConsoleLauncher` should provide an option `--print-default-properties`. That would print all generic JUnit Platform-related and also all engine-specific options to stdout.

## Sample output

```
##
## JUnit Platform
##

# Not applicable, yet.

##
## JUnit Jupiter
##

# Description, Link to User Guider and/or Javadoc
junit.jupiter.conditions.deactivate=...
# ...
junit.jupiter.execution.parallel.enabled=...
junit.jupiter.execution.parallel.mode.default=...
junit.jupiter.extensions.autodetection.enabled=...
junit.jupiter.testinstance.lifecycle.default=...

##
## JUnit Vintage
##  
...

##
## More properties from other test engines
##
...
```




# 47 this is title
Having `@TestInstance` on a toplevel test class changes the lifecycle of this class. 

My simple assumption would be, that the lifecycle of all nested `@Nested` test classes are changed accordingly. 
This is not the case, they also need to be configured.

While I find this behaviour irritating and would expect all classes down the hierarchy to share the lifecycle of the container class, I also can life with configuring it.

It would be important to document this however. 

Sometimes one notices, sometimes don't. 

Documentation can be in form of docs (apparently), but a warning log maybe helpful, too.

On a side note, current docs state:

> Used to configure the test instance lifecycle for the annotated test class. Such annotations are inherited.

Now, "inherited" of course refers to annotation inheritance with `@Inherited` which only applies to  real inheritance, but to a causal reader it could seem that an outer class actually inherits its lifecycle.




# 48 this is title
I understand that for memory/performance you probably want to recommend everyone use a Stream-returning method and `@MethodSource`, but given that an `@ArraySource` would be easier to use without having to convert all test data into methods, this would be a nice-to-have.



# 49 this is title
Thanks for providing the `junit-testkit` module, it has made testing extensions more straightforward and supported. I have been documenting some of my usability concerns with it while it is still in the experimental phase. These can most likely be split into multiple issues to decide what to do, but I thought I would put them here in aggregate to see how the team and other users feel about them.

For each section, I tried to demonstrate the problem with a code sample and offer up proposal idea for how I would like to see it behave. Take the proposals as an initial idea or to help frame the discussion around if my feedback is warranted or not.

### `assertStatistics()` failure output

The failure output for `assertStatistics()` hasn't been useful, and the feature kind of feels like a trap. Asserting on events produces more helpful output than when using the statistics.

#### Demonstration

The example below let's say that one of the assertions failed:

```kotlin
results.tests().assertStatistics {
    it.failed(0)
    it.succeeded(1)
}
```

The failure output is then:

```
Expected :0
Actual   :1
 <Click to see difference>

Expected :1
Actual   :0
```

Which doesn't help when debugging.

We have found ourselves instead just using the `assertThatEvents()` chaining as the events contain more information about why it succeeded/failed.

```kotlin
results.tests()
    .failed()
    .assertThatEvents()
    .isEmpty()

results.tests()
    .succeeded()
    .assertThatEvents()
    .hasSize(1)
```

#### Proposal

For us, we have tried to remove any usage of `assertStatistics` and only use the events as demonstrated above.

### AssertJ `Condition`s are cumbersome

`junit-testkit` is tightly coupled to AssertJ, so the best way to build additional assertions is to use  `Condition`. For example, there are already [`EventConditions`](https://github.com/junit-team/junit5/blob/672ef9a2c50a50c96fca791e17b1d876a5caa7f4/junit-platform-testkit/src/main/java/org/junit/platform/testkit/engine/EventConditions.java) and [`TestExecutionResultConditions`](https://github.com/junit-team/junit5/blob/672ef9a2c50a50c96fca791e17b1d876a5caa7f4/junit-platform-testkit/src/main/java/org/junit/platform/testkit/engine/TestExecutionResultConditions.java) that comprise a good chunk of the conditions you may use. However, chaining `Condition` together can be cumbersome and also creating new ones can be a bit ugly.

#### Throwable Demonstration

```kotlin
results.tests()
    .failed()
    .assertThatEvents()
    .hasSize(1)
    .haveExactly(
        1,
        finishedWithFailure(
            cause(
                allOf(
                    message("can't create configuration"),
                    instanceOf(RuntimeException::class.java)
                )
            )
        )
    )
```

I find using nested `Condition`s tough. This feels closer to Hamcrest territory, and it misses out on all of the built-in assertions and output that AssertJ already provides.

#### Report Entry Demonstration

Here is an example for testing for `ReportEntry` and the published values. There aren't built-in `Condition`s for `ReportEntry` yet in `junit-testkit`, so we have a few of our own.

```kotlin
import org.assertj.core.api.Condition
import org.junit.platform.engine.reporting.ReportEntry
import org.junit.platform.testkit.engine.Event
import org.junit.platform.testkit.engine.Event.byPayload
import org.junit.platform.testkit.engine.Event.byType
import org.junit.platform.testkit.engine.EventType

fun reportEntryPublished(): Condition<Event> {
    return Condition(
        byType(EventType.REPORTING_ENTRY_PUBLISHED),
        "report entry published event"
    )
}

fun reportEntryPublished(condition: Condition<ReportEntry>): Condition<Event> {
    return Condition(
        byPayload<ReportEntry>(ReportEntry::class.java) { condition.matches(it) },
        "report entry published event with result where %s",
        condition
    )
}

fun keyValuePairs(condition: Condition<Map<String, String>>): Condition<ReportEntry> {
    return Condition(
        Predicate { condition.matches(it.keyValuePairs) },
        "key value pairs where %s",
        condition
    )
}

fun hasEntry(key: String, value: String): Condition<Map<String, String>> {
    return Condition(Predicate { it[key] == value }, "has entry (%s, %s)", key, value)
}
```

Using those `Condition` implementations on `EngineExecutionResults`:

```kotlin

results.tests()
    .reportingEntryPublished()
    .assertThatEvents()
    .haveExactly(1, reportEntryPublished(keyValuePairs(hasEntry("thing_happened", expectedValue))))
```

I think this shows a few things:

* `Condition` types can be difficult to write
* Nested conditions can be tough to use
* No ability to use built-in AssertJ assertions like `MapAssert.hasKey`
* No (I don't see one) clear path to using other assertion libraries (use `.list()` or `.stream()` to get `Events`, but you still need to filter and combine them with `Condition`)

#### Proposal

My proposal would be to try and make most of the types in `junit-testkit` agnostic of assertion library and also add stronger typing. This will enable users to use whatever assertion library they want, reducing size of needed APIs (I think), and not having to provide custom assertion entrypoints like the `assertStatistics()` above.

For example, instead of having `enum EventType` and `class Event`, they could be combined for stronger typing - like `ReportingEntryPublished`

Then, AssertJ might look like:

```kotlin
assertThat(result.tests().events())
    .filteredOn { it is ReportingEntryPublished }
    .extracting<ReportingEntryPublished> { it as ReportingEntryPublished }
    .extracting<Map<String, String>> { it.keyValuePairs }
```

Possibly with some built-in helpers. Or, if AssertJ improves in this area (or I'm missing something), then users can use that version of AssertJ.

Or, when other assertion libraries like strikt/Kotlin are used:

```kotlin
expectThat(result)
  .get { tests() }
  .get { events() }
  .filter { it is ReportingEntryPublished }
  .map { it.keyValuePairs }
```

### `EngineExecutionResults` method chaining

I find the chaining to be a bit misleading and confusing at times as the method chaining is not strongly typed. The meaning when doing this is unclear

#### Demonstration

```kotlin
results.tests().containers().tests().failed().success().all()
```

```kotlin
results.tests().failed().failed().all()
```

#### Proposal

In the same theme as the proposal above, is to make `junit-teskkit` agnostic of assertion library and make results more strongly typed.

### Mocking dependencies in extensions

We often find ourselves wanting to "inject" behavior into our extensions to flex different behaviors in both them and the tests that would consume them.
This comes up especially when our extensions are used with external tools that we don't necessarily want to actually use during testing of that extension.
This is a little tough to do today due to the test engine constructs those extensions.

#### Demonstration

One of the incredibly ugly ways we have been doing this today is serializing/deserializing behavior we want by using `configurationParameter(String key, String value)`.
This works for us, so ¯\\\_(ツ)\_/¯.

We have also started to experiment using `@RegisterExtension` and providing some factory that retrieves the "mocked" instance/behavior we want.

#### Proposal

I don't have anything concrete here, more just food-for-thought, and open to suggestions for how to make this better.




# 50 this is title
Sometimes an extension should not be applied to nested containers, e.g. if the extension wants to open and close a resource just once per annotated container. It seems to me that currently any registered extension will also be applied to its children and I couldn't find a way to switch that off.

The workarounds I can think of require strange things like storing the first context object in order to compare the current context object with it. I might be missing something, though.

## Related Issues

- #506




# 51 this is title
Fixes #2104, along with corresponding test case.

## Overview

`ReflectionUtils.loadRequiredParameterType()` will now use class' classloader to resolve parameter type names into `Class` objects.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [ ] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 52 this is title
## Overview

**Feature request.** 

Console tasks are flagged with various statuses, such as `SUCCESSFUL` and `FAILED`.  These are mapped (as of #930, as `final` constants) to `GREEN` and `RED`.
These may seem like reasonable choices, until you encounter people who are red-green colour blind, or completely colour blind, who may be unable to distinguish between success and failure cases at a glance, unlike the fully sighted.
Worse, they may find it hard to read the text as high-contract text (green-on-black) is for them low-contrast dark-grey-on-black.

## Deliverables

JUnit5 should allow the user to customize the `Color.ansiString` that is associated with the various status values.  At a minimum, this should allow customize the status colour, but could include:
- [ ] a ANSI text attribute, such as `underline`, `bold` or `italic`.
- [ ] reverse video
- [ ] (forgive me) blink

This applies only to console output.
An IDE will apply its own colour/style to the various test statuses.





# 53 this is title
## Overview

Addresses : #1139

Adding a BeforeParameterizedTestExecutionCallback to be called prior to test method execution with a copy of the actual test arguments.

Points for discussion:

- Naming of the callback.
- Currently, the arguments are resolved twice via the DefaultParameterResolver.  It would be better to do this once (and pass a copy to the callback) but this would require a change to the ExecutableInvoker API.  I'm happy to do this but thought I'd wait from feedback first.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [ ] There are no TODOs left in the code
- [ ] Method [preconditions](http://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [ ] [Coding conventions](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#javadoc) and [`@API` annotations](http://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/meta/API.html)
- [ ] Change is documented in the [User Guide](http://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](http://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 54 this is title
I observed the following behavior as detailed below, where test methods using resource lock with READ mode appear to be unnecessarily sequenced.

Even though ResourceLock documents that `[...] the annotated element _may_ be executed concurrently with other test classes or methods [...]` (emphasis mine), the observed test executions are somewhat a surprise to me.

## Steps to reproduce

Consider the following MWE:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;


//@ResourceLock(value = "sharedResource", mode = ResourceAccessMode.READ)
class ResourceLockTest {
	private static AtomicInteger executingRead = new AtomicInteger();
	private static AtomicInteger maxRead = new AtomicInteger();

	@AfterAll
	static void afterAll() { System.out.println("max executing reads = " + maxRead); }

	@ParameterizedTest
	@MethodSource("ints")
//	@ResourceLock(value = "sharedResource", mode = ResourceAccessMode.READ)
	void test(final int arg) { rememberMax(); }

	@Test
//	@ResourceLock(value = "sharedResource", mode = ResourceAccessMode.READ)
	void test2() { rememberMax(); }

	@Test
//	@ResourceLock(value = "sharedResource", mode = ResourceAccessMode.READ)
	void test3() { rememberMax(); }

	@Test
//	@ResourceLock(value = "sharedResource", mode = ResourceAccessMode.READ)
	void test4() { rememberMax(); }

	@Test
//	@ResourceLock(value = "sharedResource", mode = ResourceAccessMode.READ_WRITE)
	void testWrite() { assertEquals(0, executingRead.get()); }

	private void rememberMax() {
		final int active = executingRead.incrementAndGet();
		maxRead.getAndUpdate(v -> v > active ? v : active);
		try {
			Thread.sleep(50);
		}
		catch (final InterruptedException e) {}
		executingRead.decrementAndGet();
	}

	private static IntStream ints() { return IntStream.rangeClosed(1, 100); }
}
``` 

### Results

* Baseline to check correct junit concurrency config, running with resource lock commented out: consistently results in _max executing reads_ of 8 (on my machine), and `testWrite` can fail. **Expected**.

* Enable ResourceLocks *on methods*:
    - normal test methods with READ run usually in parallel. **Expected**.
    - the parameterized test has consistently a max read of 1. **Correct, but unexpected**.

* Enable ResourceLock on class: consistently a max read of 1. **Correct, but very unexpected**.

Especially the last point I find surprising. With many test methods, it makes sense to move the lock to the class (and not have it on each method). Such change seems valid but results in degraded execution time.

## Context

junitJupiterVersion = '5.5.2'

```
Gradle 5.6.2
Build time:   2019-09-05 16:13:54 UTC
Revision:     55a5e53d855db8fc7b0e494412fc624051a8e781

Kotlin:       1.3.41
Groovy:       2.5.4
Ant:          Apache Ant(TM) version 1.9.14 compiled on March 12 2019
JVM:          12.0.2-BellSoft (BellSoft 12.0.2-BellSoft+11)
OS:           Mac OS X 10.15 x86_64
```

junit.platform.properties

```
junit.jupiter.execution.parallel.enabled = true
junit.jupiter.execution.parallel.mode.default = concurrent
junit.jupiter.execution.parallel.mode.classes.default = concurrent
junit.jupiter.execution.parallel.config.dynamic.factor = 1
```

## Deliverables

- [ ] Clarify if the current performance behavior of the built-in ResourceLock is intended 




# 55 this is title
## Overview

Currently, the target of `@ParameterizedTest` is constrained to methods. When creating technology compatibility kits, it would be awesome to be able to apply this (or a similar annotation) to the test class so that all tests in that class are parameterized the same way.

## Proposal

Rather than:

```java
class MyTest {
   @ParameterizedTest
   @ArgumentSource(...)
   void feature1() { ... }

   @ParameterizedTest
   @ArgumentSource(...)
   void feature2() { ... }
}
```

Something like:

```java
@ParameterizedTest
@ArgumentSource(...)
class MyTest {
   @Test // ?
   void feature1() { ... }
   
   @Test
   void feature2() { ... }
}
```

## Related Issues

- #871  
- #1141 




# 56 this is title
Support additional or alternate `--module-path` entries, similar to the already available `-cp` option:

https://github.com/junit-team/junit5/blob/master/junit-platform-console/src/main/java/org/junit/platform/console/options/AvailableOptions.java#L74-L80

## Use case

Given a directory `lib/` that contains all required modules and a _test_ module named `it`, this would allow the Console Launcher to be started like:

`java --module-path lib --module org.junit.platform.console --module-path build/test/modules --select-module it`

This enhancement is especially useful for 3rd-party tools, that make use of `"junit"` tool provider introduced via #2034 (related issue: #797).

```
var junit = ToolProvider.findFirst("junit");
int code = junit.run(..., "--module-path=build/test/modules", "--select-module=it");
```

### Work-around

Create the module path a-priori using `java` options ... and spawn a new JVM for each test run:

`java --module-path lib:build/test/modules --add-modules it --module org.junit.platform.console --select-module it`

## Deliverables

- [ ] Add option `--module-path` to [`AvailableOptions.java`](https://github.com/junit-team/junit5/blob/master/junit-platform-console/src/main/java/org/junit/platform/console/options/AvailableOptions.java)
- [ ] Parse passed values and create and use a custom [`ModuleLayer`](https://docs.oracle.com/javase/9/docs/api/java/lang/ModuleLayer.html) at runtime.



# 57 this is title
<!-- Start by telling us what problem you’re trying to solve. Often a solution already exists! Please, don’t send pull requests to implement new features without first getting our support. -->

While discussing [Sarek](https://github.com/SarekTest/Sarek/) with @kriegaex we discovered the need to initialize the Sarek agent was soon as possible. Right now, it uses a Jupiter/Spock extension to load, but as the Platform can execute multiple engines it would be possible for other engines to run earlier and load classes, that then couldn't be "unfinalized" by the agent.

A platform level hook that would run as early as possible would be the best solution, so that users wouldn't have to manually call the java executable with javaagent arguments.

## Deliverables

- [ ] ServiceLoader interface to initialize Agents, could be as simple as `interface AgentLoader { void install(); }` this should be calles as early as possible




# 58 this is title
## Short story:

For our test infrastructure to create test data, we must distinguish calls during the static initialization of each test class from calls during test instantiation for each test method.
This could be solved by the proposed `BeforeTestInstantiationCallback`.

## Long story:

When we write our tests, we want to restrict the data that have to be set explicitly to those that the specific test requires. All other properties are set randomly, but valid. Naturally using random data may introduce randomly failing tests, so we need the means to easily reproduce test failures that e.g. happen in the CI environment.
Reproducing such failures requires knowing the seed values for our random data when the specific test was executed. This is where we want to take advantage of a JUnit 5 extension. It has to store one seed value at the class level, for example if static constants are initialized using our random mechanism. In addition, it has to store the seed value at the instance level, for each test run. If a test should fail, the respective seed values must be reported in the failure message. If the failure is related to the use of random data, all this together allows us to reproduce it in any other environment. Example:

```java
private static final Address staticAddress = 
    createRandomAddress(); // determined by the class seed
 
private Address instanceAddress = 
    createRandomAddressBuilder() // determined by the instance seed
        .withStreet("some street")
        .build();
 
@Test
void someTest() {
    Address anotherAddress = 
        createRandomAddress(); // also determined by the instance seed
    // ...
}
```

We note the class seed in a `BeforeAllCallback`, which is the perfect place. The switch to using the instance seed however, has to be right before the test instance is created, to cover random data used for instance field initialization, which is a rather common use case in our tests.
Obviously, the `TestInstancePostProcessor` callback is too late for switching from the class seed to the instance seed. Currently we have an ugly workaround, where we check the stacktrace to switch to the instance seed, as soon as we detect a call from the test's constructor. If there are no such calls we switch to the instance seed in the `TestInstancePostProcessor` callback.

The proposed `BeforeTestInstantiationCallback` would be the natural place to make the required switch to the instance seed trivial.

Do you think, adding the `BeforeTestInstantiationCallback` would be harmful?



# 59 this is title
## Overview

Hi,
I found that when I write Parameterized tests in Kotlin with `@MethodSource` referred method from Kotlin class have to be placed in Companion object and marked with `@JvmStatic` annotation.
This PR make it possible to use regular companion object's method.
What do you think?
Thx,
Ivos

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [ x [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [x] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 60 this is title
## Overview

Given a test class annotated with `@TestInstance(PER_CLASS)` with `static` `@BeforAll` and `@AfterAll` methods, if the constructor for the test class throws an exception, these callback methods are currently not executed.

Technically there is no restriction why these would not run (since an instance of the test class is not required to execute `static` methods in that class), so it is a matter of design what the expected behavior here would be. 

 - On the one hand, having a `PER_CLASS` class failing on the constructor suggests a major problem that warrants aborting everything. Also why run `@BeforeAll` of `@AfterAll` when we have run no tests? 
 - On the other hand, this seems inconsistent with what JUnit Jupiter does for classes that are instantiated _per method_ where a failing constructor does not affect the execution of methods annotated with `@BeforeAll` or `@AfterAll`.  So I personally consider this as unexpected behavior.

This was discussed in #1460 and refers to point _b)_ in comment https://github.com/junit-team/junit5/issues/1460#issuecomment-395965906

## Deliverables

- [ ] Clarify what the expected behavior in this case is.
- [ ] Document the expected behavior in the User Guide
- [ ] Review if automated tests currently cover the expected behavior.




# 61 this is title
## Overview

This is an implementation of #1963, with a couple of other changes thrown in.

I created a new package in junit-platform-reporting called `org.junit.platform.reporting.console` and moved all the three listener class implementations into that package. I also had to remove a couple of the ancillary classes along with them that were used for configuring the listeners (`Theme`, `Color`), or for implementing some of their core functionality (`TreePrinter`). This part was fairly straightforward, and hopefully uncontroversial. The listener classes and those used for configuration were made public; the implementation classes were left package private.

In order to make the classes more user friendly, I added some overloaded constructors with default options and added some documentation. The documentation is based on my reading of the code - hopefully I didn't get it too wrong (in particular, if someone could check my comments about the relative merits & functionality of the `TreePrintingListener` vs `VerboseTreePrintingListener`, that would be appreciated).

I marked all of the newly publicized classes with the `@API` annotation, marking them as experimental as of 1.6.

Internally, the console listeners all had a flag `disableAnsiColors`. I have taken the opportunity to flip the polarity on this and called it `useAnsiColors`, as this is easy to do while the API is not public. The console executor still processes the command line the same way and takes care of the conversion.

Another changes was to move `LegacyReportingUtils` from `junit-platform-launcher` to `junit-platform-reporting`. Reasoning:

* It seems to belong more properly in that module rather than in the launcher module - it is a reporting tool, not a launching tool.
* The only place in the JUnit 5 source tree where it was actually used is in the reporting module (`LegacyXmlReportGeneratingListener`).
* The fact that this class was split and in the wrong package/module caused me a few headaches when I was trying to use it in an OSGi context.

Finally, I added a feature to `LegacyXmlReportGeneratingListener` so that you can override the behaviour as to when an xml file is generated. The original implementation would generate one file per root in the test hierarchy. The new feature allows you to override this so that you can (eg) produce one xml file per test class, or per other container level. This is a feature that I would have found useful for the Bnd JUnit Platform tester implementation. This feature is isolated to its own commit and if necessary could be hived off to its own PR.

Thoughts/comments/suggestions welcome!



# 62 this is title
I'm trying to run all JUnit5 test methods which are tagged as "Special" and NOT tagged with any other tags.  I'm trying to avoid the need to hardcode/discover the superset of all tags, just so that I can form an exclude tag expression to accomplish this.  It should be possible to form a tag expression that says: everything tagged ONLY with 'special' (i.e. the 'special' tag is present AND no other tags are present).



# 63 this is title
The clone of https://github.com/junit-team/junit5 takes a lot. It downloads ~500MiB+, and the resulting repository is full of various pdf files.

Here are the top consumers:

```
hash bytes path
fffea6e6616e 3812203 docs/5.5.1/user-guide/index.pdf
d3f697d9c019 3812203 docs/5.5.0/user-guide/index.pdf
30d099b3af05 3812203 docs/5.5.2/user-guide/index.pdf
6267c2a59eb1 3812011 docs/snapshot/user-guide/index.pdf
...
```

and so on.

It does impact both regular development experience (as everybody is used to just `git clone $url`), and it does impact GitHub Actions CI: it takes 1minute for the "checkout action".

Note: GitHub Action could probably be improved to skip `gh-pages` branch, however, the issue for humans would sill be there.

1) Are PDFs required? Could they be pushed somewhere else? Do all the snapshots need to be stored in the main repository?

2) Could you please consider the use of `noTimestamp` for the `javadoc`? It will avoid printing the timestamps, thus it would reduce the changes in the html files.
See https://github.com/gradle/gradle/pull/8619

Sample:
```kotlin
withType<Javadoc>().configureEach {
                (options as StandardJavadocDocletOptions).apply {
                    noTimestamp.value = true
```




# 64 this is title
I'm running a test suite in parallel which uses `@ResourceLock` on a few tests. Most tests don't use any resource locks. There are two tests which lock resource `X`. If the first test runs rather late, the second will have to wait for the first to finish, often being the last test being executed, while the other threads already finished and have nothing left to do.

It would be helpful if all tests with locking would be scheduled before any tests without locking. The workers can pick a lock-less test if there's nothing else. This should on average result in a shorter total execution time, as the blocking of lock-awaiting tests will happen while there are still other tests to be executed by other workers, instead of having a sequential test execution order at the end.



# 65 this is title
## Overview

JUnit 3 had "static Test suite()" method where you could create suites as you wish: e.g. first add one class, then another one repeated 100 times, then another one, etc. That's quite handy when you have unstable tests that also spoil some global state, and want to increase the probability of them failing.

JUnit5 has dynamic tests with similar possibilities, but it seems that currently it only allows to generate suites of test methods (via lambdas). It would be nice if it'd also be possible to add classes there, maybe even nested dynamic test generators (aka suites).

## Related Issues

- #744 



# 66 this is title
## Overview

Whenever a test case sets the thread context `ClassLoader`, the test runner thread keeps using that `ClassLoader` for the following tests. This causes failures when combined with Mockito and mocks of package private classes/interfaces.

## Expected Behavior

When the thread is reused to run another test, the context `ClassLoader` should be reset to the original one.

## Steps to Reproduce

To reproduce the problem I created this example repo: https://github.com/bacer-esteco/junit5-bug-report.

Just run the 'test' task.

This problem is reproducible using both Jupiter and Vintage (tried on version 5.4.0), launching the test both from Gradle 5.2.1 and IntelliJ IDEA 2018.3 (and previous).

## Related Issues

- #201
- #1688 



# 67 this is title
I am writing a test execution listener. A little extension for Junit5 framework. There is a necessity to know what class is used when running a particular test having TestIdentifier and TestPlan.

`((MethodSource) id.getSource().get()).getClassName(); `


Gives only the class, where a test is declared. But, that does not mean that it is run from declared class.

For instance a test can be run from a subclass.

Parsing results for TestIdentifier#getUniqueId() Can differ from case to case (single test for junit4, single test for junit5, dynamic test for junit5 , parametrized test for junit4, etc)

At this moment I did not find any possibility to do that.
Is there any reliable way to get class of an executed test ?

I asked that question here  
http://stackoverflow.com/questions/42781020/junit5-is-there-any-reliable-way-to-get-class-of-an-executed-test/42808147

Seems like that at the moment there is no reliable way to get class (classname) of an executed test method. 
If it is not really so. Suggest you providing this feature.







# 68 this is title
As noted in #1587, the JUnit 5 home page doesn't provide a link to the compiled JARs like JUnit 4's page did.  For the rare user that's not using a dependency management tool with defined repositories, this will give them a place to start their dependency hell.

## Deliverables

- [ ] Add a "Download JARs" link to the "Resources" section of https://junit.org/junit5/ that points to the latest release JARs.
- [ ] Add "Download JAR" links to the `README` in this repository.




# 69 this is title
## Overview

This is a WIP PR for #1309. Some documentation is _deliberately_ missed, because we haven't yet agreed on the approach to go with, and on some implementation details.

Feedback is welcome! Perhaps some of TODOs are better to be discussed in the [issue](https://github.com/junit-team/junit5/issues/1309), not in the PR.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#junit-contributor-license-agreement).

---
### TODO
- [ ] CsvSource & CsvFileSource (need to agree on requirements, see the issue).
- [ ] Consider lazy `Arguments#get` (a decorator) and more factory methods (depends on ^, see the [thread](https://github.com/junit-team/junit5/pull/1310#discussion_r170445795))
- [ ] Test description is preserved when arguments are stripped.
- [ ] Default `ParameterizedTest#name` and how it is expanded (need to agree on requirements, see the issue).

### Definition of Done

- [ ] There are no TODOs left in the code
- [x] Method [preconditions](http://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#tests)
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#javadoc) and [`@API` annotations](http://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/meta/API.html)
- [ ] Change is documented in the [User Guide](http://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](http://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 70 this is title
https://github.com/junit-team/junit5/issues/78 solved the problem for just Jupiter and (probably) Vintage. If other engines introduce the same all IDEs will have to adapt to each engine's naming of params and values.

I suggest to either:
- Choose config param name that is agnostic to engine. Currently it is `junit.jupiter.conditions.deactivate`.  This will also require to standardize the possible values which currently refer to class names in Jupiter/Vintage.
- Add dedicated property  in `ConfigurationParameters` e.g. `ConfigurationParameters.getDeactivatedConditions() : List<ConditionType>`.

Any other ideas?



# 71 this is title
I have a project with mixed junit 4 and junit 5 tests, one of junit 4 test method is disabled with @Ignore annotation. If there is no junit 5 in the classpath, then IDEA is able to run the test when explicitly selected, e.g. to ensure that it still fails, etc. When there is junit 5, IDEA pass launcher with the method name has no influence on the org.junit.vintage.engine.discovery.DefensiveAllDefaultPossibilitiesBuilder which creates ignoreBuilder. Would be cool if junit.conditions.deactivate would influence this or some other mechanism would be provided. 



# 72 this is title
## Steps to reproduce

Having some code running infinitely, but the timeout annotation(neither the class level nor testable method level) can interrupt the execution. Instead, the program hang forever. 

I was hoping it can behave like the `assertTimeoutPreemptively` to interrupt the running test method.

e.g. I have a class with just one single infinite running method:

```java
public class A {

    public void infinite() {
        while (true) {
            continue;
        }
    }
}
```

```java
	@Test
	@Timeout(1) // run at most 1 seconds
	void pollUntil() {
		A a = new A();
		a.infinite();
		assertEquals(1,1);
	}
```

## Context

 - Used versions: Jupiter 5.5.2




# 73 this is title
At the moment, the JUnit Platform properties are loaded from the first (and sole) resource named `junit-platform.properties` available via the `ClassLoader` resource-loading facility.

Internally, the JUnit Platform `Launcher` already supports by-passing this logic by providing an explicit location of a `junit-platform.properties` file or stream.

## Deliverables

- [ ] Introduce a new launcher system property, like `junit.platform.properties.location`, that lets users specify an alternate location of the JUnit Platform properties file to load.




# 74 this is title
## Overview

I'd like to know if the equivalent exists or is in the works to match `TestNG`'s suite XML file format. I asked on Stack Overflow and was directed by @marcphilipp to open a feature request for this. Here are the details from the [original SO post](https://stackoverflow.com/q/47938209/1478636):

I've been dynamically generating TestNG XML suites in a project I'm working on. In an effort to take some initiative in migrating to JUnit 5. The TestNG specification is [very easy to find](http://testng.org/doc/documentation-main.html#testng-xml), but I cannot find the equivalent for JUnit 5.

All I can find are references that a file or URI can be specified for test discovery. Either by [command line option or URI](http://junit.org/junit5/docs/current/user-guide/#running-tests-console-launcher-options) and again under the [configuring selectors section](http://junit.org/junit5/docs/current/user-guide/#running-tests-build-gradle-selectors).

Naively, I'd like to assume that it's just the `fully.qualified.package.ClassName#methodName` format because I can find this as an example in the [MethodSelector](http://junit.org/junit5/docs/current/api/org/junit/platform/engine/discovery/DiscoverySelectors.html#selectMethod-java.lang.String-). The [UriSelector](http://junit.org/junit5/docs/current/api/org/junit/platform/engine/discovery/DiscoverySelectors.html#selectUri-java.lang.String-) and [FileSelector](http://junit.org/junit5/docs/current/api/org/junit/platform/engine/discovery/DiscoverySelectors.html#selectFile-java.io.File-) don't show what the actually expected format of the document is supposed to look like.

## Related Issues:

- #744 



# 75 this is title
## Overview

This is a follow-up task for #436.


## Deliverables

- [ ]  Set the `consumers` attribute for `@API` declarations across the JUnit 5 code base.




# 76 this is title
## Overview

<!-- Please describe your changes here and list any open questions you might have. -->

Hello! 

I have attempted to fix issue #2381 

What I added: 

1. Details option now takes comma separated values now
2. Added a new mode called testfeed
3. Added unit tests for it
4. TestFeed prints according to https://github.com/junit-team/junit5/issues/2381#issuecomment-674025977

Questions: 

1. Are there colors you need there ? How should the coloring scheme should look like ? 
2. Should we print containers ? Like override testPlanExecutionStarted or dynamicTestRegistered ? 
3. Code needs feedback as I am not sure whether it looks as expected

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [ ] There are no TODOs left in the code
- [ ] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [ ] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 77 this is title
## Overview

The invocation index of a parameterized test is accessible for templating when setting the display name of the test.

When it comes to accessing the invocation index using `TestInfo` it is not possible as it looks like the `TestInfo` implementation for `@ParameterizedTest` is of the default type. I would expect to get an `RepetitionInfo` instance so that I can access the invocation index programmatically. 

## Related Issues

- #944
- #1139
- #1884




# 78 this is title
As it stands argument converters need to be applied (with `@ConvertWith`) either to a custom annotation (at least it looks like that; couldn't make it work) or to the argument. When the former is not an option (for example because you can't make it work :wink:), the latter quickly becomes repetitive.

An extension point that allows registering argument converters as the class and method level (much like parameter resolvers) would remedy this problem.

Beyond ease of use, this extension point would also enable creating more wholesome extensions which, applied to a test class, can register parameter resolvers, argument converters, post instance extensions, and more _all in one annotation_. It would also make it possible to do something like `@ConvertByCalling("fromString")` (either on class, method, or parameter), which would try to call a static method `fromString(String)` on the target type.

If you think this is a valuable feature, I'd like to take a shot at implementing it.



# 79 this is title
_On the last JUG I met @sormuras and he motivated me to participate for the first time by presenting a feature-request. So here it is._

**Motivation:**
When we write tests we do this mostly because of two reasons:

1. Avoid technical errors (like NPE)
2. Ensure our code fullfills the defined requirements / avoid functional errors

But as of today (_as far as I know_) the only way to "link" a test to a requirement is by using it's (displayed) name, for example putting the id of the requirement (_I'll call this "req-id" in the following lines_) in front of the name - like `req123_testSomethingInThisMethod`. I think you all agree that this is not a good way to show that this method is a test to ensure the requirement with the id `req123`.

**Suggestion:**
Therefore I would like to suggest do add a new annotation `@Requirement`.

This annotation should be used to show that a particular test is written to ensure the specific requirement. The annotation takes the req-id as a string parameter, e.g. (`@Requirement("REQ-123")`). In the test result this req-id is then published as an attribut of the test case. This allows tools which parse the result to show if all tests annotated with a given req-id have passed and therefore the requirement is fullfilled.

I don't see the need of making this annotation repeatable on a method. In my opinion each test method should only verify one aspect. I also don't see the need of using this annotation on class level as I in my opinion a test calls - especially for small methods - may contain technical and functional tests.

Maybe this can also be taken into the considerations about a standard test result format (https://github.com/ota4j-team/opentest4j/issues/9)

**Lookout:**

To be honest only printing an additional attribut containing the id of a requirment is only one part of a useful funcitonality to check if all requirements are fullfilled. As without a list of definied requirements the report only containts information about tests which are annotation with a requirment but the report (tool) doesn't know if there were tests to all requirements. While I'm quite sure the suggested annotation should be a feature of JUnit I'm not sure if the "linking functionality" is seen as one by the JUnit-Team. I'll make a short description of what I mean, then maybe it's more clear:

To compare a list of requirements to the list of test results a comparator needs an input of this list. So I see the need of some module which takes this list (e.g. a file, service call, etc.) as an input and compares it with the test results and then creates a report which shows the reader which requirements don't have test at all, or which tests of a given requirement have passed/failed.

But maybe this is just a second step and - as mentioned - maybe not even in focus of JUnit.





# 80 this is title
TL;DR: On `ArgumentAccessor`, implement `<T> T get(int, Class<T>, ArgumentConverter)` or `<T> T get(int, ArgumentConverter<T>)`

## Current situation

Say there's a parameterized test that uses `ArgumentAccessor` and wants to convert a single argument to a custom type. This doesn't work out of the box if that type has no suitable factory:

```java
@ParameterizedTest
@CsvSource({ "0" })
void testPointNorm_(ArgumentsAccessor arguments) {
	// "ArgumentAccessException: Argument at index [0] with value [0] and
 	// type [String] could not be converted or cast to type [NoFactory].""
	NoFactory nope = arguments.get(0, NoFactory.class);
	assertNotNull(nope);
}

static class NoFactory {
	NoFactory(int __) { }
}
```

## Proposal

Would be nice to convert that `String` to a `NoFactory`. If only there was some kind of converter... oh, wait: 😉

```java
@ParameterizedTest
@CsvSource({ "0" })
void testPointNorm_(ArgumentsAccessor arguments) {
	NoFactory yay = arguments.get(0, NoFactory.class, NoFactoryConverter.class);
	assertNotNull(yay);
}
```

(Using the converter manually is near impossible because it needs a `ParameterContext`.)

Now, if `ArgumentConverter` were generic in the returned type, `get` could even elide the type token:

```java
<T> T get(int, ArgumentConverter<T>);
```




# 81 this is title
Right now [release notes are combined](https://junit.org/junit5/docs/current/release-notes/index.html#release-notes). There is a number of issues with this approach:

* when using a custom `TestEngine` users don’t really care about JUnit changes, but care very much about platform changes;
* there is no per-version changes for platform components — for example, `junit-platform-launcher` was updated to `1.5.2` recently but there is no way to find out what was changed from `1.5.1`;
* relates to the previous point but it is a bit weird to see `5.x` and `1.x.x` together which is confusing for new people (it fades away once you start thinking about the platform and Jupiter / Vintage as different-level things).

Also, it might be useful to actually split all the documentation into two blocks — one is for the platform, another one for Jupiter / Vintage. I think a lot of people don’t really care about the platform since their user interactions are based around engines built on it.



# 82 this is title
## Overview

When trying to run a large number of dynamic tests the framework throws an out of memory error.

For the sake of simplicity, below is a sample test I ran.

```java
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DynamicNode;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestFactory;

import java.util.stream.IntStream;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.DynamicTest.dynamicTest;

class RunnerTest {

    @TestFactory
    Stream<DynamicNode> dynamicTestPerformance() {
        return IntStream
                .rangeClosed(1, 14_000_000)
                .mapToObj(num -> dynamicTest("Test " + num, () -> {
                    System.out.println("Running Test " + num);
                    assertEquals(num, -1);
                }));
    }
}
```

I have run this using both `ConsoleLauncher` and `maven-surefire-plugin` 2.21.0, but both approaches give the same problem. Below is the error.

```
Running Test 1019735
Running Test 1019736
Running Test 1019737
Jun 04, 2018 3:28:25 PM org.junit.platform.launcher.core.DefaultLauncher handleThrowable
WARNING: TestEngine with ID 'junit-jupiter' failed to execute tests
java.lang.OutOfMemoryError: GC overhead limit exceeded
	at java.util.Arrays.copyOfRange(Arrays.java:3664)
	at java.lang.String.<init>(String.java:207)
	at java.lang.StringBuilder.toString(StringBuilder.java:407)
	at org.junit.platform.engine.UniqueIdFormat.encode(UniqueIdFormat.java:148)
	at org.junit.platform.engine.UniqueIdFormat.describe(UniqueIdFormat.java:134)
	at org.junit.platform.engine.UniqueIdFormat$$Lambda$153/459296537.apply(Unknown Source)
	at java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:193)
	at java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1380)
	at java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:481)
	at java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:471)
	at java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:708)
	at java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)
	at java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:499)
	at org.junit.platform.engine.UniqueIdFormat.format(UniqueIdFormat.java:129)
	at org.junit.platform.engine.UniqueId.toString(UniqueId.java:205)
	at org.junit.platform.launcher.TestIdentifier.from(TestIdentifier.java:57)
	at org.junit.platform.launcher.core.ExecutionListenerAdapter.dynamicTestRegistered(ExecutionListenerAdapter.java:39)
	at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor$NodeExecutor.lambda$executeRecursively$0(HierarchicalTestExecutor.java:114)
	at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor$NodeExecutor$$Lambda$170/701141022.execute(Unknown Source)
	at org.junit.jupiter.engine.descriptor.TestFactoryTestDescriptor$$Lambda$216/133250414.accept(Unknown Source)
	at java.util.Optional.ifPresent(Optional.java:159)
	at org.junit.jupiter.engine.descriptor.TestFactoryTestDescriptor.lambda$invokeTestMethod$1(TestFactoryTestDescriptor.java:92)
	at org.junit.jupiter.engine.descriptor.TestFactoryTestDescriptor$$Lambda$210/1730173572.execute(Unknown Source)
	at org.junit.jupiter.engine.execution.ThrowableCollector.execute(ThrowableCollector.java:40)
	at org.junit.jupiter.engine.descriptor.TestFactoryTestDescriptor.invokeTestMethod(TestFactoryTestDescriptor.java:79)
	at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.execute(TestMethodTestDescriptor.java:113)
	at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.execute(TestMethodTestDescriptor.java:58)
	at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor$NodeExecutor.lambda$executeRecursively$3(HierarchicalTestExecutor.java:113)
	at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor$NodeExecutor$$Lambda$169/1268066861.execute(Unknown Source)
	at org.junit.platform.engine.support.hierarchical.SingleTestExecutor.executeSafely(SingleTestExecutor.java:66)
	at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor$NodeExecutor.executeRecursively(HierarchicalTestExecutor.java:108)
	at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor$NodeExecutor.execute(HierarchicalTestExecutor.java:79)
```

## Versions

- JUnit 5.2.0
- maven-surefire-plugin 2.21.0

## Use Case

I am writing a small application to find and report differences between two databases and am generating a dynamic test for each db row for comparison. 




# 83 this is title
## Overview

When analyzing the existing JUnit 4 ```TestRules``` in #343, I completely missed the point of the ```DisableOnDebug``` rule.  It's purpose is to disable the encapsulated rule when the JVM is in debug mode and it has nothing to do with which tests are selected for execution.

- (X) **Feature request.** I'd like to propose that there's an additional member added to the ```@ExtendWith``` annotation in the following form:

```
boolean disableOnDebug() default false;
```

This flag would conditionally allow one or more ```Extension```s to be disabled when the JVM is in debug mode.  Code using this feature might look something like:

```
@ExtendWith(WeldExtension.class)
@ExtendWith(StopwatchExtension.class, disableOnDebug = true)
public void testSomething() { ... }
```

## Deliverables

- [ ] Change the ```@ExtendWith``` annotation.
- [ ] Alter the Jupiter engine to ignore extensions during debug.




# 84 this is title
While working on an issue about parallel execution and for this I checked [synchronization docs](https://junit.org/junit5/docs/current/user-guide/#writing-tests-parallel-execution-synchronization) and was still unsure about **where** it is possible / needed / suggested to place the `@ResourceLock` and `@Execution(SAME_THREAD)` annotations. (_The current example only shows the test case, but it's also possible to place them at the annotations._)

@marcphilipp was so kind to answer this and I think the docs should be updated with these information, because I think they help for further understanding. So I quote his answers here:

> > 1. Annotation? What about repeatable - do they have to be at the singluar one or the plural ones?
> 
> If you use it as a meta-annotation on a `@Repeatable` annotation you should put it on both annotations due to the way annotation lookup works for repeatable annotations in `AnnotationSupport`.

> 
> > 2. Extension implementation? What about parameter resolvers etc.?
> 
> Both annotations need to be present or meta-present on test methods or classes. Thus, putting them on the extension implementation class won't help.


> > 3. At test class level? What about inner classes?
> 
> Both annotations take effect for the whole subtree, i.e. putting `@ResourceLock("foo")` on a top-level test classes means all test methods in that class, all `@Nested` classes and their tests methods, recursively, require that resource. Similarly, `@ExecutionMode(SAME_THREAD)` forces the whole subtree to use the same thread.



# 85 this is title
## Overview

- (X) **Feature request.**

When implementing a JUnit 5 extension to provide ```@Suite```, ```@BeforeSuite``` and ```@AfterSuite```, I had to create a new test engine that recreates a lot of the discovery mechanisms already provided by the Jupiter test engine.  Ultimately the test execution is delegated to a specified engine, so all this engine really does is alter the way discovery works.

There are currently no ```Extension``` points in the Jupiter API that interact with the discovery process - they're all focused on the contextual execution of the already discovered hierarchy.  I'd like to propose the following new Jupiter API types (but I'd be happy with the equivalent functionality in any form):

-   ```@TestContainer```
-   ```ContainerDescriptorFactory```

I'm picturing the ```@TestContainer``` annotation being used like this:

```
@TestContainer(MyContainerDescriptorFactory)
```

And the ```@Suite``` example I used as the basis for this request becomes a composed annotation like this:

```
@Retention( ... )
@Target( ... )
@TestContainer(SuiteFactory.class)
public @interface Suite
```

The ```TestDescriptorFactory``` would be a functional interface with the following method:

```
    void addTestContainer(TestDescriptor parent);
```

When called, this method would add one or more children to the parent ```TestDescriptor```.  There are a couple of beautiful (in my opinion) features of this design:

1.  A child ```TestDesciptor``` created by the factory can itself have an arbitrary test hierarchy, perhaps even by invoking other ```@TestContainer```s to help build the structure.
2.  At an arbitrary depth, ```@BeforeSuite/@AfterSuite``` become meaningless.  Every ```@TestContainer``` can simply execute ```@BeforeAll/@AfterAll``` callbacks at their own level in the test hierarchy and the set-up and tear-down is automatically nested correctly.
3.   It's not as inherently dangerous as the DiscoveryCallback described in #354 and implemented in #577.
4.  Building this into the existing ```HierarchicalTestEngine``` is trivial as it simply delegates the addition of child containers (and their contents) to the factory.

This also leaves me with a few questions:

1.   What happens in non-hierarchical test engines?
2.   How do engines that execute test concurrently (Surefire's default) make sure they don't multi-thread a hierarchy?
3.   Should ```@TestContainer``` be marked ```@Testable```?  I can argue both ways but I can see IDEs that inspect the source getting confused.

## Deliverables (this is a long-shot at being correct on the first pass)

- [ ] Add the `@TestContainer` annotation
- [ ]  Create the `ContainerDescriptorFactory`
- [ ]  Move the `TestDescriptor` interface to the `junit-jupiter-api` project

Also relates to #19.




# 86 this is title
## Motivation

With testing frameworks which consider test names as documentation/specification, the order of test results matters. IDEs and CIs should report all tests in the order they were written (not necessarily same as their execution order), especially if they are used for generating documentation.

For example see [Specsy's Fibonacci example](http://specsy.org/documentation.html#naming-tests) which has two tests ("The first two Fibonacci numbers are 0 and 1" and "Each remaining number is the sum of the previous two") whose names make sense only when read in the order they were written. This is also required by Cucumber and similar tools (assuming Cucumber features, scenarios and steps are represented as nested tests).
## Current state

AFAIK, currently JUnit 5 does not maintain the order of tests, because methods like `TestPlan.getChildren` return a `Set`. I hope that the test reporting order will be made a first-class citizen.
## Ideas for a solution

JUnit 4 maintained the test order by returning a `List` from `Description.getChildren`, but relying on a mutable class has its problems, and I'm not sure whether maintaining test order was a design goal or just an implementation detail in JUnit 4.

[Jumi](http://jumi.fi/) uses the [fi.jumi.api.drivers.TestId](https://github.com/orfjackal/jumi/blob/v0.5.437/jumi-api/src/main/java/fi/jumi/api/drivers/TestId.java) class to specify both test order and test identity using a "path", which is a list of integers.

A solution which I think would work for JUnit 5 is to combine its string-based `org.junit.gen5.launcher.TestId` with information about the order of tests. If each part of the unique ID (see #106) would have both `String name` and `int order`, and the unique ID would be a list of those pairs, then they would be easy to sort predictably: order firstly by `part.order`, secondly by `part.name`, thirdly by the next part. The `order` may be the same for all parts at the same level, in which case the `name` will determine the order (for example packages should be sorted like this). It would need to be discussed whether the order should affect the ID's equality; I have arguments against and for it.

This issue relates to #48 (scenario tests), but not directly to #13 (runtime order). My proposed solution relates to #106 and #68 (unique ID).




# 87 this is title
Hello, everyone! I'm just starting to contribute, so if I'm making any mistakes, please tell me how to do it right :)

## Overview
I'm enjoying using TestTemplateInvocationContextProvider in conjuction with @ExtendsWith and @TestTemplate - it's a powerful tool that helps to bring all test invocation configuration in one place, do some fine tuning without using TestBase classes. And it helps to avoid tons of annotations above test methods. All of which greatly increases readability and maintainability of the tests.

## Proposal
Introduce TestTemplateInvocationContextBuilder, which contains following methods:

- withDisplayName(String displayName)

self explanatory

- withDisplayNamePrefix(String displayNamePrefix)
- withDisplayNamePostfix(String displayNamePostfix)

this allows grouping of display names which makes them more readable 

- addExtension(Extension extension)

adds extension at the end of the extension list, which makes it first or last among others, depending on type 
[Docs reference](https://junit.org/junit5/docs/current/user-guide/#extensions-execution-order-wrapping-behavior)

- addExtension(int index, Extension extension)

adds extension at certain place in list of extensions to force certain order of execution

- addParameterResolver(Class<T> parameterType, T value)

syntactic sugar for adding ParameterResolver if test method parameters contains only one parameter with T type

- addParameterResolver(Class<T> parameterType, T value, String parameterName)

syntactic sugar for adding ParameterResolver if test method parameters contains one or more parameters with T type and they need to be distinguished.

- build()

returns TestTemplateInvocationContext with displayName and extensions

## Deliverables
Speeding up of test creation, ease of maintenance, increase in readability



# 88 this is title
## Overview

Adds test case for issue https://github.com/junit-team/junit5/issues/981.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [x] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 89 this is title
## Overview

I currently have a JUnit 4 based [custom `Suite`](https://github.com/xwiki/xwiki-rendering/blob/2e7af2e60fd6661ec48142324cd3fe10411fe0bc/xwiki-rendering-test/src/main/java/org/xwiki/rendering/test/integration/RenderingTestSuite.java#L78) which automatically registers new tests to the JUnit runner and which allows to write very simple tests:

```java
@RunWith(RenderingTestSuite.class)
public class IntegrationTests {
}
```

The custom suite reads `*.test` files found in the CL's classpath and generates dynamic tests from them.

I'd like to move this to JUnit 5, but I'm a bit stuck ATM since it seems the best approach would be to use some test factory or parameterized test, but this would require each of my tests to declare a test method with something like:

```java
class IntegrationTests {

   @TestFactory
   Stream<DynamicTest> renderingTests() {
           return RenderingTestSuite.generateStreamOfDynamicTests();
   }
}
```

I'd really like my tests to remain as simple as the following (and this without duplication):

```java
@ExtendWith(RenderingExtension.class)
public class IntegrationTests {
}
```

PS: I've also asked the question on [Gitter](https://gitter.im/junit-team/junit5?at=5b142454c712f5612555bfcc) (which contains additional details).

## Related Issues

- #371 



# 90 this is title
Similar to the existing `@CsvFileSource` used for `@ParameterizedTest` I would be looking to get access to the raw content of a file, or collection of files in a directory (based on file filters, etc) from one or more classpath resources via a proposed annotation like `@FileSource`.

This would allow a user to also apply custom converters to the retrieved files to convert them to domain specific models if needed.

To elaborate, suppose you have the following files in `src/test/resources`:

`01.json` containing JSON content:

```json
{
"name": "John Doe",
"age": 30
}
```

`02.yml` containing YAML content:

```
name: John Doe
age: 30
```

If I just want to test based on the raw strings of the file based inputs, I would do something like the following:

```java
public class ParameterizedFileSource {
     @ParameterizedTest
     // or also @FileSource(directory = "/") to read all files in directory
     @FileSource(files = ["01.json", "02.yml"])
     public void test(List<File> files) {
         assertThat(files.size()).isEqualTo(2);  // etc...
     }
}
```

However if I had some class `Person` for which the file represents, and some deserialization logic for it, I would like to have direct access to those objects as inputs to the tests:

```java
public class ObjectFixtureTests {
     @ParameterizedTest
     @FileSource(directory = "/")
     public void test(@ConvertWith(PersonConverter.class) Person person) {
          assertThat(person.name()).isEqualTo("John Doe"); //etc
     }
}
```

## Deliverables

- [ ] Functionality for new `@FileSource` annotation (with similar context to `@CsvFileSource`)
- [ ] Documentation on usage for new `@FileSource` annotation, with examples with/without converters
- [ ] Tests for the `@FileSource` annotation (with/without using converters as well)





# 91 this is title
## Overview

Add `expected` attribute to `@ParameterizedTest` and if present change default output to `[{index}] {input} ~> {expected}` (or similar).

## Status Quo

When writing parameterized tests it is common to pass in input data together with the expected output, e.g.:

```java
@ParameterizedTest
@CsvSource({ "I, 1", "II, 2", "V, 5" })
void testWithDisplayName(String roman, int arabic) { /*...*/ }
```

```
# display names
[1] I,1
[2] II, 2
[3] V, 5
```

This is nice, but can be improved by pointing out what is input and what is expected:

``` java
@DisplayName("Roman numeral")
@ParameterizedTest(name = "\"{0}\" should be {1}")
```

```
# display names
"I" should be 1
"II" should be 2
"V" should be 5
```

But... [can't somebody else do that](https://www.youtube.com/watch?v=YihiSqO4jnA&t=25s)?

## Proposal

Add an attribute `expected` to `@ParameterizedTest` that names the parameter holding the test's expected result:

```java
@ParameterizedTest(expected = "arabic")
@CsvSource({ "I, 1", "II, 2", "V, 5" })
void testWithDisplayName(String roman, int arabic) { /*...*/ }
```

If `expected` is present, Jupiter makes the new placeholders `{input}` and `{expected}` (a partition of `{arguments}`) available for naming tests and switches the default from name from `[{index}] {arguments}` to `[{index}] {input} ~> {expected}`. (All names and formats are up for bike-sheds!)

## Related Issues

- #1309 



# 92 this is title
For example, a test method that spawns asynchronous tasks in the background may not have completed when the execution the test method completes. It would therefore be beneficial if such a test method had a mechanism for signaling that it was complete in order for _verify_ methods to be invoked at the appropriate time.




# 93 this is title
Pending the resolution of #2095:

I would also like to see us leverage the OSGi capability mechanism in some way to define dependency relationships between test bundles and test engine bundles. That way, the resolver can help with making sure that the correct engines are included in the set of run bundles. For example, the test engine bundle could declare something like this:

```
Provide-Capability: org.junit.platform.engine;
    org.junit.platform.engine.id='junit-jupiter;version="[5.5.1]"' # By convention, make this == TestEngine.getId()
    version=5.5.1
```
...then the test bundle can declare its dependency on a particular versions of particular engines by (eg) the following:

```
Require-Capability: org.junit.platform.engine;
   org.junit.platform.engine.id='junit-jupiter;version="[5.5,6)",junit-vintage;version=4.12,org.myorg.my-test-engine;version=1.0'
```

Now the resolver will be able to ensure that the test bundles are paired with the correct versions of the correct test engines. The syntax might need a bit of tweaking (I'm not an expert in this area), but hopefully the idea makes sense.

## Deliverables

- A specification for the capability namespace for test engine implementations.
- Add the appropriate `Provide-Capability` metadata to the `junit-jupiter-engine` and `junit-vintage-engine` OSGi manifests.




# 94 this is title
## Goal
Add support for some level of parallelization inside the Junit Vintage engine.
Ideally the level of configuration should be similar to maven surefire parallel options.

## Why
When including junit 5 tests in a project containing junit4 tests the natural path is to use junit 5 platform with the jupiter and vintage engines.

However this causes problem with parallelization. 
In a project with Junit4 tests only maven surefire level parallelization works fine. (See https://maven.apache.org/surefire/maven-surefire-plugin/examples/fork-options-and-parallel-execution.html).
For Junit5 tests the jupiter engine [parallel execution works great](https://junit.org/junit5/docs/snapshot/user-guide/#writing-tests-parallel-execution). 

However when a project contains a mix of Junit4 and Junit 5 there is no great way to configure parallelism:
* Surefire parallel does not work with Junit Platform Provider so it's not an option
* Surefire forkCount or gradle maxParallelForks can be used but:
  * It's not available at all when using  [tycho surefire](https://www.eclipse.org/tycho/sitedocs/tycho-surefire-plugin/plugin-info.html)
  * It introduces some memory and execution time overhead compared to surefire parallel or junit 5 parallel.
  * It provides less control than Junit 5 parallel execution options.
* Combining fork + junit 5 parallel execution leads to more parallel executions than expected  when executing junit 5 tests because parallelization is done at two level.

Another option is to configure two distinct test tasks one for junit 4 using surefire parallel and one for junit 5 but it kind of defeats the point of junit platform.

## Deliverables

- [x] Not sure




# 95 this is title
The word `container` is used more than 50 times in the current Guide https://junit.org/junit5/docs/current/user-guide/

This term wasn't used in JUnit4 and is new to many JUnit users. In the development industry we have just too many different containers to leave this to "common sense" understanding.

Please just add the definition of JUnit5 "container" in the User Guide. 



# 96 this is title
Actual:
The sources/javadoc JARs on maven only contain the manifest information, but are missing the real information.

Expected:
I would expect the files to contain the sources and javadocs of all the classes delivered in junit-platform-console-standalone-1.3.0.jar

Rationale:
The standalone JAR offers an easy way to migrate an old JUnit 3/4 code base to JUnit Jupiter.
But without Javadoc and/or Java sources a lot of important information how to perform the migration (e.g. deprecation notes) is harder to access.

The can easily be seen if you have a look at the artefact list:
http://central.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.3.0/




# 97 this is title
## Overview

Validation errors (e.g., for invalid `@BeforeEach` method declarations) should not abort the entire discovery phase. Instead the _discovery phase_ should continue, with the error tracked and reported during the _execution phase_. 

## Areas of Applicability

- invalid `@BeforeAll`, `@AfterAll`, `@BeforeEach`, and `@AfterEach` method declarations
- invalid `@Test`, `@TestFactory`, `@RepeatedTest`, and `@ParameterizedTest` method declarations (see #2244)
- invalid `@Nested` test class declarations (see #1223)
- _blank_ display names supplied by the user, as discussed in #743
- exceptions thrown by test engines, as discussed in #750
- unresolvable unique IDs, as discussed in #210
  - note, however, that a TestEngine should not report a unique ID as unresolvable if the unique ID does not apply to the particular TestEngine (see #1026 ).
- non-static test class declaration (see #2311)

## Proposals

1. Allow engines to track errors by creating a special type of `TestDescriptor` such as an `AlwaysFailingTestDescriptor`, `DeadOnArrivalTestDescriptor`, or `ErrorReportingTestDescriptor`.
    - Tracked errors for such a corresponding `TestDescriptor` could then be thrown as an exception during the execution phase instead of executing the corresponding container or test.
2. Introduce a new property in `TestDescriptor` that signals an error that was encountered during the _discovery phase_.
3. Pass a _reporting object_ from the `Launcher` into each `TestEngine` to report errors.
    - See https://github.com/junit-team/junit5/issues/242#issuecomment-294301875

## Related Issues

- #121 
- #210 
- #743 
- #750 
- #835
- #876  
- #949 
- #971 
- #1026 
- #1074 
- #1223
- #1944
- #2244
- #2311

## Deliverables

- [ ] Introduce a mechanism that allows validation and configuration errors to be _tracked_ during the test engine discovery phase and then thrown or reported during the execution phase.
- [ ] Use the new mechanism to replace the current ad hoc use of logging and transparent defaulting as a work-around.
  - Search for `TODO [#242]` within the code base.
  - See https://github.com/junit-team/junit5/issues/750#issuecomment-294296045
- [ ] Determine where else the new mechanism can be used and apply it.
- [ ] Revisit the results of #835 and update the code accordingly by tracking such errors instead of just ignoring such incorrect usage.
- [ ] Revisit the changes made in #971 and determine if it makes sense to move the look-up of lifecycle methods back to the constructor of `ClassTestDescriptor`.
  
  



# 98 this is title
## Overview

In Mockito, we want to support injection of multiple parameters. To that end, we have to check for a multitude of acceptable annotations and then later act on that annotation. This issue appeared when working on https://github.com/mockito/mockito/pull/1503 which had to add a new annotation (`@Captor`) besides our `@Mock` injection-capabilities.

The author of the PR [wrote a CompositeParameterResolver](https://github.com/mockito/mockito/blob/d88929cf338b1acc51d3072b14a01378934394b2/subprojects/junit-jupiter/src/main/java/org/mockito/junit/jupiter/resolver/CompositeParameterResolver.java) which would support this usecase. However, it feels like this kind of solution should live in JUnit, rather than being Mockito-specific. I would suspect that other projects will run into this problem (eventually).

Therefore, I would like to request a JUnit-official implementation for the use-case of composing various resolvers into a single parameter resolver, that then can be used in the extension.

## Related Issues

- #1802 

## Deliverables

- [ ] A means to compose multiple parameterresolvers together, such that an extension can provide a list of resolvers and pass that automatically in `resolveParameter`.




# 99 this is title
JUnit 5 cannot produce correct .xml report file.

While executing task `junitPlatformTest`:

```
:junitPlatformTest                                                           
cze 23, 2016 7:31:03 PM org.junit.platform.launcher.core.ServiceLoaderTestEngineRegistry loadTestEngines
INFO: Discovered TestEngines with IDs: [junit-jupiter]
Could not write XML report: D:\project\build\test-results\junit-platform\TEST-junit-jupiter.xml
javax.xml.stream.XMLStreamException: java.nio.charset.MalformedInputException: Input length = 1
        at com.sun.xml.internal.stream.writers.XMLStreamWriterImpl.writeAttribute(XMLStreamWriterImpl.java:553)
        at org.junit.platform.console.tasks.XmlReportWriter.writeTestcase(XmlReportWriter.java:122)
        at org.junit.platform.console.tasks.XmlReportWriter.writeTestsuite(XmlReportWriter.java:83)
        at org.junit.platform.console.tasks.XmlReportWriter.writeXmlReport(XmlReportWriter.java:66)
        at org.junit.platform.console.tasks.XmlReportWriter.writeXmlReport(XmlReportWriter.java:58)
        at org.junit.platform.console.tasks.XmlReportsWritingListener.writeXmlReportSafely(XmlReportsWritingListener.java:100)
        at org.junit.platform.console.tasks.XmlReportsWritingListener.writeXmlReportInCaseOfRoot(XmlReportsWritingListener.java:93)
        at org.junit.platform.console.tasks.XmlReportsWritingListener.executionFinished(XmlReportsWritingListener.java:87)
        at org.junit.platform.launcher.core.TestExecutionListenerRegistry$CompositeTestExecutionListener.lambda$executionFinished$23(TestExecutionListenerRegistry.java:63)
        at java.lang.Iterable.forEach(Iterable.java:75)
        at org.junit.platform.launcher.core.TestExecutionListenerRegistry.notifyTestExecutionListeners(TestExecutionListenerRegistry.java:37)
        at org.junit.platform.launcher.core.TestExecutionListenerRegistry.access$100(TestExecutionListenerRegistry.java:26)
        at org.junit.platform.launcher.core.TestExecutionListenerRegistry$CompositeTestExecutionListener.executionFinished(TestExecutionListenerRegistry.java:63)
        at org.junit.platform.launcher.core.ExecutionListenerAdapter.executionFinished(ExecutionListenerAdapter.java:56)
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:93)
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:51)
     rg.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:43)
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:124)
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:84)
        at org.junit.platform.console.tasks.ExecuteTestsTask.executeTests(ExecuteTestsTask.java:60)
        at org.junit.platform.console.tasks.ExecuteTestsTask.lambda$execute$6(ExecuteTestsTask.java:52)
        at org.junit.platform.console.tasks.CustomContextClassLoaderExecutor.invoke(CustomContextClassLoaderExecutor.java:33)
        at org.junit.platform.console.tasks.ExecuteTestsTask.execute(ExecuteTestsTask.java:52)
        at org.junit.platform.console.tasks.ConsoleTaskExecutor.executeTask(ConsoleTaskExecutor.java:38)
        at org.junit.platform.console.ConsoleRunner.execute(ConsoleRunner.java:51)
        at org.junit.platform.console.ConsoleRunner.main(ConsoleRunner.java:36)
        Suppressed: java.nio.charset.MalformedInputException: Input length = 1
                at java.nio.charset.CoderResult.throwException(CoderResult.java:281)
                at sun.nio.cs.StreamEncoder.implWrite(StreamEncoder.java:285)
                at sun.nio.cs.StreamEncoder.write(StreamEncoder.java:125)
                at java.io.OutputStreamWriter.write(OutputStreamWriter.java:207)
                at java.io.BufferedWriter.flushBuffer(BufferedWriter.java:129)
                at java.io.BufferedWriter.close(BufferedWriter.java:265)
                at org.junit.platform.console.tasks.XmlReportsWritingListener.writeXmlReportSafely(XmlReportsWritingListener.java:101)
                ... 20 more        
Caused by: java.nio.charset.MalformedInputException: Input length = 1
        at java.nio.charset.CoderResult.throwException(CoderResult.java:281)
        at sun.nio.cs.StreamEncoder.implWrite(StreamEncoder.java:285)
        at sun.nio.cs.StreamEncoder.write(StreamEncoder.java:125)
        at java.io.OutputStreamWriter.write(OutputStreamWriter.java:207)
        at java.io.BufferedWriter.flushBuffer(BufferedWriter.java:129)
        at java.io.BufferedWriter.write(BufferedWriter.java:230)
        at com.sun.xml.internal.stream.writers.XMLStrerImpl.writeXMLContent(XMLStreamWriterImpl.java:1486)
        at com.sun.xml.internal.stream.writers.XMLStreamWriterImpl.writeAttribute(XMLStreamWriterImpl.java:547)
        ... 25 more                

Test run finished after 744 ms     
[       666 tests found     ]
[         0 tests skipped   ]
[       666 tests started   ]
[         0 tests aborted   ]
[       666 tests successful]
[         0 tests failed    ]
```

The XML looks like 2 line file (which has 116 368 chars):
![image](https://cloud.githubusercontent.com/assets/6240704/16313657/78ea03d0-397a-11e6-8e2e-7c247fa78ba6.png)

and finishes in unexpected way:
![image](https://cloud.githubusercontent.com/assets/6240704/16313687/a7b2c562-397a-11e6-8a0a-9936b287fa0f.png)




# 100 this is title
So I have a parameterized test, and each parameter is a List of Beans where each bean represents a line in a csv file (opencsv). What I want for the actual "parameterized name" is the filename.

I'm thinking something like return 

```java
Arguments.of( Named.by(file.getName()), new ArrayList<>() );

@ParameterizedTest
@ArgumentsSource(MyArgumentsProvider.class)
void test( List<AlgorithmVerification> verifications )
```

Obviously the workaround is to simply pass it as the first parameter and include it as an unused argument. I just have a dislike of unused arguments.

```java
@ParameterizedTest
@ArgumentsSource(MyArgumentsProvider.class)
void test( String filename, List<AlgorithmVerification> verifications )
```



# 101 this is title
## Overview

_(tl;dr: I feel JUnit might be easier to use for developers if things failed more explicitly when developers make certain specific mistakes. I've got a suggestion for how to do this that I'd like to discuss. I'm willing to do much of the work if it's the right approach and if the submission would be acceptable.)_

While using JUnit 5 (excellent work by the way!) I've encountered some situations where an innocent developer error can cause tests not to be executed in ways that are easy to miss.

- When using the `@Nested` annotation with a static inner class, the class (and any tests declared within it) are not executed. No error messages of any kind that I can see are emitted. This situation is difficult to spot by visual inspection of the code, and because the tests aren't marked as skipped, catching the mistake is difficult in a larger project — one would need to take a very close look at test totals, read test results by hand, etc.

- When using the JUnit 5 platform with JUnit 4 tests, if the JUnit Vintage dependency isn't on the classpath but JUnit 4 somehow is, tests can easily get skipped. I know that this sounds theoretical but it happened to some colleagues of mine just before Christmas. It took us an hour or so to debug (once they figured out that it was happening) because it wasn't obvious to them from looking at the gradle build file or output what the cause was. Even worse, the IDE (IntelliJ in this case) was still happily running the JUnit 4 tests, so it wasn't immediately obvious that something wrong was even happening until somebody took a close look at build script output on the CI server.

There are some commonalities between these problems:
- They both involve things that developers need to know, but sometimes don't.
- When a mistake happens, it's difficult to diagnose just by visual inspection unless you are aware of the thing you need to know.
- It can be easy to miss these mistakes if you aren't consciously looking for them.

It might be annoying to people in the short term, but
ultimately I think JUnit would be safer for developers if test runs explicitly failed in both of these conditions, rather than just not executing tests.

## Proposal
I propose fixing this by causing a test run to fail whenever either of the above mistakes is made. I took a brief look at JUnit's source code, and the idea that occurred to me is some new Resolver implementations that detect each scenario and cause tests (or just the build) to fail.

I've got some ideas on how to programatically find the error conditions for each resolver:
- For the "non static `@Nested` class" case, it should just be inverting the existing predicate (org.junit.jupiter.engine.discovery.predicates.IsNestedTestClass) and checking for inner classes annotated with the `@Nested` that don't match the predicate.
- The Junit 4/5 case is a bit harder, but it should be possible to find methods annotated with `org.junit.Test` when the JUnit vintage classes are not on the runtime classpath. We could use reflection to check for the existence of the `org.junit.Test` annotation and JUnit vintage so no extra dependencies are be needed. This resolver could shorrt circuit into a no-op in cases where JUnit4 isn't present on the classpath, or JUnit4 and JUnit Vintage are both on the class path.

What wasn't immediately obvious to me was the best way for resolvers like this to cause tests (or just the whole build) to fail. I could really use some advice on this part.

## Feedback requested:
- Is guarding against these issues a desirable feature?
- If so, is writing some new Resolvers the best way to go about it?
- If so, what's the best way for a Resolver or associated Descriptor to emit an error message and fail the build?
- If I develop a patch of appropriate quality for this, is it likely to be accepted?

## Deliverables
If all of the above is acceptable then I imagine that it might be best to open a separate PR for each case when I've got something workable.

Any and all feedback gratefully requested!



# 102 this is title
Hello there, and thanks for JUnit! :wave:

My team has recently migrated to JUnit 5, and previously we were previously using the [junit-hierarchicalcontextrunner](https://github.com/bechte/junit-hierarchicalcontextrunner) for nested tests.
One big difference from that one is that on JUnit 5 the native nested tests require that nested classes be annotated with the `@Nested` annotation.

We've now been using it for a few weeks, and my team found that sometimes we forget to add an `@Nested` annotation to an inner class.

This leads to a test suite that is _apparently_ green, but that in reality is missing tests, and is hard to spot.

Would it be possible to either:

* add a validation that would warn us that we could possibly be missing `@Nested` -- by for instance detecting that a nested class had JUnit annotations on it but would not be executed

* have a mode/option/top-level annotation for executing tests in nested classes without needing an explicit `@Nested`

Thanks! :pray: 

## Related issues

* #242
* https://stackoverflow.com/questions/54107409/how-do-detect-missing-nested-annotations/54130013




# 103 this is title
## Overview

When a `ParameterResolutionException` is thrown, the message currently states something similar to the following.

```
No ParameterResolver registered for parameter [java.lang.String arg0] in executable [org.example.MyTests(java.lang.String)].
```

In the above example, the "executable" is actually a constructor, but many developers might not recognize that immediately based on the somewhat cryptic error message.

In addition, the cause of the above exception is that the developer introduced a constructor in a test class that accepts a parameter for which there is no registered `ParameterResolver`. However, many developers do not know what a `ParameterResolver` is or what the error message is intending to convey.

## Deliverables

- [x] Replace "executable" with "constructor" or "method" in all error messages used in `ParameterResolutionException`s.
- [ ] Consider introducing further contextual information when a test class introduces a constructor that accepts arguments for which there is no registered `ParameterResolver`.
  - for example, by providing a hint for how to fix the problem.





# 104 this is title
## Status Quo

This issue picks up where #319 left off.

The user guide of a release should point to GitHub sources and Javadoc of the corresponding release tag.
## Deliverables
- [ ] Investigate if it's possible to determine if the commit we're building has a release tag using the [versioning plugin](https://github.com/nemerosa/versioning).
- [ ] If the release tag or branch is available via the `versioning` plugin, set the `releaseBranch` project property accordingly.




# 105 this is title
## Overview

Users who are familiar with JUnit 5 will still rely on the javadocs displayed by their IDE for reference information.  One example of where the javadocs could be more helpful is the ```@CsvSource``` annotation.  The user's guide has an extremely useful paragraph for this ```@ArgumentSource``` that describes how to use single quotes as well as how to produce null values versus empty String objects.  The table referenced in the users guide would definitely be a bonus.

Note that I'm not proposing the users guide move completely into the javadocs (e.g. Mockito) and that I recognize this adds housekeeping complexity to ensure that the javadocs and users guide don't contradict each other.  But in thinking about how I program with libraries I know well, there are definitely still javadoc pages that I rely on (e.g. the Java SE Pattern and SimpleDateFormat javadocs)

- (X) **Feature request.** Update the javadocs for types that commonly require looking at reference information.  This request could be limited to the ```junit-jupiter-api``` and ```junit-jupiter-params``` packages which would be sufficient to provide documentation to both test and extension writers.

## Deliverables

- [ ] CsvSource
- [ ] CsvFileSource
- [ ] ...

*Prompted by the discussion on #1014*



# 106 this is title
## Overview

> This is a draft because the PR is still missing crucial parts like tests and documentation. However, the implementation itself is mostly finished and I would like to gather feedback. 😊

Using `junit-jupiter-params` in Kotlin is awkward for many reasons and why I propose the addition of a programmatic, functional API to JUnit that will make `junit-jupiter-params` obsolete for many use-cases.

```kotlin
private class JunitJupiterParamsKt {
    /** @see dataProvider */
    @ParameterizedTest
    @MethodSource("dataProvider")
    fun isPalindrom(candidate: String) {
        assertEquals(candidate.reversed(), candidate)
    }

    companion object {
        @JvmStatic
        fun dataProvider(): Stream<Arguments> =
            Stream.of(
                arguments("mum"),
                arguments("dad")
            )
    }
}
```

Above is an extremely simple test written in Kotlin that makes use of `junit-jupiter-params` but there are many issues with it (ordered from top to bottom as they occur in the file above):

- We have to add the kdoc block with an `@see` reference to the actual method source to please IntelliJ and stop insisting on `dataProvider` being unused (this is a total IDE issue that can be solved but it is a real issue).
- We need to add two annotations to our function to enable the parameterization.
- We need to add an annotation with a string value matching the name of the data provider function, keeping it up-to-date manually.
- We need to define the signature as we expect things to arrive, however, there are no compile-time checks that actually ensure that the arguments of the data provider are actually compatible with our signature. We might have been running tests for five minutes already until we run into the issue at runtime.
- We need to create a companion object where we collect all data providers. This means that the data providers will end up far away from the spot where they are actually being used. Forcing us to scroll and jump around to find everything that makes up a test case.
  
  There is the ability to change the test instance lifecycle to class that lifts this requirement. However, many users do not know about it and I also had to learn that tests can be written in ways that make it impossible to switch.
- We need to annotate each data provider with `@JvmStatic`.
- We need to add `Stream<Arguments>` as the return type (or add `!!` at the end of the stream construction and each `arguments` call) to disable warnings about missing nullability information.
- We need to use `Stream` which is not very idiomatic in Kotlin.

Here is the very same parameterized test written with the programmatic API that I am proposing:

```kotlin
private class JunitJupiterTestBuilderKt {
    @TestFactory fun isPalindrom() =
        testOf(case("mum"), case("dad")) { 
            assertEquals(it.reversed(), it)
        }
}
```

It solves all mentioned issues, better yet, it is also much faster than the version from above because there is no runtime discovery necessary and nothing needs to be wired by JUnit since its all done by the language. We can have all these benefits in Java too:

```java
class JunitJupiterTestBuilderJ {
    @TestFactory
    TestCases isPalindrom() {
        return testOf(
            it -> assertTrue(StringUtils.isPalindrom(it)),
            caseOf("mum"),
            caseOf("dad")
        );
    }
}
```

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 107 this is title
Using traditional JUnit structure there are no problems executing a single isolated test.

```kotlin
class Suite {
    @Test a() = Unit
    @Test b() = Unit
 }
```
In the snippet above re-running `b` in isolation usually is not an issue in such IDEs as IJ. There is a green arrow nearby which executes a single method. This is great.

However, using non-traditional DSLs, similar to RSpec does not provide such a luxury.

```kotlin
@Testable
class Suite : Spec({
    context("A") {
        it("works") {
        }
    }
    context("B") {
        it("works") {
        }
    }
})
```
Since both `context` and `it` are not method declarations but invocations there are no IDE hints to execute a single `B`. 

In RSpec this is achieved using skipping (`xit`, `xcontext`) and focusing (`fit`, `fcontext`).

Lucky for us there is the `org.junit.platform.engine.support.hierarchical.Node.SkipResult` API which can be used to provide skipping. Unfortunately there is nothing for focusing. Of course it is possible to implement focusing manually going over the `TestDescriptor` tree, finding if there are focused nodes, then go over the whole tree again and mark all non-focused nodes as skipped. However, I thought maybe there is a chance to provide a mirror API for `Node.SkipResult` like `Node.FocusResult`. 

WDYT? Is there some other way to achieve focusing using JUnit Platform? Or maybe hint the IDE that it is possible to execute a single node?



# 108 this is title
## Overview

Original title: "Support ParameterResolver registration via @ResolveWith on parameter"

While experimenting with parameter resolvers I realized that they can not be applied like argument converters can, i.e. by annotating the parameter directly. This complicates their application and implementation if they are "annotation based".

An example is the `@Mock` proof of concept. The resolver has to be applied to the test method or class and because of that has to check the individual parameter for the presence of the `@Mock` annotation. This indirection causes unnecessary complexity for implementers and users of the extension.

## Original Proposal

I propose an annotation similar to `@ConvertWith`, e.g. `@ResolveWith`, that takes precedence over all registered parameter resolvers. It does not need a `supports` method because it is assumed to support the parameters it is applied to. If it turns out during `resolve` that that's not the case, the test should be aborted by an exception.

With this mechanism, `@Mock` (and I am planning to write something like `@Random`) would get simpler to use because they only need to be applied in one place.

More broadly, I think parameter resolvers and argument converters are conceptually very similar and the API would hence improve considerably if both would operate similarly as well. In that regard I already opened #853, which proposes an extension point to register converters at the method and class level. Together with this issue, the two aim to align both mechanisms.

If there is interest in this, I would give it a shot, preferably together with #853.

## Related Issues

- #416
- #497 



# 109 this is title
Currently, child nodes are forced to `SAME_THREAD` execution if the parent has any locks. 

If the parent only has `READ` locks, then it would be valid for the child nodes to execute concurrently. This would also alleviate the issues of #2038 and we partly have this logic already for the isolated execution of #2142 

## Deliverables

- [ ] Don't force child nodes to `SAME_THREAD` execution if only `READ` locks are acquired




# 110 this is title
I am trying to create a `Stream<DynamicTest>` from a set of different sources (read: different types) and the way that generics work makes this quite cumbersome. Here's an example from Spring HATEOAS:

```java
Links links = Links.NONE;
Link link = Link.of("/foo");
		
List<NamedLinks> sources = Arrays.asList(
		NamedLinks.of("via varargs", links.and(link)),
		NamedLinks.of("via Iterable", links.and(Arrays.asList(link))),
		NamedLinks.of("via Stream", links.and(Stream.of(link))));

return DynamicTest.stream(sources.iterator(), NamedLinks::getName,
		it -> assertThat(it.links.getRequiredLink(IanaLinkRelations.SELF)).isNotNull());
```

The test is supposed to verify that *different parameter types* (here: some object, an `Iterable` of objects, and a stream) handed to the `Links.and(…)` method lead to a certain result. Ideally, I would like to treat those as sources but that would just hand in the common supertype to the `ThrowingConsumer`, so that I cannot call `links.and(…)` anymore as those expect the concrete types. To work around this limitation I call the method beforehand and end up with `Links` consistently but am then unable to produce test names in the second parameter as I cannot distinguish the individual `Links` instances anymore.

I created `NamedLinks` myself to be able to already eagerly bind a name to use in the setup of `Dynamic.stream(…)` but I wonder if that could be made available by JUnit OOTB providing a simple value type `NamedSource<T>` that exposes a name and source `T`and an overload of `DynamicTest.stream(Stream<NamedSource<T>> sources, ThrowingCallable<T> callback)`.



# 111 this is title
Many a times when a particular test is a failing once in a while (i.e. not consistently), I use the `@org.junit.jupiter.api.RepeatedTest` with a relatively high number like `10`:

```
@RepeatedTest(10)
```
and trigger the tests to try and reproduce the issue. Some of these 10 runs will fail (as expected). However, the only reason I used the `@RepeatedTest` was to reproduce a failure and once that failure has occurred, I'm not really interested in running the remaining number of "count" that was passed to it.

Would it be a good idea to introduce something like `stopOnFailure` attribute (which can be set to `true`, but defaults to `false`) to this `@RepeatedTest` so that it considers the `value` count as the maximum number of times to run the test and if `stopOnFailure` is set to `true` then stops as soon as the first run within those 10 runs fails?



# 112 this is title
Migrating my Tests from JUnit 4 got stuck because my productive code (not test code) contains a class that MUST be loaded with the system/bootstrap class loader (the code is quite complex).

JUnit Jupiter seems to scan all classes and loads them with the current classloader. The latter is a problem for me, because an already loaded class shadows the one which is loaded later on (in the test) by the system classloader (meaning that the test operates on a different class than the rest of the program).

Maybe it would be better to do classpath scanning in a separate classloader (and reload only those classes that were qualified by the scanner).

If you are interested in an example I will prepare a branch in my github project to contain only the classes that provoke this error.



# 113 this is title
## Overview

The `XmlReportWriter` in the `junit-platform-console` currently generates XML that is compliant with the de facto standard for JUnit 4; however, this XSD is very limiting and does not support many of the features of the JUnit Platform.

## Goals

Define a new XML report schema that supports the features of the JUnit Platform.

The following is only a partial list of features needed beyond the JUnit 4 de facto standard.

- unique IDs
- display names
- tags
- test sources
- custom reporting entries
- nested test classes
- skipped vs. aborted execution

## Additional Considerations

- Provide a mechanism for converting between the JUnit 4 XSD and JUnit Platform XSD (e.g., via XSLT).
- Provide a JSON based format compatible with the XML format.

## Related Discussions

- https://github.com/ota4j-team/opentest4j/issues/9
- #86 
- #350 
- #372 




# 114 this is title
## Overview

A comment in [SPR-15366](https://jira.spring.io/browse/SPR-15366?focusedCommentId=157903&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-157903) has made me aware of a potential bug in JUnit Jupiter's handling of `@BeforeEach` methods with regard to the `ExtensionContext` supplied to a `ParameterResolver` registered for an enclosing test class when executing a test method within a `@Nested` test class.

Specifically, Jupiter invokes a `@BeforeEach` method in the enclosing class using the `ExtensionContext` for a `@Test` method in a `@Nested` class. The same may be true for other lifecycle callback methods as well, but I have not investigated that.

## Analysis

It would appear that the cause of this behavior is due to a combination of how `ClassTestDescriptor.invokeMethodInExtensionContext(Method, ExtensionContext, ExtensionRegistry)` and `TestMethodTestDescriptor.invokeBeforeEachMethods(JupiterEngineExecutionContext)` operate. The latter invokes each synthesized `BeforeEachMethodAdapter` using the `ExtensionContext` for the current test method instead of supplying the `ExtensionContext` for the context in which the method is declared. Consequently, if a `ParameterResolver` is asked to resolve a parameter for a `@BeforeEach` method in an enclosing class and the resolver needs the test class (or information tied to the test class via annotations) to resolve the parameter, then the resolver gets the test class for the currently executing `@Nested` test class when invoking `extensionContext.getRequiredTestClass()`.

However, this _behavior_ does not appear to apply to the invocation of `TestInstancePostProcessor` implementations as can be seen in `TestInstancePostProcessorTests`.

Similarly, the behavior is different for a `ParameterResolver` applied to the constructor of an enclosing class for the currently executing `@Nested` test class.

## Deliverables

- [ ] Determine which lifecycle callback methods are affected by this.
  - [ ] Ensure appropriate tests are in place for `@BeforeAll`
  - [ ] Ensure appropriate tests are in place for `@AfterAll`
  - [ ] Ensure appropriate tests are in place for `@BeforeEach`
  - [ ] Ensure appropriate tests are in place for `@AfterEach`
- [ ] Ensure that extensions registered and invoked for a given lifecycle callback are supplied an appropriate `ExtensionContext`.




# 115 this is title
Resolves #1919.

## Overview

Add a `ClassFileMethodOrderer` that orders test methods according to the order in the class file (which is the same as the order in the source file)

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](http://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [x] Change is documented in the [User Guide](http://junit.org/junit5/docs/snapshot/user-guide/)
- [ ] Change is documented in the [Release Notes](http://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass



# 116 this is title
As requested in https://github.com/spockframework/spock/pull/1207/files#r511436053 

## Deliverables

- [ ] make `org.junit.platform.engine.support.hierarchical.DefaultParallelExecutionConfiguration` public




# 117 this is title
## Overview

Sample module descriptor: `src/test/java/module-info.java`
```java
open module test {

  // Read exported JUnit Jupiter API
  requires org.junit.jupiter.api;

  // Prevent "unknown enum constant Status.STABLE" + "org.apiguardian.api.API$Status not found" warnings
  requires org.apiguardian.api;

  // Prevent "org.opentest4j.TestAbortedException not found" when using `Assumptions`
  requires org.opentest4j;
}
```




# 118 this is title
Hello,

this is not a bug, but instead is a feature request. With latest JUnit 4.x I want to compare `BigDecimal` 
values so I do the following:

```
assertThat("1x125$ price - 1x25$ discount - 1x20$ voucher + 1x10$ delivery = 90$", new BigDecimal("90.0"),
                   comparesEqualTo(cart.getTotalPrice().getNumber().numberValue(BigDecimal.class)));
```

unfortunately this prints the following in the command line:

```
Expected: a value equal to <1.1E+2>
     but: <90.0> was less than <1.1E+2>
```

I'm not sure if it is a problem in hamcrest or junit but I will just log it here so that it doesn't get lost. Please make sure with the latest JUnit 5 that you use `toPlainString()` or some other way to correctly format `BigDecimal`.




# 119 this is title
Test templates are a great way to create extensions that generate test cases per method. If an extension wants to generate suites of tests per class, though, this is not easily possible. I propose to implement a container template extension point that functions similarly to test template:

* it defines the number of executions `n` - but in this case per container, which makes Jupiter work all its "execute tests in this class" magic not once but `n` times
* each invocation is called with a context, which most importantly contains the index of the current iteration
* additional extensions can be registered

It might make sense to consider whether other extensions should be allowed to easily access the container invocation context, maybe from the `ExtensionContext` they already receive. (Thinking about that, wouldn't it make sense to do the same for test templates, i.e. give `ExtensionContext` a method that returns the invocation context?)

Where parameterized test methods were the canonical example of how to use test templates, theories would be the canonical example for container templates. With this extension point the theories extension would use reflection to find out how many parameters were defined and then have the class be executed so many times, each time dropping a different set of parameters into all test methods:

* `a = 0; b = 0`
    * `testAddition(a, b)`
    * `testSubtraction(a, b)`
* `a = 0; b = 1`
    * `testAddition(a, b)`
    * `testSubtraction(a, b)`
* ...

## Related Issues

- #878 
- #1141 
- #723 
- #1239
- #2092
  



# 120 this is title
I have a project where it would be nice to be able to plug in arbitrary test listeners to get the output that you want.

It would be nice to be able to use the listeners in the console package to optionally produce nicely-formatted test output. Unfortunately, I can't do this easily because the classes are package private, so I have to use reflection if I want to use them.

It seems a pity that JUnit 5 now has all this nice modularity to facilitate plug-and-play code re-use like this, but the opportunity to re-use it is thwarted by hiding it away in a private package.



# 121 this is title
In order to speed up builds on GitHub Actions: https://github.com/marketplace/actions/cache

### Jobs

- [ ] Linux (uses `container: junitteam/build:latest`)
- [ ] Windows
- [ ] Mac OS
- [ ] Coverage (uses `container: junitteam/build:latest`)
- [ ] Publish Snapshot Artifacts
- [ ] Update Snapshot Documentation



# 122 this is title
`CsvArgumentProvider` does not support configuration of the underlying `CsvParser` by univocity.

## Steps to reproduce

```java
    @ParameterizedTest
    @CsvSource(
        "        SW34NT,SW34NT   "
    )
    fun test(one: String, two: String) {
        assertThat(one).isEqualTo(two)
    }

```

This should **NOT** work, or at least the behavior should be configurable:

CsvParserSettings.ignoreTrailing/LeadingWhitespace = false

## Context

 - Used versions (Jupiter/Vintage/Platform): 5.7.0
 - Build Tool/IDE: IntelliJ

## Deliverables

- [ ] ...




# 123 this is title
## Overview

Since Eclipse Photon supports separation of test source sets in the classpath, we should configure that within the Gradle build.

## Workaround

The following workaround has been proposed by @howlger until Gradle and Buildship properly support the new feature in Eclipse.

```groovy
apply plugin: 'eclipse'
eclipse.classpath.file.whenMerged {

	// separate output folders required to set the 'test' attribute
	entries.find { it.path == 'src/main/java' }.output = 'bin/main'
	def testSrc = entries.find { it.path == 'src/test/java' }
	testSrc.output = 'bin/test'
	testSrc.entryAttributes['test'] = 'true'

	// libraries visible for test sources only?
	entries.forEach { entry ->
		def entryIn = { it.find { file(entry.path).equals(it) } }
		if (entry.kind == 'lib') {
			entry.entryAttributes['test'] =
				entryIn(configurations.testRuntimeClasspath) &&
				!entryIn(configurations.runtimeClasspath)
		}
	}
}
```

## Related Issues

- [Gradle Issue](https://github.com/gradle/gradle/issues/4802#issuecomment-396165166)
- [Buildship Issue](https://github.com/eclipse/buildship/issues/689)

## Deliverables

- [ ] Configure test source sets in the Eclipse classpath.
- [ ] Update [contributor guidelines](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md) to suggest the use of Eclipse Photon.




# 124 this is title
It would be sweet if the `assertNotNull(actual:)` method returned the object that is passed into it back out as a non-null type.

This would help with writing JUnit 5 tests in Kotlin big time and avoid the need to force unwrap properties like this:

```
assertNotNull(myObject?.myProperty)
val myProperty = myObject!!.myProperty
assertEquals("Foo", myProperty.someOtherProperty)
```

Instead, tests like the above code snippet could be simplified to the following:

```
val myProperty = assertNotNull(myObject?.myProperty)
assertEquals("Foo", myProperty.someOtherProperty)
```

Note that the [kotlin-test](https://kotlinlang.org/api/latest/kotlin.test/) library already offers this mechanism in its [assertNotNull](https://kotlinlang.org/api/latest/kotlin.test/kotlin.test/assert-not-null.html) method, and Apple offers a similar [XCTUnwrap](https://developer.apple.com/documentation/xctest/3380195-xctunwrap) method in their [XCTest](https://developer.apple.com/documentation/xctest) framework.



# 125 this is title
Jupiter's `@TempDir` does not allow the configuration of custom file systems. It would be nice if it would.

A key motivation for me to open this issue is that custom file systems are the only thing that Pioneer's `@TempDir` can do that Jupiter's can't. Since Jupiter's is quite a bit more powerful than ours now, we'd like to remove our extension (this also prevents confusion for users), but we don't feel comfortable doing that as long as there's a feature we offer that you don't.

If Jupiter isn't fundamentally opposed to such a feature, we could implement it and open a PR.



# 126 this is title
This is a follow-up on #138 where we used `new AssertionFailedError(message, expected, actual)` to pass `expected` and `actual` for `assertEquals`, `assertSame`, and `assertNull`.

However, we should consider passing `unexpected` and `actual` for
- [ ] `Assertions.assertNotEquals`
- [ ] `Assertions.assertNotSame` (hmm... `unexpected == actual` in this case)
- [ ] `Assertions.assertNotNull` (just `actual`?)




# 127 this is title
## Overview

As discussed in the [Gitter channel](https://gitter.im/junit-team/junit5?at=5b7717ae796f7b601d576d2e), users would greatly benefit from detailed documentation and examples regarding how to make use of `CloseableResource` in the `ExtentionContext.Store`.

## Deliverables

- [ ] Document how to use `CloseableResource` in various scenarios, potentially via examples in the `junit5-samples` repository.




# 128 this is title
I am contributing to a bunch of JUnit 5 extensions that rely on a form of field injection to achieve their goals.

Field injection, if done in a `@BeforeEach` callback, works well for both parallel and sequential testing. It also works well for both `PER_CLASS` and `PER_METHOD` lifecycle semantics. However, it does not work very well if you're combining parallel execution with `PER_CLASS` lifecycle semantics, as the parallel execution threads for each test method will each inject their own instances into the single test class instance and clobber each other, interfering with the tests running in other threads. In such situations, it is necessary to inject into a `ThreadLocal` container instead.

Accordingly, I would like my extensions to be able to give fail-fast-and-loud behaviour in these circumstances - throwing an `ExtensionConfigurationException` if it finds it is being asked to run in an environment where it is being asked to run `CONCURRENT` and `PER_CLASS` at the same time, and informing the user that they should use a `ThreadLocal` in such a case.

The problem: the `ExtensionContext` that is passed to the extension's lifecycle methods has a method for telling you which class instance lifecycle mode is in force. However, it doesn't seem to give you a way to easily determine the execution mode. This can be inferred by manually examining the annotations and the global execution mode, but I feel that this breaks encapsulation a little bit - I don't have to do the same for the lifecycle.

## Deliverables

Method `ExecutionMode getExecutionMode()` in `ExtensionContext`.

Possibly a pair of methods - one that returns the value annotated on the class, and one that returns the *actual* execution mode in force (taking into account any global setting). The latter would be more directly useful to my use case.



# 129 this is title
## Overview

Currently, AFAICT, no static analysis or formal verification tools are being used to catch bugs in the JUnit 5 code base. IMO it would be a sensible thing to do to start using a combination of various tools now, so that when we reach GA and proceed beyond GA, we are less likely to be inundated by preventable bug reports and/or suffer from potential security issues.

I'd personally suggest a combination of the following tools, but I'm more than happy to discuss the merits of the tools listed and to discuss other tools which aren't listed or that I may have not thought of:
- [error-prone](http://errorprone.info/)
- [SpotBugs](https://spotbugs.github.io/) or FindBugs
- SpotBugs/FindBugs plugins:
    - [fb-contrib](http://fb-contrib.sourceforge.net/)
    - [find-sec-bugs](http://find-sec-bugs.github.io/)
- PMD
- [Checker Framework](https://checkerframework.org/) (specifically for [nullness formal verification](https://checkerframework.org/manual/#nullness-checker))

## Deliverables

- [ ] A number of agreed-upon static analysis and/or formal verification tools are adopted.




# 130 this is title
`LauncherDiscoveryListeners` can now be registered via Java's `ServiceLoader`
mechanism in addition to those
passed as part of each `LauncherDiscoveryRequest` and the default one.

## Overview

<!-- Please describe your changes here and list any open questions you might have. -->

The idea of this PR is to enable registering `LauncherDiscoveryListener` through an SPI. I am creating this PR in order to hear the opinion of the JUnit Team. Is something like this acceptable for you? If it is I am going to add add the documentation and finish whatever needs to be finished from your feedback.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [ ] There are no TODOs left in the code
- [ ] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [ ] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 131 this is title
## Goals

Support running suspend test in JUnit Jupiter:

```kotlin
class Kit {
    @Test 
    suspend fun foo() {
        delay(1000) // suspend call
        assertEquals(1, 1)
    } 
}
```

Currently, such test can be written this way:

```kotlin
class Kit {
    @Test 
    fun foo() = runBlocking {
        delay(1000) // suspend call
        assertEquals(1, 1)
        assertThrows { /* ... */ } 
        Unit // test should return void, but `assertThrows` returns `Throwable`, so `foo` returns `Throwable` too 
    } 
}
```

Also, will be nice to provide `CoroutineScope` through params, or as receiver in extension:

```kotlin
class Kit {
    suspend fun foo(scope: CoroutinesScope) {  /* ... */  } // (1)
    suspend fun CoroutinesScope.foo() {  /* ... */  } // (2)
}
```
1 and 2 actually the same on bytecode level. `suspend` is optional.

And finally, support for `runBlockingTest`:

```kotlin
class Kit {
    suspend fun foo(scope: TestCoroutinesScope) {  /* ... */  }
    suspend fun TestCoroutinesScope.foo() {  /* ... */  } 
}
```

## What can be done currently

`ParameterResolver` can be used to provide stubs for `Continuation`, `CoroutineScope` and `TestCoroutineScope`. These stub arguments can be replaced with real arguments in invocation.

## Problems

Current extensions points not enough to implement this feature as extensions, since:

1. **Discovery**. Jupiter discovers tests that returns `void`, but `suspend fun` returns `Object`;
2. **Invocation**. `InvocationInterceptor` in 5.5-M1(SNAPSHOT) don't providing mechanism to override actual invocation, only to decoration of existing invocation. Conversion of `method` to `kotlinFunction`, and then executing using [`callSuspend`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect.full/call-suspend.html) is necessary to execute `suspend fun`.

Also, my [slides](https://ruslan.ibragimov.by/pages/cv/speaker/kotlin-night-kiev-2019-junit.pdf) about this topic.



# 132 this is title
## Overview

Although current use of `ClassLoaderUtils.getDefaultClassLoader()` works for the most common class loading scenarios, it is not always appropriate to default to using the thread context `ClassLoader` (TCCL) when loading user types via reflection.

This issue is inspired by the issues discussed in #805 and serves as an umbrella issue for potential class loading issues across the platform.

## Related Issues

- #201 
- #805 

## Comparison to class loading in Spring

If we take inspiration from the Spring Framework, we can see that `org.springframework.util.ClassUtils.forName(String, ClassLoader)` accepts a user-supplied `ClassLoader` and falls back to the "default ClassLoader" only if the supplied `ClassLoader` is `null`. For loading services, Spring does not use Java's `ServiceLoader` mechanism but rather its own `SpringFactoriesLoader` which performs the same task as Java's `ServiceLoader` but with explicit control over which `ClassLoader` is used. Note that `SpringFactoriesLoader` delegates to `org.springframework.util.ClassUtils.forName(String, ClassLoader)` to actually load the service class.

## Initial Analysis

JUnit does not necessarily need the flexibility of `SpringFactoriesLoader`, but for certain scenarios we will likely have to supply a custom `ClassLoader` instead of relying on the "default ClassLoader" which currently is typically the thread context ClassLoader (TCCL).

Supplying `getClass().getClassLoader()` is likely a viable option. However, we should not change the implementation of `ClassLoaderUtils.getDefaultClassLoader()`. Rather, we should simply use it less often and then only as a fallback.

FWIW, we actually did have the foresight to create `org.junit.platform.commons.util.ReflectionUtils.loadClass(String, ClassLoader)`, but... we never supply it anything other than the default ClassLoader. 😉 

## Use Cases to Investigate

The following use cases should be investigated to determine how best to look up the `ClassLoader` to use.

- `TestEngine` loading in `ServiceLoaderTestEngineRegistry`
- `TestExecutionListener` loading in `ServiceLoaderTestExecutionListenerRegistry`
- Jupiter `Extension` loading  in `ExtensionRegistry#registerAutoDetectedExtensions`
- Additional classpath entries in `ConsoleTestExecutor#createCustomClassLoader`
- `ClasspathScanner` configuration/instantiation in `ReflectionUtils`
- `ReflectionUtils#loadClass(String)`

## Deliverables

- [ ] For each of the aforementioned _Use Cases to Investigate_, determine how best to look up the `ClassLoader`.
- [ ] Use the `ClassLoader` for the current framework class (e.g., via `getClass().getClassLoader()`) instead of `ClassLoaderUtils.getDefaultClassLoader()` where appropriate.
- [ ] Ensure that tools have the ability to set the thread context `ClassLoader` (TCCL) where necessary.




# 133 this is title
The [AbstractClassBasedTestEngine](https://github.com/sormuras/mainrunner/blob/master/src/de.sormuras.mainrunner.engine/main/java-8/de/sormuras/mainrunner/engine/AbstractClassBasedTestEngine.java) already implements the base logic needed to support a (Java) class-based `TestEngine`. Derived classes only have to specify what a test class and what a test method is, and all "communication" with the JUnit Platform is handled under the hood.

## Deliverables

- [ ] Decide if JUnit Platform should provide such abstract `TestEngine` support class
- [ ] Another abstract support class `AbstractAnnotationBasedTestEngine<MyTest>` that handles a custom method annotation.




# 134 this is title
## Overview

Implements a test engine that allows declarative execution of test suites using
the `@Suite` annotation.

Internally the Suite Engine uses the JUnit Platform Launcher. The engine works
by mapping the `TestIdentifier` used by the launcher to `TestDescriptor` used
by the engine during discovery and in reverse during execution.

```java
package org.junit.platform.suite;

import org.junit.platform.suite.api.SelectPackages;

@Suite
@SelectPackages("org.junit.suite.testcases")
class SelectPackageSuite {

}
```

Is equivalent to:

```java
import org.junit.platform.engine.discovery.DiscoverySelectors;
import org.junit.platform.launcher.Launcher;
import org.junit.platform.launcher.LauncherDiscoveryRequest;
import org.junit.platform.launcher.core.LauncherDiscoveryRequestBuilder;
import org.junit.platform.launcher.core.LauncherFactory;

public class Main {

    public static void main(String[] args) {
        Launcher launcher = LauncherFactory.create();
        LauncherDiscoveryRequest request = LauncherDiscoveryRequestBuilder.request()
                .selectors(DiscoverySelectors.selectPackage("org.junit.suite.testcases"))
                .build();
        launcher.execute(request);
    }
}
```

Issue: #744

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 135 this is title
## Overview

The methods in `AbstractTestDescriptor`allows the parent/child relationship to be inconsistent.

## Deliverables

- [x] The `setParent()` method should throw an exception if the passed-in descriptor is not `null` and `this.parent` is not `null`
- [x] The `removeFromHierarchy()` method should call `setParent(null)` on all children.




# 136 this is title
## Overview

See https://github.com/junit-team/junit5/issues/1748#issuecomment-457612952

I've started to use this feature and I miss constructor injection quite a lot. Being able to inject the directory and then creating my tester as a final field was quite what I was looking for. 

I've moved that code to `@BeforeEach` but that's yet another annotation I have to add for no good reason. I actually don't need to create the tester for every test but I don't want to flag the tester static.

## Related Issues

- #1748 
- #1752



# 137 this is title
My use case:

* At the end of each test, save a video of the test in a file.
* It has to support the `@RepeatedTest` annotation and thus the computed file name must include the repetition index.

It seems the info is in RepeatedTestInvocationContext but there are 2 issues:

1. I don't know how to get access to that object in my afterEach, i.e. from an ExtensionContext. I guess I could use instanceof on the parent but it seems it's a TestTemplateExtensionContext so it wouldn't even work (and it feels hacky ;))
2. Even if I were able to get access to RepeatedTestInvocationContext it doesn't contain any API to get the current repetition. The only thing it offers is a custom displayName but having to parse that to get the repetition index doesn't feel right.

## Related Issues

- #944
- #1139
- #1668




# 138 this is title
Would there be interest in a bash/zsh completion script that would allow users to TAB-complete options and option parameters when invoking the `ConsoleLauncher`?

Currently the launcher is started with 

```
java -jar junit-platform-console-standalone-1.2.0.jar <Options>
```

By using the Gradle `application` plugin, it is straightforward to generate a distribution that includes a script for running the application. 

This script would become the main way to invoke the console launcher. For example:

```
consolelauncher.sh <Options>
```

Once we have a starter script, picocli can easily generate a [completion script](https://picocli.info/autocomplete.html) that suggests possible completion candidates for anything following `consolelauncher.sh` on the command line.

Let me know if there’s interest in doing this. 



# 139 this is title
## Overview

With the current Kotlin `assertAll` API you still have the the doubly nested braces `{ { } }`.
Eg:
```kotlin
@Test
fun `assertions from a collection`() {
    assertAll(
        "people with last name of Doe",
        people.map { { assertEquals("Doe", it.lastName) } }
    )
}
```
One thing I was just thinking about that might make the API even nicer for kotlin would be exposing extension methods that would let you do something like this:

```kotlin
@Test
fun `assertions from a collection`() {
    assertAll(
        "people with last name of Doe",
        people.mapExecutable { assertEquals("Doe", it.lastName) }
    )
}
```

The signature of that would be something like this:
```kotlin
package org.junit.jupiter.api

public inline fun <T, () -> Unit> Iterable<T>.mapExecutable(transform: (T) -> Unit): Collection<() -> Unit> {
    return map { { transform(it) } }
}
```
This might go beyond the scope of the API that the team wants to expose.

Other possible names for the function:
 - `mapAssert`
 - `mapExec`
 - `mapTest`
 - `test`

## Deliverables

- [ ] Decision to support adding this extension method.
- [ ] New Kotlin extension method `mapExecutable`




# 140 this is title
## Overview

Introduce migration support for JUnit 4's `@RunWith(Parameterized.class)`.

@marcphilipp mentioned through email that it would be nice to have an extension in `junit-jupiter-migration-support` that allows tests to be run that were originally written with JUnit 4 using the `Parameterized` runner. 

What this would look like:

```java
import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.Collection;
import org.junit.jupiter.api.TestTemplate;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.migrationsupport.extensions.Parameterized;
import org.junit.runners.Parameterized.Parameters;

@ExtendWith(ParameterizedExtension.class)
public class FibonacciTest {

    @Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][] {     
                 { 0, 0 }, { 1, 1 }, { 2, 1 }, { 3, 2 }, { 4, 3 }, { 5, 5 }, { 6, 8 }  
           });
    }

    private int input;

    private int expected;

    public FibonacciTest(int input, int expected) {
        this.input= input;
        this.expected= expected;
    }

    @TestTemplate
    public void test() {
        assertEquals(expected, Fibonacci.compute(input));
    }
}
```

```java
public class Fibonacci {
    public static int compute(int n) {
    	int result = 0;
    	
        if (n <= 1) { 
        	result = n; 
        } else { 
        	result = compute(n - 1) + compute(n - 2); 
        }
        
        return result;
    }
}
```

If everybody agrees this is a good idea, I would like to tackle this issue.

## Deliverables

- [ ] Introduce `ParameterizedExtension` extension in `junit-jupiter-migration-support`.
- [ ] An updated section in the user guide.
- [ ] Document in release notes.




# 141 this is title
## Overview

Currently, AFAICT, no classes (apart from utilities classes) document their support for inheritance (that is, whether they are designed to be subclassed or not). _Effective Java 2nd edition_, Item 16 describes the dangers of allowing users and extension writers to subclass JUnit 5 classes that aren't designed for inheritance. Therefore we should follow Item 17's advice to prevent this.

Specifically, each class should meet the following criteria (more or less ripped from the book):
1. For classes that support inheritance:
    1. Make those methods which aren't intended to be overridden final.
    2. **The class must document it's _self-use_ of overridable methods**.
    3. To allow programmers to write efficient subclasses without undue pain, **a class may have to provide hooks into its internal workings in the form of judiciously chosen protected methods or fields**.
    4. **The _only_ way to test a class designed for inheritance is to write subclasses; classes must be tested by writing subclasses **before** releasing it.** (Before GA, in our case.)
    5. **Constructors must not invoke overridable methods.**
    6. For classes implementing `Cloneable` or `Serializable`, **neither `clone` nor `readObject` may invoke an overridable method, directly or indirectly.**
2. For classes that _don't_ support inheritance:
    1. **Prohibit subclassing** by making the class final or replacing all public constructors with public static factory methods.

## Deliverables

- [ ] Each and every class meets the criteria above.




# 142 this is title
would be nice to have _some_ way of specifying inter-test dependencies.
this could be between different methods within the same class or between classes.

such a feature is very useful in large codebases with hundreds or thousands of tests. if something really basic breaks it could cause dozens of test classes to fail, and then tracking down the root cause depends on the developer choosing which test to debug - if you pick a complicated one it'll take a while.

with such a feature you could have all the higher-level tests depend on the basic tests so that such a failure will who up 1st on tests reports causing execution to skip the higher-level tests - saving on time and noise. 

## Related Issues

- #13 
- #48 



# 143 this is title
As it stands the JUnit 5 project publishes a user guide (which is awesome, btw) with every milestone and also has a current one tracking master (so to speak). This is pretty cool but suffers from the problem that a lot of very similar texts exist that Google, SO, blogs and other sites index and link to in a pretty random fashion. User can easily get lost in a guide that does not apply to their version (which is hopefully current or the most recent milestone).

I have two ideas that could help users find their way around:

* Add a one-line banner that sticks to the top of the screen and announces which version this is for and whether it is the current one. Alternatively the current version could not have a banner (making the common case not annoying) and the dev version a differently styled (maybe colored) one.
* Add a list to the guide (e.g. above "1. Overview") that links to all available versions, similarly to the drop-down box in [the Hibernate docs](http://hibernate.org/orm/documentation) (on the right).



# 144 this is title
TestExecutionListener is very useful to write custom reports, trace tests or view test plans. Informations like displayname, test source and legacy report name are already very useful for most situations.

But what if those infos from TestIdentifier are not enough? What if for creating reports etc. more informations are needed (i.e. like "usecase_ID", "authors" or "description") even before execution phase (ReportEntry only works during execution phase)? These infos could be stored in a Map<String,String> or Map<String,Object> for that purpose.

Therefore it would be useful to introduce mechanics to add additional informations. This would require extensions in a few areas:

Examples:
`Map<String,String> TestIdentifier.getAdditionalInfos()`
`Optional<String> TestIdentifier.getAdditionalInfo(String key)`

I can imagine following way to add these infos to TestIdentifier (in Jupiter)

- `@Info(key = "key", value = "value")` can be used to add additional infos to Class- or MethodTestDescriptors (repeatable annotation)
- TestDescriptor needs to be extended to return a Map<String,Object>
- `TestIdentifier.from(TestDescriptor descriptor)` needs to be extended to get this info map from TestDescriptor

That way TestIdentifier is more flexible for report creating frameworks (i.e. [Extent Report](http://extentreports.com/)) using not just Jupiter Engine but also custom TestEngine implementations.



# 145 this is title
## Overview

Based on discussions in #1184 and https://github.com/weld/weld-junit/issues/3, it is apparent that we need to document _best practices_ for implementing `ParameterResolver`, particularly with regard to "playing nicely" with other registered `ParameterResolver` implementations.

## Proposed Categories

After having put a bit more thought into the subject, I am tossing around the idea of categorizing `ParameterResolver` implementations by behavior as follows.

- **explicit**: support requires an annotation for disambiguation.
- **implicit**: support is automatic for types _owned_ by the resolver.
- **speculative**: a resolver claims it _can_ support a given parameter even if it potentially _should not_ (a.k.a., _greedy_ or _eager_).

## Deliverables

- [ ] Document best practices for `ParameterResolver` implementations in JavaDoc.
  - more succinct than the documentation in the User Guide
- [ ] Document best practices for `ParameterResolver` implementations in the User Guide.
  - including examples and explanations of how to avoid conflicts




# 146 this is title
## Description

Running `jdeps [...] --check org.junit.platform.commons` yields:

```
org.junit.platform.commons (file:///Z:/junit10570588147507757156/lib/junit-platform-commons-1.5.0-SNAPSHOT.jar)
  [Module descriptor]
    requires mandated java.base;
    requires java.compiler;
    requires java.logging;
    requires transitive org.apiguardian.api (@1.1.0);
  [Suggested module descriptor for org.junit.platform.commons]
    requires mandated java.base;
    requires java.compiler;
    requires java.logging;
    requires transitive org.apiguardian.api;
  [Transitive reduced graph for org.junit.platform.commons]
    requires mandated java.base;
    requires java.compiler;
    requires java.logging;
    requires transitive org.apiguardian.api;
  [Unused qualified exports in org.junit.platform.commons]
    exports org.junit.platform.commons.logging to org.junit.jupiter.migrationsupport,org.junit.jupiter.params,org.junit.platform.console,org.junit.platform.reporting,org.junit.platform.runner,org.junit.platform.suite.api
    exports org.junit.platform.commons.util to org.junit.platform.suite.api
```

### Analysis

- Directives actually compiled into the the module descriptor (`[Module descriptor]`) do match those listed below `[Suggested module descriptor for <module>]`.
- Directives listed below `[Transitive reduced graph for <module>]` ignored here, as we should favor the explicite declaration of all required modules.
- Directives listed below `[Unused qualified exports in <module>]` may be pruned from the module descriptor. Or they may stay for potential future-use.

## Deliverables

- [ ] Add integration test checking all modules
- [ ] Consult output and apply suggested directives when applicable





# 147 this is title
While JUnit5 provides an ability to look use SPI for extension activation, right now it activates all of the extensions. 

In reality extensions could be very different - you wouldn't want to activate SpringExtension for all your tests, but others (like Reporting) would be convenient to turn on globally instead of marking literally each test class with `@ExtendWith`.

So would be great to pass some variables (like extension class names) to surefire to be able to activate that extension for all tests at once.



# 148 this is title
## Overview

I tried to build a Powermock `Extension` similar to the Mockito example. I have to test some classes that create new objects within their constructors. In JUnit 4 I simply use the `PowerkmockRunner` and the `whenNew` from Powermock.

At least I ended with many problems and gave up. However in JUnit 4 Powermock creates an instrumented class loader and even duplicates everything (the test instance etc.) by using the new class loader. It is simple because the loader/rule are aware of executing the test itself. In JUnit Jupiter an `Extension` is not able to execute the test by itself.

I am wondering how this will be done in JUnit Jupiter. Are you planning to introduce some `CreateTestInstance` extension API? Something that is aware of manipulating class loaders. Or at least an `AroundAll` extension API to instrument the whole test class?

## Related Issues

- #157
- #805
- #806 
- #1680
- #1799 



# 149 this is title
## Overview

Issues #333, #976, and #978 addressed the topics of generics and overridden methods in various ways; however, as conjectured in #978, we may still have lingering bugs in this regard.

## Dedicated test class

[ReflectionUtilsWithGenericTypeHierarchiesTests](https://github.com/junit-team/junit5/blob/master/platform-tests/src/test/java/org/junit/platform/commons/util/ReflectionUtilsWithGenericTypeHierarchiesTests.java) contains a set of interesting and some unclear cases.

## Deliverables

For each of the following, introduce additional tests across multiple-level class hierarchies using generic interfaces, generic abstract classes, etc.

In other words, try to _break_ the search algorithms.

- [ ] `ReflectionUtils.findMethod(*)`
- [ ] `ReflectionUtils.findMethods(*)`




# 150 this is title
The ability to have a good report (tree) does not prevent to have some real time hints about executed tests.
Currently, these requirements are not fulfilled OOTB by the console launcher.
Would be great to have a listener logging each test being executed (a bit like surefire does "Running X") + the global report at the end.



# 151 this is title
## Overview

I have a `@TestTemplate` method, which tests a group of classes that are different implementations of the same `interface`. The test method is extended with multiple `TestTemplateInvocationContextProvider`-s, each providing the different implementation, with their own test cases.

I'd like to have a way give them a parent dynamically, so the different classes (`TestTemplateInvocationContextProvider`s) can show up in their own lists, without writing new test cases, for every single one of them.

My goal is to make the test results easier to handle, by grouping them together, so they are not in the same list. (especially since they can have a lot of cases)

## Proposal

Make `TestTemplateInvocationContextProvider` have a method, (`getGroup`, or `getParent` are my suggestions) return a String which is the name used as the `display name` of the parent of every test provided by it. The parent class value for this test can either be set to nothing, the actual parent class, or the extension's class.

Returning null, results in the current behavior.



# 152 this is title
First of all thanks for the `EngineTestKit` &mdash; it just came in time, as I need to test exception handling in my extension.

Unfortunately the test detection mechanism in Idea as well as when run from Gradle also finds the referenced class to run (which should fail) instead of ignoring it.

My workaround: I annotated my "test under test" with `@EnabledIfSystemProperty(named = "engine.test.kit", matches = "enabled")` and in the test class with `EngineTestKit` I defined `BeforeAll` and `AfterAll`:

```java
  @BeforeAll
  static void setUpAll() {
    System.setProperty("engine.test.kit", "enabled");
  }

  @AfterAll
  static void tearDownAll() {
    System.setProperty("engine.test.kit", "");
  }
```

This works... but I think there should be a simpler way of doing so. Any ideas?

If there is no solution up to now, I suggest to have an `ExecutionCondition` like `@OnlyRunViaEngineTestKit` or something similar.

Possibly related to #1372.




# 153 this is title
## Overview

_Jansi is a small java library that allows you to use ANSI escape sequences to format your console output which works even on windows._

http://fusesource.github.io/jansi/

## Picocli already shadowed

As `junit-platform-console.gradle` is configured to `shadowed('info.picocli:picocli:3.5.1')` it is possible that there is already _external_ support for ANSI coloring.

See `picocli.CommandLine.Help.Ansi.Style` for the definition of colors. Also `picocli.CommandLine.Help.ColorScheme`.

## Deliverables

- [ ] First, try to re-use picocli's console colors types.
- [ ] Replace [Color](https://github.com/junit-team/junit5/blob/master/junit-platform-console/src/main/java/org/junit/platform/console/tasks/Color.java) class and its usages with Jansi types
- [ ] Shadow Jansi into `junit-platform-console` artifact




# 154 this is title
Version: JUnit 5.5.0

When MethodOrderer.Random is used a message is printed displaying the default seed that was generated. This is useful when attempting to recreate a build if an issue was discovered, however if a seed has been provided this message should not be printed as it could be confusing as to which seed was used when executing tests in random order.

## Deliverables

- [ ] Default seed should only be printed when no seed is supplied




# 155 this is title
Support for generating JavaDocs for Kotlin methods is now supported in Dokka.

I don't really have the cycles to add this myself, but I wanted to make the JUnit team aware as this question came up when the Kotlin methods were introduced.

https://github.com/Kotlin/dokka/issues/211

If this is a low/no priority issue, feel free to close this. I just wanted to make the JUnit team aware.



# 156 this is title
## Overview

In the User Guide we have [section 5.11](https://junit.org/junit5/docs/current/user-guide/#extensions-execution-order) where the _happy path_ relative execution order is described. 

During our work on #1465 and #1460 I was trying to find in the user guide what would be the expected behavior when something fails. Specifically in that case I wanted to know what is expected to run when there is an exception in the constructor of the test class.

I would have expected this information to be described in the User Guide, yet it is not or I was unable to find it.

## Deliverables

- [ ] Document the expected execution paths and order in case of failures.
- [ ] Add link to this information in `Relative Execution Order Section` of the User Guide so it easy to find.




# 157 this is title
With reference to this thread, https://github.com/junit-team/junit5-samples/issues/118#event-2883368068 

It would be nice to have the ability to add tags during runtime (especially for Data-Driven Testing). 

Use Case: 
1. We are using different test data for a test case. We want to group all the positive test data as a smoke suite and add negative test data to the Regression suite. 

Model Test Data:

` {
    "testName": "Sample 1",
    "tag":"smoke",
    "testData":"TD"

  },

{
    "testName": "Sample 2",
    "tag":"Regression",
    "testData":"TD12"

  }`

Let me know if this is feasible!  



# 158 this is title
My project requires that I do not write to `/tmp` or whichever location it is when I use the [`TempDirectory` extension](https://junit.org/junit5/docs/current/user-guide/#writing-tests-built-in-extensions-TempDirectory). So right now I have no choice but to still use [`junit-pioneer`'s implementation](https://junit-pioneer.org/docs/temp-directory/), e.g. like this:

 ```java
@RegisterExtension
Extension tempDirectory = TempDirectory.createInCustomDirectory(() -> Paths.get("build"));
 
@BeforeEach
void setup(@TempDir Path testProjectDir) {
    // Do something with "testProjectDir".
}
```

But it would be nicer if I could just use stock JUnit 5 for this. JUnit 4 supported setting the parent dir, so I find the JUnit 5 way a bit too limiting.

Thanks in advance.



# 159 this is title
This issue originates from a dicussion in https://github.com/junit-team/junit5/pull/1422#issuecomment-390582297.

While often it suffices to specify each set of arguments for the invocation of a parameterized test explicitly, there are cases where it's simply the combination of lists of potential values for each parameter, i.e. the cartesian product of these collections. While it's certainly already possible to compute these combinations manually, e.g. in a method referenced by `@MethodSource`, it would be more convenient if there were a declarative way to specify that.

Recently, @sormuras has written a sample [`CartesianProductProvider`](https://github.com/junit-team/junit5-samples/blob/master/junit5-jupiter-extensions/src/main/java/com/example/cartesian/CartesianProductProvider.java) extension which does that by implementing `TestTemplateInvocationContextProvider`. However, by implementing this functionality as a `ArgumentsProvider` users would not have to learn a new concept and we could reuse the existing infrastructure.

One possibility would be to use fields and methods, like the `Theories` runner from JUnit 4.

```java
@BaseSet
static final Set<String> strings = Set.of("foo", "bar");

@BaseSet
static Set<Integer> ints() {
    return Set.of(23, 42);
}

@ParameterizedTest
@AllCombinationsSource
void test(String a, int b) {...}
```

@junit-team/junit-lambda Thoughts?

## Deliverables

- [ ] Introduce new `ArgumentsProvider` and related annotations




# 160 this is title
Dynamic Tests are non-deterministic in nature. Sometimes it might not be clear to the test author (let alone the IDE) when or even if the execution will terminate. 
It has been suggested to introduce a timeout to stop the execution before it would terminate by itself. An alternative would be to terminate the execution when a certain number of failed (or successful tests)  have been executed.




# 161 this is title
With these changes I was able to go from ~57160 to ~125205 dynamic tests with a `-Xmx64m` and the sample project provided by @ben-manes in #2450 without compromising any functionality.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [ ] There are no TODOs left in the code
- [ ] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [ ] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 162 this is title
## Overview

This is a *feature request* and a follow-up to the discussion in #1306. Currently if a user needs to add a description of a set of arguments (e.g., because their string representation is not enough, or the differences between adjacent arguments are subtle), they need to (ab)use the `Arguments` by adding an additional one. This has a couple of drawbacks:
- That argument must be specified in the test method signature. Although it may be given a descriptive name to clarify its purpose (e.g., "testDescription"), it will still be highlighted by an IDE as _unused_ (see #1306).
- A proper workaround is ugly: `@SuppressWarnings("unused")  // Used in the test name above`
- Such argument is misleading, as it isn't a test _parameter_, but a meta-data about test parameters. It shall not affect the test results.

### Example
```java
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.util.stream.Stream;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class SampleTest {

  @ParameterizedTest(name = "{1}: {0}")
  @MethodSource("testParameters")
  void test(String s,
            @SuppressWarnings("unused")  // Used in the test name above
            String testDescription) {
    assertThrows(NumberFormatException.class,
        () -> Integer.parseInt(s)
    );
  }

  static Stream<Arguments> testParameters() {
    return Stream.of(
        Arguments.of("1a", "illegal character"),
        Arguments.of("10000000000000", "out of bounds")
    );
  }
}
```

## Possible solutions
As suggested by @sormuras  in the [discussion](https://github.com/junit-team/junit5/issues/1306#issuecomment-368229340), an optional attribute may be added to `Arguments`.

## Alternatives
- #1306, but it will enable users to write confusing code (= reference some arguments that do not appear in the method parameters by index).

## Questions
- [ ] Q1: Shall `CsvSource` & `CsvFileSource` be expanded with a similar attribute (e.g., description column index):
```java
@CsvSource(arguments = {
    "Arg1, Arg2, Test Case #1 Description",
    // …    
}, descriptionColumnIndex = 2)
``` 
?
- [ ] Q2:  Shall we change the default value of `org.junit.jupiter.params.ParameterizedTest#name` or the interpretation of `{arguments}` to include the description if it's non-empty?
- [ ] Q3: What a name of the method setting a description should be (consider IDE auto-complete!):
   - ~~`desc`~~
   - `description`
   - `describedAs`
   - `withDescription`?
- [x] Q4: What return type of the method returning the description should be:
   - ~~String, with empty string meaning no description.~~
   - Optional<String>, with empty meaning no description. PoC shows, that this one is preferred.
- [ ] Q5: Shall the method setting a description accept:
   - `String`.
   - `CharSequence`
   - `Object` and format as it does the parameters?
- [ ] Q6: How to separate parameters and their description:
  - a space: ` `
  - a dot + space: `. `
  - a colon + space: `: ` (A colon is likely to appear in description itself, e.g. "Regression: Integer.MIN_VALUE, see XYZ-123").


## Deliverables

- [ ] User Guide must be updated
- [ ] **TBD**




# 163 this is title
## Overview

- Inlined `ExecutableStream` and `ExecutableCollection` type aliases since each is only used in two places that don‘t warrant dedicated type aliases. There is also [KT-24700](https://youtrack.jetbrains.com/issue/KT-24700) that makes private type aliases kind of dangerous.
- Removed the two map extension functions and instead inlined it at a single spot, all other functions are now calling that function and there is no need for the additional symbols anymore.
- Removed the `toList()` calls and exchanged them with `Arrays.stream()`, there is really no need to construct a list first.
- Moved the examples to Kotlin files and made them actual tests. This ensures that the code from the examples stays up-to-date and is correct since they are treated like normal tests. In fact, I fixed some samples that where using `Duration.seconds` which actually needs to be `Duration.ofSeconds`.

We could make every trivial, forwarding function `inline` but I didn‘t do it right away because I would first like to know if there are any good reasons not to. I will leave a comment on every function that I believe should be inlined. Instead of making them `inline` we could also drop them altogether since some of them are just forwarding to their corresponding Java functions. Instead of redeclaring the whole Java API in Kotlin we could just start annotating the Java code with the [JetBrains annotations](https://github.com/JetBrains/java-annotations), the result would be the same but the experience would not only be improved for Kotlin users but for Java users as well (given they use IntelliJ).

Moving the samples to actual tests means that I had to enable tests in the API module. I am not sure if this is a good thing. Let me know what you think.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [x] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass



# 164 this is title
## Foreward
First off, I want to thank the Junit 5 team from being so willing to officially support Kotlin as a first-class citizen in the Junit 5 library. It has been absolutely wonderful being able to use my own contributions in all of my Kotlin projects.

## Feature Request

I believe that this API can be further enhanced with the new Kotlin 1.3 feature, [Contracts](https://kotlinlang.org/docs/reference/whatsnew13.html#contracts).

Contracts are making guarantees to the compiler that various methods have certain characteristics.

Here's an example from the Kotlin Std-Lib:

```kotlin
/**
 * Throws an [IllegalStateException] if the [value] is null. Otherwise
 * returns the not null value.
 *
 * @sample samples.misc.Preconditions.failCheckWithLazyMessage
 */
@kotlin.internal.InlineOnly
public inline fun <T : Any> checkNotNull(value: T?): T {
    contract {
        returns() implies (value != null)
    }
    return checkNotNull(value) { "Required value was null." }
}
```

Before Kotlin Contracts, the following code wouldn't have compiled:
```kotlin
fun validateString(aString: String?): String {
    checkNotNull(aString)
    return aString
}
```

I believe that JUnit 5 has a few places where these contracts would be valuable.

### Examples

#### `assertNotNull`

```kotlin
@ExperimentalContracts
fun <T: Any> assertNonNull(actual: T?, message: String): T {
    contract {
        returns() implies (actual != null)
    }
    Assertions.assertNotNull(actual, message)
    return actual!!
}
```

The above would allow something like this:

```kotlin
val exception = assertThrows<IllegalStateException { /** whatever **/}
val message = exception.message
assertNotNull(message)
assertTrue(message.contains("some expected substring")) 
```

Alternatively, it would also allow for this sort of use case:
```kotlin
val message = assertNotNull(exception.message)
```

#### `assertThrows` / `assertDoesNotThrow`
Since the `callable` passed to `assertThrows` is only ever called once, we can expose that in the contract.
```kotlin
@ExperimentalContracts
inline fun <reified T : Throwable> assertThrows(noinline message: () -> String, noinline executable: () -> Unit): T {
    contract {
        callsInPlace(executable, InvocationKind.EXACTLY_ONCE)
    }
    return Assertions.assertThrows(T::class.java, Executable(executable), Supplier(message))
}
```

Similar 

This would for something like this:
```kotlin
val something: Int
val somethingElse: String
assertDoesNotThrow {
    something = somethingThatDoesntThrow()
    somethingElse = gettingSomethingElse()
}
```

## Caveats

Kotlin Contracts are only supported in Kotlin 1.3 and higher.
This would require a discussion regarding what version of Kotlin the Junit 5 team want's to officially support.

## Deliverables

- [ ] Add Kotlin method `assertNotNull`
- [ ] Add Contracts to Kotlin method `assertNotNull`
- [ ] Add Contracts to Kotlin method `assertThrows`
- [ ] Add Contracts to Kotlin method `assertDoesNotThrow`




# 165 this is title
Hello Developers

I use `Spock Framework` which is based on `Groovy`, there is a special feature very useful. It contains some special blocks or labels such as `given`, `where` etc where appears in some special kind of reports. It is very useful by itself

Such feature would be added in JUnit 5?

Thanks




# 166 this is title
While writing an own `TestEngine` we found it quite handy to reuse JUnit Jupiter's extension mechanism along with `ExecutionCondition` to conditionally run/skip classes and methods (see mp911de/microbenchmark-runner#19 for further details). 

However, some implementations (such as `DisabledCondition`) are not visible or internal API (e.g. `ExtensionRegistry`). As an implementer, there are two ways to implement extension support:

* Using internal API
* Reimplementing

Neither is great, so it would be better to be able to reuse the existing bits of JUnit Jupiter's engine implementation.

## Deliverables

- [ ] Stable implementation of `ExtensionRegistry`
- [ ] Stable implementation of support classes (such as `AbstractExtensionContext` and `ExtensionUtils`)





# 167 this is title
## Overview

I am trying to create my own implementation of TestEngine, MyCustomExecutionEngine. I want to re-use the discovery mechanism from JupiterTestEngine and just do a custom execute() implementation. Hence, I want the test junit-jupiter-engine present as a dependency. But, I don't want the junit-jupiter-engine to run, I want only my custom engine to run.

## Problem

- I register MyCustomExecutionEngine in META-INF/services/org.junit.platform.engine.TestEngine 
- I run a test class from IDEA. The test class and my custom engine implementation are in the same project. 
- Because the implemented methods in MyCustomExecutionEngine are empty I get this warning (twice):
> WARNING: TestEngine with ID 'my-custom-engine' failed to discover tests
- But then the tests are run after all.
- When debugging, in DefaultLauncher#discoverRoot (called twice) I can see that testEngines iterable contains three engines: MyCustomExecutionEngine, JupiterTestEngine, and VintageTestEngine. 
- If I completely remove junit-jupiter-engine as a dependency the problem is solved. 

 ## Versions

- Junit 5.1.0
- IDEA 2017.3.4



# 168 this is title
I have this test

```java
    @Test
    void equalsAndHashcodeForFields() {
            EqualsVerifier.forClass( Emr.class )
                    .withRedefinedSuperclass()
                    .withIgnoredFields( AbstractEntityBase.ID )
                    .verify();
    }
```

currently it's failing for reasons not relevant here, verify returns void and throws an exception. I was hoping I could wrap it in an assumption of some kind.  Instead I guess I'll mark it disabled.



# 169 this is title
When initially developing tests against legacy code that utilizes the filesystem extensively, I often find myself creating using `@TempDir`, which is fantastic. But oftentimes when debugging and/or initially writing the test I need to capture the outputs to get a "golden file" that I can regression test against on future runs. As such, currently I just use a non-TempDir folder to capture them, then need to update my test using TempDir later.

It would be super helpful if instead the TempDir annotation provided an option so that I could disable cleanup for a couple of runs then re-enable cleanup later in the development lifecycle. I'm envisioning something like the following

```java
@TempDir(cleanup=false)
private Path outputFolder;
```



# 170 this is title
The `MethodOrderer` implementation `OrderAnnotation` uses an `@Order` annotation to allow sorting the execution order of tests (which is generally a smell, but sometimes necessary). But that means another annotation for every test method. It would be nicer to simply use the order of the methods in the source. As this information is not provided by the Java reflection API, we'd have to parse the class file. Maybe we don't need a full parser, but a simple heuristic may be enough.

Some years ago I already wrote a simple JUnit 4 runner for this [here](https://github.com/t1/test-tools/blob/master/src/main/java/com/github/t1/testtools/OrderedJUnitRunner.java)

## Deliverables

- [ ] `ClassFileMethodOrderer` implementing `MethodOrderer`




# 171 this is title
## Overview

Feature request to add native support to rerun failing flaky tests

**Feature request** 

Is there any plan to support the ability of rerunning failed flaky tests? For example, it would be great to have something like `@Flaky(rerun=3)`, which would rerun a failing flaky test up to n times.

In the *past*, in Surefire/Failsafe we could use `rerunFailingTestsCount`. However, it does not work in JUnit 5. As JUnit 5.0.0 was released nearly 1 year ago, it is unclear if and when it will be supported in Maven.

And, even if it will be supported in Maven in the future, it could be good to have a special annotation to specify that only some tests are expected to be flaky, and not *all* of them.

At the moment, the workaround is to stick with JUnit 4, which is a kind of a shame as JUnit 5  has a lot of interesting features :(  (which I can only use in projects with no flaky tests)

Related [SO question](https://stackoverflow.com/questions/46181026/junit5-how-to-repeat-failed-test).





# 172 this is title
Let's imagine that:
1. We run large number of tests via command line
2. Some tests fail
3. We investigate why they failed
4. We fix the problem, for example in the code
5. Now we want to rerun failed tests only

**It would be great to have something like --rerun-failed-tests command option**.

IntelliJ IDEA IDE has "Rerun Failed Tests" feature, so why not to have it directly in Junit 5 Console Launcher?




# 173 this is title
Spring Framework would like to be able to resolve parameters from its `ApplicationContext` so that users can easily create tests that inject beans. We'd also like to allow any existing `ParameterResolver` instances to take precedent so that Spring only attempts to resolve parameters that have not been otherwise claimed.

i.e., given something like this:

```java
@ExtendWith(SpringExtension.class)
@ExtendWith(MockitoExtension.class)
class MyTest {

    MyTest(@Mock Customer customer, CustomerService service) {
    }
}
```

We'd like to allow the `MockitoExtension` to support `customer` and the `SpringExtension` to support `service`.

One option to allow this might be to have a `FallbackParameterResolver` interface which would be used only if no regular `ParameterResolver` supports the parameter.




# 174 this is title
### Introduction

Hi,

I want to implement the feature as I suggested in #1767: A mechanism for scenario testing. I really want to make a contribution to open source project. If there is something not good, it would be great if you can give me some advice :). 

Thank you.

---

### Usage 

###### You can add the following annotations to your test class.

**_@TestMethodOrder(DependsOnAnnotation.class)_** - Most important: It sorts the test methods according to the dependent order, but this alone does not disable child method if any ancestor method fails.

**_@ExtendWith(DependsOnTestWatcher.class)_** - Second most important: It will disable child method if any ancestor method fails.

###### You can add the following annotation to your test method.

**_@DependsOn("ancestorMethodName")_** - Most important: It will provide the relative relationship that you want to realize.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [ ] There are no TODOs left in the code
- [ ] Method [preconditions](http://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [ ] [Coding conventions](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](http://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](http://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 175 this is title
## Overview

I have found that it would be useful if you could use argument fields as a part of parametrized test name. Right now, when using just `{0}` as described in docs, it results in injecting into a test name string in form of `ClassName(fieldName1=fieldValue1, fieldName2=fieldValue2, ...)`. But that doesn't seen readable at all especially then you have a class with more than just few fields. Now I would like to be able to use some semantics as `{0.name}` or `{0}.name` to use just name field of class used as test method argument, so I can write test name as follows:

``` java
@BeerTest
class BeerConversionServiceTest {

    @Autowired
    private BeerConversionService beerConversionService;

    private static Stream<Arguments> createBeers() {
        return Stream.of(
                Arguments.of(new Beer(...), 25L),
                Arguments.of(new Beer(...), 50L)
        );
    }

    @DisplayName("Get alcohol content of a beer in mg")
    @ParameterizedTest(name = "Alcohol content of {0.name} should be equal to {1}")
    @MethodSource("createBeers")
    void getAlcInMg(Beer beer, long mg) {
        Assertions.assertEquals(beerConversionService.getAlcInMg(beer), mg);
    }

}
```

This would give users possibility to keep test names simple, yet still descriptive, as they could reference objects passed as arguments and use only parts of them which identifies test cases.

I didn't look into the source code so I cannot tell which approach would be easier to implement but I would guess that `{0.name}` seems more reasonable.

## Deliverables

- [ ] Introduce an SPI (similar to what has been [proposed above](https://github.com/junit-team/junit5/issues/1154#issuecomment-345445625)) and provide a SpEL-based and/or OGNL-based implementation.
- [ ] Ensure that display names for `@ParameterizedTest` and `@RepeatedTest` can make use of the same facility (see #2452).



# 176 this is title
## Question

Will this project's release numbers conform to [Semver](http://semver.org/)?

Inevitably in every project mistakes are made and the team realizes that API's that made sense once no longer do. Semver defines a versioning schema.

Many projects say that they conform to Semver but they ignore the 8th point:

> 8\. Major version X (X.y.z | X > 0) MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY include minor and patch level changes. Patch and minor version MUST be reset to 0 when major version is incremented.
> \- [Semver Section 8](http://semver.org/#spec-item-8)

Many projects are afraid to bump the major version unless there is some major feature addition or wild rewrite of the API.
One exception to this is [Google Guava's releases](https://github.com/google/guava/releases).
They will perform many major version releases in a year because they break API's. That team isn't afraid of the major version number.

That being said, they have a prominent warning in their [README about their versioning](https://github.com/google/guava#important-warnings).

The `@API` annotations are great; guava has something similar with their `@Beta` annotation.

## Implications

If JUnit 5 decides to follow Semver and makes a release that has a breaking API change, it would be JUnit 6!

## Deliverables

- [ ] Document detailing the release number versioning decisions of the JUnit Team




# 177 this is title
For recent PRs codecov reports are not available.
https://codecov.io/gh/junit-team/junit5/pulls

In the CI pipeline, Codecov `Coverage ` step (Codecov returning 400 for URL.)


```
    ‌query:‌ branch=merge&amp;commit=853385448e466fc4c64505a0d69a6065dba387b8&amp;build=20190401.4&amp;build_url=https%3A%2F%2Fdev.azure.com%2Fjunit-team%2Fjunit5%2F_build%2Fresults%3FbuildId%3D111&amp;name=&amp;tag=&amp;slug=junit-team%2Fjunit5&amp;service=azure_pipelines&amp;flags=&amp;pr=&amp;job=111‌
    ‌-&gt;‌ Pinging Codecov‌
https://codecov.io/upload/v4?package=bash-8a28df4&token=$(codecovToken)&branch=merge&commit=853385448e466fc4c64505a0d69a6065dba387b8&build=20190401.4&build_url=https%3A%2F%2Fdev.azure.com%2Fjunit-team%2Fjunit5%2F_build%2Fresults%3FbuildId%3D111&name=&tag=&slug=junit-team%2Fjunit5&service=azure_pipelines&flags=&pr=&job=111
HTTP 400‌
Provided token is not a UUID.‌
##[section]Finishing: Coverage
```

Ex Build: https://dev.azure.com/junit-team/junit5/_build/results?buildId=111






# 178 this is title
Subject says it all. Would be especially useful for TCR (test && commit || reset) workflow.
Feature could be globally configured or switched of from IDE / build tool.

https://github.com/junit-team/junit5/issues/431 is related and https://github.com/pitest/pitest-junit5-plugin/pull/15 might also profit.




# 179 this is title
<!-- Start by telling us what problem you’re trying to solve. Often a solution already exists! Please, don’t send pull requests to implement new features without first getting our support. -->

Currently, the `MethodSource` methods are supposed to not have any parameters, however, it'll help to have Parameters to be resolved in these Methods if registered similar to Before/After methods.

Along with https://github.com/junit-team/junit5/issues/2190, this'll give access to MethodSource methods to possibly use `Extension.Store` and store any initialised details, which could be purged in After all methods

Also, in case of creating dynamic tests using details from a resolved Object, `ParameterResolver` can enhance abilities of `MethodSource` by a fair bit.

Currently, the way to achieve the same is to have a class implementing `ArgumentsProvider` and possibly manage the value of the Object there, or have it in the `MethodSource` method itself statically initialising it in test class


## Deliverables

- [ ] ...




# 180 this is title
The following is an analysis of which JUnit 4 TestRule functionality is provided by JUnit 5.  This should be documented in an addendum to the User Guide.
-   [ ] DisableOnDebug - ~~partially accomplished using [DisableIf/EnableIf](https://github.com/junit-team/junit5/issues/219), partially allowed via the use of [@Tags](https://junit.ci.cloudbees.com/job/JUnit5/javadoc/org/junit/jupiter/api/Tags.html) as described in sections [3.7 Tagging and Filtering](http://junit.org/junit5/docs/snapshot/user-guide/#tagging-and-filtering) of the user guide.  But is it completely covered?~~  I was completely off base with this assessment.  This ```@TestRule``` allows you to disable a test rule if the JVM is in debug mode and has absolutely nothing to do with deciding what tests should be run.
-   [x] ExpectedException - use [Assertions.expectThrows()](https://junit.ci.cloudbees.com/job/JUnit5/javadoc/org/junit/jupiter/api/Assertions.html#expectThrows-java.lang.Class-org.junit.jupiter.api.Executable-) as described in section [3.4 Assertions](http://junit.org/junit5/docs/snapshot/user-guide/#assertions) of the User Guide.
-   [ ] ExternalResource
  -   [ ] TemporaryFolder - Provide [TemporaryDirectory](https://github.com/junit-team/junit5/blob/459aefa6d5eb5838e8aa36423bfe386005df9bdf/junit-tests/src/test/java/org/junit/gen5/console/tasks/TempDirectory.java) which is used for internal JUnit 5 tests as part of https://github.com/junit-team/junit5-samples.  See https://github.com/junit-team/junit5-samples/issues/4.
-   [x] RuleChain - JUnit 5 extensions enable via @ExtendWith are executed in declaration order.
-   [ ] Stopwatch - partially provided via the [TimingExtension](http://junit.org/junit5/docs/snapshot/user-guide/#test-lifecycle-callbacks) in section [5.6.1 Before and After Test Execution Callbacks](http://junit.org/junit5/docs/snapshot/user-guide/#test-lifecycle-callbacks) of the user guide.  See this comment: https://github.com/junit-team/junit5-samples/issues/4#issuecomment-190330403.  Reporting of the result state could be accomplished by injecting [TestReporter](https://github.com/junit-team/junit5/blob/master/junit-jupiter-api/src/main/java/org/junit/jupiter/api/TestReporter.java) via parameter resolution (using @BeforeAll?) but there are potentially use cases that can't be handled.
-   [x] TestWatcher
  -   [x] TestName - inject [TestInfo](https://junit.ci.cloudbees.com/job/JUnit5/javadoc/) into the test using parameter resolution.
-   [x] Timeout - JUnit 4 allows the timeout to be specified via [@Test](http://junit.org/junit4/javadoc/latest/org/junit/Test.html#timeout%28%29).  Is there an equivalent in JUnit 5?  For performance testing, it would also be nice to have the test fail if it exceeded a threshold.
-   [x] Verifier
  -   [x] ErrorCollector - use [Assertions.assertAll()](https://junit.ci.cloudbees.com/job/JUnit5/javadoc/org/junit/jupiter/api/Assertions.html#assertAll-java.lang.String-org.junit.jupiter.api.Executable...-) as described in section [3.4 Assertions](http://junit.org/junit5/docs/snapshot/user-guide/#assertions) of the User Guide.
## Related Issues
- #169 
## Related Blog Posts
- http://www.codeaffine.com/2016/04/06/replace-rules-in-junit5/
- http://blog.codefx.org/libraries/junit-5-conditions/




# 181 this is title
This is kind of a follow up on #1109 ... I didn't get around to this up to now, but now I have a working POC of a `TestEngine` with similar features to the custom JUnit 4 runner.

You can check this out here
https://github.com/TNG/ArchUnit/tree/junit5-support/archunit-junit/junit5/src/main/java/com/tngtech/archunit/junit

I like the power, e.g. that I can just mark `@AnalyzeClasses` with `@Testable` and my IDE will pick it up, and the engine will be 'magically' discovered, without the need to specify sth. like the old `ArchUnitRunner` :smiley: 

However, with regards to the `TestEngine` itself, I'm kind of unsure. Maybe I've overlooked some documentation here, the design seems very flexible, but that also makes it hard to know which contract to adhere to.

As an example: `TestDescriptor` offers an `Optional<TestSource> getSource()` with the JavaDoc "Get the source of the test or container described by this descriptor, if available.". So I assumed, I could leave that out for my first draft, implement only the most necessary. And the tests ran in IntelliJ and they ran in Maven. However, in Gradle they were silently skipped. It took me some digging into the Gradle sources to find out, that Gradle uses the test source, to determine, if this test is a 'composite' or not. And if the source is absent, an `AssertionError` is thrown, which in turn gets silently swallowed.

Or another one, I'm pretty sure, that the "old" Gradle JUnit 5 plugin (before Gradle 4.6) would call the engine with a `ClasspathRootSelector`, while with Gradle 4.6 this suddenly changed to a set of `ClassSelector`.

For my POC now, I've only added support for `ClassSelector`, the question is, do I need to add support for all the selector types?
I'm just not sure, how I can be certain, that I covered the minimum to run on all common platforms. Do I really need to add support for `UriSelector` for example, or is this irrelevant for all common IDEs and Build tools anyway?

It feels a little bit, that to implement a `TestEngine`, one has to study the Jupiter engine and copy the behavior, since sticking to API + Javadoc does sometimes lead to surprising results (which can of course also be my fault for not completely understanding the concepts :wink: )

Anyway, any tipps what I really need to be somewhat on the safe side (that this will behave natural for daily development tasks) would be highly appreciated!!



# 182 this is title
## Issue

Extension methods all have `ExtensionContext` which provides us many useful information like `displayname`, `method` or `tags`. This helps  in writing custom test reports.

What I'm missing is a way to get argument instances of a `@ParameterizedTest`. When not running tests extended by a `ParameterResolver` using `ExtensionContext.Store` you can only make a workaround to get a clue of what arguments were used for the test:

- Filter displayname (objects need to override `toString()` for important informations)
- get values from annotations

If parameters are simple strings, integers etc. there is no problem when parsing displayname. The problem starts when one of the parameters is an object containing lots of informations. A new instance would have to be created when analyzing the test, but this doesn't garanty an object with exact the same content like in the test and might also lead to memory issues.

Most simple way is to reimplement Parameterized Test Template, extend from each class, catch resolved parameters and store them directly in ExtensionContext.Store, but I'm not a fan of writing Wrapper classes for such small extensions in existing codes.

## Possible Suggestions

- Provide a method `Arguments[] ExtensionContext.getArguments()` or `List<Arguments> ExtensionContext.getArguments()` which returns a list of all Arguments used for the test (empty list if no arguments were used).
- Store arguments in `ExtensionContext.Store` with a predefined namespace in your `ParameterizedTestParameterResolver` class (then there is no need to do it in custom `ArgumentsProvider` classes)
- Provide an Extension interface which is called between `BeforeTestExecutionCallback` and `@Test`. As parameters it should have `ExtensionContext` and `Arguments[]`.

## Related Issues

- #944
- #1668
- #1884




# 183 this is title
Hi,

org.junit.jupiter.engine.execution.InvocationInterceptorChain.ValidatingInvocation#markInvokedOrSkipped prevents to implement some retry like interceptors and I'm not sure what this validation intends so my request is to drop that validation or at least enable interceptors to disable it to avoid to have to use getExecutable().invoke() which bypasses interceptor chain.

Romain



# 184 this is title
## Overview

As requested in issue #681 (```Introduce junit-platform-suite-api module```), the annotations used for test discovery and selection in the ```JUnitPlatform``` runner have been refactored into the ```junit-platform-suite-api```.  This allows a purely JUnit 5 test suite to be defined declaratively, though it currently requires an alternate engine (as opposed to an extension).

This issue describes a generalized JUnit platform suite that's suitable for the Jupiter test engine as well as any others that might be chosen.  It's my opinion that unit tests rarely require test suites, but it becomes far more common when integration, system and acceptance tests are being executed due to the very common integration with external systems that should only be initialized before the entire test run.  Examples of resources that can be safely shared among tests are database connection pools (or really any connection pool), test frameworks that require significant set-up time (e.g. GWT test suites eliminate 20s of HtmlUnit set-up time for each test - it's only incurred once at the beginning of each suite).

The examples shown below indicate how the ```@Suite``` annotation can be used in conjunction with those already in the ```junit-platform-suite-api``` module.  Originally I'd also defined the ```@BeforeSuite``` and ```@AfterSuite``` annotations but after further consideration decided that since suites are really just an arbitrary collection of indeterminately nested test containers, it would be better if the ```@BeforeAll``` and ```@AfterAll``` annotations were contextual (nested in the same way the hierarchy would be presented in the test tree).  I've also assumed that these annotations no longer require the static modifier as discussed elsewhere.

Imagine if you will a set of acceptance tests that have a custom reporting mechanism that should be configured for the entire test run.  Included within this outer suite is a set of tests that require a database connection pool and a different set of tests that require an LDAP connection pool.  The top-level suite definition for the acceptance tests might look something like:

```java
@Suite
@IncludeEngines("jupiter-engine") // not required if there's only one engine on the classpath
@IncludeClassNamePatterns(".*AcceptanceTestSuite$")
public class AcceptanceTestSuite {

    @BeforeAll
    void setUp() {
        ... // code to set-up custom test reporting
    }

    @AfterAll() {
    void tearDown() {
        ... // code to tear-down custom test reporting
    }

}
```

There are two notable characteristics of this test suite:

1. It specifies which engine will be used for the entire container/test hierarchy (assuming there is more than one).
2. It includes potentially numerous other test suites as sub-containers which can each have their own contextual set-up and tear-down.

A child suite for tests that require a database connection pool might look something like this:

```java
@Suite
@IncludeTags({"integration", "database"})
@IncludeClassNamePatterns(".*IT$")
public class DatabaseAcceptanceTestSuite {

    @BeforeAll
    void setUp() {
        ... // code to set-up the database connection pool
    }

    @AfterAll() {
    void tearDown() {
        ... // code to tear-down the database connection pool
    }

}
```

If run under Maven, test classes that end in "IT" would be run using the ```maven-failsafe-plugin```.  If there are other classes of integration tests not run during acceptance testing it would also be necessary to make sure the acceptance test classes were not run (as they'd fail without the suite's set-up methods).

## Feature Request

Provide the means for arbitrarily nested, declarative tests suites in JUnit 5 including the execution of set-up and tear-down methods

## Related Issues

- #330 
- #456
- #746
- #687 (perhaps superseded by this issue)
- #964 
- [Eclipse IDE issue](https://bugs.eclipse.org/bugs/show_bug.cgi?id=511183)
- #1243

## Deliverables

- [ ] TBD




# 185 this is title
This is a follow up to  
https://github.com/junit-team/junit5/issues/1938
Jmockit used to call into internal API to register it's extension. Now JMockit changed their code to set the Systemproperty 
`junit.jupiter.extensions.autodetection.enabled=true`
which is kind of official API but also is a lot worse.

- It' my decision as a user whether i want autodetection or not ,an external framework shouldn't invalidate my choice
- autodetection will pick up anything thats on the classpath, especially things i am not aware of and don't need or want. 

But the root cause seems to me that junit5 doesn't seem to provide a straighforward API for jmockit (and other frameworks) to globally register their (and only their) extension. So you can't really blame jmockit to much on there choice.

## Deliverables
Sort of: Being able to to insert a single extension in a controlled way into the extension registry.



# 186 this is title
On method execution of `executionStarted(...)`, `executionFinished(...)` in the `TestExecutionListener` class, it seems it's not possible to get the value of the parameters for `ParameterizedTest`, but using `displayName` attribute in the `TestIdentifier`. 

**Feature request**: Add the capability to have `parameters` to the `TestIdentifier` class in order to obtain those values.

*Related to*: https://stackoverflow.com/questions/56319857/getting-the-values-of-parameters-for-parameterizedtests-in-testexecutionlistener



# 187 this is title
## Context

I've written an extension which deterministically 'shards' my tests to ensure they run on exactly one CircleCI node (by hashing the name into CIRCLE_NODE_TOTAL buckets), allowing me to dial up [parallelism](https://circleci.com/docs/2.0/parallelism-faster-jobs/#specifying-a-jobs-parallelism-level) and make my builds go faster.

However, it's kinda annoying having to add my annotation `@CircleCiSharding` to every single test class.  I considered using the [automatic registration](https://junit.org/junit5/docs/current/user-guide/#extensions-registration-automatic) functionality (`-Djunit.jupiter.extensions.autodetection.enabled=true`), but I don't like the risk that some other obscure test dependency will then magically start applying its own extension to my tests.  I'd prefer to retain 100% control of exactly what I enable, it's just quite verbose with annotations on every class at the moment.

Another option is to have a single TestBase which all other tests inherit from, but it's very easy to accidentally forget to use this when writing a new test.

## Proposal

My suggestion would be to allow people to write a `package-info.java`:

```java
@ExtendWith(CircleCiShardingExtension.class)
package com.foo.bar;
```

I'm imagining this would apply the extension to all tests within this package. This satisfies my goals because:

- I don't have to enable magical auto-registration, so dependency changes can't change the behaviour of my tests
- newly authored test classes will just 'do the right thing' without devs having to remember to my `@CircleCiSharding` annotation



# 188 this is title
We were using ant Junit4 task to run our tests and we migrated to Junit platform console launcher, but we are experiencing some stdout/stderr loss.

I added the proper configuration settings as advised in the documentation:

```
<sysproperty key="junit.platform.output.capture.stdout" value="true"/>
<sysproperty key="junit.platform.output.capture.stderr" value="true"/>
```


But there is still some stdout/stderr loss compared to our reports before the change. My initial assumption is that I do not have a proper test listener in place but isn’t the launcher having some default listener that receives the stdout/stderr? (we cannot use the ant junitlauncher as it does not support jacoco configuration)

What am I missing? Can I still use the launcher and get the generous stdout/stderr as in Junit4 ant task


Old ANT task:

  ```
<macrodef name="test.executor">
    <attribute name="suite"/>
    <attribute name="test.jvm.classpath"/>
    <attribute name="server.jvm.classpath" default=""/>
    <attribute name="license.file" default="${server.license.file}"/>
    <attribute name="license.directory" default="${server.license.directory}"/>
    <attribute name="extra.server.classpath" default=""/>
    <attribute name="category" default="nocategory"/>
    <attribute name="exclude.category" default=""/>
    <attribute name="run.jacoco.reporter" default="true"/>
    <attribute name="junit.print.summary.option" default="${junit.task.print.summary.option}"/>
    <attribute name="maxmemory" default="${junit.maxmemory}"/>
    <sequential>

      <split-by-dot-and-get-the-last-item input.string="@{category}"
        result.project.property="trimmed.category"/>
      <mkdir dir="${basedir}/${trimmed.category}/@{suite}"/>

      <local name="generate.event.uid"/>
      <condition property="generate.event.uid" value="true" else="false">
        <contains string="@{suite}"
          substring="TraceLoggerClientGenerateUUIDTest"/>
      </condition>

      <jacoco:coverage destfile="${basedir}/${trimmed.category}/@{suite}/jacoco.exec" append="true">
        <junit showoutput="true" printsummary="@{junit.print.summary.option}" fork="yes"
          maxmemory="@{maxmemory}"
          dir="${basedir}/${trimmed.category}/@{suite}" haltonfailure="${haltonfailure}"
          logfailedtests="true">
          <sysproperty key="java.io.tmpdir" value="${custom.java.tmp.dir}"/>
          <sysproperty key="DOCKER_TEST_SERVER" value="${docker.test.server}"/>
          <sysproperty key="DOCKER_IMAGE_VERSION" value="${docker.image.version}"/>
          <sysproperty key="DOCKER_HOST" value="${docker.host}"/>
          <sysproperty key="DOCKER_ADAPTER" value="${docker.adapter}"/>
          <sysproperty key="DOCKER_IMAGE_REPOSITORY_URL" value="${docker.image.repository.url}"/>
          <formatter type="xml"/>
          <jvmarg line="${jvm.args}"/>
          <jvmarg value="-XX:+HeapDumpOnOutOfMemoryError"/>
          <jvmarg value="-XX:HeapDumpPath=${basedir}"/>
          <jvmarg value="-Dnirvana.test.requiredCategories=@{category}"/>
          <jvmarg value="-Dnirvana.test.excludeCategories=@{exclude.category}"/>
          <jvmarg value="-Djava.io.tmpdir=${custom.java.tmp.dir}"/>
          <jvmarg value="-DLOGLEVEL=${log.level}"/>
          <jvmarg value="-DTESTLOGLEVEL=${test.log.level}"/>
          <jvmarg value="-DTESTLOGFILELEVEL=${test.log.file.level}"/>
          <jvmarg value="-DEnableDebug=${debug.flag}"/>
          <jvmarg value="-DLICENCE_DIR=@{license.directory}"/>
          <jvmarg value="-DLICENCE_FILE=@{license.file}"/>
          <jvmarg value="-DPROJECT_ROOT_FOLDER=${project.root}"/>
          <jvmarg value="-DTEST_WORKING_DIR=${basedir}/${trimmed.category}/@{suite}"/>
          <jvmarg value="-DJUnitBasePort=${junit.base.port}"/>
          <jvmarg value="-DFAILON_SESSION_LEAKS=${check.session.leaks}"/>
          <jvmarg
            value="-Dnirvana.test.server.classpath_extra=@{server.jvm.classpath}${path.separator}@{extra.server.classpath}"/>
          <jvmarg value="-Dnirvana.test.server.classpath_nostd=yes"/>
          <jvmarg value="-DGETCOVERAGE=${server.code.coverage.option}"/>
          <jvmarg value="-DJACOCO_PATH=${jacocoagent.location}"/>
          <jvmarg value="-Dcom.softwareag.um.client.GenerateEventUID=${generate.event.uid}"/>
          <classpath>
            <pathelement path="@{test.jvm.classpath}"/>
            <pathelement path="@{server.jvm.classpath}"/>
          </classpath>
          <test name="@{suite}" todir="${basedir}/${trimmed.category}/@{suite}"
            outfile="TEST-@{suite}-${current.os}">
            <formatter type="xml"/>
          </test>
        </junit>
      </jacoco:coverage>
      <jacoco.reporter
        reporting.dir="${basedir}/${trimmed.category}/@{suite}"
        suite="@{suite}"
        category="${trimmed.category}"
        run.reporter="@{run.jacoco.reporter}"/>
    </sequential>
  </macrodef>
```

New ANT task (using junit-platform-console-standalone-1.5.2.jar):

```
<macrodef name="console.runner">
    <attribute name="console.arguments" default=""/>
    <attribute name="max.memory" default=""/>
    <attribute name="jvm.args" default=""/>
    <attribute name="test.jvm.classpath" default="${test.jvm.classpath}"/>
    <attribute name="server.jvm.classpath" default="${server.jvm.classpath}"/>
    <attribute name="license.file" default="${server.license.file}"/>
    <attribute name="license.directory" default="${server.license.directory}"/>
    <attribute name="extra.server.classpath" default=""/>
    <attribute name="fail.if.no.tests" default="true"/>
    <attribute name="fail.on.error" default="false"/>
    <attribute name="maxmemory" default="${junit.maxmemory}"/>
    <attribute name="reporting.dir" default="${basedir}"/>
    <attribute name="identifier" default=""/>
    <attribute name="jupiter.engine.timeout.milliseconds" default="600000"/>
    <sequential>

      <path id="discovery.path">
        <fileset dir="${project.root}/jars">
          <include name="*.jar"/>
        </fileset>
      </path>
      <local name="test.discovery.classpath"/>
      <pathconvert property="test.discovery.classpath" refid="discovery.path"/>

      <mkdir dir="@{reporting.dir}"/>
      <jacoco:coverage destfile="@{reporting.dir}/@{identifier}.exec"
        append="true">

        <java fork="true"
          failonerror="@{fail.on.error}"
          append="true"
          maxmemory="@{max.memory}"
          classname="org.junit.platform.console.ConsoleLauncher"
          dir="@{reporting.dir}">

          <sysproperty key="junit.platform.output.capture.stdout" value="true"/>
          <sysproperty key="junit.platform.output.capture.stderr" value="true"/>

          <sysproperty key="DOCKER_TEST_SERVER" value="${docker.test.server}"/>
          <sysproperty key="DOCKER_IMAGE_VERSION" value="${docker.image.version}"/>
          <sysproperty key="DOCKER_HOST" value="${docker.host}"/>
          <sysproperty key="DOCKER_ADAPTER" value="${docker.adapter}"/>
          <sysproperty key="DOCKER_IMAGE_REPOSITORY_URL" value="${docker.image.repository.url}"/>
          <sysproperty key="junit.jupiter.execution.timeout.default"
            value="@{jupiter.engine.timeout.milliseconds}"/>

          <arg
            line=" --disable-ansi-colors --details-theme=ascii --details=tree --fail-if-no-tests=@{fail.if.no.tests} --reports-dir=@{reporting.dir} --classpath=${test.discovery.classpath}@{console.arguments}"/>

          <jvmarg line="${jvm.args}"/>
          <jvmarg line="@{jvm.args}"/>
          <jvmarg value="-XX:+HeapDumpOnOutOfMemoryError"/>
          <jvmarg value="-XX:HeapDumpPath=${basedir}"/>
          <jvmarg value="-Djava.io.tmpdir=${custom.java.tmp.dir}"/>
          <jvmarg value="-DLOGLEVEL=${log.level}"/>
          <jvmarg value="-DTESTLOGLEVEL=${test.log.level}"/>
          <jvmarg value="-DTESTLOGFILELEVEL=${test.log.file.level}"/>
          <jvmarg value="-DEnableDebug=${debug.flag}"/>
          <jvmarg value="-DLICENCE_DIR=@{license.directory}"/>
          <jvmarg value="-DLICENCE_FILE=@{license.file}"/>
          <jvmarg value="-DPROJECT_ROOT_FOLDER=${project.root}"/>
          <jvmarg value="-DJUnitBasePort=${junit.base.port}"/>
          <jvmarg value="-DFAILON_SESSION_LEAKS=${check.session.leaks}"/>
          <jvmarg
            value="-Dnirvana.test.server.classpath_extra=@{server.jvm.classpath}${path.separator}@{extra.server.classpath}"/>
          <jvmarg value="-Dnirvana.test.server.classpath_nostd=yes"/>
          <jvmarg value="-DGETCOVERAGE=${server.code.coverage.option}"/>
          <jvmarg value="-DJACOCO_PATH=${jacocoagent.location}"/>

          <classpath>
            <pathelement location="${console.runner.location}"/>
            <pathelement path="@{test.jvm.classpath}"/>
            <pathelement path="@{server.jvm.classpath}"/>
          </classpath>

        </java>
      </jacoco:coverage>
    </sequential>
  </macrodef>
```


Sample output files:

Using the JunitPlatform with the proper config options in place (49,6 KB): 
[TEST-JmsMessageIdFailoverTest-windows_JunitPlatform_stdout_stderr_options_added.txt](https://github.com/junit-team/junit5/files/4627014/TEST-JmsMessageIdFailoverTest-windows_JunitPlatform_stdout_stderr_options_added.txt)

Using the JunitPlatform without the proper config options (48,6 KB): 
[TEST-JmsMessageIdFailoverTest-windows_JunitPlatform_no_sterr_stdout_options.txt](https://github.com/junit-team/junit5/files/4627016/TEST-JmsMessageIdFailoverTest-windows_JunitPlatform_no_sterr_stdout_options.txt)

Using old school junit4 ant task (378 KB): 
[TEST-com.pcbsys.nirvana.nAdminAPI.cluster.failover.JmsMessageIdFailoverTest-windows_junit4_ant_task.txt](https://github.com/junit-team/junit5/files/4627015/TEST-com.pcbsys.nirvana.nAdminAPI.cluster.failover.JmsMessageIdFailoverTest-windows_junit4_ant_task.txt)



# 189 this is title
## Overview

`IsTestMethod` and `IsTestTemplateMethod` currently validate that `@Test` and `@TestTemplate` methods have a `void` return type; however, `IsTestFactoryMethod` only validates that `@TestFactory` methods do _not_ have a `void` return type. Consequently, `@TestFactory` return types are not validated during the discovery phase.

On the other hand, `@TestFactory` return types are in fact validated during the execution phase, but this is late and inconsistent with the behavior for all other types of _testable_ methods.

## Related Issues

- #242 
- #835 

## Deliverables

- [ ] Move `@TestFactory` method return type validation from `TestFactoryTestDescriptor` to `IsTestFactoryMethod`.
- [ ] Enable `@Disabled` tests in `IsTestFactoryMethodTests`.




# 190 this is title
## Status Quo

JUnit Jupiter 5.0.0-M4 introduced generic support for test templates and concrete support for repeated and parameterized tests. The latter also include support for custom display names with placeholders.

For example, `@RepeatedTest` supports `{displayName}`, `{currentRepetition}`, and `{totalRepetitions}`; whereas, `@ParameterizedTest` supports `{index}`, `{arguments}`, and `{#}` (where `#` is the current argument index: 1, 2, 3, etc.).

## Considerations

- `{displayName}` could also be supported by `@ParameterizedTest`.
- `{displayName}` and `{index}` could be supported generically for `@TestTemplate`.

## Deliverables

- [ ] Determine if any new placeholders would be useful with test templates, in addition to the placeholders already supported by `@RepeatedTest` and `@ParameterizedTest`.
- [ ] Determine which placeholders are _common_ to all test templates.
- [ ] Support all _common_ placeholders in all custom display name patterns for all test templates.




# 191 this is title
## Overview

Using: JUnit: 5.2.0

Great job on the new `ParameterizedTest` support in v.5. The replacement of the static, one-per-class Parameters annotation with more flexible `MethodSource`, etc. has been like a breath of fresh air and allowed me to remove thousands (!!) of lines of supporting code from my system. I'm really loving it.
However, someone decided to disallow zero parameters with this precondition check in `ParameterizedTestExtension`.

```java
.onClose(() ->
    Preconditions.condition(invocationCount.get() > 0,
    "Configuration error: You must provide at least one argument for this @ParameterizedTest"));
```

The problem with this is that we have some testing situations where parameterized tests with zero parameters are not exceptional. For example, we run tests against thousands of a certain type of class generically against a database of past production failures, and many of these classes have never experienced a production failure. When the tests are run, we now get failures due the above precondition check. JUnit 4 handled this cleanly: it would simply not run any tests on those classes.

## Workaround

I can get around this by adding a `null` to the method creating the collection of parameters if it is empty, and then return from the beginning of the `@ParameterizedTest` method code if the passed parameter is `null`. That lets us continue to run the parameterized tests against all of the classes, but comes with some disadvantages:

- We must add specific code to the front and back of every parameterized pair just to avoid a failure that doesn't matter to the tests.
- The handling of the `null` causes the test count inflation for these "phantom" tests.
- `null` is now reserved as a signal for no parameters, rather than something wrong in the parameter creation.

## Proposal

If nobody has any strong feelings about disallowing the no-parameter case, can we just have this precondition removed from a future version?

Thanks.



# 192 this is title
Hi, I tried to set up timeouts for extension methods (`BeforeAllCallback` or `AfterEachCallback`) by using the `@Timeout` annotation with it, but it didn't work.

Also I've tried to set global timeouts such us `junit.jupiter.execution.timeout.aftereach.method.default`, and this also hasn't worked. 

It would be great to see this feature in JUnit 5 next releases.




# 193 this is title
## Overview

<!-- Please describe your changes here and list any open questions you might have. -->

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [x] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [x] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 194 this is title
## Actual behavior

I have a JUnit extension which implements the `TestInstancePostProcessor` and `TestInstancePreDestroyCallback`. When using this extension for a test class with inner nested test classes, if the lifecycle of the enclosing class is `PER_METHOD`, then an instance of the enclosing class is created for the tests in the nested class, as well as a nested instance for each or all of the tests (depending on the lifecycle of the nested class). The post-process hook is then called for the enclosing instance and the nested instances, but the pre-destroy hook is only called for the nested instances and not for the enclosing instance.

## Expected behavior

The post-process and pre-destroy hooks are called both for the nested instances as well as for the enclosing instance.

## Steps to reproduce

Example test which shows the behavior:
```java
@ExtendWith(OuterTests.LifecycleExtension.class)
class OuterTests {
    @Test
    void testOuter1() {
        System.out.println("testOuter1");
    }

    @Test
    void testOuter2() {
        System.out.println("testOuter2");
    }

    @Nested
    class InnerTests {
        @Test
        void testInner1() {
            System.out.println("testInner1");
        }

        @Test
        void testInner2() {
            System.out.println("testInner2");
        }
    }

    static class LifecycleExtension implements TestInstancePostProcessor, TestInstancePreDestroyCallback {
        @Override
        public void postProcessTestInstance(Object testInstance, ExtensionContext context) {
            System.out.println("postProcess: " + testInstance);
        }

        @Override
        public void preDestroyTestInstance(ExtensionContext context) {
            System.out.println("preDestroy: " + context.getRequiredTestInstance());
        }
    }
}
```

Output for lifecycle = PER_METHOD for outer and inner class (indentations for better readability):
```
postProcess: mypackage.OuterTests@7bedc48a
-- testOuter1
preDestroy: mypackage.OuterTests@7bedc48a

postProcess: mypackage.OuterTests@38e79ae3
-- testOuter2
preDestroy: mypackage.OuterTests@38e79ae3

postProcess: mypackage.OuterTests@63070bab
-- postProcess: mypackage.OuterTests$InnerTests@291b4bf5
---- testInner1
-- preDestroy: mypackage.OuterTests$InnerTests@291b4bf5

postProcess: mypackage.OuterTests@2d2ffcb7
-- postProcess: mypackage.OuterTests$InnerTests@762ef0ea
---- testInner2
-- preDestroy: mypackage.OuterTests$InnerTests@762ef0ea
```

Output for lifecycle = PER_CLASS for outer and inner class (indentations for better readability):
```
postProcess: mypackage.OuterTests@fa4c865
-- testOuter1
-- testOuter2

-- postProcess: mypackage.OuterTests$InnerTests@2d2ffcb7
---- testInner1
---- testInner2
-- preDestroy: mypackage.OuterTests$InnerTests@2d2ffcb7
preDestroy: mypackage.OuterTests@fa4c865
```

## Context

 - Used versions (Jupiter/Vintage/Platform): JUnit Jupiter 5.7.0
 - Build Tool/IDE: Maven 3.6.3, IntelliJ IDEA 2020.2, OpenJDK 11



# 195 this is title
Given the code

```java
import org.junit.jupiter.api.*;

@Disabled
class DisabledTest {
    @Disabled
    @Test
    void testIgnorance() throws Exception {
        Assertions.assertEquals("1", "1", "strings doesn't match");
        System.out.println("Assertion performed");
    }
    @Test
    void shouldBeExecuted() throws Exception {
        Assertions.assertTrue(true, "True is always true");
    }
}
```

When user runs `testIgnorance`, IDEA disables the `DisabledCondition` and allows to run the test. Works as it was in JUnit 4. But when user runs the whole class, the same idea not really works: the disabled method also runs. I don't see how to influence the discovery mechanism to ignore `@Disabled` annotations differently. Please correct me if I am wrong.

On the other hand, from the point of JUnit 5 itself: storing information of the entry point (discovery selector root, when exactly one) and then using this information to ignore top level annotations looks not that strange (though it's strange of cause). What do you think?



# 196 this is title
## Overview

Various logging frameworks have mechanisms for test configuration. For example, log4j2 supports a `log4j2-test.xml` file in the root of the classpath, which people typically store under `src/test/resources`.

Java Util Logging (JUL) on the other hand has no mechanism for automatic discovery of test configuration. One can of course set the `java.util.logging.config.file` JVM system property, but that can be cumbersome since one would have to set it for every single run configuration within an IDE.

For the Spring Framework, I introduced a JUnit Platform `TestExecutionListener` that automatically looks for a file named `jul-test.properties` in the root of the classpath and used it to configure JUL. See this commit for details: https://github.com/spring-projects/spring-framework/commit/89b3a9cef218c0d6ff3121d3f0c386b0c2f06dbc

## Deliverables

- [ ] Decide if it would be useful to introduce such a `TestExecutionListener` as an opt-in feature of the JUnit Platform.




# 197 this is title
<!-- Start by telling us what problem you’re trying to solve. Often a solution already exists! Please, don’t send pull requests to implement new features without first getting our support. -->

I have a shared base class with a couple of `@Test` methods (like [this one](https://github.com/sewe/junit5-samples/blob/reproducer/junit5-jupiter-starter-gradle/src/test/java/com/example/BaseClass.java)).

Now suppose the `TestInfo` object injected into the test methods should be used to derive unique, test-specific directory names.

Unfortunately, no combination of `TestInfo.getTestClass()` and `TestInfo.getTestMethod()` does the trick, at least not for `@Nested` tests, as their `TestInfo.getTestClass()` is the base class, not the concrete subclass.

Consider [this reproducer](https://github.com/sewe/junit5-samples/commit/e4d905db390c371aedd3c56495c9c5cc3a84bc8c#diff-a349a9b76e6a99bbcce3b1d8711f2dbabe8c4fe238845e286629a7ea3344e2df) based on [junit5-samples](https://github.com/junit-team/junit5-samples):

```java
abstract class BaseClass {

    @Test
    void test(TestInfo testInfo) {
        String actualName = testInfo.getTestClass().get().getName();
        Assertions.assertTrue(actualName.matches("com.example.Example[123]Test"), actualName);
    }

    @Nested
    class NestedClass {

        @Test
        void nestedTest(TestInfo testInfo) {
            String actualName = testInfo.getTestClass().get().getName();
            Assertions.assertTrue(actualName.matches("com.example.Example[123]Test\\$NestedClass"), actualName);
        }
    }
}
```

```java
class Example1Test extends BaseClass { }
```

```java
class Example2Test extends BaseClass { }
```

While the test class for the two invocations of `BaseClass.test` is `Example1Test` and `Example2Test`, respectively, for the two invocations of `BaseClass.NestedClass.nestedTest` it is in both cases `BaseClass.NestedClass` (making `nestedTest` fail as written). This means that `TestInfo.getTestClass()` is unusable for deriving the name of a test-specific directory.

```
[INFO] Running com.example.Example1Test
[ERROR] Tests run: 2, Failures: 1, Errors: 0, Skipped: 0, Time elapsed: 0.001 s <<< FAILURE! - in com.example.Example1Test
[ERROR] nestedTest{TestInfo}  Time elapsed: 0.001 s  <<< FAILURE!
org.opentest4j.AssertionFailedError: com.example.BaseClass$NestedClass ==> expected: <true> but was: <false>
	at com.example.BaseClass$NestedClass.nestedTest(BaseClass.java:22)

[INFO] Running com.example.Example2Test
[ERROR] Tests run: 2, Failures: 1, Errors: 0, Skipped: 0, Time elapsed: 0.025 s <<< FAILURE! - in com.example.Example2Test
[ERROR] nestedTest{TestInfo}  Time elapsed: 0.006 s  <<< FAILURE!
org.opentest4j.AssertionFailedError: com.example.BaseClass$NestedClass ==> expected: <true> but was: <false>
	at com.example.BaseClass$NestedClass.nestedTest(BaseClass.java:22)
```

## Deliverables

I would hence like to see some alternative to `TestInfo.getTestClass()` (`getInvokedClass()` perhaps?), that changes based on the class that is "invoked" (for lack of a better name) by the test runner, not the class where the test method ultimately executed resides.

Alternatively, since for non-`@Nested` tests, `getTestClass()` already behaves as expected by me, it's behavior might be (incompatibly) changed for `@Nested` tests.

## Considered Alternatives

`@TempDir` is unfortunately not an alternative, for two reasons:
- The test-specific directories MUST to be created below a specific directory
- The directory names SHOULD be human-readable and easily correlatable to the tests; what `@TempDir` produces is too cryptic.



# 198 this is title
In Junit 5 how can I register an extension programmatically without doing it per-test. I'm currently using the java services mechanism which is activated by the system property junit.jupiter.extensions.autodetection.enabled, but I'm trying to achieve the same as a JVM system wide without using the services mechanism.

```
import mockwebserver3.MockWebServer
import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.extension.RegisterExtension
import org.junit.jupiter.engine.JupiterTestEngine
import org.junit.platform.console.options.Theme
import org.junit.platform.engine.TestEngine
import org.junit.platform.engine.discovery.DiscoverySelectors.selectClass
import org.junit.platform.launcher.Launcher
import org.junit.platform.launcher.LauncherDiscoveryRequest
import org.junit.platform.launcher.PostDiscoveryFilter
import org.junit.platform.launcher.TestExecutionListener
import org.junit.platform.launcher.core.LauncherConfig
import org.junit.platform.launcher.core.LauncherDiscoveryRequestBuilder
import org.junit.platform.launcher.core.LauncherFactory
import org.junit.platform.launcher.listeners.SummaryGeneratingListener
import java.io.PrintWriter
import kotlin.system.exitProcess

class MySampleTest {
  @Test
  fun failingTest(server: MockWebServer) {
    assertThat("hello").isEqualTo("goodbye")
  }
}

fun main() {
  System.setProperty("junit.jupiter.extensions.autodetection.enabled", "true")

  val summaryListener = SummaryGeneratingListener()

  val jupiterTestEngine = JupiterTestEngine()

  val config = LauncherConfig.builder()
    .enableTestExecutionListenerAutoRegistration(false)
    .enableTestEngineAutoRegistration(false)
    .enablePostDiscoveryFilterAutoRegistration(false)
    .addTestEngines(jupiterTestEngine)
    .addTestExecutionListeners(summaryListener, DotListener)
    .build()
  val launcher: Launcher = LauncherFactory.create(config)

  val request: LauncherDiscoveryRequest = LauncherDiscoveryRequestBuilder.request()
    // TODO replace junit.jupiter.extensions.autodetection.enabled with API approach.
//    .enableImplicitConfigurationParameters(false)
    .selectors(selectClass(MySampleTest::class.java))
    .build()

  val result = launcher.execute(request)

  val summary = summaryListener.summary
  summary.printTo(PrintWriter(System.out))

  exitProcess(if (summary.testsFailedCount != 0L) -1 else 0)
}
```



# 199 this is title
## Overview

As I'm working on https://github.com/junit-team/junit5/pull/961, I've come to realise that the `build.gradle` file could be organised better, as I'm currently having to jump about and edit disparate lines in the file just to import error-prone and get it working properly on both JDK 8 and JDK 9.

Consider organising the Gradle build in a similar fashion to [Caffeine](https://github.com/ben-manes/caffeine)'s, where dependencies, code quality tools, publishing functions etc. are extracted into their own `gradle/*.gradle` sub-scripts, which are then imported into the project's other `.gradle` files as needed.

## Deliverables

- [ ] ` build.gradle` is broken down into sub-scripts as appropriate.




# 200 this is title
When the `ParameterResolver`'s `supports()` and `resolve()` methods were changed to use `ParameterContext`, the statement that the `Parameter` was never `null` was replaced by text that stated `ParamterResolver` is never null.  `ParameterResolver` itself makes no assertion that [getParameter()](https://junit.ci.cloudbees.com/job/JUnit5/javadoc/org/junit/jupiter/api/extension/ParameterContext.html#getParameter) always returns a non-null value.  Thus, I'm now checking for null parameters as follows:

```java
    boolean supported = false;
    Parameter parameter = parameterContext.getParameter();
    if (parameter != null && Performance.class.equals(parameter.getType())) {
      supported = true;
    }
    return supported;
```

For the `ParameterContext`, it wouldn't make sense to ever have a non-null parameter (otherwise it would be a `SomethingElseContext`), so this code is probably completely unnecessary.  As a defensive coder, I put it in anyway.  Here are my recommendations in order of priority/complexity:

-   [ ] For every returned value, explicitly state in the Javadoc whether or not the return type may be null.
-   [ ] Globally use `Optional` when a return type might be `null`.
-   [ ] State in the User Guide that no public APIs ever return `null`.
-   [ ] Add the JSR-305 annotation library with a provided scope and add `@CheckForNull`, `@Nonnull` and `@Nullable` to all public APIs.

I know the JUnit team's policy on avoiding dependencies - adding JSR-305 as provided allows those of us who chose to perform static analysis on our Engine, Extension and test code to choose to add the dependency to our classpath.

## Related Resources

- There is additional detail in #741.
- [SPR-15540](https://jira.spring.io/browse/SPR-15540) and the [related commit](https://github.com/spring-projects/spring-framework/commit/f813712f5b413b354560cd7cc006352e9defa9a3).



# 201 this is title
## Overview

Follow-up from #1557 which introduced a warning when a TestEngine ID starts with `junit-`, except those published by the JUnit Team from the JUnit 5 repository for public consumption.

## Deliverables

- [ ] Ignore such engines




# 202 this is title
Motivation: https://github.com/junit-team/junit5/pull/1768#issuecomment-473538214

Using a proof-of-concept implementation...
![image](https://user-images.githubusercontent.com/2319838/54489542-a2d63480-48ad-11e9-80fa-fb0aabe5aff3.png)

...yields
![image](https://user-images.githubusercontent.com/2319838/54489559-cd27f200-48ad-11e9-85eb-a28218821a97.png)

## Related Issues

- #703 
- #1515




# 203 this is title
## Overview

With dynamic tests in large classes (`TestClass`) it is difficult to find out where they were actually defined.
The containing/declaring method (`testMethod()`) helps to get a rough understanding of the source of the test and assertion stacktrace shows where it went wrong, but dynamic tests are meant to test different setups/environment/instances and might be generated/inherited from a different method or class, so it would be nice if double-clicking the test would show the actual source (`"setup3"`) of the dynamic test.

## Usage-Example

- ❌ TestClass (a)
  - ❌ testMethod (b)
    - ✔️ setup1
    - ✔️ setup2
    - ❌ setup3 `<-- This is where I (probably) need to do things`
    - ✔️ setup4

````java
class TestClass {

    @TestFactory
    List<DynamicTest> testMethod() {
        return asList(

                dynamicTest("setup1", () -> { // Might be created in a factory method
                        // [...]
                }),

                dynamicTest("setup2", () -> { // or inherited from a parent class
                        // [...]
                }),

                dynamicTest("setup3", () -> { // <--- I wish to get here (wherever "here" might be, e.g. in another/super method or class)
                        // [...]
                       assert(foo, bar); // The assertion fails here
                        // [...]
                }),

                dynamicTest("setup4", () -> {
                        // [...]
                }),

        ).map(this::resetMocks);
    }

}
````

## Content

This PR adds a `TestSourceLocator` that automatically calculates a testSourceUri if none is specified.
It isn't a finished implementation yet (It does what I believe it should do, but eclipse doesn't seem to be support it yet)
but I would like to start a discussion regarding this feature request.

I also considered creating an issue for that first, but IMO actual code is more expressive.

## Next steps

1. Discussion whether the feature request gets conceptually accepted
2. Convert to an actual PR with tests
3. Wait for merge
4. Add support to IDEs (if necessary)

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [x] There are no TODOs left in the code
- [x] Method [preconditions](https://junit.org/junit5/docs/snapshot/api/org.junit.platform.commons/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [x] [Coding conventions](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [x] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/HEAD/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](https://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](https://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [x] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 204 this is title
We are providing a test suite for our applications as Spring Boot application. The test suite is basically a set of regular JUnit 5 tests that are launched in the Spring Boot application.
The application is packaged as Spring Boot JAR (created with the `spring-boot-maven-plugin`).

We do now have the problem, that the tests are not found when we are using `DiscoverySelectors.selectPackage()` and run the application as Spring Boot JAR. Everything works fine, when we select the tests by classname. Executing the application within an IDE works fine as well.

The problem seems to be in `ClasspathScanner#findClassesForPath())`. `Files.walkFileTree()` does not work with nested JAR files. A similar problem was already reported in #399.

## Steps to reproduce
I created a [project on GitHub](https://github.com/ferstl/junit5-spring-boot) to reproduce this issue. When the `Application` is run within the IDE, everything works fine. When it is executed as Spring Boot JAR, the test is not found.

## Context

 - Used versions (Jupiter/Vintage/Platform): junit-bom 5.3.2
 - Build Tool/IDE: Maven, OpenJDK11, IntelliJ
- Spring Boot: 2.1.1.RELEASE




# 205 this is title
## Overview

I have seen a jmh warning about ```fork=0``` and found the [too long command line on Windows has been fixed](https://github.com/melix/jmh-gradle-plugin/issues/107).

This patch set ```fork=1```.

Remark : I have not tested on Windows

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [ ] There are no TODOs left in the code
- [ ] Method [preconditions](http://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [ ] [Coding conventions](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#javadoc) and [`@API` annotations](http://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/meta/API.html)
- [ ] Change is documented in the [User Guide](http://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](http://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 206 this is title
The `TestPlan` returned by `Launcher.discover()` and passed to `TestExecutionListener.testPlanStarted()` is currently modifiable for backwards compatibility (see #1695 for background).

This issue is used to track progress of tool adoption so the JUnit team can decide when it's safe to ignore/forbid modification of `TestPlan`.



# 207 this is title
Like `@TestMethodOrder`, could you please introduce a `@TestClassOrder` annotation to define the execution order of test classes?




# 208 this is title
I've just had my first attempt to use `TestFactory` "in anger". The idea is to take the output from EngineTestKit, rebuild the `TestDescriptor` hierarchy generated by the testkit run, and transform that hierarchy into a series of dynamic tests and containers. In this way, individual failures inside the testkit run will be directly reported in the top-level testing framework rather than swallowed up in the low-level test run and only reported "in aggregate" at the top-level.

Anyway, while implementing this I discovered that while `TestDescriptor`s in a JUnit Platform test hierarchy can be _both_ a container and a test, in the dynamic testing interface these are mutually exclusive - a DynamicNode can be ~both~ either  a `DynamicTest` or a `DynamicContainer`, but not both. It seems to me to be a bit of a capability gap in the dynamic testing interface that it can't generate dynamic test nodes that cover the full gamut of functionality available in `TestDescriptor`s. 

For a real-world example of a test hierarchy with a TestDescriptor that is both a container and a test, consider the case in Jupiter (or JUnit 4) where a test class has several test methods that all pass, but then it has an `@AfterAll/@AfterClass`-annotated method that throws an exception (this is the exact real-world situation I encountered in my experiment above and led to this feature request). 

In my case, I have a workaround - to add a `DynamicTest` child to the `DynamicContainer` that represents my `TestDescriptor` container, which carries the execution state of the `TestDescriptor` container. However, IMO it is visually not quite as nice as how (eg) a failed `@AfterAll` method is represented in the regular hierarchy, and (again IMO) it would be nice if testing developers had the option.

## Deliverables

A few of options:
* Add an optional `Executable` property to `DynamicContainer`.
* Add optional children property to `DynamicTest`.
* Come up with a third class `DynamicContainerTest` that requires both properties. If `DynamicTest` and `DynamicContainer` had been interfaces this could have simply been through multiple inheritance (which would probably have been the best option) but I think that ship has sailed...

_Edit: fixed potentially confusing typo_



# 209 this is title
This is a specific sub-issue of #806.

I've been adapting JUnit Platform to run in an OSGi environment as part of the Bndtools project (see bndtools/bnd#3145). This project consists of a `BundleEngine` which discovers test bundles in the running OSGi framework, and then delegates to other TestEngines it finds in the environment for each such bundle that it finds.

It became apparent during this implementation that the discovery selectors that do class loading (eg, selectClass(String) and selectMethod(String, String)) ideally needed variants that allowed you to explicitly specify the classloader, rather than always using the default classloader. I had to write a fair bit of code to work around the lack of such a feature when I implemented `BundleEngine`.

The call to `ReflectionUtils.tryToLoadClass(String)`:

https://github.com/junit-team/junit5/blob/cfe9a9928a6c040e8fd6edf96ed70e7eaac94a80/junit-platform-engine/src/main/java/org/junit/platform/engine/discovery/ClassSelector.java#L74-L76

...could then simply be replaced with a call to the `ReflectionUtils.tryToLoadClass(String, ClassLoader)` variant (and possibly update the precondition error message to indicate which classloader it used to try and load the class).

For backwards compatibility, if the classloader is not explicitly specified, simply use the default classloader (current behaviour).



# 210 this is title
Current `BeforeEachCallback` and `BeforeTestExecutionCallback` are invoked after ArgumentProvider finished. Would be either add more methods to the existing callbacks or to create a new callback that would run before the ArgumentProvider starts.

*Rationale*: in my extension I'd like to impact how the data is generated in the ArgumentProviders (I'm interested in `@MethodSource` in particular). So that it's possible to set the seed for randomization that happens in the `@MethodSource`.



# 211 this is title
## Overview

There doesn't seem to be a way for developers who aren't using Maven to download JUnit 5 and reference it from their projects.  Am I missing something, or is this something that JUnit doesn't support as yet?

## Deliverables

A method of downloading JUnit and getting it running in a Java build system which doesn't use Maven.



# 212 this is title
I'm trying to update [CDI-Unit](http://bryncooke.github.io/cdi-unit) to [support JUnit 5](https://github.com/BrynCooke/cdi-unit/issues/103), specifically CDI-Unit's [`ProducerConfig` feature for JUnit 4](https://github.com/BrynCooke/cdi-unit/blob/805e077660d7d609b24b0d2b8dc1fa264ad30082/cdi-unit/src/test/java/org/jglue/cdiunit/TestProducerConfig.java) which uses annotations on the test method to help configure the deployment payload for Weld. Weld is then used to construct test instances. This can almost be replicated in JUnit 5, by implementing a `TestInstanceFactory`.  (Obviously this won't be compatible with `Lifecycle.PER_CLASS`, because the instances must allow for per-method configuration.)

The problem is, when `TestInstanceFactory.createTestInstance()` is called, `extensionContext.getTestMethod()` always returns `Optional.empty()`, even when using `Lifecycle.PER_METHOD`.

If the `TestInstanceFactory` were to receive the test Method, when using `Lifecycle.PER_METHOD`, it would be possible to use annotations from the test method to control test instance creation, thus allowing features like `ProducerConfig` to be created.



# 213 this is title
As a follow-up to #2343:

In our `DynamicNodeGenerator` implementation, we had to jump through some hoops to re-create the test hierarchy, as the information is not directly provided by the testkit's `EngineExecutionResults`. I think it would be useful if `EngineExecutionResults` provided access to the following:

1. Access to the root `TestDescriptor` generated by the execution run;
2. A mapping function which, when supplied with a `TestDescriptor` instance, will return the corresponding `TestExecutionResult` instance generated for that test.

For example:

```java
public class EngineExecutionResults {
  public TestDescriptor getRootDescriptor() {...}

  public TestExecutionResult getResultFor(TestDescriptor test) {...}

  // Although we didn't have a need for it, the following two would be useful in other cases too:
  public ReportEntry getReportEntryFor(TestDescriptor test) {...}

  public String getSkippedReasonFor(TestDescriptor test) {...}
}
```

In this way, rather than the meta-test needing to be concerned about verifying the order and correctness of low-level test events (something that I believe that `ExecutionRecorder` should handle directly), they can be more concerned about examining and asserting on the the actual test results (which are more likely to be of interest to a higher-level test). Assertion frameworks like AssertJ and Truth can then also come up with their own custom assertions that operate directly on the test results.



# 214 this is title
I have a series of tests which are rather expensive to set up and build on each other. ATM, I use nested tests like so:

```java
@DisplayName("An empty repository")
class RepositoryTest {

  @BeforeEach
  void setUpEmptyRepository() { /* expensive I/O */ }

  @DisplayName("has no revisions")
  void testGetRevisions() { ... }

  @DisplayName("has no files in head revision")
  void testGetFiles() { ... }

  @Nested
  @DisplayName("after adding a file")
  class WhenFileAdded {

    @BeforeEach
    void addFile() { /* expensive I/O */ }

    @DisplayName("has a single revisions")
    void testGetRevisions() { ... }

    @DisplayName("has the file in its head revision")
    void testGetFiles() { ... }

      @Nested
      @DisplayName("after removing the file again")
      class WhenFileRemovedAgain { /* expensive @BeforeEach */ ... }

      @Nested
      @DisplayName("after adding another file")
      class WhenAnotherFileAdded { /* expensive @BeforeEach */ ... }
  }
}
```

This works, but does expensive set-up operations along each path in the `@Nested` hierarchy over and over again, once for each test method:

- `RepositoryTest`
    - `testGetRevisons`
    - `testGetFiles`
    - `WhenFileAdded`
        - `testGetRevisons`
        - `testGetFiles`
        - `WhenFileRemovedAgain`
            - `testGetRevisons`
            - `testGetFiles`
        - `WhenAnotherFileAdded`
            - `testGetRevisons`
            - `testGetFiles`

Executing `WhenAnotherFileAdded.testGetRevisons` performs the `@BeforeEach` set up for `RepositoryTest`, `WhenFileAdded`, and `WhenAnotherFileAdded`. And  `WhenAnotherFileAdded.testGetFiles` does so **again** – even though the test methods are "read only" (only the set up does heavy I/O).

Unfortunately, switching to `@BeforeAll` for the set-up methods does not work, as in that case the set-up methods are just executed once, not once for each path in the `@Nested` hierarchy.

For example, when executing `WhenAnotherFileAdded.testGetRevisons` it might be that the set-up methods executed are, in this order:

1. `RepositoryTest.setUpEmptyRepository`
2. `WhenFileAdded.setUp`
3. `WhenFileRemoveAgain.setUp`
4. `WhenAnotherFileAdded.setUp`

This is obviously wrong: `WhenFileRemovedAgain.setUp` was meant for a different _branch_ of the `@Nested` hierarchy. Thus the assumption that, say, `WhenAnotherFileAdded.testGetFiles` makes no longer hold, as some file was removed.

It would hence be nice if the behavior of `@BeforeAll`/`@AfterAll` were changed (or at least tweakable) for `@Nested` tests.

I am aware that some amount of set-up work needs to be duplicated, e.g., as both the tests in `RepositoryTest.WhenFileAdded.WhenFileRemovedAgain` and `RepositoryTest.WhenFileAdded.WhenAnotherFileAdded` have some overlap in their nesting context, but it would be nice to at least avoid the set-up for all tests that share the same nesting context (for lack of a better term).

## Deliverables

- [ ] Either switch the behavior of `@BeforeAll` and `@AfterAll` to be executed once for each nesting context (rather than once for each class, regardless of nesting context)
- [ ] Or introduce a new `TestInstance.Lifecycle` constant to switch to such a behavior.



# 215 this is title
I'm using parameterized tests for quite a while now and for the most part they work really intuitive
.
However today I stumbled upon one thing that felt like it should work, but to my initial surprise didn't.
Basically I expected this code to work (in my case it was a `@CsvFileSource`, but doesn't matter):
```
@ParameterizedTest
@CsvSource({"1,a", "1,a,b,c"})
void testAbc(int arg1, String... elements) {
    System.out.println(Arrays.toString(elements));
}
```

I had a quick look at the implementation of the source suppliers and it looks like this ultimately boils down on how an `Argument` instance is "spread" to the individual test method arguments.
And from my testing it seems like any additional arguments are just cut off.
I'd really like to see sort of smart behaviour here: If the last argument of a method is an array (aka varargs) it should try to stuff any trailing arguments into this parameter instead of treating it as a normal object.
I must admit that I don't really know what the implications of such a change are. I can imagine that this might break an extension or two that rely on the current behaviour, but overall I think this could be a quality of life improvement, especially if the varargs argument has a different type than String, like java.time or some other more complex type so the dev doesn't have to manually implement a conversion method.

### Alternative
EDIT: I just learned about argument aggregators, which is more or less the thing I'm describing below (pleasant surpsrise tbh 😅), but I still couldn't find a built-in way of splitting a string and potentially auto-converting it to something else.


I came up with a different solution for my particular problem that goes a little bit further, but allows for consistent behaviour and even more complex argument structures.

Think of a fixed example of my previous code:
```
@ParameterizedTest
@CsvSource({"1,a", "1,a:b:c"})
void testAbc(int arg1, String elements) {
    System.out.println(Arrays.toString(elements.split(":")));
}
```

Basically I ended up splitting the variable arguments on my own, but what if there was an annotation similar to `@ConvertWith`, let's call it `@Split` that accepts an optional separator to further subdivides any argument passed to it? So my example would look like this:
```
@ParameterizedTest
@CsvSource({"1,a", "1,a:b:c"})
void testAbc(int arg1, @Split(':') String[] elements) {
    System.out.println(Arrays.toString(elements));
}
```

The benefit of making such a step explicit is that it allows to use this behaviour more than once inside a method.
If we go one step further in the example we could even allow for nesting to get n dimensional structures:
```
@ParameterizedTest
@CsvSource({"1,a", "1,a.0:b.1:c.3"})
void testAbc(int arg1, @Split(value = ':', sub= @Split('.')) String[][] elements) {
    System.out.println(Arrays.toString(elements));
}
```
Note that in all cases `@Split` is just a special `@ConvertWith` annotation, so they should be interchangeable.

### Conclusion

I ended up writing a custom ArgumentConverter that accepts a string and splits it accordingly, but it would still be nice if JUnit-Params offered such a behaviour out-of-the-box



# 216 this is title
## Overview

As a followup from #664, add an optional caption to describe a test report map entry set like:

`TestReporter.publishEntry("user table", Map.of(...));`

which could yield in `--details tree` mode:
```
   ├─ TestReporterDemo ✔
   │  ├─ reportSingleValue(TestReporter) ✔
   │  │     a key = `a value` @ 2017-03-07T22:12:59.510 
   │  └─ reportSeveralValues(TestReporter) ✔
   │        user table @ 2017-03-07T22:12:59.514
   │           user name  = `dk38`
   │           award year = `1974`
```

## Deliverables

- [ ] Enhance `ReportEntry` to store an optional caption of type `String` and add `void publishEntry(String caption, Map<String, String> values);` to `TestReporter`.
- [ ] Adopt printing of reports to emit the caption, if present.




# 217 this is title
In this code here:

https://github.com/junit-team/junit5/blob/b4fef4a8a01c0bfeb8f008a331ec5dc5a9df0869/junit-platform-commons/src/main/java/org/junit/platform/commons/util/ReflectionUtils.java#L1208-L1215

... the `tryToLoad(String)` method uses the default classloader to attempt to load the parameter class. It would probably make more sense to use the `tryToLoad(String, ClassLoader)` variant, and use `clazz.getClassLoader()` instead, because the test class' methods should resolve from the perspective of the test class itself.

Related to #1987.

## Steps to reproduce

I intend to submit a PR to demonstrate the issue (hopefully along with a fix).

## Context

 - Test discovery clients that use `selectMethod(Class<?>...)` variants for methods with parameters.

## Deliverables

* `selectMethod(Class<?>, String, String)` should work across classloaders.



# 218 this is title
## Overview

Provide a way to have values injected into a class that are created once before any test methods are created.

If your test class has constructor with a parameter annotated with `@PerClass`, then JUnit Jupiter will create it once per run of the test class, using the default constructor of the class (in Kotlin, the primary constructor). That class can have non-static methods annotated with `@BeforeAll`, `@AfterAll`, `@BeforeEach`, or `@AfterEach`.

Here's an example of a class that creates a local database:

```java
    @PerClass
    public class Database {
        @BeforeAll void createDatabase() {
        }
 
        @AfterAll void dropDatabase() {
        }

        @BeforeEach void clearDatabase() {
        }

        public void insert(long id, Account) }{
       }
    }

    class DatabaseTestCase {
      private final Database db;

      DatabaseTestCase(@PerClass Database db) {
        this.db = db;
      }

      @Test
      public void insertAccount() {
        Account account = ...
        db.insert(1, account);
        ...
      }
    }
```

You could think of this as a better version of JUnit4's `ExternalResource` rule.

This could also be used to support `@BeforeAll` in Kotlin tests

```kt
    class SimpleKotlinTestCase constructor(@PerClass db: Database) {
      class Database {
        @BeforeAll fun createDatabase() {
        }
 
        @AfterAll fun dropDatabase() {
        }

        @BeforeEach fun clearDatabase() {
        }

        fun insert(id: Int, account: Account) {
        }
      }

      @Test
      fun insertAccount() {
        val account = ...
        db.insert(1, account);
        ...
      }
    }
```

This could also be used to support integration tests.

## Deliverables

- [ ] ?




# 219 this is title
## Overview

Simple parameter resolution for strings, ints, doubles, longs works in M4, but no longer works in M5 and throws the following exception. 

```
ParameterResolutionException: No ParameterResolver registered for parameter [java.lang.String arg0] in executable
```

Was previously using M4, upgraded to M5 and issue began occurring.

Example:

```java
@ParameterizedTest (name = "{index} [{arguments}] User Flags CONDITION NAME")
@ValueSource(strings = { "dev", "sit" })
@DisplayName("{index} [{arguments}] User Flags CONDITION NAME")
public void testUseTestScenario(String testEnvironment, TestInfo info, TestReporter testReporter) throws Exception {
}
```

Do not get a build exception, get a runtime exception with jUnit5 with gradle 3.5 running in Jenkins.

```
    => org.junit.jupiter.api.extension.ParameterResolutionException: No ParameterResolver registered for parameter [java.lang.String arg0] in executable [public void com.orgname.TestSituation.setUpBeforeEach(java.lang.String,org.junit.jupiter.api.TestInfo,org.junit.jupiter.api.TestReporter) throws java.lang.Exception].
  JUnit Jupiter:TestSituation:User Flags Situation A:2 [sit] User Flags Situation A
    MethodSource [className = 'com.orgname.TestSituation', methodName = 'testSituationA', methodParameterTypes = 'java.lang.String, org.junit.jupiter.api.TestInfo, org.junit.jupiter.api.TestReporter']
    => org.junit.jupiter.api.extension.ParameterResolutionException: No ParameterResolver registered for parameter [java.lang.String arg0] in executable [public void com.orgname.TestSituation.setUpBeforeEach(java.lang.String,org.junit.jupiter.api.TestInfo,org.junit.jupiter.api.TestReporter) throws java.lang.Exception].
```

## Related Issues

- #833 
- #1139
- #1668
- #1884

## Deliverables

- [ ] ...




# 220 this is title
## Overview

As discussed in #981, `ReflectionUtils.findMethod` currently returns the first method that satisfies the signature requirements rather than the method with the most specific (non-generic) matching signature.

This can cause methods with matching generic signatures to be chosen over a matching non-generic signature. This test enforces that a matching non-generic signature is chosen over a matching generic signature.

This PR will fail the build until `ReflectionUtils.findMethod` prioritizes a method with non-generic parameters that satisfy the required signature over a method with generic parameters that satisfies the required signature. 

I think that the issue in the search algorithm lies [here](https://github.com/junit-team/junit5/blob/311bb71a793c07d7e3000a5d32204e0cf598f590/junit-platform-commons/src/main/java/org/junit/platform/commons/util/ReflectionUtils.java#L1237-L1242), where a method with a matching signature is immediately returned, making it ordering sensitive.
Perhaps instead of immediately returning the matching method, all matching methods should be saved and the most specific/non-generic method should be determined and returned?

I'd be happy to try and investigate the possibilities of such a solution.

---

I hereby agree to the terms of the [JUnit Contributor License Agreement](https://github.com/junit-team/junit5/blob/002a0052926ddee57cf90580fa49bc37e5a72427/CONTRIBUTING.md#junit-contributor-license-agreement).

---

### Definition of Done

- [ ] There are no TODOs left in the code
- [ ] Method [preconditions](http://junit.org/junit5/docs/snapshot/api/org/junit/platform/commons/util/Preconditions.html) are checked and documented in the method's Javadoc
- [ ] [Coding conventions](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#coding-conventions) (e.g. for logging) have been followed
- [ ] Change is covered by [automated tests](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#tests) including corner cases, errors, and exception handling
- [ ] Public API has [Javadoc](https://github.com/junit-team/junit5/blob/master/CONTRIBUTING.md#javadoc) and [`@API` annotations](https://apiguardian-team.github.io/apiguardian/docs/current/api/org/apiguardian/api/API.html)
- [ ] Change is documented in the [User Guide](http://junit.org/junit5/docs/snapshot/user-guide/) and [Release Notes](http://junit.org/junit5/docs/snapshot/user-guide/#release-notes)
- [ ] All [continuous integration builds](https://github.com/junit-team/junit5#continuous-integration-builds) pass




# 221 this is title
## Status Quo

Since 5.0 M1, dynamic tests can be registered as lambda expressions, but there are a few limitations with the current feature set.
## Topics
1. Lifecycle callbacks and extensions are not applied _around_ the invocation of a dynamic test.
2. A dynamic test cannot directly benefit from parameter resolution.
   - A dynamic test cannot make use of a `TestReporter`.
## Related Issues
- #14 ~~"Introduce support for parameterized tests"~~
- #386 ~~"Improve documentation of DynamicTest lifecycle"~~
- #393 ~~"TestReporter does not capture the correct TestIdentifier when used with DynamicTests"~~
- #431 "Introduce mechanism for terminating Dynamic Tests early"
- #694 (duplicates this issue, with example)

## Deliverables

Address each _topic_.




# 222 this is title
## Overview

I'm working on some tests using scenario based testing. To mark those tests I'm using an annotation `@Scenario("Description of my scenario")`. This results in some reports containing the scenario title and some information about execution of that scenario. The scenario title works for my custom reports, but not for JUnit reporting, since `@DisplayName` isn't set.

A possible solution would be to annotate those scenarios with `@DisplayName`, i.e.

```java
@Scenario
@DisplayName("Description of my scenario")
```

However, that's not my favored solution, since there is one more annotation cluttering my code. I would like to be able to inherit annotations including their attributes.

A possible solution could be something like

```java
@Retention(RUNTIME)
@Target(METHOD)
@Test
@InheritedAnnotation(inheritFrom=DisplayName.class)
public @interface Scenario {
	String value();
}
```

This would lead to `@DisplayName` being found as an annotation when `@Scenario` is scanned. Since `@Scenario` declares a `value` attribute with the same type as defined in `@DisplayName`s `value` attribute, the attribute is inherited.

The default behavior for attribute inheritance would be something like: All attributes with same signature are inherited from `sourceAnnotation` to `targetAnnotation`. For all others default implementation is used.

One might think of something like:

```java
@Retention(RUNTIME)
@Target(METHOD)
@Test
@InheritedAnnotation(inheritFrom=DisplayName.class, attributeMapper=MyCustomAttributeMapper.class)
public @interface Scenario {
	String value();
}
```

to allow writing one's own attribute inheritance strategies.

## Related Issues

- #614
- #1504
- #1543





# 223 this is title
I have a bunch of tests that require me to initialise a temporary directory with some files, so that the methods in my tests can read and write to it.
Currently, the solution is to implement a BeforeAll/BeforeEach tag and initialise the temporary directory for each test class.
As this is a common routine, it would be more reuse friendly if we could write an extension that encapsulates this routine, and which only needs to receive an input of a Path to initialise a temporary directory with all the files.
I envision the extension to look something like

DirectoryInitExtension.java
```java
public class DirectoryInitExtension implements BeforeEachCallback {

    private Path TEST_DATA_FOLDER;

    @TempDir
    public Path tempDir;

    public static DirectoryInitExtension initializeWith(Path folder) {
        return new DirectoryInitExtension(folder);
    }

    @Override
    public void beforeEach(ExtensionContext extensionContext) throws IOException {
        // Copy files from TEST_DATA_FOLDER into tempDir, then return this tempDir as part of the test context.
    }
}
```
MainTest.java
```java
 @RegisterExtension
    public static DirectoryResetExtension tempDir = DirectoryResetExtension.initializeWith(TEST_DATA_FOLDER);
```

However, as I soon learnt (thanks to a fast response [here](https://stackoverflow.com/questions/54647577/how-to-use-tempdir-in-extensions)), TempDirs are not supported in extensions.

I wonder if it is a possibility to enable the same capabilities of TempDirs in extensions.

## Deliverables

- [ ] Support TempDir in extensions? (Sorry, not too sure what to write here)




# 224 this is title
## What is EditorConfig?
_EditorConfig helps maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs. The EditorConfig project consists of a file format for defining coding styles and a collection of text editor plugins that enable editors to read the file format and adhere to defined styles. EditorConfig files are easily readable and they work nicely with version control systems._
https://editorconfig.org

## Deliverables

- [ ] Provide `.editorconfig` matching settings declared in https://github.com/junit-team/junit5/tree/master/src/eclipse as close as possible.




# 225 this is title
I suggest that `@BeforeSuite` and `@AfterSuite` annotations should be added to JUnit 5.

Obviously they should execute before and after the whole suite.

Or is there some other mechanism to accomplish that?

I suggest that there should not be static restriction, i.e. also non-static methods could be annotated with `@BeforeSuite` and `@AfterSuite`.

I personally prefer non-static as we use Spring in our tests and want to use injected beans in `@BeforeSuite` method.




