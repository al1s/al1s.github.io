.. title: Plan and done for June-28-2018
.. slug: plan-and-done-for-june-28-2018
.. date: 2018-06-28 03:23:31 UTC-07:00
.. tags: web-dev, JS, D3
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

#. Learn D3 fundamentals.
#. Practice D3 selections.

==============================
  Done
==============================

.. role:: strike
    :class: strike

#. There are bunch of links to good articles to grasp what D3 is about:

   * `Bostock's entry point <https://bl.ocks.org/mbostock/3808234>`_ with many links inside;
   * `Elijah Meeks explanation <https://medium.com/@Elijah_Meeks/d3-is-not-a-data-visualization-library-67ba549e8520>`_

#. It takes some time to grasp how selection works in D3. Misunderstanding starts from `Introduction to D3 <https://www.youtube.com/watch?v=8jvoTV54nX://www.youtube.com/watch?v=8jvoTV54nXw>`_ by Curran Kelleher and his `notebooks <http://curran.github.io/screencasts/introToD3/examples/viewer/#/66>`_. If Update and Enter are different selections, then why when I set X coordinate and block color for update selection only, the whole result is correct - the color of all blocks is the same and they are divided appropriately along X axis? 

   The only explanation is that there is only the whole cycle every time and all objects are involved: 

   * after :code:`selection.data()` we have empty placeholder for each data point in a dataset;
   * after :code:`selection.enter()` we have DOM constructed accroding to data and attributes defined on stage 'Enter' applied to each new element;
   * after :code:`selection.update()` we have additional attributes applied to 'old' elements, those which weren't added during Enter processing... and (it was the main bug in my understanding of the rendering stages in D3) to new elements if the attributes weren't defined during 'Enter' and defined on 'Update' stage;
   * :code:`select.exit().remove()` just removes unbound elements; something like a garbage collection.

   In order to illustrate notes above I crafted two versions of the code:

.. code-block:: javascript
  
  function render(data, color){
    var t = d3.transition()
       .duration(2750);
    var rects = svg.selectAll("rect").data(data);
    console.group('Render');

    // Enter
    log('Before enter', rects);
    rects.enter().append("rect")
      .attr("y", 50)
      .attr("width",  20)
      .attr("height", 20)
      .style("fill-opacity", 1e-6)
    .transition(t)
      .style("fill-opacity", 1)
    log('After enter', rects);

    // Update
    rects
      .attr("fill", color)
      .attr("x", scale)
    log('After update', rects)

    // Exit
    rects.exit().remove()
      .transition(t)
      .style("fill-opacity", 1e-6)
    log('After exit', rects);
    console.groupEnd('Render')
    }

  setTimeout(() => render([1, 2], "red"),0);
  setTimeout(() => render([1, 2, 3, 4, 5], "blue"),2500);
  setTimeout(() => render([1, 2, 3], "green"),5000)

