.. title: Plan and done for June-11-2017
.. slug: plan-and-done-for-june-11-2017
.. date: 2017-06-11 12:20:31 UTC-07:00
.. tags: web-dev, JS30
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

1. What is this all about - http://al1s.github.io/posts/plan-and-done-for-may-25-2017/.

   Day 13 - show pictures only if they are in a visible part of a screen. And yes it is not a screen, it's a viewport - visible part of a document. Its dimensions are properties either :code:`window` or :code:`document.documentElement` objects (here is excerpts from spec - https://stackoverflow.com/a/7205786), so the task is simple - check on scroll if relative element position less then a viewport. How to find relative position? Here is a method :code:`getBoundingClientRect()`. And to toggle classes on an element I have :code:`classList` methods - add and remove.

   More broad solution - lazy images loading - is here - https://css-tricks.com/snippets/javascript/lazy-loading-images/.
