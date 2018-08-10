.. title: Plan and done for May-27-2018
.. slug: plan-and-done-for-may-27-2018
.. date: 2018-05-27 6:03:31 UTC-07:00
.. tags: javascript, freeCodeCamp, React
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

FreeCodeCamp React projects: Camper Leaderboard.

==============================
  Done
==============================

Challenges
----------

#. I want to use async/await for fetching data but what about catching errors?
#. When and where to fetch initial data to React app?


Solutions
---------

1. Here is the `receipt <https://blog.grossman.io/how-to-write-async-await-without-try-catch-blocks-in-javascript/>`_ to do it with style:
   
.. code-block:: javascript

   function to(promise) {
     return promise.then(data => {
         return [null, data];
       })
       .catch(err => [err]);
   }

2. The right place is :code:`componentDidMount`. An explanation - `Initial data via AJAX <https://zhenyong.github.io/react/tips/initial-ajax.html>`_.
