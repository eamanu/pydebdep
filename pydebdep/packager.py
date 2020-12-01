import apt

class Packager:
    def __init__(self):
        pass

    def get_list_package_on_debian(self):
        cache = self._get_cache_updated()
        # ACcording to documetation we need to open cache
        cache.open(None)
        packages = [p['name'] for p in cache]
        return packages

    @staticmethod
    def _get_cache_updated():
        cache = apt.Cache()
        cache.update()
        return cache


