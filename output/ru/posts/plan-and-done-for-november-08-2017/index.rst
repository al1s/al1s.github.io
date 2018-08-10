.. title: Plan and done for November-08-2017
.. slug: plan-and-done-for-november-08-2017
.. date: 2017-11-08 15:32:31 UTC-07:00
.. tags: javascript, freeCodeCamp
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

FreeCodeCamp curriculum: No repeat please.

==============================
  Done
==============================

Permutations and combinations. There are bunch of algorithms to construct permutations. I've tried Heap recursive, Heap iterative and Steinhaus-Johnson-Trotter. The code for each is here - https://codepen.io/alstof/pen/jarvNx. Couldn't get grounded intuition behind Heap algo: the reason it works - it has a pattern of elements swapping, but it's very easy to implement:

  .. code-block:: javascript

    var heapPermute = (n, arr) => {
      var swap = (arr, pos1, pos2) => [arr[pos1], arr[pos2]] = [arr[pos2], arr[pos1]];
      if (n === 1) console.log(arr.join(''));
      else {
        for (let i = 0; i < n - 1; i++) {
          heapPermute(n - 1, arr);
          swap(arr, n % 2 === 0 ? i : 0, n - 1);
        }
        heapPermute(n - 1, arr);
      }
    }

SJT looks a little more complicated, but it has more sense for me - just build the whole pyramid from scratch - starting with permutation of 1, 2, 3 ... elements and add every next element to what you've already got in every porision from last to first for every odd element of previous permutation and first to last for every even one.

Good source of explanation is Khan Academy - https://www.khanacademy.org/math/precalculus/prob-comb/combinatorics-precalc/v/factorial-and-counting-seat-arrangements.

Pictures with explanation are available at Wiki:

* Heap - https://en.wikipedia.org/wiki/Heap%27s_algorithm
* SJT - https://en.wikipedia.org/wiki/Steinhaus%E2%80%93Johnson%E2%80%93Trotter_algorithm

