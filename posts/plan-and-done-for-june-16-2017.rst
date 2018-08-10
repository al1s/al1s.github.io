.. title: Plan and done for June-16-2017
.. slug: plan-and-done-for-june-16-2017
.. date: 2017-06-16 14:45:31 UTC-07:00
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

   Continue day 16. It's quite easy assignment but I'm in a lack of time. Build tons of helper functions.

   * :code:`getElmCenterPoint()` - to get any element center;
   * :code:`getDistanceToElm()` - to calculate distance between a target element and the mouse pointer;
   * :code:`shiftCoordinates()` - to get mouse pointer coordinates taking the element center as a coordinates origin;
   * :code:`mirrorCoord()` - to get coordinates opposite (the kind of oppositeness depends on the function arguments: it could be mirrored around one or another axes, or both) to the mouse pointer.

   Here is about paralax effect by Dudley Storey - http://thenewcode.com/1162/Cheap-Parallax-with-JavaScript-and-CSS-Transforms.

   Used debounce function to prevent performance degradation. More info on debounce is here - https://css-tricks.com/debouncing-throttling-explained-examples/.

   Learned how to work with boxShadow/textShadow style attributes: get - getComputedStyle(elm).textShadow and https://stackoverflow.com/a/17819623, set - https://stackoverflow.com/a/10890994.

   Here is working example - https://al1s.github.io/JavaScript30/16%20-%20Mouse%20Move%20Shadow/index.html.

   And an appointment on the day 17 is easy one: sorting list excluding articles - a, the, an. My approach was to iterate through articles list and replace every occurence of it in a target string. After it just :code:`Array.prototype.sort()`. Wes's solution is more elegant.

   Here is working example - https://al1s.github.io/JavaScript30/17%20-%20Sort%20Without%20Articles/index.html.
