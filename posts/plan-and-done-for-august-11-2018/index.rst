.. title: Plan and done for August-11-2018
.. slug: plan-and-done-for-august-11-2018
.. date: 2018-08-11 04:57:31 UTC-07:00
.. tags: web-dev, JS, Code Fellows, Code201
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

#. Practicing Javascript at CodeFellow.
#. Generation ideas for Code 201 Final projects.

==============================
  Done
==============================


Idea for the final project.
___________________________

Chrome extension for tracking and presenting user with his activities in the browser.

Events to track:
++++++++++++++++

* New tab opened.
* New page loaded (with an url to track). 
* Time spent in the current tab (all user events are tracked with attach to the 1st level domain).
* User clicked in the current tab.
* User typed in the current tab.
* Tab switched.
* User followed a link to a new domain.

Time scope 
++++++++++
The last 7 days.

Domain scope
++++++++++++
All domains.

Final result 
++++++++++++
2 diagrams showing top 20 domain names:

* for the time user spent on each during the last 7 days.
* for the user clicks on each during the last 7 days.

Data format:
++++++++++++

.. code-block:: javascript

  var domainLastVisited = {
    lastDateVisited: domain
  };

  var trackingData = {
    [domain]: {
      timeSpent: [seconds],
      clicks: [count],
      visits: [time],
    }
  }

User stories:
+++++++++++++

As a user, I want to have information of my internet activities to understand where I spend most of the time browsing.

As a user, I want to know what attracted me the most during the past week. 

As a user, I want to know which sites I've attended the most.

As a user, I want to track my activities in Chrome for the week: the sites I spent the most of the time and those which requires me to interact the most.

As a user I want all tracking information to be presented to me in forms of beautiful diagrams.

As a dev, I want to get an experience of development of browser extensions.

As a dev, I want to work with data presentation tools.

As a dev, I want to work with available in-browser data storage techniques.

Sources:
++++++++

#. `Google <https://www.google.com/search?q=track+user+actions+in+browser+tabs+by+extension+site:stackoverflow.com&safe=active&client=ms-android-google&prmd=nisv&sa=X&ved=2ahUKEwjM5IL77OTcAhUo4IMKHY5SAXwQrQIoAjACegQICRAG&biw=412&bih=604&dpr=2.63>`_ it.
#. `Tracking <https://stackoverflow.com/q/36243128>`_ user activity.
#. Tab is `focused <https://stackoverflow.com/a/6184276>`_.
#. extensions on my machine: ~/.config/google-chrome/Default/Extensions/
#. `CRUD <https://docs.telerik.com/kendo-ui/controls/data-management/grid/how-to/Editing/grid-localstorage-crud>`_ with local storage.
