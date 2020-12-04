from pydebdep.packager import Packager
from pydebdep.libs import get_dependencies_of

class PyDebDep:
    def __init__(self):
        pass

    def get_missing_dependencies_of(self, package_name: str):
        packager = Packager()
        list_debian_packages = packager.get_list_package_on_debian()
        list_packages_dep = get_dependencies_of(package_name)
        return self._get_missings(list_debian_packages, list_packages_dep)

    @staticmethod
    def _get_missings(debian_packages, dependencies):
        missing_list = list()
        for dep in dependencies:
            if f'python3-{dep["name"]}' not in debian_packages:
                missing_list.append(dep)

        return missing_list

