import pkg_resources

GENERATOR_ENTRY_POINT = 'thrifty.generators'


def find_plugin_generators():
    for entrypoint in pkg_resources.iter_entry_points(GENERATOR_ENTRY_POINT):
        yield entrypoint.load()
