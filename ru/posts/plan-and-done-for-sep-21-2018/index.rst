.. title: Plan and done for Sep-21-2018
.. slug: plan-and-done-for-sep-21-2018
.. date: 2018-09-21 13:06:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

Retro about getting data by Express server from external API (Google Books)
____________________________________________________

==============================
What did we do well, that if we don’t discuss we might forget?
==============================
Practiced in debugging Express <=> Postgres interaction;

==============================
What did we learn?
==============================
Craft your database schema carefully not to be bitten by poor design later: we created the table with the unique constraint on author column and today were debugging insertion error for 20 minutes before found the reason why we can't add another book.

==============================
What should we do differently next time?
==============================
Spend more time on styling.

==============================
What still puzzles us, or what do we need to learn more about?
==============================
Best practices for creating a robust server with Node/Express/DB with input validation and unified error handling. Current state looks fragile.

