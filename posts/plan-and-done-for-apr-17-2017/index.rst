.. title: Plan and done for Apr-17-2017
.. slug: plan-and-done-for-apr-17-2017
.. date: 2017-04-17 10:42:14 UTC-07:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Practicing vim and git (CLI via hub)
2. Study another 5 CSS things on tympanus.net
3. Add "To top" link.
4. Add menu animation on page down.
5. Add sprites for retina.
6. Format search form to make labels more aligned with input fields.
7. Fix readme.md for the project (it contains original NTH-starter-kit text).
8. Work with styleguide.
9. Migrate all notes about web-dev progress to the blog.
10. Tweet my findings.

==============================
  Done
==============================

3. Done. Just included existing block to the project and rerun gulp.

4. Done, but without smooth animations. I don't want to use JQuery animations, because of performance. Here is - https://apeatling.com/2014/01/building-smooth-sliding-mobile-menu/ - example how to handle such animation right, but I stuck in catching ``transitionEnd`` event. Tried to attach it to ``nav`` and to ``body``, but it haven't worked.

   Finally made it with a little help from the codepen - https://codepen.io/andiio/pen/gspxJ.

5. Done. Details (how to handle icons, images and favicon) are taken from http://ivomynttinen.com/blog/a-guide-for-creating-a-better-retina-web. Exact media query for background-image should looks like http://brettjankord.com/2012/11/28/cross-browser-retinahigh-resolution-media-queries/. And https://bjango.com/articles/min-device-pixel-ratio/ is a pixel ratio tester.

**Spontaneous**. How to deploy projects to gh-pages? https://gist.github.com/cobyism/4730490 one of the answers. But I have better one - it's already integrated into NTH-starter-kit: "gulp delpoy" and you're done.

**Spontaneous**. Publish with Nikola. Installation is http://brunettoziosi.eu/posts/blogging-with-nikola-ipython-github/. After it starts use CLI with::

  source /Users/alstof/Documents/virtualenv/nikola/bin/activate
  nikola post
  nikola github-deploy

From http://louistiao.me/posts/how-i-customized-my-nikola-powered-site/. There are more about tuning nilola.

Thinking on autodeploy functionality just like ``gulp watch`` does: I create a blog post and save it and ... it's on my site. Here - http://entrproject.org/ - is utility to start moving in the direction.

Nikola engine is written with Python, so its primary text format is reStructuredText (aka .rst). Resources to taste it:

* Here is Gist - https://gist.github.com/dupuy/1855764 - with comparision.
* And Sphinx manual - http://www.sphinx-doc.org/en/stable/rest.html - with quick examples.

**Spontaneous**. Start a project with NTH-starter-kit::

  git clone https://github.com/al1s/NTH-start-project.git technomart
