import sys

from pydebdep.pydebdep import PyDebDep


if __name__ == '__main__':
    # TODO: Defintly improve this.
    pdd = PyDebDep()
    print(pdd.get_missing_dependencies_of(sys.argv[1]))

