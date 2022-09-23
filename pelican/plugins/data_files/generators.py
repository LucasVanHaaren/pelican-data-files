import logging
import pathlib
import json
from sys import exit
from pelican.generators import Generator
from .file_formats import SUPPORTED_FORMATS


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class DataGenerator(Generator):
    """
    Load data from files
    """

    CONTEXT_PREFIX = "DATA_"

    def __init__(
        self,
        context,
        settings,
        path,
        theme,
        output_path,
        readers_cache_name="",
        **kwargs,
    ):
        super().__init__(
            context,
            settings,
            path,
            theme,
            output_path,
            readers_cache_name=readers_cache_name,
            **kwargs,
        )
        log.info("PLUGIN: pelican-data-files was successfully loaded")
        self.settings.setdefault("DATA_FILES_DIR", "data")

    def _format_filename(self, file):
        """Format context var name from filename.

        params:

        - file -- pathlib.Path object
        """
        return file.stem.replace(".", "_").upper()

    def _read_file(self, file):
        """Read and parse data from file.

        params:

        - file -- pathlib.Path object
        """
        with file.open() as f:
            try:
                return json.load(f)
            except ValueError:
                return None

    def _add_data_to_context(self, name, data):
        """Add data into context.

        params:

        - name -- str
        - data -- dict
        """
        ctx_name = self.CONTEXT_PREFIX + name
        self.context[ctx_name] = data

    def generate_context(self):
        """Generate context from data files"""

        data_dir = pathlib.Path(self.settings["DATA_FILES_DIR"])

        # turn path into absolute if not already
        if not data_dir.is_absolute():
            data_dir = pathlib.Path(self.settings["PATH"]).joinpath(data_dir)

        # check if path exists
        if not data_dir.exists():
            log.error("pelican-data-files: DATA_FILES_DIR path doesn't exists.")
            exit(1)

        if not data_dir.is_dir():
            log.error("pelican-data-files: DATA_FILES_DIR path isn't a directory.")
            exit(1)

        # return all valid files in path
        # TODO check for duplicates (eg: profile.json and profile.yaml)
        for file in data_dir.iterdir():
            for file_format in SUPPORTED_FORMATS:
                # Skip invalid formats
                if file.suffix.lower() not in file_format["extensions"]:
                    continue

                name = self._format_filename(file)

                with file.open('rb') as f:  # TOML requires binary mode
                    data = file_format["parser"](f)

                self._add_data_to_context(name, data)
                log.info(f"{file.name} was loaded.")

def get_generators(pelican_object):
    return DataGenerator
