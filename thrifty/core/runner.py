from optparse import OptionParser
from thrifty.gen import generator


def execute():
    parser = OptionParser()
    parser.add_option('--gen', action='append', dest='generators',
        help='Generate code with a dynamically-registered generator')
    parser.add_option('-v', action='store_true', dest='verbose',
        help='Verbose mode')

    (options, args) = parser.parse_args()

    for gen in options.generators:
        print gen
