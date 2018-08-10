.. title: Plan and done for July-04-2017
.. slug: plan-and-done-for-july-04-2017
.. date: 2017-07-04 05:03:31 UTC-07:00
.. tags: javascript, hackerrank
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Dive into JS.

==============================
  Done
==============================

1. Moving to another appartment took tons of time and efforts. Now we've settled and I'm able to continue my practice. The last problem was too tough. I'm stuck with all exceptional cases and it still doesn't pass all tests. Let's move on.

   Next problem is Queen attack II - https://www.hackerrank.com/challenges/queens-attack-2. The approach was to take it as a distance appraisal problem. There is only 2d space with relative center of coordinates (which is a queen position) and available routes on it (only vertical, horizontal and both diagonals). And the solution is to find length of each route and get a total:

   * appraise whether an obstacle is on any available route and find distance to each;
   * find distance from queen position to any side of the board in any direction available.

   My first thought was to implement a simple function which would return me a distance in math way - as a square root of the sum of squared differences of respective point coordinates. It's obvious that it won't work - I have longer distances diagonally, than in vertical and horizontal directions. Next move - why not take it simpler: the distance in board squares is already here - it's just any of coordinates (because my diagonals are at 45 degrees to horizontal line).

   The next question was how to find whether an obstacle is on the queen way or not? The solution was to find the angle between two sections. The most obvious way is to find a tangent (because I already know both cathetus - they are just obstacle coordinates) and apply :code:`Math.atan` to it.
