<!-- markdownlint-disable MD041 -->
![pelican-data-files_banner](https://user-images.githubusercontent.com/29121316/99832308-a29d3a80-2b60-11eb-9e44-1ba3438bbe6b.png)

![pypi_badge](https://img.shields.io/pypi/v/pelican-data-files?logo=pypi&logoColor=yellow&style=for-the-badge)
![licence_badge](https://img.shields.io/pypi/l/pelican-data-files?style=for-the-badge)
![open_issues_badge](https://img.shields.io/github/issues-raw/lucasvanhaaren/pelican-data-files?color=orange&logo=github&style=for-the-badge)
![closed_issues_badge](https://img.shields.io/github/issues-closed-raw/lucasvanhaaren/pelican-data-files?color=green&logo=github&style=for-the-badge)

---

> Pelican plugin that allows to load data from files like JSON or YAML.

This plugin loads all the data files found in the project's `data/` directory, and makes them accessible in jinja templates by injecting them into the context (with the prefix `DATA_` followed by the name of the file).

This is roughly the default behavior of the well known [Jekyll](https://jekyllrb.com/) static site generator.

For example, the data of a `profile.json` file will be accessible from any template via `DATA_PROFILE`.

## Getting started

You can use it directly in a personnal project, or to build a [Pelican theme](https://docs.getpelican.com/en/stable/themes.html).

This plugin is avaiable as a [python package](https://pypi.org/project/pelican-data-files/) hosted on PyPI.

### Setup

All you have to do is install the latest version of the package with pip:

```bash
pip install pelican-data-files
```

By default, Pelican will automatically discover and register the plugin. (see more [here](https://docs.getpelican.com/en/stable/plugins.html#how-to-use-plugins))

To be sure, run this command which displays all the registered plugins, pelican-data-files should be printed:

```bash
pelican-plugins
```

### Usage

Place some JSON valid files into `data/` folder. Then you can acces your data by querying `DATA_<FILE_NAME>["<VAR_NAME>"]`

For example, consider a simple file named `profile.json` with the followed content:

```json
{
  "firstname": "John",
  "lastname": "Doe",
  "age": 25,
  "contact": {
    "phone": "+1 302-516-3307",
    "mail": "john@doe.com"
  }
}
```

Then, see what following queries return:

```python
DATA_PROFILE["firstname"] => "John"
DATA_PROFILE["age"] => 25
DATA_PROFILE["contact"]["mail"] => "john@doe.com"
```

So, you can access all the data in `data/` folder in jinja templates from pelican context.

### Build a theme

It is of course possible to create a theme that uses this plugin, it will not necessarily be dependent on it but must in all cases be designed for. (Usage of `DATA_` prefix in theme templates and provide sample data files)

First set the plugin as an install requirement, for example with a package managed with setuptools (`setup.py`):

```python
...
install_requires=[
  "pelican",
  "pelican-data-files"
],
...
```

Next, you have to provide sample data files for your theme.

Users can easily fetch the files in their pelican project by running the following command:

```bash
pelican-data-files --fetch <THEME_NAME>
```

This will copy the `data/` folder of the theme, into the `data/` folder of their Pelican project.

They will only have to modify the files and generate their site.

## Example

[orbelican](https://github.com/LucasVanHaaren/orbelican) is a theme which use pelican-data-files plugin to build an online resume from orbit-theme.
