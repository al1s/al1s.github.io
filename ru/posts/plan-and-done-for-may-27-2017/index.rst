.. title: Plan and done for May-27-2017
.. slug: plan-and-done-for-may-27-2017
.. date: 2017-05-27 04:21:27 UTC-07:00
.. tags: web-dev
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

7. Yesterday's JS30 exercise is to implement an analog clock using JS and CSS. The best way to do it is with CSS transform rules. There are two functions: one to sync visual appearance of the clock with current time, another - to animate clock hands movements.

   I move the clock's hands by rotating them with :code:`transform-origin: right` and :code:`transform: rotate(30deg)`. The second hand rotates every second and the quantum of rotation is 360/60=6deg. The minute hand rotates 6deg every 60 seconds or 1deg every 10sec and the hour hand rotates 30deg every 3600 seconds or 1deg every 120sec.

   Added digits to the clock face. First tried to do it with :code:`position: absolute; top: ...px; left: ...px;`. Horrible. Found the great article by Hugo Giraudel - http://hugogiraudel.com/2013/04/02/items-on-circle/. I don't have the SASS freedom with JS30 exercises, because there is already prepared html with all styles integrated, so I just took approach from Ana's article (mentioned by Hugo) - https://stackoverflow.com/a/12817454 and applied transformation :code:`rotate(${angle}) translate(${half-of-the-parent-width}) rotate(-${angle});` to :code:`div.class:nth-of-type()` elements of my digits circle.

   Today's assignment was to work with CSS variables via JS. It was easy. Here is short article on CSS variables and how to work with them via JS - https://developers.google.com/web/updates/2016/02/css-variables-why-should-you-care. It even has some examples but it's not intresting just to copy-paste everything. When I finished I check Wes Bos approach. It's way better utilizes JS facilities such as :code:`this` to achieve the true brevity.

