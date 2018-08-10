.. title: Plan and done for September-17-2017
.. slug: plan-and-done-for-september-17-2017
.. date: 2017-09-17 5:22:31 UTC-07:00
.. tags: javascript, freeCodeCamp
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

FreeCodeCamp project: Wikipedia viewer.

==============================
  Done
==============================

Trasforming search bar is implemented. Here is a pen on Codepen - https://codepen.io/alstof/pen/yzNdKj, here is a stand-alone page - https://al1s.github.io/AskWiki/.

Besides there was a todo list:

* fix address bar - remove submit parameters from it;
* clear the page if the input value is undefined;
* speed up loading and displaying data;
* limit the keys to react to meaningful - letters and entry control;
* fix browser history: make backspace to return a user to the previous page;
* fix images size - it's too crane;
* show a message on no search results;
* make the page functional on iPad mini (Safari 7);
* deal with Promise object manipulation;
* how to get the page similar to Wiki's one on no data found;

Fix browser history
-------------------
There is the :code:`history` object wich may be used to control browser behavior on back and forward buttons. Here is MDN article - https://developer.mozilla.org/en-US/docs/Web/API/History_API.

Now the page restores previous search phrase on back and forward.

Show a message when there are no results returned
-------------------------------------------------
Implemented custom error object based on https://stackoverflow.com/a/5251506/2255031. The reason was to get cutomized variables inside error object to pass it between functions. I'm not sure if it's correct coding style.

Promise with resolves and rejects
---------------------------------
I used promises in the code but the question left - how to return a value from a Promise: e.g. I've implemented common ajax request wrapper for fetch and it could be used as a call to get results but it didn't work when I tried to use it inside Promise.all function.

Special search results when nothing found
-----------------------------------------
The Wiki returns special page on no data found result - Special:search. I haven't found it was mentioned anywhere in API docs or discussed as possible result on unsuccessful search. I've tried to retrieve the same page I have in a browser but got the CORS error that I treated such as the functionality wasn't implemented in a Wiki's public API.

Unlisted
------------
I like the way VS Code simulates Vim keyboard control scheme. Everything I used in pure Vim, I use now in VS Code.
