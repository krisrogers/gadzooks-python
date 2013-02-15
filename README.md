# Gadzooks!

Gadzooks! is a simple utility for displaying the results of Python unit tests in HTML.

It requires Python 2.7+ due to the addition of test discovery features in unittest.

Right now it is in very early stages and only supports being run directly from source as follows:
    python gadzooks/ --discovery_dir /path_to_tests/
    
For a list of supported options:
    python gadzooks/ -h
    
## Examples
To run the example tests:
    python gadzooks/ --discovery_dir gadzooks/examples/tests