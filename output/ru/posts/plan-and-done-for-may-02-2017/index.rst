.. title: Plan and done for May-02-2017
.. slug: plan-and-done-for-may-02-2017
.. date: 2017-05-02 10:23:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

#. PixelPerfect tablet and desktop versions.
#. Replace logo with SVG elements.
#. Prev: Format search form to make labels more aligned with input fields.
#. Prev: Work with styleguide.

==============================
  Done
==============================

1. While fitting layout to tablet version found many funny decisions made in the beginning of the project. They all aligned to mobile version pretty well but ablolutely rigid for adapting the main page to another media-width. For example, my ``.media-body`` class was a flexbox and three elements inside of it were ``column`` directioned. But it's absolutely counterintuitive to align them to a specific vertical rhythm. I have to remove ``flexbox`` attribute from the wrapper to have a chance to adjust inner elements with a ``margin-top``.


   Done. But now I have to go back to mobile and fix all stuff which now became broken.


