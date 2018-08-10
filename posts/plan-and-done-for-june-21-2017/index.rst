.. title: Plan and done for June-21-2017
.. slug: plan-and-done-for-june-21-2017
.. date: 2017-06-21 10:13:31 UTC-07:00
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

1. Today's problem is about properties of dividing integers - https://www.hackerrank.com/challenges/non-divisible-subset.

   Sum of which numbers isn't dividable by third number? The brute-force approach is to check each combination of two numbers in a set has O(n^2) complexity. I want it to be better.

   Division is an opposite to multiplication and the last is just a compressed version of addition::

    9 / 3 = 3 => 3 * 3 = 9 => 3 + 3 + 3 = 9;

   If the number isn't dividable by other number it means we have a skewed view of addition::

    10 / 3 = 3.333(3) => 3.3(3) * 3 = 10, but let's make it simpler: 3 + 3 + 3 + 1 = 10;

   The only thing that changes is the last addendum - we have the remainder now. Let's add some numbers to our ``10`` and look what'll happen.::

    10 + 1 = 11 => 3 + 3 + 3 + (1 + 1) = 11 => 3 + 3 + 3 + 2 = 11;
    11 / 3 = 3 remainder 2;

    10 + 2 = 12 => 3 + 3 + 3 + (1 + 2) = 12 => 3 + 3 + 3 + 3 = 12;
    12 / 3 = 4;

    10 + 5 = 15 => 3 + 3 + 3 + (1 + 2) + 3 = 15 => 3 + 3 + 3 + 3 + 3 = 15;

   Looks like the remainders of two addendums divided by the third number shouldn't add up to divisable number if we want the sum won't. My approach according to above is to accumulate all numbers in a given set into dictionary using remainder as a key. Then choose the largest groups which remainders sum will not be dividable and sum all such groups together. It will be the answer.
