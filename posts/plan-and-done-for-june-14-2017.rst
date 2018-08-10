.. title: Plan and done for June-14-2017
.. slug: plan-and-done-for-june-14-2017
.. date: 2017-06-14 11:26:31 UTC-07:00
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

   Still on the day 16. What dimensional properties are available in a browser window? Here are officials by MDN:

   * mouseEvent.offsetX, mouseEvent.offsetY - the X and Y coordinates of the mouse pointer relative to the position of the padding edge of the target node;
   * mouseEvent.clientX, mouseEvent.clientY - the X and Y coordinates of the mouse pointer in local (DOM content) coordinates.
   * mouseEvent.pageX, mouseEvent.pageY - the X and Y coordinates of the mouse pointer relative to the whole document.
   * mouseEvent.screenX, mouseEvent.screenY - the X and Y coordinates of the mouse pointer in global (screen) coordinates.
   * elm.getBoundingClientRect() - the size of an element and its position relative to the viewport.
   * window.innerHeight, window.innerWidth - height and width (in pixels) of the browser window viewport including, if rendered, the horizontal scrollbar. These are dimensions of the page being displayed. Source - https://developer.mozilla.org/en-US/docs/Web/API/Window/innerHeight;
   * window.scrollX, window.scrollY - the number of pixels that the document is currently scrolled horizontally and vertically. https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollX;

   Here is demo of different dimension aspects and basic paralax helper functions - https://codepen.io/alstof/full/xrEaRB/.
