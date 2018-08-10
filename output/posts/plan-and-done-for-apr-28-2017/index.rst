.. title: Plan and done for Apr-28-2017
.. slug: plan-and-done-for-apr-28-2017
.. date: 2017-04-28 10:55:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Practice vim and git (CLI via hub)
2. Make the marker on the map clickable.
3. Prev: Format search form to make labels more aligned with input fields.
4. Prev: Work with styleguide.
5. PixelPerfect tablet and desktop versions.
6. Make a dropdown menu for mobile.
7. Replace logo with SVG elements.

==============================
  Done
==============================

2. Done. Made an error in marker variable name when assign listener to event. Google Map API is handy. It's interesting to implement something like multiple markers on the map with infoWindows for each of them, something like Booking.com or other geolocated projects do. Here - https://www.w3schools.com/graphics/google_maps_events.asp - is an example.

6. Plan for a dropdown menu:

   * Make checkbox ``input`` control and hide it;
   * Link ``label`` to this checkbox and make a hamburger as a background image for it.
   * Change ``display`` property of the ``<nav>`` depending on the ``:checked`` state of the input.
   * Set ``flex-direction`` for ``nav`` in mobile layout to ``column``.
