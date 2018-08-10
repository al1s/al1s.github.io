.. title: Plan and done for Apr-27-2017
.. slug: plan-and-done-for-apr-27-2017
.. date: 2017-04-27 04:17:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Change background height to align the photo with original.
2. Make the map live.
3. Prev: Format search form to make labels more aligned with input fields.
4. Prev: Work with styleguide.
5. PixelPerfect tablet and desktop versions.
6. Make a dropdown menu for mobile.
7. Replace logo with SVG elements.

==============================
  Done
==============================

1. Blurry edges in the background shape. The reason - ``background-size: cover;`` so it makes the shape scaling.

   Done! The picture finally matched with original by scaling explicitly with ``background-size`` and then setting exact ``background-position``. It started scaling enormously on screens larger than 320px, but I gonna fix it with media-queries.

   Another challenge was scaling of italic text SVG in masthead. The reason was the use of relative height bigger then needed for elements being aligned - I use it more as positioning tool, but it's totally unnatural for a height to be a positioning tool of the element. Fixed it with the use of correct (smaller) height and ``margin-top``.

2. Basic Google map tutorial - https://www.w3schools.com/graphics/google_maps_basic.asp - provides with all needed functionality. In addition to the JS code I need coordinates of the place I wanna show on the map and Google API key to work with map engine with my own credentials. In order to get coordinates (taken from - https://www.lifewire.com/latitude-longitude-coordinates-google-maps-1683398):

   * Open Google maps, locate the place.
   * Right-click (Control-click on a Mac) the location.
   * Click on "What's here?" in the menu that pops up.
   * Click on coordinates.

   Almost done - the map is on the page, it's zoomable, it has a marker. What left is an event handler. It doesn't work with error - ``Cannot read property 'click' of undefined``. Looks like google api handler conflicts with JQuery.

6. A dropdown menu receipt is here - https://scotch.io/tutorials/building-a-morphing-hamburger-menu-with-css - and living example is in the playground - https://codepen.io/lmgonzalves/pen/KaWaJO.
