import json

# Detect support for other file formats
# (1) TOML
try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        pass

# (2) YAML
try:
    import yaml
except ImportError:
    pass


# Define supported file formats
SUPPORTED_FORMATS = [{"extensions": [".json"], 'parser': json.load}]

try:
    SUPPORTED_FORMATS.append({"extensions": [".toml"], "parser": tomllib.load})

except NameError:
    pass

try:
    SUPPORTED_FORMATS.append({"extensions": [".yml", ".yaml"], "parser": yaml.safe_load})
except NameError:
    pass
