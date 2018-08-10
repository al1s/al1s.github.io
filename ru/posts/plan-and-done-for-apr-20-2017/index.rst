.. title: Plan and done for Apr-20-2017
.. slug: plan-and-done-for-apr-20-2017
.. date: 2017-04-20 05:21:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Practice vim and git(CLI via hub)
2. Make sprites for retina smaller - now they look double-sized.
3. Prev: Format search form to make labels more aligned with input fields.
4. Prev: Work with styleguide.
5. Align the project's main page to the design layout via PixelPerfect.

==============================
  Done
==============================

2. Done.
   What is the problem? I have a sprite where all my icons are kept. There are both normal and retina icons. I manage how they are presented to user by @media-queries. They look great on normal pixel density, but for retina they become doubled in size. The reason - how my gulp pipe build css for them - it provides width and height for retina with doubled values exactly as they look in a sprite. But I don't want them bigger, I want them to be double density.

   But hard way - using additional wrapper and changing original positioning of an image inside a sprite. Hard coded shifts, hard coded background-size scaling. The better way is to use svg-images instead of bitmap image. More on the topic:
   * Using compass - https://gist.github.com/thulstrup/2140082#gistcomment-1234980.
   * Hard code - http://miekd.com/articles/using-css-sprites-to-optimize-your-website-for-retina-displays/.

5. Working through the project. Started with mobile version.
