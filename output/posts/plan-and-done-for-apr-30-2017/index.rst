.. title: Plan and done for Apr-30-2017
.. slug: plan-and-done-for-apr-30-2017
.. date: 2017-04-30 16:56:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

#. Make a dropdown menu for mobile.
#. Prev: Format search form to make labels more aligned with input fields.
#. Prev: Work with styleguide.
#. PixelPerfect tablet and desktop versions.
#. Replace logo with SVG elements.

==============================
  Done
==============================

1. Done. What was interesting? I've built it with a pure CSS basing on Dudley's manual - http://thenewcode.com/599/A-Responsive-Animated-Menu-For-Single-Column-Web-Designs. I've changed trigger mechanics - instead of ``:hover`` it fires on hamburger click which is nothing else then ``label`` for a hidden ``input`` element. Took an example here - http://thenewcode.com/625/A-Visual-Database-Gallery-In-Pure-CSS. Here is another UI-rich implementation - https://scotch.io/tutorials/building-a-morphing-hamburger-menu-with-css. And here - http://callmenick.com/post/animating-css-only-hamburger-menu-icons - pure CSS animation around hamburger symbol.

   Works great, but then I've found that it won't change to a large screen menu layout in case of screen resize when the mobile menu is open - it just stays as a screen-wide column of menu items. There is no CSS only solution for it, so switched to JS alternative. Found many JQuery receipts, major of them use ``setTimeout()``, so have performance issues. There is a solution - http://marcj.github.io/css-element-queries/ - which implements an alternative logic and it says that it has no performance drawbacks, but for my current knowledge level of JS is way hard to understand. I've choosen simpler one - http://alvarotrigo.com/blog/firing-resize-event-only-once-when-resizing-is-finished/. It shouldn't freeze the page much and does what I need - toggle menu layout by toggle the checkbox input. My menu implementation is here - https://codepen.io/alstof/pen/ybMEqM. It has a little weird timeout of menu layout toggle on resize and it won't work on ongoing resize - only when resize is finished.

   Tried to implement different order for menu items depending on a screen size. It works, but due to timeout I mentioned above it behaves funny - the items' order changes before the layout. Looks terrible. Have to rework JS implementation (can't keep it as is, because order of items has to change on resize as layout too).
