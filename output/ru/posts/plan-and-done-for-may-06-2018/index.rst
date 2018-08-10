. title: Plan and done for May 06
.. slug: plan-and-done-for-may-06-2018
.. date: 2018-05-06 6:23:31 UTC-07:00
.. tags: javascript, React, freeCodeCamp
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

FreeCodeCamp React projects: Markdown online parser - start coding.

==============================
  Done
==============================

Online markdown editor app
--------------------------

The user `story <https://www.freecodecamp.org/challenges/build-a-markdown-previewer>`_ and the desired result.

Challenges
__________
#. Estimated size of the bundle over 50kB gzipped.
#. How to make browsersync work with react application?
#. Can't make work webpack hot reload with gulp.
#. How to render escaped HTML inside component?


Solutions
_________
#. `Explanation <https://github.com/facebook/react/issues/10780>`_ from Dan Abramov. Google for `solution alternatives <https://www.google.com/search?q=webpack+different+plugins+for+production+and+development&ie=utf-8&oe=utf-8&client=firefox-b-ab>`_.
#. I've found this `receipt <https://words.mxbry.com/making-react-webpack-browsersync-gulp-play-nice-and-hot-reload-b2c1e01522e3>`_. Here is an example of `config <https://github.com/BrowserSync/recipes/blob/master/recipes/webpack.react-hot-loader/webpack.config.js>`_
#. The problem looks like::

    react-hot-loader\index.js' is not a loader (must have normal or pitch function)

   To solve it we need to move :code:`react-hot-loader` from webpack.config.js to .babelrc as described in Dan's `post <http://gaearon.github.io/react-hot-loader/getstarted/>`_ (check step 3.2.a).

   Second problem with dependencies of eslint and depricated rule :code:`jsx-a11y/href-no-hash`. Solved it including to rules into .eslintrc - :code:`"jsx-a11y/href-no-hash": 2, "jsx-a11y/anchor-is-valid": 2`;

   Third problem is the working server doesn't produce bundle.js. But as I've got it's not a bug but a feature - webpack doesn't generate output when it runs in with devServer.

   Fourth problem is server does rebuild, but after checking for update and finding the updated module doesn't hot reload react components saying::

    App is up to date.

   Solved it after a couple of hours by reading different issues (`#581 <https://github.com/gaearon/react-hot-loader/issues/581>`_ and `#100 <https://github.com/gaearon/react-hot-loader/issues/100>`_ gave me a clue) and finally using manual of `react-hot-reload <https://github.com/gaearon/react-hot-loader#code-splitting>`_. I've exported all my components as hot.

#. I've got escaped HTML result of a `markdown converter <https://github.com/markedjs/marked>`_ function. When I tried to put the result into an output component on the page I got raw HTML on the page. The way to convert it into renderable HTML is to use weird function :code:`dangerouslySetInnerHTML` as described on `SO page <https://stackoverflow.com/a/19277723>`_ . Here is a `bit <https://github.com/facebook/react/issues/2778>`_ about the function name and sense begind it.
