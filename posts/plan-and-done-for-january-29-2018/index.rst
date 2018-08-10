.. title: Plan and done for January-29-2018
.. slug: plan-and-done-for-january-29-2018
.. date: 2018-01-29 5:03:31 UTC-07:00
.. tags: javascript, freeCodeCamp
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

FreeCodeCamp projects: Weather - fix error with unreacheble host for ip resolution; Pomodoro - start coding.

==============================
  Done
==============================

While I was editing my application to the LEAP project I found that WeatherNow app stoped working on my laptop. After light research (developer tools -> console and network tabs) I found the reason. The resource I've used for retrieving geolocation data based on my IP-address started responding with error message.

The first impulse was to replace current resource with another one. I checked for available resources and found a bunch here - https://stackoverflow.com/a/35123097/2255031. I payed attention to the list of resources which were available before but are down now. The most optimal and natural way is to add many resources to the app and then just request location from all of them and work with the first available. But how to get data from first successful promise resolved if we have multiple resources? Here is elegant solution from SO - https://stackoverflow.com/a/37235274/2255031:

  .. code-block:: javascript

    function oneSuccess(promises){
      return Promise.all(promises.map(p => {
        // If a request fails, count that as a resolution so it will keep
        // waiting for other possible successes. If a request succeeds,
        // treat it as a rejection so Promise.all immediately bails out.
        return p.then(
          val => Promise.reject(val),
          err => Promise.resolve(err)
        );
      )).then(
        // If '.all' resolved, we've just got an array of errors.
        errors => Promise.reject(errors),
        // If '.all' rejected, we've got the result we wanted.
        val => Promise.resolve(val)
      );
    }
