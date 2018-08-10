.. title: Plan and done for June-07-2017
.. slug: plan-and-done-for-june-07-2017
.. date: 2017-06-07 16:23:31 UTC-07:00
.. tags: web-dev, JS30
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Dive into JS.

Decided to clear the TODO list to keep focused.

==============================
  Done
==============================

1. Tried another approach:

   * on any keypress on :code:`input` element, put it into an array;
   * if :code:`Shift` is pressed, set all elements between two last items in the array to checked state.

   Encountered weird misunderstanding - I push elements with each keypress but when I want to check if an element in the array in some cases it says - NO, there is no such element. And when I log the array, I can easily spot it. WTFj

   The reason of weirdness was simple - name for array in JS is just a pointer. I added elements to an array inside the loop. I've checked the last two array's elements on equality to my loop variable. And yes, I've just pushed array's elements out of the search scope. Moved out array initialization out of the search loop and made it immutable in some way - no addition to it at all.

   Done.

   Learnt how to use :code:`console.group()` to make logs grouping in Chrome console. Learnt it from the Dat 9.
