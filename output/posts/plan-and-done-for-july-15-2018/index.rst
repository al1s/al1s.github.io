.. title: Plan and done for July-15-2018
.. slug: plan-and-done-for-july-15-2018
.. date: 2018-07-15 10:43:31 UTC-07:00
.. tags: javascript, D3, graphs
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

Data visualization project: build US map with top economic activities for each state.  I want to get data spread over all industry groups for each state to see what are economy drivers for each state. 

==============================
  Done
==============================

Challenges
----------

#. Unable to get much data from API in the way I want.
#. 


Solutions
---------

#. There are too much data I want to retrieve from `Census bureau API <https://www.census.gov/data/developers/data-sets/cbp-nonemp-zbp/cbp-api.html>`_ - it's ok to get 200 rows, but if I want to break it down to more grained data - the API shuts down. The reason I want more data - its current aggregation seems weird for my goals. For example - two industries (5415 - Computer Systems Design and Related Services is not in 51 - Information) belonging in my opinion to one group are actually in different.

   One way to solve it - prefetch all data to local storage and work with it. Then what is the best way to do it? Or maybe it's better to pretend that I have one, and just work with data as if I have the API for it.

#. 
