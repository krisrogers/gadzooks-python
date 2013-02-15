"""
Run Gadzooks from source.

"""
import argparse

import core

parser = argparse.ArgumentParser(description='...')
parser.add_argument("--discovery_dir", default='.', help="Start directory for test discovery")
parser.add_argument("--discovery_pattern", default='test*.py', help="File pattern for test discovery")
parser.add_argument("-o", "--output_file", default='test_results.html', help="Output file for HTML test results")
parser.add_argument("-s", "--silent", action='store_true', help="Hide test output from console")
parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity")
core.TestRunner(**vars(parser.parse_args()))