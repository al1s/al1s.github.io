.. title: Plan and done for Apr-19-2017
.. slug: plan-and-done-for-apr-19-2017
.. date: 2017-04-19 06:35:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Practice vim and git(CLI via hub)
2. Resolve JQuery datepick plugin error.
3. Prev: Format search form to make labels more aligned with input fields.
4. Prev: Work with styleguide.
5. Align the project's main page to the design layout via PixelPerfect.

==============================
  Done
==============================

1. Deep dive into Vim - http://learnvimscriptthehardway.stevelosh.com/.

2. Done. The reason of datepick didn't work was unnecessary class usage - `is-datepick`. This class is internal for plugin and connects to an element by JS. I included it manually, because it shows in example page for plugin. I shouldn't.

   To find it I fired up blank project (it's easy with boilerplates like NTH or something from - ) setup minimal configuration with only plugin scripts and basic html. Then I started to play with different versions of html and finally found unnecessary class.
