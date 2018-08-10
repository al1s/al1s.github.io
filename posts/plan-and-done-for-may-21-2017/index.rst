.. title: Plan and done for May-21-2017
.. slug: plan-and-done-for-may-21-2017
.. date: 2017-05-21 04:34:21 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

#. Make menu hide only on tablet and desktop versions or add input-label to hide JS-function.
#. Fix quirks in Safari: icons have became too small, everything become a mess on a wide screen.
#. Fix a masthead height on resolution wider 640px.
#. Fix an offer body text align for the gift message - now it aligns to center on resolutions less than 570.
#. Build additional pages - hotels, impression, blog.
#. Style the form on impression page.
#. Dive into JS.

==============================
  Done
==============================

6. Combined my project's radio and checkbox elements in a playground - https://codepen.io/alstof/pen/ybQVyE.

   There are two things left on the review page: layout everything according to original design and make it live. The second goal is quite large - I have to implement simple backend - storing feedback as a json file with basic CRUD. As an example or a main candidate for it here is OS project - http://brian.io/lawnchair/.

7. Found great workshops with potential to become an meetup or event. The map is located here - https://nodeschool.io/ru/#functionaljavascript. I came here while trying to implemnt element counter (something like my native SQL syntax - :code:`SELECT element, count(*) FROM element_list GROUP BY element;`) in ES6 with :code:`reduce`. It turned out to be easier than I expected but I still haven't got how it works: why :code:`undefined` value in a named array could be incremented and how :code:`or` worked the way it did:

   .. code-block:: javascript

    let specieList = creatures.reduce((species, creature) => {
      species[creature.species] = ++species[creature.species] || 1;
      return species;
    }, {});

