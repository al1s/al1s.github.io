.. title: Plan and done for Apr-26-2017
.. slug: plan-and-done-for-apr-26-2017
.. date: 2017-04-26 05:16:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Practice vim and git (CLI via hub)
2. Implement the masthead slogan of the project (as SVGs from sprite).
3. Prev: Format search form to make labels more aligned with input fields.
4. Prev: Work with styleguide.
5. PixelPerfect tablet and desktop versions.

==============================
  Done
==============================

2. Chris is the source of knowledge - https://css-tricks.com/lodge/svg/. Essentially:

   * no. 15 - where to put your icon system inside the html-body file and the practical ways to do this and what is limitation for this (Safari wants our inline-SVG before ``<use>``, so it means just after ``<body>`` tag). And here is a text version - https://css-tricks.com/svg-sprites-use-better-icon-fonts/.
   * no. 16 - using SVG-file as external resource (our SVG-file has to be on the same domain, protocol, port as our html-file).
   * no. 18-19 - how to automate icon system building process with grunt or gulp.

   Here is some gotchas with SVG - https://css-tricks.com/gotchas-on-getting-svg-into-production/ and first is about using svg4everybody if we need IE support - https://css-tricks.com/gotchas-on-getting-svg-into-production/#article-header-id-2. The main point - we can't style or swap icons on hover polyfill SVG images in IE, instead we should use some additional techniques.

   And finally - done! Somewhat unsteady yet, but it lives.

   Here are two alternatives on automated building tools for Gulp:

   * https://github.com/shakyshane/gulp-svg-sprites
   * https://github.com/w0rm/gulp-svgstore

   The first has a built-in data transform engine and generates a preview as http://www.grumpicon.com/ does. The second is in my boilerplate project. Both can generate png fallback images.

**Spontaneous.** Encountered the error in autoprefixer already mentioned as an issue - https://github.com/postcss/autoprefixer/issues/655 - it doesn't add prefixes for flexbox in Safari. Added explicitly in a browser list ``Safari >= 8``. Now the project looks the same in all browsers.

**Spontaneous.** Another gotchas - ``calc`` and ``CSS-variables`` don't work in Safari 8 and since I used them to center logo, went to find another solution for centering fixed ``div`` with ``position: fixed``. Found it on stackoverflow - http://stackoverflow.com/a/2006008 (but its origin is Chris again - https://css-tricks.com/quick-css-trick-how-to-center-an-object-exactly-in-the-center/)- set ``left`` and ``right`` to 0 and side margins to ``auto``. Works great.


