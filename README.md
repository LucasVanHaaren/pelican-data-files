# pelican-data-files

> Pelican plugin that allows to load data from files like JSON or YAML.

This plugin loads all the data files in the `data /` directory, and makes them accessible via the context with the prefix `DATA_` followed by the name of the file. This is roughly the default behavior of the well known [Jekyll](https://jekyllrb.com/) static site generator.

For example, the data of a `profile.json` file will be accessible from any template via `DATA_PROFILE`.

You can use it directly on your personnal project, or to build a theme.
