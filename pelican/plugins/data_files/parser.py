import json
import pathlib
from typing import Any, Dict, List, Optional

try:
    import tomllib
except ModuleNotFoundError:
    try:
        import tomli as tomllib
    except ModuleNotFoundError:
        pass

try:
    import yaml
except ModuleNotFoundError:
    pass


class DataParser:
    """
    Handles data files
    """

    handlers: Dict[str, List[str]]

    def __init__(self) -> None:
        """
        Constructor

        :return: None
        """

        # Support JSON by default
        handlers = {"json": [".json"]}

        # Detect support for other file formats
        # (1) TOML
        if "tomllib" in globals():
            handlers["toml"] = [".toml"]

        # (2) YAML
        if "yaml" in globals():
            handlers["yaml"] = [".yml", ".yaml"]

        self.handlers = handlers

    def load(self, file: pathlib.Path) -> Optional[Dict[str, Any]]:
        """
        Loads data from FILE

        :param file: pathlib.Path Filepath
        :return: Dict[str, Any] | None
        """

        # Determine file extension
        extension = file.suffix.lower()

        for handler, extensions in self.handlers.items():
            if extension in extensions:
                try:
                    return getattr(self, f"load_{handler}")(file)
                except Exception:
                    pass

    def load_json(self, json_file: pathlib.Path) -> Dict[str, Any]:
        """
        Loads data from JSON file

        :param json_file: pathlib.Path Filepath
        :return: Dict[str, Any] Data
        """

        with json_file.open("r") as file:
            return json.load(file)

    def load_yaml(self, yaml_file: pathlib.Path) -> Dict[str, Any]:
        """
        Loads data from YAML file

        :param yaml_file: pathlib.Path Filepath
        :return: Dict[str, Any] Data
        """

        with yaml_file.open("r") as file:
            return yaml.safe_load(file)

    def load_toml(self, toml_file: pathlib.Path) -> Dict[str, Any]:
        """
        Loads data from TOML file

        :param toml_file: pathlib.Path Filepath
        :return: Dict[str, Any] Data
        """

        with toml_file.open("rb") as file:
            return tomllib.load(file)
