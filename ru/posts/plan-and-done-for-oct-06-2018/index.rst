.. title: Plan and done for Oct-06-2018
.. slug: plan-and-done-for-oct-06-2018
.. date: 2018-10-06 11:37:14 UTC-07:00
.. tags: c#
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

Keep solving and submitting CodeWars assignments.

==============================
  Done
==============================

`Solved reverse or rotate <http://www.codewars.com/kata/reverse-or-rotate/train/csharp>`_ assignment and the most interesting as always - what is considered as best practice and clever solution by other members. The `give solution <http://www.codewars.com/kata/reviews/56b5b65783df365700000091/groups/578b6a9384ac69f8110000be>`_ is definitely clever and declarative (I strive to be as declarative as I can) and I've learned some stuff from it.

#. Dividing integer by integer in C# you'll get an integer and never a float/double/decimal. No decimal delimiter! Never. No need for :code:`Math.round` or :code:`Math.floor`. Short `SO explanation <https://stackoverflow.com/a/10851437>`_.

#. There is an :code:`Enumerable.Range()`. It works almost like :code:`range()` in Python: :code:`string.Join(",", Enumerable.Range(1,5))` will produce `"1,2,3,4,5"`. Almost like Python but not exactly because in Python the upper bound isn't included in the result, and we have additional method overload with a third parameter as step for generating the sequence.

#. There are two versions of :code:`Reverse()` method: one is for :code:`List` collection, another is for objects with :code:`IEnumerable` implemented. First is in place, second returns :code:`IEnumerable` compatible. The reasons are historical. For strings we can use both, but the second seems more declarative.

.. code-block:: C#

  char[] charArray = chunk.ToCharArray();
  Array.Reverse( charArray  );
  string result = new string( charArray  );

.. code-block:: C#

  string result = new string(chunk.Reverse().ToArray());

