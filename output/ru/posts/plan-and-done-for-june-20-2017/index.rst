.. title: Plan and done for June-20-2017
.. slug: plan-and-done-for-june-20-2017
.. date: 2017-06-20 04:35:31 UTC-07:00
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

1. I'm still on the same problem as yesterday - https://www.hackerrank.com/challenges/sherlock-and-squares.

   My initial approach was overcomplicated way of thoughts (as usual). The solution was much simpler - just find two square roots of given numbers and round them to ceil and floor respectfully. The difference between calculated roots increaces by one is the answer except the case when both given numbers are equal.

   While my attempts to figure out why HR built-in tests were failing I decided to switch to my local test suit. After short analysis of different testing frameworks I stopped on Jasmine - it has everything I need already integrated, opposite to Mocha, where assertion framework should be chosen separately. Jasmine is well documented so to integrate test inside a browser was easy.

   It was challenging to implement the test itself - I wanted to generate randomly both boundaries and then knowing what were initial values for calculating powers of two and if I know initials than it's easy to get how many values I have in between. The challenge was to get a random value exluding upper and lower boundaries - MDN advices on :code:`random` are about inclusive implementations. Finally I've got it by increasing and decreasing low and high limits of squares.
