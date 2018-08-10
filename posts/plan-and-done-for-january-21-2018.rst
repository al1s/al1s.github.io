.. title: Plan and done for January-21-2018
.. slug: plan-and-done-for-january-21-2018
.. date: 2018-01-21 7:31:31 UTC-07:00
.. tags: javascript, freeCodeCamp
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

FreeCodeCamp project: Calculator.

==============================
  Done
==============================

1. To invoke numeric keyboard on mobile we need::

   <input type="tel" />

And :code:`type="number"` gives numeric keyboard too, but without symbols for arithmetic operations.

2. Tried to implement insertion of digits into :code:`<input>` with :code:`execCommand('insertText', ...)` but it seems doesn't work in FF (v57.0.4). Found old working code on SO - https://stackoverflow.com/a/1064139. It has separate routes for old IE < 9.0 and modern browsers, and the way to put elements in text field is to manually cut and then concatenate text in the field. Had some troubles with inability to put cursor at the end of the whole text after insertion but found it was due sending number primitive into the function instead of string.

3. To turn off virtual keyboard on mobile we may use HTML5 :code:`readonly` property for :code:`input` - https://codepen.io/agorilla/pen/FJIic. But it makes impossible to control calculator using real keyboard. How to detect activation of the :code:`input` field by user? By intercepting `click` mouse event. And to route :code:`click` and :code:`touchend` events differently inside a handler.

4. How to set one handler for multiple events? :code:`['click', 'touchend'].forEach(e => document.addEventListener(e, handlerFunc);`.

5. Add vibration for pressing virtual keys on mobile:

   .. code-block:: javascript

      function vibrateOnTouch() {
        if ('vibrate' in navigator) {
          navigator.vibrate =
            navigator.vibrate ||
            navigator.webkitVibrate ||
            navigator.mozVibrate ||
            navigator.msVibrate;
          navigator.vibrate(30);
        }
      }

6. I applied Kyle Simpson's OLOO pattern by separating data processing and UI into different objects and then creating and invoking application as a combination of those two. Feels clearer than mashup of both into one peace of code.

7. As a start point for UI I've choosen keybord JQuery plugin - https://github.com/Mottie/Keyboard/blob/master/js/jquery.keyboard.js.

8. Almost perfection - https://web2.0calc.com/
