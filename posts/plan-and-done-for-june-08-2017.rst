.. title: Plan and done for June-08-2017
.. slug: plan-and-done-for-june-08-2017
.. date: 2017-06-08 16:05:31 UTC-07:00
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

   Day 11 - Custom video player. Here is MDN manual on media element control - https://developer.mozilla.org/en/docs/Web/API/HTMLMediaElement. And here is a walkthrough on building custom player - https://developer.mozilla.org/en-US/Apps/Fundamentals/Audio_and_video_delivery/cross_browser_video_player.

   Done. What were interesting:

   * to set progress bar to position relative to movie position I used :code:`setInterval` with percentage number rounded with custom :code:`round` function which supports arbitrary precision.
   * to make progress bar controllable (it's a simple colored :code:`div` with flexible width with another :code:`div` as a wrapper) I had to find position of the mouse relative to element. Here is example - https://stackoverflow.com/a/10109204 - how to get it.

   Used JS elements:

   * querySelector;
   * addEventListener, removeEventListener;
   * setInterval, clearInterval;
   * mediaElement.play, mediaElement.pause, mediaElement.currentTime, mediaElement.duration, mediaElement.volume, mediaElement.playbackRate.
