.. title: Plan and done for Sep-19-2018
.. slug: plan-and-done-for-sep-19-2018
.. date: 2018-09-19 06:10:14 UTC-07:00
.. tags: web-dev, c#
.. category:
.. link:
.. description:
.. type: text

C#
__

I've started practicing basic C# fluency by taking small assessments on CodeWars. The first logistical question I've got - how to setup a test env for C# projects? My steps (based on many sources but primarily on `MS dotnet Core guide <https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test>`_) include:

Packages to install (with :code:`dotnet add package PackageName`):
* NUnit;
* NUnit.Console;
* NUnit.ConsoleRunner;
* NUnit.Runners;

Folders/files setup:
* start a project: :code:`dotnet new console -o "MyAppName"`;
* initialize a solution :code:`cd MyAppName; dotnet new sln`;
* initialize a main project :code:`mkdir ProjectName; cd ProjectName; dotnet new classLib`;
* add the main project to the solution :code:`cd ..; dotnet sln add ./ProjectName/ProjectName.csproj`;
* initialize a test project :code:`mkdir ProjectName.Tests; cd ProjectName.Tests; dotnet new nunit`;
* add reference to the main project :code:`dotnet add reference ../ProjectName/ProjectName.csproj`;
* add the test project to the solution :code:`cd ..; dotnet sln add ./ProjectName.Tests/ProjectName.Tests.csproj`;

VSCode extension - .NET Core Test Explorer


Retro about 
____________________________________________________

==============================
What did we do well, that if we don’t discuss we might forget?
==============================

==============================
What did we learn?
==============================

==============================
What should we do differently next time?
==============================

==============================
What still puzzles us, or what do we need to learn more about?
==============================


