.. title: Plan and done for June-22-2017
.. slug: plan-and-done-for-june-22-2017
.. date: 2017-06-22 12:47:31 UTC-07:00
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

1. Stuck a little with the yesterday's problem. The reason - can't add up only those remainder's groups which don't give a divider mutually - I've set an array of 'banned' remainders and try to use it inside :code:`Array.prototype.reduce()` but it seems like it's not seen inside :code:`reduce` loop.

   The solution for this was quite easy - I added to an array numbers and checked if an element is included with a string equivalent. Added plus sign before an element so it looked like :code:`Arr.includes(+num)` and everything started to work great.
