import pkg_resources

GENERATOR_ENTRY_POINT = 'thrifty.generators'


def find_plugin_generators():
    """
    Find all generator plugins using setuptools entrypoints.
    """
    for entrypoint in pkg_resources.iter_entry_points(GENERATOR_ENTRY_POINT):
        yield entrypoint.load()


def get_generator_by_name(_alias):
    """
    Get a generator by an alias.
    """
    for cls in find_plugin_generators():
        if _alias in cls.aliases:
            return cls()
    raise ClassNotFound('no generator for alias %r found' % _alias)
