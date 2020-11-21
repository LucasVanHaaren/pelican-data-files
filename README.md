<!-- markdownlint-disable MD041 -->
![pelican-data-files_banner](https://user-images.githubusercontent.com/29121316/99832308-a29d3a80-2b60-11eb-9e44-1ba3438bbe6b.png)

![pypi_badge](https://img.shields.io/pypi/v/pelican-data-files?logo=pypi&logoColor=yellow&style=for-the-badge)
![licence_badge](https://img.shields.io/pypi/l/pelican-data-files?style=for-the-badge)

---

> Pelican plugin that allows to load data from files like JSON or YAML.

This plugin loads all the data files in the `data /` directory, and makes them accessible via the context with the prefix `DATA_` followed by the name of the file. This is roughly the default behavior of the well known [Jekyll](https://jekyllrb.com/) static site generator.

For example, the data of a `profile.json` file will be accessible from any template via `DATA_PROFILE`.

## Usage

You can use it directly on a personnal project, or to build a theme.

### For a personnal project

All you have to do is install package with pip:

```bash
pip install pelican-data-files
```

### To build a theme

First set the plugin as an install requirement, for exemple with a package managed with setuptools (`setup.py`):

```python
...
install_requires=[
  "pelican",
  "pelican-data-files"
],
...
```

Next, inform your users to run the following command in order to fetch sample data files of your theme:

```bash
pelican-data-files --fetch <THEME_NAME>
```

This will copy the `data/` folder of the theme, into the `data/` folder of their Pelican project.
