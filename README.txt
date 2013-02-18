Gadzooks!
=========

Gadzooks! is a simple utility for displaying the results of Python unit tests in HTML.

It can be run directly from source::
    
    python path_to_gadzooks_source/gadzooks/ -h

Or, it can be installed::

    cd path_to_gadzooks_source
    python setup.py install
    
Once installed, run from the command line (make sure Python's scripts directory is on your PATH)::

    gadzooks --discovery_dir /path_to_tests/
    
Or, from within Python::

    from gadzooks.core import TestRunner
    TestRunner(discovery_dir='.', discovery_pattern='test*.py', output_file='test_results.html') 
    
Examples
========
To run the example tests::

    gadzooks --discovery_dir path_to_gadzooks_source/examples/tests

Authors
=======

* Author: `Kris Rogers`

Note
----

Gadzooks! only supports Python 2.7.x due to the addition of test discovery features in unittest.