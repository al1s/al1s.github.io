.. title: Plan and done for June-06-2017
.. slug: plan-and-done-for-june-06-2017
.. date: 2017-06-06 16:43:31 UTC-07:00
.. tags: web-dev, JS30
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

#. Make menu hide only on tablet and desktop versions or add input-label to hide JS-function.
#. Fix quirks in Safari: icons have become too small, everything become a mess on a wide screen.
#. Fix a masthead height on resolution wider 640px.
#. Fix an offer body text align for the gift message - now it aligns to center on resolutions less than 570.
#. Build additional pages - hotels, impression, blog.
#. Style the form on impression page.
#. Dive into JS.
#. Implement form validation.

==============================
  Done
==============================

7. Day 10 of JS30 (day 9 was about web dev panel utilization, without any assignment). Build a checkbox's list with ability to select the range of items with :code:`Shift` pressed. My plan:

   * iterate through the list of checkboxes (divs in this case);
   * find first checked :code:`input` element;
   * set flag and start to put this and all following :code:`input` elements into array;
   * if next checked found, release flag and finish iteration;
   * if flag released, :code:`Shift` pressed, and array of elements is not empty - set :code:`checked` property to :code:`true` for all of them.

   It would work for a list of unchecked items, but if I already have checked items the approack will fail. Try something new.
