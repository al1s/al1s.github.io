.. title: Plan and done for Aug-24-2018
.. slug: plan-and-done-for-aug-24-2018
.. date: 2018-08-24 07:02:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
Challenges we faced
==============================

#. Implement a carousel for pictures.

   * number of libraries and approaches is overwhelming;
   * pure JS (aka vanilla JS) requires a lot of routine work;
   * existing libraries vary in sizes and functionality - from tens to hundreds of kb, from one kind of carousels to tens different;
   * some of them are ghosts despite thousands of stars on the Github;

#. Gather photos and descriptions.

   * it's exhaustive if you use many sources with different licensing requirements;
   * you have to check what each license asks for: how the subject could be used and what the attribution should be like;

#. Deal with transfer of data between pages.
   The user can interact with pages by:

   * following links;
   * clicking buttons;
   * pressing "Back" and "Forward" buttons in browser;
   * reloading a page;

   All of the interactions should be handled appropriately and the data in localStorage should be actualized accordingly.

#. An SVG is great for web but what about developers?

   * steep learning path;
   * at list four different ways to include it in the page;
   * each of the these ways has its own advantages and drawbacks;

#. Vertical scrollbar

   * fight it with :code:`overflow: hidden`;
   * but what if the whole page overflow the screen?
   * what if you want to work with a one css file and have scrollbar on other pages?

#. Deal with :code: `<textarea>` positioning

   * <textarea> is a replaced element, like an image, so...
   * it's an inline block aligned to text bottom line.

#. Responsiveness

   * Crave the space on mobile.
   * Make photos' size friendly for mobile.
   * Make an app accessible for different types of users.

     * in terms of human interaction - accessible for screenreaders; with enough contrast for text; controllable by keyboard;
     * In terms of different platforms - Firefox, Chrome, Edge, IE, Opera, Safari, Mobile stuff;

