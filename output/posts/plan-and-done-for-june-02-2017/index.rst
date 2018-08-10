.. title: Plan and done for June-02-2017
.. slug: plan-and-done-for-june-02-2017
.. date: 2017-06-02 10:48:31 UTC-07:00
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

7. The next JS30 assignment is to build a free drawing tool using HTML5 canvas element. The plan is to implement:

   * draw circle function with two supporting functions: the first should get a mouse position and the second should get a mouse velocity. The first I need to draw circle in a place where mouse is located in a moment and the second - to manage line width: the faster the mouse is moved - the thinner line is drawn;
   * spline interpolation - to make the line drawn looks more natural. Without it I have only dots with intervals which depend on a mouse velocity.

   Here is a manual on canvas drawing - https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_usage. An example on mouse movement tracking - https://stackoverflow.com/a/7790764. It's a bit weird - uses both event driven and interval scanning, but I didn't get how the last works. How to measure velocity - https://stackoverflow.com/a/19794374. How to work with a bezier curve - http://scaledinnovation.com/analytics/splines/aboutSplines.html.

   Got stuck a little - spline code do the job, but I don't want so complex logic, I want to try to implement the drawing canvas only with cubic bezier curve, so I want to calculate control point position. I know coordinates of two other points, I can find the distance between them, I can set the distance from to the desired control point voluntary and calculate its coordinates accordingly. Here is description of the process - https://math.stackexchange.com/a/544025.
