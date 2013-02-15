import base64
import os.path

class PageBuilder(object):
    """
    Use string templates to insert content into results HTML page.
    
    """
    
    def __init__(self, groups, summary):
        self.groups = groups
        self.summary = summary
        self.module_path = os.path.dirname(__file__)
        self.head_content = self.get_tpl('includes').format(
            bootstrap_css=self.get_res('css/bootstrap.min.css'),
            bootstrap_css_resp=self.get_res('css/bootstrap-responsive.min.css'),
            style_css=self.get_res('css/style.css'),
            bootstrap_js=self.get_res('js/bootstrap.min.js'),
            gadzooks_js=self.get_res('js/gadzooks.js'),
            jquery_js=self.get_res('js/jquery.min.js')
        )
    
    def generate_html(self, path):
        """
        Generate main results HTML file.
        
        """
        content = self.get_tpl('index').format(
            head_content=self.head_content,
            log=self.summary['raw_log'].replace('\n', '<br/>'),
            summary=self.generate_summary(),
            test_group_links=self.generate_test_group_links(),
            tests=self.generate_tests()
        )
        with open(path, 'w') as out_file:
            out_file.write(content)
            
    def generate_summary(self):
        """
        Generate HTML for main summary.
        
        """
        return self.get_tpl('summary').format(
            discovery_dir=self.summary['discovery_dir'],
            discovery_pattern=self.summary['discovery_pattern'],
            num_groups=self.summary['num_groups'],
            num_groups_fail=self.summary['num_groups_fail'],
            num_groups_fail_pct=self.summary['num_groups_fail'] * 100.0 / self.summary['num_groups'],
            num_groups_pass=self.summary['num_groups_pass'],
            num_groups_pass_pct=self.summary['num_groups_pass'] * 100.0 / self.summary['num_groups'],
            num_tests=self.summary['num_tests'],
            num_tests_fail=self.summary['num_tests_fail'],
            num_tests_fail_pct=self.summary['num_tests_fail'] * 100.0 / self.summary['num_tests'],
            num_tests_pass=self.summary['num_tests_pass'],
            num_tests_pass_pct=self.summary['num_tests_pass'] * 100.0 / self.summary['num_tests'],
            num_tests_skip=self.summary['num_tests_skip'],
            num_tests_skip_pct=self.summary['num_tests_skip'] * 100.0 / self.summary['num_tests'],
        )
            
    def generate_test_group_links(self):
        """
        Generate HTML for test group links.
        
        """
        content = ''
        template = self.get_tpl('test_group_link')
        for name, data in self.groups.items():
            content += template.format(
                name=name,
                name_fmt=name.replace('.', '-'),
                status='fail-icon' if int(data['tests_errored']) > 0 else 'pass-icon'
            )
        return content
        
    def generate_tests(self):
        """
        Generate HTML for all tests.
        
        """
        content = ''
        fail_template = self.get_tpl('fail_test')
        pass_template = self.get_tpl('pass_test')
        for group, data in self.groups.items():
            for t in data['tests']:
                template = fail_template if t['status'] == 'fail' else pass_template
                content += template.format(
                    description=t['description'].replace('\n', '<br/>'),
                    group=group.replace('.','-'),
                    name='{0}'.format(t['name']),
                    status=t['status'],
                    status_icon='{0}-icon'.format(t['status'])
                )
        
        return content
                                  
    def get_res(self, rel_path):
        """
        Get arbitrary resource content.
        
        """
        with open(os.path.join(self.module_path, 'resources', rel_path)) as res:
            return res.read()
        
    def get_tpl(self, rel_path):
        """
        Get template content.
        
        """
        with open(os.path.join(self.module_path, 'templates', rel_path + '.html')) as tpl:
            return tpl.read()
    
