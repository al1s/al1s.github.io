.. title: Plan and done for May-14-2017
.. slug: plan-and-done-for-may-14-2017
.. date: 2017-05-14 04:03:14 UTC-07:00
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
#. Style the form on impression page.

==============================
  Done
==============================

6. Styled radio with ``:before`` element of the label. Technique for hiding real input and customizing label is from MDN - https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Advanced_styling_for_HTML_forms.

   Triyng to make spin element - two buttons with plus-minus glyphs and textbox. Made them flexboxes but text input is wider than need to be. The reason - it scales automatically depending on font-size. ``overflow: hidden`` for the ``input`` element to the rescue.

   On the way to make spin animated by JS and behave naturally - on mousedown starts to raise number inside ``input`` element until a user release the button. Have found this resource - http://eloquentjavascript.net/14_event.html, but still has no idea how to handle repeated increase. My common sense says that it should be done with ``setTimeout`` or ``setInterval``, but it doesn't work. JS is funny in a way of all this garbage - braces - {}, quotation marks - "". Here is my playground - https://codepen.io/alstof/pen/JNZGBb.
