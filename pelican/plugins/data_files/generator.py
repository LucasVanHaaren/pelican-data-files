import sys
import os
import logging
import pathlib

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
            sys.exit(1)

        if not data_dir.is_dir():
            log.error("pelican-data-files: DATA_FILES_DIR path isn't a directory.")
            sys.exit(1)

        # Initialize parser object
        obj = DataParser()

        # Sort files by modified time
        files = sorted(data_dir.iterdir(), key=os.path.getmtime, reverse=True)

        # Create data array
        buffer = []

        for file in files:
            # Skip duplicate files
            if file.stem in buffer:
                continue

            # Load data from file
            data = obj.load(file)

            # Check whether file (type) is supported
            if data is None:
                # Report back
                log.info(f"{file.name} wasn't loaded.")

                # Move on to next file
                continue

            # Determine context variable
            name = file.stem.replace(".", "_").upper()

            # Add data to context
            self.context[f"DATA_{name}"] = data

            # Remember filename
            buffer.append(file.stem)

            # Report back
            log.info(f"{file.name} was loaded.")
