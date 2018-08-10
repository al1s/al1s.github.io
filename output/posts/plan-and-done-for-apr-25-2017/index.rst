.. title: Plan and done for Apr-25-2017
.. slug: plan-and-done-for-apr-25-2017
.. date: 2017-04-25 04:17:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Practice vim and git (CLI via hub)
2. Implement the masthead of the project.
3. Prev: Format search form to make labels more aligned with input fields.
4. Prev: Work with styleguide.
5. PixelPerfect tablet and desktop versions.

==============================
  Done
==============================

2. Is there any way to change the color of svg if I use it as background image? No - because as a background img, it isn't part of the DOM and you can't manipulate it (from here - http://stackoverflow.com/a/13367916).

   There is a bunch of solutions, starting from svg embedded into stylesheet (https://css-tricks.com/cascading-svg-fill-color/), encode it in the url in base64 way (https://css-tricks.com/probably-dont-base64-svg/). Here is demo for different alternatives - http://codepen.io/noahblon/post/coloring-svgs-in-css-background-images. It looks like I should change svg manually, create different color versions of it, glue it into a sprite and then use it as bg-image. Gulp provides me with svg, bunched into a sprite, but with ability to work with original pictures like they are embedded (). Ok, but now - how to scale them to the right size easily?

   Found less mixin for replacing colors and work with svg as bg-image here - https://zslabs.com/articles/svg-background-fill/, converted it into scss (http://www.rubydoc.info/gems/less2sass/1.2.0) and here is explanation about conversion - http://mstrutt.co.uk/blog/2013/08/converting-from-less-to-sass/. And here I've found replace function for SASS - https://www.sassmeister.com/gist/1b4f2da5527830088e4d.

   Haven't made it work. Tried with a codepen playground - doesn't work at all - funny.
