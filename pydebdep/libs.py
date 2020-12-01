import json

from typing import List, Dict
from johnnydep.lib import JohnnyDist


def get_dependencies_of(package: str):
    jd = JohnnyDist(package)
    dep_raw = jd.serialise(fields=('name'), format='json')
    dep = json.loads(dep_raw)
    return dep


