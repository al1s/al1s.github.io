.. title: Plan and done for August-27-2017
.. slug: plan-and-done-for-august-27-2017
.. date: 2017-08-27 05:28:31 UTC-07:00
.. tags: javascript, freeCodeCamp
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

I am moving towards application to Microsoft LEAP program - http://www.industryexplorers.com/applicants. What should I do to fit better? My deadline is 15 September 2017.

==============================
  Done
==============================

1. How to terminate (stop, interrupt) Chrome session without closing `tab`? Go to ::

     Menu → More Tools → Task Manager

   find the task hanging, press `End process` button.

   From here - https://stackoverflow.com/a/27261978/2255031.

2. How to calculate number of unique words in a file with \*nix shell ::

     cat someFileName.txt | tr ' ' '\n' | sort | uniq -c | awk '{print $2": "$1}'

   and you've got your numbers.
