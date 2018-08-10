.. title: Plan and done for July-12-2017
.. slug: plan-and-done-for-july-12-2017
.. date: 2017-07-12 13:25:31 UTC-07:00
.. tags: javascript, hackerrank
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

Dive into JS.

==============================
  Done
==============================

I've solved Queen attack II. It wasn't hard, but in some way mind bending. The next two challenges are Roads and libraries - https://www.hackerrank.com/challenges/torque-and-development and Climbing the leaderboard - https://www.hackerrank.com/challenges/climbing-the-leaderboard. I solved both, but my solutions didn't meet time complexity criteria, so now I'm in optimization mode.

My approach to Roads and libs is:

* The idea is to find whether we have a connected graph.
* If not, then we need at least the same number of libraries as independent graphs.
* If graph is connected, we build at least one library.
* If library cost > road cost, fix all roads, otherwise, build a library in every town.
* In order to find the graph roots and edges I built node adjacency list and all nodes list.

The last two are sources of latency. At first I tried to build all nodes list by concatenating all nodes within :code:`forEach` loop and then moving the result into a set to get a list of nodes without repetitions. I've got rid of concatenation, and just pushed all nodes into flat array and then copied it into a set. The adjacency list is looked harder. I want to get a list of all nodes with their neighbours for each. I use for it an array and each position is my node number filled with arrays of neighbours. Maybe the better idea is to use object for storing the list.

In order to understand how my solution works under load I use a dataset I've found under the first link here - https://cstheory.stackexchange.com/a/740.

The solution works faster with an object as a storage of adjacency list, but it fails HR performance tests.
