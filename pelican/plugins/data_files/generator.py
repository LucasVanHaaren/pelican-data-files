import logging
import pathlib
from sys import exit

from pelican.generators import Generator

from .parser import DataParser

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class DataGenerator(Generator):
    """
    Load data from files
    """

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

    def generate_context(self) -> None:
        """
        Generate context from data files

        :return: None
        """

        data_dir = pathlib.Path(self.settings["DATA_FILES_DIR"])

        # Turn path into absolute if not already
        if not data_dir.is_absolute():
            data_dir = pathlib.Path(self.settings["PATH"]).joinpath(data_dir)

        # Check if path exists
        if not data_dir.exists():
            log.error("pelican-data-files: DATA_FILES_DIR path doesn't exists.")
            exit(1)

        if not data_dir.is_dir():
            log.error("pelican-data-files: DATA_FILES_DIR path isn't a directory.")
            exit(1)

        # Initialize parser object
        obj = DataParser()

        # TODO check for duplicates (eg: profile.json and profile.yaml)
        for file in data_dir.iterdir():
            # Determine name of context variable
            name = file.stem.replace(".", "_").upper()

            # Load data from file
            data = obj.load(file)

            # If file is supported ..
            if data is not None:
                # .. add its data to context
                self.context[f"DATA_{name}"] = data
                log.info(f"{file.name} was loaded.")
