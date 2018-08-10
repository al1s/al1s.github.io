.. title: Plan and done for May-23-2017
.. slug: plan-and-done-for-may-23-2017
.. date: 2017-05-23 15:49:23 UTC-07:00
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
#. Implement form validation.

==============================
  Done
==============================

6. Stuck a little with :code:`datepick` element again. I've added it to the project's review page and I've got an error: :code:`The specified value "24-05-2017" does not conform to the required format, "yyyy-MM-dd".` Tried to fix it quickly with setting :code:`dateFormat` property for an element to the value: :code:`dateFormat: "dd-mm-yyyy"`, but still no result.

   But it works if I set the default value: :code:`yyyy-mm-dd`. And I've found another thing to improve - to implement validation for all fields and especially checking whether the start date is before the end date. Added to TODO.

7. Tried to extract all values from an array and represent them as a list of strings. Tried to get to with :code:`arr.toString().replace(',', '\n')` and discovered that it replaces only the first occurance of search string. Found an advice to make it with :code:`arr.toString().split(',').join('\n')`.
