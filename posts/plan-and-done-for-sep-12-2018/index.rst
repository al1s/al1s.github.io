.. title: Plan and done for Sep-12-2018
.. slug: plan-and-done-for-sep-12-2018
.. date: 2018-09-12 11:46:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================================================
What did we do well, that if we don’t discuss we might forget?
==============================================================
We accomplished the tasks given in quite short period and find only two things which required some research. One of them - how to implement 404 error handler. The way we have it implemented - by some 'anything else goes' - seems weird 'cause handling errors and routing are different behavior. We need some middleware to implement this handler.

==============================
What did we learn?
==============================
We've learned that the routes in `express.static` routes are relative, but in `get` they are absolute. That's why we need to setup them with `__dirname`.

==============================================================
What should we do differently next time?
==============================================================
Switch between roles earlier, maybe every 15 minutes?

==============================================================
What still puzzles us, or what do we need to learn more about?
==============================================================
How to correctly implement 404 handler.
