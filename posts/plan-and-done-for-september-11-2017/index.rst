.. title: Plan and done for September-11-2017
.. slug: plan-and-done-for-september-11-2017
.. date: 2017-09-11 12:32:31 UTC-07:00
.. tags: javascript, freeCodeCamp
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. I am moving towards application to Microsoft LEAP program - http://www.industryexplorers.com/applicants. What should I do to fit better? My deadline is 15 September 2017.

2. FreeCodeCamp project: Wikipedia viewer.

==============================
  Done
==============================

1. I've done with the application to Microsoft LEAP. The last versions of the application essays are here - https://al1s.github.com/posts/plan-and-done-for-august-22-2017/.

2. Wikipedia viewer completed as a prototype.

   Challenges:

   * huge variety of wikipedia API's parameters;
   * smooth slide-in/slide-out of search result panels;
   * icon inside input element;
   * searching in different languages in Wiki;
   * get wiki data with title, excerpt, and image;
   * validate unicode input;
   * keyup and keydown - the difference is in the last entered charecter; the first doesn't return it and the last - does.

Variety of Wiki's API parameters
--------------------------------
I've tried different ways to get data but then two things pushed me in the right way: the article on using generators to get thumbnail and excerpt from search results - https://www.mediawiki.org/wiki/API:Page_info_in_search_results and a backtrace of


Icon inside input element
-------------------------
The problem is that we cannot use :code:`::after` or :code:`::before` with replaced elements (https://developer.mozilla.org/en-US/docs/Web/CSS/Replaced_element) and :code:`input` is one of them.

The hard way to place images inside input is to wrap an input and an icon into container div and position them accordingly with relative and absolute values and indents. A lot easier is to set icon as a background-image (https://stackoverflow.com/a/917636/2255031).

There is a list of SVG icons from Font Awesome - https://github.com/encharm/Font-Awesome-SVG-PNG/tree/master/black/svg.

Validate unicode input
----------------------
The reason was - to validate user input without info on what user language is. The wrong way is to start digging to ennumerate all possible unicode ranges - http://kourge.net/projects/regexp-unicode-block. Twitter does something like this for hashtags - https://github.com/twitter/twitter-text/blob/master/js/twitter-text.js#L76. I don't need it - just filtered out all non language specific symbols::

  formInput.replace(/([.,;:=+[\]\\|\/?<>!@#$%\^\&*()'"\n\r])/g, '');

Wiki data with title, excerpt, and image
-----------------------------------------
Use :code:`generator=search` - https://en.wikipedia.org/wiki/Special:ApiSandbox#action=query&format=json&uselang=user&prop=pageimages%7Cextracts&list=&generator=search&redirects=1&formatversion=2&piprop=thumbnail&pithumbsize=300&exsentences=2&exintro=1&explaintext=1&gsrsearch=trump.

Searching in different languages
--------------------------------
Here is some topic on FreeCodeCamp forum - https://forum.freecodecamp.org/t/wikipedias-api-query-problem-with-getting-data-in-different-language/6740/9. But they discuss only one issue that could be fixed using generators in request parameters. But my question was - how to get data in your language. I used :code:`navigator.language` for it and it's the same as Wiki does, but they have more complex logic inside the search scripts for particular languages (at least with regards to Chinese).

**Unlisted**. I switched from Atom to VS Code as a primary project editor and it fits my requirements.

**Unlisted**. How to fix not repeating down or up keys in Vim on MacOS::

  defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false

From SO - https://stackoverflow.com/a/44010683/2255031.
