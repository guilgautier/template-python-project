# template-python-project

- [template-python-project](#template-python-project)
  - [Development environment](#development-environment)
  - [Dependency management](#dependency-management)
  - [Installation](#installation)
  - [Documentation](#documentation)
  - [Miscellaneous](#miscellaneous)

This repository may serve as a template for scientific projects written in [Python](https://www.python.org/).

## Development environment

[Visual Studio Code (VSCode)](https://code.visualstudio.com/) is recommended to simplify your coding experience.

The [.vscode](https://github.com/guilgautier/template-python-project/blob/main/.vscode) directory contains a list of suggested extensions together with the corresponding settings.
You can place it at the root of your project workspace.

See also the [vscode-workflow](https://github.com/guilgautier/vscode-workflow) repository.

## Dependency management

[Poetry](https://python-poetry.org/) is recommended for its simplicity to help your project meet the Python packaging standards, including

- working in / activating the virtual environment (cf. [poetry.toml](poetry.toml))

  ```bash
    poetry shell
  ```

- managing your project dependencies (cf. [`pyproject.toml`](pyproject.toml) according to [cf. PEP 517-518](https://www.python.org/dev/peps/pep-0518/#file-format))

  - main (non-optional) dependencies, see `tool.poetry.dependencies` in [`pyproject.toml`](pyproject.toml)

  ```bash
      poetry add numpy
      poetry remove numpy
  ```

  - optional dependencies, see `tool.poetry.dependencies` in [`pyproject.toml`](pyproject.toml)

  ```bash
      poetry add jupyter --optional
      poetry remove jupyter
  ```

  - development dependencies, see `tool.poetry.dev-dependencies` in [`pyproject.toml`](pyproject.toml)

  ```bash
      poetry add black --dev
      poetry remove black --dev
  ```

- installing your project in editable mode along with

  - main (non-optional) dependencies, see tool.poetry.dependencies in [`pyproject.toml`](pyproject.toml)
  - dev dependencies, `tool.poetry.dev-dependencies` in [`pyproject.toml`](pyproject.toml)

  ```bash
    poetry install
  ```

- installing your project extras dependencies, see `tool.poetry.extras` in [`pyproject.toml`](pyproject.toml)

  ```bash
    poetry install --extras "name1 name2"
  ```

## Installation

Your package can be added as a dependency to an existing Python project:

- If your project is already available on [PyPI](https://pypi.org/),

  ```bash
    poetry add packagename  # using `poetry`, or
    pip install packagename  # using `pip`
  ```

- Otherwise

  ```bash
    poetry add git+https://github.com/USERNAME/packagename.git  # using `poetry`, or
    pip install git+https://github.com/USERNAME/packagename.git  # using `pip`
  ```

---

To install the package from source and potentially contribute to it

- with [Poetry](https://python-poetry.org/)

  ```bash
    git clone https://github.com/USERNAME/packagename.git
    cd packagename
    poetry shell  # create/activate local .venv (see poetry.toml)
    poetry install  # install package in editable mode with main (non-optional) dependencies and dev dependencies (see pyproject.toml)
    # poetry install --extras "docs notebook"  # install extra documentation and jupyter notebook dependencies (see pyproject.toml)
  ```

- with pip

  Note that it is not possible to install the project in editable mode `pip install -e .` (at least in a straightforward way) from the `pyproject.toml` file.
  Please consider installing with Poetry instead.

  ```bash
    git clone https://github.com/USERNAME/packagename.git
    cd packagename
    # activate your virtual environment
    pip install .  # install package with main (non-optional) dependencies (see pyproject.toml)
    # dev dependencies are not installed
    # pip install ".[docs, notebook]"  # install extra documentation and jupyter notebook dependencies (see pyproject.toml)
  ```

## Documentation

[Sphinx](https://www.sphinx-doc.org/en/master/index.html) is recommended to generate the project's documentation.

The source files of the documentation are simply  `.rst` (reStructuredText) or `.md` (Markdown) files.
However we suggest using reST markup to keep the same syntax and format as used for [Python docstings](https://devguide.python.org/documenting/).

Sphinx is in charge of building the documentation and generates HTML output in the `docs/_buil`
Note: Sphinx can also be set up to generate a PDF using LaTeX.

- Install `docs` extras dependencies, see `tool.poetry.extras` in [`pyproject.toml`](pyproject.toml)

  ```bash
    poetry install -E docs
  ```

## Miscellaneous

Consider reading

- [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [Python naming algorithm](https://melevir.medium.com/python-functions-naming-the-algorithm-74320a18278d)
