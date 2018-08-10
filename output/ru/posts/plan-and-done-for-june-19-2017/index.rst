.. title: Plan and done for June-19-2017
.. slug: plan-and-done-for-june-19-2017
.. date: 2017-06-19 04:35:31 UTC-07:00
.. tags: web-dev, hackerrank
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

1. The next problem - https://www.hackerrank.com/challenges/sherlock-and-squares.

   My initial approach was based on calculating increments between difference of current and the next square root. The reasoning looked like this:

   Let's assume, that we know the sequence of full square difference::

                 1, 2, 3, 4,  5,  6,  7,  8,  9...
     for the row 1, 4, 9, 16, 25, 36, 49, 64, 81...
     it would be   3, 5, 7,  9,  11, 13, 15, 17...
     so each time the difference increases by 2.

   The formula for it is 2*n - 1, where n is our initial number. Then to solve the problem just get the square root of the first number and find the difference, then check if my second given number within it.

