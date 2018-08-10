.. title: Plan and done for Apr-23-2017
.. slug: plan-and-done-for-apr-23-2017
.. date: 2017-04-23 04:37:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Practice vim and git(CLI via hub)
2. Prev: Align the project's main page with the design layout via PixelPerfect.
3. Prev: Format search form to make labels more aligned with input fields.
4. Prev: Work with styleguide.

==============================
  Done
==============================

2. Built it with a stand-alone ``<div>`` and a separate menu list. Menu is a flexbox with elements evenly spaced along the string (at least I expect it to run this way). The logo is background image positioned absolutely with calculated position to be fluid.

   Everything is ok till my menu items is a one word long - the logo is centered and items are evenly spaced. It's not my case. I want items to be longer - two, three words long, but then all evenness goes away - the logo is still centered, menu items start to float uncontollably.

   A  simple solution is to add explicit width value, that will ensure even spaced items. Here is example - http://jsfiddle.net/alstof/9fbvL900/6/
