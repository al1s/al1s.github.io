.. title: Plan and done for July-26-2017
.. slug: plan-and-done-for-july-26-2017
.. date: 2017-07-26 12:48:31 UTC-07:00
.. tags: javascript, freeCodeCamp
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

Dive into JS.

==============================
  Done
==============================
.. raw:: html

    <style>
      .t30 {background-color: #A50021; color: #fff;}
      .t25 {background-color: #D82632; color: #fff;}
      .t20 {background-color: #F76D5E; color: #242442;}
      .t15 {background-color: #FFAD72; color: #00365c;}
      .t10 {background-color: #FFE099; color: #001F66}
      .t5 {background-color: #FFFFBF; color: #000040;}
      .t0 {background-color: #E0FFFF; color: #1F0000;}
      .t-5 {background-color: #AAF7FF; color: #1F0000;}
      .t-10 {background-color: #72D8FF; color: #1F0000;}
      .t-15 {background-color: #3FA0FF; color: #1F0000;}
      .t-20 {background-color: #264CFF; color: #fcc;}
    </style>
.. role:: t30
.. role:: t25
.. role:: t20
.. role:: t15
.. role:: t10
.. role:: t5
.. role:: t0
.. role:: t-5
.. role:: t-10
.. role:: t-15
.. role:: t-20

Who this article addresses to? - developers who starts they journey.
What I want to show? - System approach to an implementation.
What is my system of interest? - Users who wants to check current weather condition.
We've got user story list.


Implementing the FreeCodeCamp project - Local weather app.

User stories (published on the appointment page - https://www.freecodecamp.org/challenges/show-the-local-weather):

* I can see the weather in my current location.
* I can see a different icon or background image (e.g. snowy mountain, hot desert) depending on the weather.
* I can push a button to toggle between Fahrenheit and Celsius.

I want to mention that I haven't seen example app (https://codepen.io/freeCodeCamp/full/bELRjV) before I've finished my initial working prototype so all considerations below are based on common sense. I want to move along the plan below to demonstrate my implementation process.

1. Design considerations:

* pure JS;
* minimalistic design;
* a11y is for accessability and it's one of the goals;
* responsive design;

2. Plan of the app:

* fetch data from weather API;
* prepare visual representation of the page depending on data fetched;
  * get the photo which reflect the current condition;
  * get the color depicting current temperature;
* use HTTP cookie to store user scale preference - celsius or fahrenheit;

3. Challenges and implementation:

* CSS variables don't work with CSS SVG styles - solved;
* Geolocation silently dies on tablets and phones - solved;
* CORS for WeatherUnderground's autocomplete API - solved;
* Support for a wide range of browsers - solved.


Design
======

Frameworks vs. Pure JS
----------------------
The first thought was to dive into React to wrap my head around its basics. The second one was calm and clear: I have to implement it just with knowledge I've already got, without shiny new and appealing stuff. All new libraries are pleasure for procrastinating mind, it's not the time for it. JQuery? Why do I need it at all - current browser engines has plenty of functionality as is, without additional wrappers.

Minimum page element set
-------------------------
I decided to use as a current weather conditions indicator the destinctive photos of nature: clear - the view where the sky is without any clouds, cloudy - the sky covered fully with clouds etc. The photo goes to the background and above it I want to see only current time, date, location and temperature. I wanted to visually highlight temperature level so I used the box for the text block colored according to the current temperature (there is a bunch of temperature coding examples in google - https://goo.gl/hsnimK). According to the user story the app needs the toggle for different temperature scales. I wanted to see neither additional preferences tab nor a checkbox floating in a space and distracting from the pure functionality. On the other hand I had to present a user with a disctinct temperature scale symbol so why not to use such a symblol as a toggle. I could just add event listener to the sybmol, but the second thought was that it's a poor UI experience. What if I put both letters depicting Celsius and Fahrenheit scales on the page together and make one vivid and another vague to make it clear, which is currently on?

Accessibility
-------------
Accessibility aspects of the page include visual, navigation, audible sections. The visual part is about color contrast and there is a great tool from Lea Verou to check whether contrast rate in compliance with WCAG (which is decrypted as Web content accessibility guidlines by W3) - https://leaverou.github.io/contrast-ratio. The navigation part means that page is controlable by a keyboard. All three control elements of the page are native HTML control elements: button for 'Info' and scale toggles which are radio with labels. A user can hop between them with :code:`<tab>` and press :code:`<Enter>` or :code:`<Space>` to make them act. The audible part includes :code:`aria-*` tags for all elements to make it clear what scale is used now and how contol elements work. I used Chrome WAVE extension as an accessibility audit tool. There are a cople of tools to analyze web pages compliance - https://soap.stanford.edu/tips-and-tools/tools. And I used examples of :code:`aria*` labels usage from - http://oaa-accessibility.org/.

(Accessibility is an important matter for me. I always notice features of physical accessibility around me and pay attention to color and texture decision in visual media - art, ads, TV. Often I notice thoughts in the background of color contrast in different media. Wish to have an app in my phone which could analize current picture and show it the way people with different visual abilities perceive. I've tried to find something like this in both app stores but didn't find any - I mean not simple color checker against WCAG recomendations but something like vision simulator which would wash out normal color perception and present you with different color world around. Maybe such app needs modern hardware and frameworks for augmented reality - ARKit like...).

Responsiveness
--------------
Responsive design means the page suits well to be displayed on any screen or by any screenless devices. The first consideration here whether content is flexible to fit different screen resolution. The second one is whether the page responds to user expectation on loading time. Chrome has built-in audit tool which shows exactly what makes a page load slow. In my case it's a usage of web fonts. Here is a great article by Zach Leatherman about web fonts optimization - https://www.zachleat.com/web/comprehensive-webfonts/#font-display but I didn't follow recomendations because a performance audit shows that the first meaningful element of the page is shown within 2 seconds including web font loading which is an acceptable result.


Through the plan of the implementation
======================================
API to get weather
------------------
My weather API is Weather Underground (WU) - https://www.wunderground.com/. Why it's not OpenWeatherMap - I use WU everyday for about a year and it provides the consistent reliable result. I've used :code:`fetch` as a method to get data. But there was a catch. Check challenges section for details.

Visual elements of the page
---------------------------
Photos are taken from Flickr. They all are under Creative Commons licenses. Here is the full list:

.. image:: /images/cloudy_winter_tn.jpg
   :target: https://flic.kr/p/RDW4Z1
   :alt: Photo of a cloudy winter day

.. image:: /images/partlysunny_winter_tn.jpg
   :target: https://flic.kr/p/RzuZS7
   :alt: Photo of a partly sunny winter day

.. image:: /images/mostlysunny_winter_tn.jpg
   :target: https://flic.kr/p/R33zcf
   :alt: Photo of a mostly sunny winter day

.. image:: /images/sunny_winter_tn.jpg
   :target: https://flic.kr/p/RHwJiG
   :alt: Photo of a sunny winter day

.. image:: /images/cloudy_summer_tn.jpg
   :target: https://flic.kr/p/cScQxy
   :alt: Photo of a cloudy summer day

.. image:: /images/partlysunny_summer_tn.jpg
   :target: http://freestock.ca/skies_clouds_g61-coastal_clouds__hdr_p1879.html
   :alt: Photo of a partly sunny summer day

.. image:: /images/mostlysunny_summer_tn.jpg
   :target: http://freestock.ca/canada_g92-beaver_brook_scenery__hdr_p804.html
   :alt: Photo of a mostly sunny spring day

.. image:: /images/sunny_summer_tn.jpg
   :target: https://flic.kr/p/fgLTUU
   :alt: Photo of a sunny summer day

.. image:: /images/partlysunny_spring_tn.jpg
   :target: https://flic.kr/p/UtjTDm
   :alt: Photo of a partly sunny spring day

.. image:: /images/mostlysunny_spring_tn.jpg
   :target: https://flic.kr/p/SbmJj2
   :alt: Photo of a mostly sunny spring day

.. image:: /images/sunny_spring_tn.jpg
   :target: https://flic.kr/p/oavqBk
   :alt: Photo of a sunny spring day

.. image:: /images/mostlysunny_fall_tn.jpg
   :target: https://flic.kr/p/qb4cbs
   :alt: Photo of a mostly sunny fall day

.. image:: /images/flurries_tn.jpg
   :target: https://flic.kr/p/k7zUGc
   :alt: Photo of a day with flurries

.. image:: /images/fog_tn.jpg
   :target: https://flic.kr/p/dkqP1t
   :alt: Photo of a day with fog

.. image:: /images/rain_tn.jpg
   :target: https://flic.kr/p/dfkuTL
   :alt: Photo of a rainy day

.. image:: /images/snow_tn.jpg
   :target: https://flic.kr/p/7AVLQR
   :alt: Photo of a snowy day

.. image:: /images/storm_tn.jpg
   :target: https://flic.kr/p/cESNRS
   :alt: Photo of a stormy day

.. image:: /images/hazy_tn.jpg
   :target: https://flic.kr/p/pusoD1
   :alt: Photo of a hazy day

.. image:: /images/sunny_fall_tn.jpg
   :target: https://flic.kr/p/i28UqP
   :alt: Photo of a sunny fall day

As I mentioned above I changed the color of the box where weather details appear according to the current air temperature. The mapping is:

.. table:: Color temperature mapping

   =============== ===================
   Color           Temperature range
   =============== ===================
   :t30:`#A50021`  more than 30
   :t25:`#D82632`  between 25 and 30
   :t20:`#F76D5E`  between 20 and 25
   :t15:`#FFAD72`  between 15 and 20
   :t10:`#FFE099`  between 10 and 15
   :t5:`#FFFFBF`   between 5 and 10
   :t0:`#E0FFFF`   between 0 and 5
   :t-5:`#AAF7FF`  between -5 and 0
   :t-10:`#72D8FF`  between -10 and -5
   :t-15:`#3FA0FF` between -15 and -10
   :t-20:`#264CFF` between -20 and -15
   =============== ===================

User preferences
----------------
I don't want to toggle scale all the time from Fahrenheit to Celsius (the last one are natural for me but I use Fahernheit as default scale) so I added cookies to keep user preferences. There are three additional functions to create, read and erase cookie. Functions are taken from QuirksMode - https://www.quirksmode.org/js/cookies.html, but I modified `read` to use regexp instead of a loop.

Challenges
==========

Two-colored SVG and Chrome.
---------------------------------
I had two colored boxes on the page, - the first is for a weather details and the second is for a photo credit - and that was the reason to use CSS variables for font and background colors. It has been working great till I added a Creative commons icon to credit. The icon was an SVG and I wanted it to reflect the main color scheme but instead Chrome made it all black with no distinct of inner element and background.

The problem was that you cannot manage different colors for different SVG inner elements by CSS styles as expected. The solution is to use :code:`color` and :code:`fill` properties for an SVG and explicitly apply :code:`currentColor` attribute to :code:`fill` property inside SVG code to one of the elements. It will inherit color from :code:`color` property set inside CSS style. Here is explanation by Fabrice Weinberg - https://codepen.io/FWeinb/post/quick-tip-svg-use-style-two-colors.

Geolocation on mobiles
----------------------
After I finished initial version of the page I tested it in Chrome, Firefox, Opera and Safari. It worked great with the first three and throws an unknown geolocation error in Safari. My thought was: Ok, let's skip it for a while and switch to mobile devices. I tested the app on an iPad, an iPhone, and an Android phone, with a range of browsers: Safari, Chrome, Firefox. The only combination that worked was Androind + Firefox. All others throw a geolocation timeout error. I digged for a little and found only that there was not only my problem and there was a bunch of advices (the first question I had to answer was whether I worked within secured HTTP or not so yes - the app was deployed on two different services - github.io and codepen.io, both provided secured HTTP). I've tried following advices:

* use :code:`PositionOptions.maximumAge` set to Infinity;
* use :code:`PositionOptions.timeout` set to long intervals;
* use :code:`PositionOptions.enableHighAccuracy` either `true` or `false`;
* use :code:`watchPosition` instead of :code:`getCurrentPosition`.

None of these worked for me so as an alternate solution to the problem I added geoIP request as a fallback if original geolocation request was unsuccessful, so everytime the app can't get the location data from a device it asks for the location of IP-adress that a data provider assigned to your device. As a free secured engine I used geoIP API - https://freegeoip.net/json/.

Support for a wide range of browsers
------------------------------------
During an initial attempt, I succeed in implementing a working prototype of the app. It worked in Chrome and Firefox (last versions) on a desktop platform and didn't work in Safari (due to lack of support of :code:`fetch` before 10.3) and on mobile (weird quirks with :code:`navigator.geolocation` mentioned below). It's not the way I wanted it to be, so I moved my project from plain single html file to gulp-powered workflow to get:

* ES6 features work in older browsers with babel - https://babeljs.io/;
* browser specific prefixes with autoprefixer - https://github.com/postcss/autoprefixer;
* fetch polyfill installed and attached as an npm module - https://github.com/github/fetch;
* browser-sync to monitor and reload app in browsers on any change;

My gulp configuration is available on github - https://github.com/al1s/WeatherNow/blob/master/gulpfile.js.

Cross-domain request fails for WU autocomplete API
--------------------------------------------------
As an addition to the pure geolocation based forecast I planned to implement user defined weather request - you provide a city name, the app gives you the current weather. There is an API for searching by city name provided by WeatherUnderground - https://www.wunderground.com/weather/api/d/docs?d=autocomplete-api. Initial attempt showed there is an Access-Control-Allow-Origin error - https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS. Managing Access-Contol-Allow-Origin policy generally is a server-side story. In a couple words - the server returns only what user's browser asks for and if a browser doesn't get in page headers explicit permission to use the page data it returns an Access-Contoll-Allow-Origin violation error. Wiki provides additional details and visual representation of the way CORS works - https://en.wikipedia.org/wiki/Cross-origin_resource_sharing. I solved the problem by adding CORS proxy (https://cors-anywhere.herokuapp.com/) in the middle. It works till there is no sensitive details flow between a user and a server.

Wrap up
========
There was an interesting journey to coding.

twitter
blog
github
