.. title: Plan and done for May-29-2017
.. slug: plan-and-done-for-may-29-2017
.. date: 2017-05-29 05:33:29 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

#. Make menu hide only on tablet and desktop versions or add input-label to hide JS-function.
#. Fix quirks in Safari: icons have become too small, everything become a mess on a wide screen.
#. Fix a masthead height on resolution wider 640px.
#. Fix an offer body text align for the gift message - now it aligns to center on resolutions less than 570.
#. Build additional pages - hotels, impression, blog.
#. Style the form on impression page.
#. Dive into JS.
#. Implement form validation.

==============================
  Done
==============================

7. Today's JS30 challange is to build photo gallery with an animation on click:

   * expand the clicked picture if it wasn't expanded before;
   * shrink the clicked picture if it was expanded before;
   * make a hidden text appear (or disappear as it's in the normal state).

   The first interesting stop on the route - how to expand the picture no matter if the mouse clicked on picture or on the text in front of it. An event listener returns different objects as a target in such case: :code:`div` with picture or :code:`p` for the text clicked.

   My first thought was just to prevent events if :code:`p` element is clicked, but it's bad UX - sometimes a user clicks the picture and it works, sometimes - it doesn't. The next thought - maybe I accidentally attach event handlers to all elements down the tree starting from my target div? I need to check if it's true, so how to get all event listeners on a page? Google says it has it right inside DevTool of Chrome - https://developers.google.com/web/tools/chrome-devtools/console/events. I've checked - no way, neither Chrome nor Canary. They both have tab called Event Listeners, but there is only events of active element in the Inspector, not all of them even if I tap :code:`body` element. I've found (https://gist.github.com/danburzo/9254630#gistcomment-1942033) the code which shows exactly what I need:

   .. code-block:: javascript

    const items = Array.from(document.querySelectorAll('*')).map(element => {
    const listeners = getEventListeners(element);

    return {
      element: element,
      listeners: Object.keys(listeners).map(key => {
        return {
          event: key,
          listeners: listeners[key]
        };
      })
    };

    }).filter(item => item.listeners.length);

   Checked it - only the divs with pictures have listeners and that's exactly what I want to get as all listeners on the page. My next step was to dive into Event capturing/bubbling threads - https://www.kirupa.com/html5/event_capturing_bubbling_javascript.htm. But it didn't bring any useful fruits, so I've switched to another tutorial - https://www.kirupa.com/html5/handling_events_for_many_elements.htm and found :code:`currentTarget` element which is exactly what I need! Here is a great visualization - http://joequery.me/code/event-target-vs-event-currenttarget-30-seconds/ which I implemented from scratch in my playground - https://codepen.io/alstof/full/gWNOdr/.

   I've implemented shrinking by reseting :code:`flex` rule of each picture element to the default value: :code:`flex: 1 1 auto`. And I've animated text in the same way - just reseting initial value of first and third text child elements of :code:`transform: translateY(+-20vh)` to undefined on :code:`transitionend` event (look here - https://developer.mozilla.org/en-US/docs/Web/Events/transitionend, and there is no any reason to use whichTransitionEnd by David Walsh - https://davidwalsh.name/css-animation-callback, because we have full support in all modern browsers - http://caniuse.com/#search=transitionend).

   Done in almost 7 hours most part of which I tried to get how events behave in browser.

**Spontaneous**. Here are tons of dev-tool screencasts - https://umaar.com/dev-tips/.
