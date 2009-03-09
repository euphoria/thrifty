from optparse import OptionParser
import thrifty.generators

class ThriftyOptionParser(OptionParser):
    """Extends the built-in OptionParser to support Thrifty generators"""

    def format_help(self, formatter=False):
        options_help = OptionParser.format_help(self)
        generators = thrifty.generators.find_plugin_generators()
        help = options_help + '\n  Available generators:\n'
        for gen in generators:
            help += '\n    %s (%s)' % (gen.aliases[0], gen.name)
        return help

def execute():
    parser = ThriftyOptionParser()
    parser.add_option('-v', action='store_true', dest='verbose',
        help='Verbose mode')
    parser.add_option('-I', '--include',
        action='append', dest='includes', metavar='DIR',
        help='Add a directory to the list of directories searched for include directives')
    parser.add_option('-g', '--gen',
        action='append', dest='generators', metavar='GENERATOR',
        help='Generate code with a dynamically-registered generator')

    (options, args) = parser.parse_args()

    generators = thrifty.generators.find_plugin_generators()

    if options.generators:
        for gen in options.generators:
            generator = thrifty.generators.get_generator_by_name(gen)
            print 'Using %s generator' % generator.name
