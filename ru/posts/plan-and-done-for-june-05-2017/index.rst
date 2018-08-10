.. title: Plan and done for June-05-2017
.. slug: plan-and-done-for-june-05-2017
.. date: 2017-06-05 05:33:31 UTC-07:00
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

7. Still on the day 8 of JS30 (https://javascript30.com) - fighting with canvas drawing. I want to implement smooth width change dependant on a mouse speed. Tried to bind it directly to the speed - it works but it's far from expected smoothness.

   Here is a snippet from MDN (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round) to make round in JS behave like in other languages - with precision:

   .. code-block:: javascript

      var myNamespace = {};

      myNamespace.round = function(number, precision) {
          var factor = Math.pow(10, precision);
          var tempNumber = number * factor;
          var roundedTempNumber = Math.round(tempNumber);
          return roundedTempNumber / factor;
      };

   Want to try to calculate a mouse acceleration and bind width to it.

   And again finally I've got something, that looks not as planned. Ok. Let's move on - perfection kills has some answers and techniques - http://perfectionkills.com/exploring-canvas-drawing-techniques/ (one is exactly about quadratic bezier curve - https://codepen.io/kangax/pen/zofsp) and here is SO answer - https://stackoverflow.com/a/10661872. I've completed it to look like Wes Bos example.

   Done:

   * recalled some math primitives - get an angle between two vectors, get point's coordinates;
   * applied ternary operator, prototype enhencement by new functions implementation, utilizing :code:`hsl()` command in coloring shapes, canvas drawing.
