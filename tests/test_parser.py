import io
import pathlib

from pelican.plugins.data_files.parser import DataParser


def test_load_invalid(tmp_path: pathlib.PosixPath) -> None:
    """
    Test invalid (= unsupported) file
    """

    # Create temporary file
    file = tmp_path / "data.txt"
    file.write_text("test")

    # Initialize parser
    parser = DataParser()

    # Assert result
    assert parser.load(file) == None


def test_load_json(tmp_path: pathlib.PosixPath) -> None:
    """
    Test JSON file
    """

    # Create temporary file
    file = tmp_path / "data.json"
    file.write_text(
        """
        {
            "key1": "value1",
            "key2": ["value2"]
        }
        """
    )

    # Initialize parser
    parser = DataParser()

    # Assert result
    assert parser.load(file) == {"key1": "value1", "key2": ["value2"]}
    assert parser.load_json(file) == {"key1": "value1", "key2": ["value2"]}


def test_load_toml(tmp_path: pathlib.PosixPath) -> None:
    """
    Test TOML file
    """

    # Create temporary file
    file = tmp_path / "data.toml"
    file.write_text(
        """
        key1 = 'value1'
        key2 = [ 'value2' ]
        """
    )

    # Initialize parser
    parser = DataParser()

    # Assert result
    assert parser.load(file) == {"key1": "value1", "key2": ["value2"]}
    assert parser.load_toml(file) == {"key1": "value1", "key2": ["value2"]}


def test_load_yaml(tmp_path: pathlib.PosixPath) -> None:
    """
    Test YAML files
    """

    # Initialize parser
    parser = DataParser()

    # Create temporary files
    for file in [
        tmp_path / "data.yml",
        tmp_path / "data.yaml",
    ]:
        file.write_text(
            """
            key1: value1
            key2:
              - value2
            """
        )

        # Assert result
        assert parser.load(file) == {"key1": "value1", "key2": ["value2"]}
        assert parser.load_yaml(file) == {"key1": "value1", "key2": ["value2"]}
