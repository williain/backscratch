#!/usr/bin/env python
# Works on python2 or 3
from __future__ import print_function
import os.path
testfolder=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')

def makeabsollink(linkfile, target):
    if os.path.islink(os.path.join(testfolder,linkfile)):
        p=os.popen('readlink '+os.path.join(
          testfolder,linkfile
        ))
        curr_target=p.read().strip()
        p.close()
        if curr_target!=os.path.join(testfolder, target):
            print("{} doesn't match {}; removing".format(
              curr_target, os.path.join(testfolder,target)
            ))
            os.unlink(os.path.join(testfolder, linkfile))
    elif os.path.exists(os.path.join(testfolder, linkfile)):
        print('{} exists as a non-link; please clean it up'.format(
          os.path.join(testfolder, linkfile)
        ))
        exit(1)
    if not os.path.islink(os.path.join(testfolder, linkfile)):
        os.symlink(
          os.path.join(testfolder, target),
          os.path.join(testfolder, linkfile)
        )

def makelinks():
    makeabsollink('absolute.link','target')
    makeabsollink('absoldir.link','dirtarget/')
