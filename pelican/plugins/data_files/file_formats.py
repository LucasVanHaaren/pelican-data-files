import json

try:
    # Python 3.11 ships with a native TOML implementation.
    import tomllib
except ModuleNotFoundError:
    # tomli is a 3rd party module with a compatible API to the Python 3.11 implementation.
    import tomli as tomllib

JSON = {"name": "json", "extensions": [".json"], "parser": json.load}
TOML = {"name": "toml", "extensions": [".toml"], "parser": tomllib.load}
#YAML = {"name": "yaml", "extensions": [".yaml", ".yml"]}
#XML = {"name": "xml", "extensions": [".xml"]}
