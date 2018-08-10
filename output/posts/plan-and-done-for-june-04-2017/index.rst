.. title: Plan and done for June-04-2017
.. slug: plan-and-done-for-june-04-2017
.. date: 2017-06-04 05:03:31 UTC-07:00
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

7. To arms! Looked through the code of spline drawing example - http://scaledinnovation.com/analytics/splines/aboutSplines.html, it's not complicated but I want to build something even simpler utilizing cubic bezier curve - only one control point for each pair of mouse movement captured points. I have to find the coordinates of that control point and my idea is:

   * to take three points with every event;
   * to calculate distance between these three points;
   * to build auxiliary similar triangle on the base of the segment connecting first two points;
   * to calculate an angle between first and third segments - it's the same angle as in my auxiliary triangle;
   * to find coordinates of the control point.

   Tried different options for calculating control point coordinates (this for example - https://math.stackexchange.com/a/1989113). All I've got is a wavy line with skips. Then I just decided to take every three points and to use middle point as a control point. It works but in a weird way - I've got two twisted lines.

   Finally I've checked what Wes Bos has in the tutorial on Day 8. It's easy! Much easier than I did - just straight lines from one point to another. I overcomplicate things - when I see a task, my approach is sometimes too twisted, too overthinked. Why am I so appealed by complex answers? Have to train, to learn myself to be open to simple solutions first. For example, the task is to implement smooth width increasing/decreasing while drawing in HTML5 canvas depending on the mouse speed. My approach leads to visual steps in line width change. But what I really need is to increament value by one step at a time in a given interval. After the tutorial all is clear and the only thing left is to rebuild from scratch.

   Get the last element of array (from SO - https://stackoverflow.com/a/9050353) by enhancing Array.prototype:

   .. code-block:: javascript

    if (!Array.prototype.last){
      Array.prototype.last = function(){
          return this[this.length - 1];
      };
    };
