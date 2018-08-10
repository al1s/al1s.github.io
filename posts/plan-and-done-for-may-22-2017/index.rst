.. title: Plan and done for May-22-2017
.. slug: plan-and-done-for-may-22-2017
.. date: 2017-05-22 15:42:22 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

#. Make menu hide only on tablet and desktop versions or add input-label to hide JS-function.
#. Fix quirks in Safari: icons have became too small, everything become a mess on a wide screen.
#. Fix a masthead height on resolution wider 640px.
#. Fix an offer body text align for the gift message - now it aligns to center on resolutions less than 570.
#. Build additional pages - hotels, impression, blog.
#. Style the form on impression page.
#. Dive into JS.

==============================
  Done
==============================

7. Returning to my last question from the day before - why the syntax :code:`++array[element] || 1`: I've found the answer here - https://en.wikipedia.org/wiki/Short-circuit_evaluation. It's common aspect of programming and for JS it works like this:

      In loosely typed languages that have more than the two truth-values True and False, short-circuit operators may return the last evaluated subexpression, so that :code:`x Sor y` and :code:`x Sand y` are equivalent to :code:`if x then x else y` and :code:`if x then y else x` respectively (without evaluating x twice).

   And from another source (http://www.grauw.nl/blog/entry/510) here is more clear explanation:

      ...if the first operand evaluates to false, the second operand is never evaluated because the result would always be false. Similarly, for || if the result of the first operand is true, the second operand is never operated.

   For my question it should be applied as: while we've got :code:`undefined` for the first part of :code:`or` we choose the second part of the statement - 1.

**Spontaneous**. To make an inline :code:`code block` in rst (reStructuredText) use \:code:\`something` notation. Look here - https://stackoverflow.com/a/12365251 - for more.
