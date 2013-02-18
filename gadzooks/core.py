"""
Core Gadzooks module for running tests.

"""
import argparse
import inspect
import json
import os.path
from StringIO import StringIO
import sys
from unittest.loader import TestLoader
from unittest.runner import TextTestRunner

import results

class TestRunner(object):
    """
    Wraps around Python's unittest classes TestLoader and TextTestRunner.
    Allows discovery-based test running and routes the test results to HTML output.
    
    """
    def __init__(self, discovery_dir='.', discovery_pattern='test*.py', output_file='test_results.html', silent=False, verbosity=2):
        
        test_groups = {}
        loader = TestLoader()
        
        groups_data = {}
        summary_data = {
            'discovery_dir' : discovery_dir,
            'discovery_pattern' : discovery_pattern,
            'num_groups' : 0,
            'num_groups_fail' : 0,
            'num_groups_pass' : 0,
            'num_tests' : 0,
            'num_tests_fail' : 0,
            'num_tests_pass' : 0,
            'num_tests_skip' : 0,
            'raw_log' : ''
        }
        
        # Discovery tests from specified directory
        tests = loader.discover(discovery_dir, discovery_pattern)
        
        # Group tests by file
        for group in tests:
            group_name = None
            for suite in group:
                # Determine group name
                if hasattr(suite, '_testMethodName'):
                    test_groups[suite._testMethodName] = group
                else:
                    for test in suite:
                        test_groups[inspect.getmodule(test).__name__] = group
                        break
        
        # Run tests for each group
        for group_name, tests in test_groups.items():
            
            raw_log = StringIO()
            runner = TextTestRunner(stream=TestRunner.StreamRouter(raw_log, silent), verbosity=verbosity)
            result = runner.run(tests)
            
            # Index errors by test class
            errors = {}
            for error in result.errors:
                errors['{0}.{1}'.format(error[0].__class__.__name__, error[0]._testMethodName)] = error[1]

            # Marshall/record data
            group_data = {
                'tests' : []
            }
            group_data['tests_errored'] = len(result.errors)
            group_data['tests_passed'] = result.testsRun - group_data['tests_errored']
            group_data['tests_skipped'] = len(result.skipped)
            group_data['tests_run'] = result.testsRun
            
            summary_data['num_groups'] += 1
            summary_data['num_tests'] += group_data['tests_run'] + group_data['tests_skipped']
            summary_data['num_tests_fail'] +=  group_data['tests_errored']
            summary_data['num_tests_pass'] += group_data['tests_passed']
            summary_data['num_tests_skip'] += group_data['tests_skipped']
            summary_data['raw_log'] += raw_log.getvalue()
            if group_data['tests_errored'] > 0:
                summary_data['num_groups_fail'] += 1
            else:
                summary_data['num_groups_pass'] += 1

            # Detailed  test data
            for suite in tests:
                cls_name = suite.__class__.__name__
                if cls_name == 'ModuleImportFailure' or cls_name == 'LoadTestsFailure':
                    # Record loader failure
                    group_data['tests'].append({
                        'name' : suite._testMethodName,
                        'status' : 'fail',
                        'description' : errors['{0}.{1}'.format(suite.__class__.__name__, suite._testMethodName)]
                    })
                else:
                    for t in suite:
                        signature = '{0}.{1}'.format(t.__class__.__name__, t._testMethodName)
                        test_data = {'name' : '{0}.{1}'.format(group_name, signature)}
                        if signature in  errors:
                            test_data['status'] = 'fail'
                            test_data['description'] = errors[signature]
                        else:
                            test_data['description'] = '';
                            test_data['status'] = 'pass'
                        group_data['tests'].append(test_data)
                
            groups_data[group_name] = group_data
        
        # Write results
        if summary_data['num_tests'] > 0:
            results.PageBuilder(groups_data, summary_data).generate_html(output_file)
            print 'Results available at {0}'.format(os.path.realpath(output_file))
        else:
            print 'No tests run; no results to publish.'
        
    class StreamRouter():
        """
        Custom routing of stream data to various destinations, based on configuration.
        
        """
        def __init__(self, log, silent):
            self.log = log
            self.silent = silent
        
        def flush(self):
            # stderr
            if not self.silent:
                sys.stderr.flush()
            # log
            self.log.flush()
        
        def write(self, str):
            # stderr
            if not self.silent:
                sys.stderr.write(str)
            # log
            self.log.write(str)
        
        def writelines(self, str_seq):
            # stderr
            if not self.silent:
                sys.stderr.writelines(str_seq)
            # log
            self.log.writelines(str_seq)
            
def main():
    import argparse    
    parser = argparse.ArgumentParser(description='...')
    parser.add_argument("--discovery_dir", default='.', help="Start directory for test discovery")
    parser.add_argument("--discovery_pattern", default='test*.py', help="File pattern for test discovery")
    parser.add_argument("-o", "--output_file", default='test_results.html', help="Output file for HTML test results")
    parser.add_argument("-s", "--silent", action='store_true', help="Hide test output from console")
    parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity")
    TestRunner(**vars(parser.parse_args()))