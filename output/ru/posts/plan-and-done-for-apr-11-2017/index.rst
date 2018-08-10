.. title: Plan and done for Apr-11-2017
.. slug: plan-and-done-for-apr-11-2017
.. date: 2017-04-11 05:50:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. How to add many style files to project on gulp and make them dance around.
2. How to add js to my project.
3. How to add datepicker to my project.
4. Study another 5 CSS things on tympanus.net

==============================
  Done
==============================

1. Start your Gulp journey here https://css-tricks.com/gulp-for-beginners/. It will make all things clear from the beginning: what is package.json, gulpfile.js. And there is a bunch https://github.com/gulpjs/gulp/tree/master/docs/recipes of receipts. I'm still curious about sass, because right now I don't use it at all. And I don't concat files.

2. Just put code into js folder and start working. Right now my gulpfile.js concatenate all js sources into one. And it doesn't have any lint inside. To add! And by the way - how to build things in order? Right now the solutions are: put files into gulp in a right order - http://stackoverflow.com/a/21961217 - by pointing specifically one by one in the gulp.src(...) and second is to use browserify - https://github.com/substack/browserify-handbook or webpack - https://github.com/vigetlabs/gulp-starter/tree/blendid. Something - https://www.viget.com/articles/gulp-browserify-starter-faq - about how to use it with gulp.

4. CSS rules and pseudo-elements::

    outline - no width unlike border, but scarce functionality and browser support for it.
    :link - for anchors with href.
    :visited - switched back to link state after a while.
    :focus - cursor with tab or mousedown on the link or input element to trigger
    :hover - mouse hover.
    :active - when user clicked the element. Main use - to give UI feedback: something happening, we didn't freeze.

3. Added, but it hasn't work yet. Need to debug and here is the article - https://developers.google.com/web/tools/chrome-devtools/javascript/ on basic debugging JS.

