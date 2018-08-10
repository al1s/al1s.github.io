.. title: Plan and done for April 15 - May 05
.. slug: plan-and-done-for-april-15-2018
.. date: 2018-04-15 6:00:31 UTC-07:00
.. tags: javascript, freeCodeCamp
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

FreeCodeCamp projects: Simon game - start coding.

==============================
  Done
==============================

Simon game app
--------------

The user `story <https://www.freecodecamp.org/challenges/build-a-simon-game>`_ and the desired result.

Game process
____________

1. On Start game load the game engine.
2. Choose a random sequence and keep it as current.
3. Save current game position - 1.
4. Play sequence from beginning to the current position inclusive.
5. Wait for user input.
6. Compare each entered element with corresponding element in sequence.
7. On error: show message; buzz.
8. On success: move current position one element right; repeat from step 3.
9. On success in strict mode: repeat from step 2.


Challenges
__________

#. What is the Simon game?
#. How to get sectors?
#. How to play sound?
#. How to make color of the sector blink lighter on click or touch?
#. How to produce a sequence of sounds?
#. How to make the shape of active element not squared?
#. How to inform user about winning in the game?
#. How to make delays to handle state changes in UI more smoothly?
#. How to synchronize ending of Web Audio API Oscillator play with UI?


Solutions
_________

#. `Explanation <https://en.wikipedia.org/wiki/Simon_(game)>`_ on the Simon game.

#. We can get circle sectors by `CSS hacking <https://stackoverflow.com/questions/21205652/how-to-draw-a-circle-sector-in-css>`_ for div elements with special background filling or trasformations. It's many lines of an unintuitive code. My way is to set a background image for each sector to inline SVG. Code is very intelligible and clear:

   .. code-block::

    <svg
       xmlns="http://www.w3.org/2000/svg"
       viewBox="0 0 200 200"
       id="fourColorsCircle">
      <path fill="red"    d="M100,100 L100,0   A100,100 1 0,1 200,100 z" id="sector_XY" />
      <path fill="blue"   d="M100,100 L200,100 A100,100 1 0,1 100,200 z" id="sector_Xy" />
      <path fill="yellow" d="M100,100 L100,200 A100,100 1 0,1 0,100   z" id="sector_xy" />
      <path fill="green"  d="M100,100 L0,100   A100,100 1 0,1 100,0   z" id="sector_xY" />
    </svg>

#. Use Web Audio API to make sounds out of HTML. Great explanation with a working code is at `CSS tricks <https://css-tricks.com/introduction-web-audio-api/>`_. Oscilator with sine wave form at a given frequency with Gain node to control fade out.

#. There is SVG modified for any touched element or inner shadow for the element (but it doesn't work with SVG). There is :code:`lighten` function in LESS but I don't want to add another framework (even if it's just CSS post-processing framework) just because of one function. I've tried to use :code:`filter: opacity` in CSS as described in the `post <https://codepen.io/noahblon/post/coloring-svgs-in-css-background-images>`_, but it produces different result on different colors - works best on green and worse on red. Finally I replace SVG for a second on key pressed to its brighter version.

#. The problem is the Web Audio API oscilators are played at once despite they are played in a loop. The way to manage sequences I need to set exact time spot for each note to be played, schedule it. Here is the `first <http://catarak.github.io/blog/2014/12/02/web-audio-timing-tutorial/>`_  short and the `second <https://www.html5rocks.com/en/tutorials/audio/scheduling/>`_ much thorough explanation.

#. I want the game to be accessible, but I don't like the shape of common active outline. Couldn't find any advices on making it more acceptable - not just plain squared, but something that repeats the form of the original element. Variant - to implement the whole keyboard layout to play the game with ARIA description on key mapping.

#. I want some fanfare-like sound. And the only thing that come to my mind is ta-da-da-daaa-da-da from hockey matches timeouts. Looked at Wiki and after a while I've found it is the `Charge! <https://en.wikipedia.org/wiki/Charge_(fanfare)>`_. In order to play it through the tone generator I had to implement additional function which let me to play chords and set note duration.

#. One way to do it is to put :code:`setTimeout()` everywhere I want a delay. But it makes it harder to deal with a sequence of delays or a sequence of UI interactions. I want a :code:`Promise()` power to chain all interactions in a highly visible structure. SO gives an `example <https://stackoverflow.com/questions/22707475/how-to-make-a-promise-from-settimeout>`_ of such implementation.

#. I want to pause listening on buttons while the app is playing a sequence: it could be inconsistent for a user to press a button during the play and wait for it to be consumed by an app as a sequential input. The problem is that an osicllator neither has callback nor returns a promise. After a little research I've `found <https://stackoverflow.com/a/32848139>`_ a solution in the form of an :code:`onended` event of an Oscillator node (`here <https://webaudio.github.io/web-audio-api/#dom-audioscheduledsourcenode-onended>`_ is description). The final solution is to implement a sequence player to return a promise of all promises and a tone player to return a promise on :code:`onended` event. But there is another problem. Gain node provides a fade-out and goes on even when the sound is barely audible but the UI is still frozen. It's inconsistent for a user to hear or see nor activity from an app but being unable to interact with it. In order to produce more reliable behavior I exluded the last tone from a waiting list and during it's play the user may start interact with the app.
