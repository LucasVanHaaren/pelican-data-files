<!-- markdownlint-disable MD033 -->
<h1 align="center">
  <br>
    <img src="https://user-images.githubusercontent.com/29121316/99832308-a29d3a80-2b60-11eb-9e44-1ba3438bbe6b.png" alt="pelican-data-files-logo" width="700"></a>
  <br>
</h1>

<!-- markdownlint-disable MD041 -->
![pypi_badge](https://img.shields.io/pypi/v/pelican-data-files?logo=pypi&logoColor=yellow&style=for-the-badge)

> Pelican plugin that allows to load data from files like JSON or YAML.

This plugin loads all the data files in the `data /` directory, and makes them accessible via the context with the prefix `DATA_` followed by the name of the file. This is roughly the default behavior of the well known [Jekyll](https://jekyllrb.com/) static site generator.

For example, the data of a `profile.json` file will be accessible from any template via `DATA_PROFILE`.

You can use it directly on your personnal project, or to build a theme.
