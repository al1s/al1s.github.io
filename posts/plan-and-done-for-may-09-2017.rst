.. title: Plan and done for May-09-2017
.. slug: plan-and-done-for-may-09-2017
.. date: 2017-05-09 11:52:14 UTC-07:00
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

==============================
  Done
==============================

3. Masthead is ready. Added intermediate width breakpoints.

2. Safari is disgusting. It collapses a height when the height is not explicitly set.

4. Done. It was a flexbox with ``flex-basis: auto`` and ``flex-grow: 1``, so the width of each of three containers wasn't evenly distibuted. Changed ``flex-grow`` to 0 and add ``min-width: 30%``.
