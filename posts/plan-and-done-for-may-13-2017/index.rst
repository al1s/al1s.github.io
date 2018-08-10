.. title: Plan and done for May-13-2017
.. slug: plan-and-done-for-may-13-2017
.. date: 2017-05-13 05:22:14 UTC-07:00
.. tags: web-dev
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

#. Make menu hide only on tablet and desktop versions or add input-label to hide JS-function.
#. Fix quirks in Safari: icons have became too small, everything become a mess on a wide screen.
#. Fix a masthead height on resolution wider 640px.
#. Fix an offer body text align for the gift message - now it aligns to center on resolutions less than 570.
#. Build additional pages - hotels, impression, blog.
#. Style the form on impression page.

==============================
  Done
==============================

3. Fixed on the May 10.

4. Fixed on the May 10. The reason was in fluid flexbox elements behavior. Chanded ``flex-grow`` to 0 - no grow on rescale for icon element.

5. Built html part of an impression/review page on the May 10.

6. There are many parts:

   * Form accessibility.

     Tried to use ``fieldset`` and ``legend`` elements for a review page but they are funny: ``legend`` positions above ``fieldset`` without any respect to indents of the last. Here is details on froms - https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/How_to_structure_an_HTML_form. Tried different ``display`` options but there is no visible effect. Kept ``div`` for grouped input elements.

     Here is a fuitful discussion why a ``legend`` element behave the way it is - http://forums.mozillazine.org/viewtopic.php?f=7&t=75083. It looks like a ``legend`` is a part of the border of a ``fieldset`` and it's a natural behavior for ``legend``. Here is how it looks in pure - https://mdn.github.io/learning-area/html/forms/html-form-structure/fieldset-legend.html.

     A solution would be to use a ``fieldset`` for accessibility reasons and skip ``legend`` at all.

   * Style radio elements.

     Here is example of a custom radio button style - http://codepen.io/AngelaVelasquez/pen/BWXbxP.

