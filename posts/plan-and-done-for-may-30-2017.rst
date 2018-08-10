.. title: Plan and done for May-30-2017
.. slug: plan-and-done-for-may-30-2017
.. date: 2017-05-30 12:03:30 UTC-07:00
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

7. Tried to implement plain text parser. I want to get JSON-like data as output. Stuck with :code:`map` because it returns the whole object but I need only one element of it. Found the solution here - https://stackoverflow.com/questions/36120265/how-to-convert-text-file-to-json-in-javascript. KISS!

   I had some issues with understanding how to get only part of the keys in JSON object. Tried to rebuild object using :code:`map` and :code:`forEach` but failed. And the funniest part was that I couldn't find the answer in Google! I know, I know - a question has and answer or at least part of it, so the question was wrong. And then I just realized that it's better to use notions of set theory as it applies to Databases. What if I would ask to fine subset of JS object such as JSON. And finally I've found the solution - https://stackoverflow.com/a/39333479. And the approach is very neat, not much longer or trickier then in declarative languages (SQL for example).

   Another obstacle was how to get data from node.js fs.readFile function. It seemed unnatural not to get data in return statement, but it's just another paradigm of programming and interrelation between objects in an async world. Here is an explanation on how to do it better - https://stackoverflow.com/questions/10058814/get-data-from-fs-readfile.

