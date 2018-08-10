.. title: Plan and done for Apr-16-2017
.. slug: plan-and-done-for-apr-16-2017
.. date: 2017-04-16 09:26:57 UTC-07:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

==============================
  What will I learn today?
==============================

1. Practicing vim and git(CLI via hub)
2. Study another 5 CSS things on tympanus.net
3. Run project in NTH starter kit.

==============================
 Done
==============================

3. Done. At least I'm at the exact point I was the day before, but now I can use  the power of almost fully automatic gulp tasks - sprites management, build management, block-files in BEM style.

1. Something new about Vim.

* Want to navigate between buffers in CtrlP? https://github.com/ctrlpvim/ctrlp.vim is the keys:

  * Press <c-f> and <c-b> to cycle between modes.
  * Press <c-d> to switch to filename only search instead of full path.
  * Press <c-r> to switch to regexp mode.
  * Use <c-j>, <c-k> or the arrow keys to navigate the result list.
  * Use <c-t> or <c-v>, <c-x> to open the selected entry in a new tab or in a new split.
  * Use <c-n>, <c-p> to select the next/previous string in the prompt's history.
  * Use <c-y> to create a new file and its parent directories.
  * Use <c-z> to mark/unmark multiple files and <c-o> to open them.

* Surroundings for vim from https://github.com/tpope/vim-surround works with:

  * ys[iw,w,s](something-to-wrap-into) - to wrap.
  * cs[iw,w,s](was-wraped)(should-be-wraped-into) - replace one wrapper with another.
  * ds(something-to-wrap-into) - delete wrapper.

* NerdTree cheatsheet is https://www.cheatography.com/stepk/cheat-sheets/vim-nerdtree/

  .. code-block:: bash

    t: open in new tab
    i: open split
    s: open vsplit
    x: close parent
    p: go to parent
    u: move tree root up a dir

* Use quickfix window effectively:

  .. code-block:: bash

    :copen # Open the quickfix window
    :ccl   # Close it
    :cw    # Open it if there are "errors", close it otherwise (some people prefer this)
    :cn    # Go to the next error in the window
    :cnf   # Go to the first error in the next file

* Want to use macligatures in Vim? What about catching errors when vim runs in cli mode? The answer is https://coderwall.com/p/yiot4q/setup-vim-powerline-and-iterm2-on-mac-os-x:

  .. code-block:: bash

    if has("gui_running")
       let s:uname = system("uname")
       if s:uname == "Darwin\n"
          set guifont=Inconsolata\ for\ Powerline:h15
       endif
    endif


  Faster git. I have a bunch of aliases in my Mac OS to handle git in a lightspeed. Some of them:

  .. code-block:: bash

     ga='git add' #usage: ga .
     gsts='git status'
     gdca='git diff --cached' #usage: gdca [FILE_NAME]
     gcmsg='git commit -m' #usage: gcmsg "Commit message"
     gp='git push'

**Spontaneous**. Show hidden files in Finder: `defaults write com.apple.finder AppleShowAllFiles YES`
