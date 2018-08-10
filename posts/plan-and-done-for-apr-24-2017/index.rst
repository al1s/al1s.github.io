.. title: Plan and done for Apr-24-2017
.. slug: plan-and-done-for-apr-24-2017
.. date: 2017-04-24 04:11:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Prev: Align the project's main page with the design layout via PixelPerfect.
2. Prev: Format search form to make labels more aligned with input fields.
3. Prev: Work with styleguide.
4. Practice vim and git (CLI via hub)

==============================
  Done
==============================

4. Change windows split from vertical to horizontal (from here - http://stackoverflow.com/questions/1269603/to-switch-from-vertical-split-to-horizontal-split-fast-in-vim):

.. code-block::

    Ctrl-w t Ctrl-w K

Horizontally to vertically:

.. code-block::

    Ctrl-w t Ctrl-w H

Explanations:

``Ctrl-w t`` makes the first (topleft) window current ``Ctrl-w K`` moves the current window to full-width at the very top ``Ctrl-w H`` moves the current window to full-height at far left.

1. Background images took about three hours to clicked. Finally I've found many tutorials (calculation method, but it haven't worked for me yet - http://www.browniesblog.com/A55CBC/blog.nsf/dx/responsive-css-sprites.html,  ), but end up on the Sprite Cow - http://www.spritecow.com/, which is great to calculate relative size  and position of a specific picture inside a sprite (here is my playground - http://codepen.io/alstof/pen/NpVKeo). I've used ``background-size`` and ``background-position`` as relative percantages of pictures, then scale them with ``width`` and fit with ``height``.

   My another concerns are too much ``padding`` and ``margin`` inside a stylesheet and code reusage. First is about using primarily an indentation to align blocks without a block height at all. Second - I have two blocks, which looks similar, with small differences in indents. Should I create another block or there is a way to reuse already created?
