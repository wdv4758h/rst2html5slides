import micawber
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class Media(Directive):
    """
    Restructured text extension for inserting any sort of media using micawber

    see: http://ralsina.me/weblog/posts/the-best-restructuredtext-directive-ever-really.html
    """
    has_content = False
    required_arguments = 1

    def run(self):
        providers = micawber.bootstrap_basic()
        return [nodes.raw('', micawber.parse_text(self.arguments[0], providers), format='html')]

directives.register_directive('media', Media)
