.. title: Plan and done for June-12-2017
.. slug: plan-and-done-for-june-12-2017
.. date: 2017-06-12 04:52:31 UTC-07:00
.. tags: web-dev, JS30
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Dive into JS.

==============================
  Done
==============================

1. What is this all about - http://al1s.github.io/posts/plan-and-done-for-may-25-2017/.

   Day 14 - build a menu list. User story:

   * As a user I want to add dishes to my plate, one at a time, so that I'll finally have a list of dishes.
   * As a user I want to keep this list after page reload, so that it persist window closing and I'll have the same list even after a browser restart.
   * As a user I want to mark items in a list and these marks have to persist page reload, so that I'll know what I marked specially before.

   Plan:

   * use local storage to persist page reload;
   * keep all entered values in one list and save it to one item in a browser local storage;
   * prevent page reload on form submission;
   * consider performance as a first class user requirement;

   First of all - my Chrome configuration didn't let me save anything in a local storage. There are one radio and one checkboxe in Advanced config in the Cookies control list which should be considered: `Allow Local data` to be set and `Block third-party cookies and site data` unchecked.

   What was interesting:

   * I've added the handler to checkbox :code:`change` event during dynamical list item composing - it let do this if you use native interface to add elements to DOM - :code:`createElement` and :code:`appendChild`;
   * I've implemented :code:`remove` button for each element added to a list just to make it more valuable. Actually it's a little TODO app, so it should have all expected functions - add/delete items to a list, check items in a list, keep items persistent.
   * I've implemented redrawing for only added item - after a user add item the only thing changes on a page - this item added to a list (Wes told about it in a tutorial video, but his code redraw the whole list). It's performance friendly way to work with a DOM.

   Link to the page - https://al1s.github.io/JavaScript30/15%20-%20LocalStorage/index.html.
