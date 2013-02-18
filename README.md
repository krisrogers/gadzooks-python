# Gadzooks!

Gadzooks! is a simple utility for displaying the results of Python unit tests in HTML.

It requires Python 2.7+ due to the addition of test discovery features in unittest.

It can be run directly from source
    
    python path_to_gadzooks_source/gadzooks/ -h

Or, it can be installed:

    cd path_to_gadzooks_source
    python setup.py install
    
Once installed, run from the command line (make sure Python's scripts directory is on your PATH):

    gadzooks --discovery_dir /path_to_tests/
    
Or, from within Python:

    from gadzooks.core import TestRunner
    TestRunner(discovery_dir='.', discovery_pattern='test*.py', output_file='test_results.html') 
    
## Examples
To run the example tests:

    gadzooks --discovery_dir path_to_gadzooks_source/examples/tests
    
## Screenshots
Some shots from the output of running the examples tests:

![Summary](http://krisrogers.github.com/gadzooks/summary.png)

![Test Details](http://krisrogers.github.com/gadzooks/tests.png)

![Raw Log](http://krisrogers.github.com/gadzooks/log.png)