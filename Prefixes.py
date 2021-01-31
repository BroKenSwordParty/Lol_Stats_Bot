from enum import Enum
import json

with open("keys.json") as tempfile:
    prefix = json.load(tempfile)['prefix']


class Prefixes(Enum):
        INFO = prefix + "info "
    # prefix.info = inf