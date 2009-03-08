from optparse import OptionParser
from thrifty.gen import generator


def execute():
    parser = OptionParser()
    parser.add_option('-g', '--gen',
        action='append', dest='generators', metavar='GENERATOR',
        help='Generate code with a dynamically-registered generator')
    parser.add_option('-v', action='store_true', dest='verbose',
        help='Verbose mode')
    parser.add_option('-I', '--include',
        action='append', dest='includes', metavar='DIR',
        help='Add a directory to the list of directories searched for include directives')

    (options, args) = parser.parse_args()

    if options.generators:
        for gen in options.generators:
            print gen
