Gadzooks!
=========

Gadzooks! is a simple utility for displaying the results of Python unit tests in HTML.

Right now it is in very early stages and only supports being run in test discovery mode::

    python gadzooks --discovery_dir /path_to_tests/
    
For a list of supported options::

    python gadzooks -h
    
Examples
========
To run the example tests::

    python gadzooks --discovery_dir path_to_gadzooks_source/examples/tests

Authors
=======

* Author: `Kris Rogers`

Note
----

Gadzooks! only supports Python 2.7.x due to the addition of test discovery features in unittest.