# template-python-project

[![CI](https://github.com/guilgautier/template-python-project/actions/workflows/main.yml/badge.svg)](https://github.com/guilgautier/template-python-project/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/guilgautier/template-python-project/branch/main/graph/badge.svg?token=9O6RRKUA3S)](https://codecov.io/gh/guilgautier/template-python-project)

- [template-python-project](#template-python-project)
  - [Development environment](#development-environment)
    - [IDE: Visual Studio Code](#ide-visual-studio-code)
    - [Install Poetry](#install-poetry)
    - [Virtual environnement](#virtual-environnement)
  - [Dependency management](#dependency-management)
  - [Installation](#installation)
    - [Install as a dependency](#install-as-a-dependency)
    - [Install from source and potentially contribute to the project](#install-from-source-and-potentially-contribute-to-the-project)
    - [Install extras dependencies](#install-extras-dependencies)
  - [Testing](#testing)
  - [Documentation](#documentation)
    - [Install documentation dependencies](#install-documentation-dependencies)
    - [Generate the documentation](#generate-the-documentation)
    - [Publish the documentation](#publish-the-documentation)
  - [Packaging and publishing](#packaging-and-publishing)
  - [Continuous integration](#continuous-integration)
  - [Miscellaneous](#miscellaneous)

This repository may serve as a template for scientific projects written in [Python](https://www.python.org/).

## Development environment

### IDE: Visual Studio Code

[Visual Studio Code (VSCode)](https://code.visualstudio.com/) is recommended to simplify your coding experience.

The [.vscode](https://github.com/guilgautier/template-python-project/blob/main/.vscode) directory contains a list of suggested extensions together with the corresponding settings.
You can place it at the root of your project workspace.

See also the [vscode-workflow](https://github.com/guilgautier/vscode-workflow) repository.

### Install Poetry

[Poetry](https://python-poetry.org/) is recommended for its simplicity to help you manage your project to meet the Python packaging standards.

See the [Poetry's installation instructions](https://python-poetry.org/docs/#installation).

### Virtual environnement

It is always good practice to work in virtual environment, isolated from your other Python project.
With [Poetry](https://python-poetry.org/) creating/activating a virtual environment is fairly simple

```bash
poetry shell
```

The way virtual environments are created is defined in the [poetry.toml](poetry.toml) file, see also [Poetry's documentation](https://python-poetry.org/docs/configuration#virtualenvscreate).
**Note:** In this template project, a virtual environment will be created at the root of the project in `.venv` folder.

To make sure your classical commands are executed in the virtual environment, e.g., `pytest`, prepend `poetry run ...` , see also the [Testing](#testing) section.

[I don’t want Poetry to manage my virtual environments. Can I disable it?](https://python-poetry.org/docs/faq/#i-dont-want-poetry-to-manage-my-virtual-environments-can-i-disable-it)

## Dependency management

[Poetry](https://python-poetry.org/) is recommended for its dependency management capabilities.
On top of installing a given package (like `pip` can do), Poetry also resolves dependencies' version to preserve compatibility.

Dependencies specified in the [`pyproject.toml`](./pyproject.toml) (according to [PEP 518](https://www.python.org/dev/peps/pep-0518/#file-format)) can be declared in the following way.

- Install main (non-optional) dependencies

  See `[tool.poetry.dependencies]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry add numpy
  poetry remove numpy
  ```

- Install optional dependencies

  See `[tool.poetry.dependencies]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry add jupyter --optional
  poetry remove jupyter
  ```

  Optional dependencies can then be combined to define package [extra dependencies](#install-extras-dependencies).

- Install development dependencies

  See `[tool.poetry.dev-dependencies]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry add black --dev
  poetry remove black --dev
  ```

## Installation

### Install as a dependency

- If your project is already available on [PyPI](https://pypi.org/),

  ```bash
  poetry add packagename
  # pip install packagename
  ```

- Otherwise, install the latest version from source (which might be broken)

  ```bash
  poetry add git+<https://github.com/USERNAME/REPOSITORY_NAME.git>
  # pip install git+<https://github.com/USERNAME/REPOSITORY_NAME.git>
  ```

### Install from source and potentially contribute to the project

- with [Poetry](https://python-poetry.org/)

  The package can be installed in **editable** mode along with

  - main (non-optional) dependencies, see tool.poetry.dependencies in [`pyproject.toml`](./pyproject.toml)
  - dev dependencies, `[tool.poetry.dev-dependencies]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  git clone https://github.com/USERNAME/REPOSITORY_NAME.git
  cd packagename

  poetry shell  # create/activate local .venv (see poetry.toml)
  poetry install  # install package in editable mode with main (non-optional) dependencies and dev dependencies (see pyproject.toml)
  # poetry install --extras "name1 name2"  # install extra dependencies (see [tool.poetry.extras] in  pyproject.toml)
  ```

- with pip

  Note that, from the current `pyproject.toml` file, it is **not** possible to install the project in editable mode ~~`pip install -e .`~~.
  Please consider installing with Poetry instead.

  ```bash
  git clone https://github.com/USERNAME/REPOSITORY_NAME.git
  cd packagename
  # activate your virtual environment
  pip install .  # install package with main (non-optional) dependencies (see pyproject.toml)
  # dev dependencies are not installed
  # pip install ".[docs, notebook]"  # install extra documentation and jupyter notebook dependencies (see pyproject.toml)
  ```

### Install extras dependencies

```bash
poetry install --extras "name1 name2"
```

See also

- `[tool.poetry.extras]` in [`pyproject.toml`](./pyproject.toml),
- [Poetry's documentation](https://python-poetry.org/docs/pyproject/#extras).

## Testing

The [`pytest`](https://docs.pytest.org/en/6.2.x/) framework is recommended to make it easy to write small tests, yet scales to support complex functional testing.

**Note:** `pytest` and `pytest-cov` are listed as development dependencies, and installed as such when `poetry install` was run.

The unit tests of the package are declared in `tests/test_*.py` files as `test_*` functions with a simple `assert` statement.

The configuration of `pytest` is defined in the [`[tool.pytest.ini_options]` section of the `pyproject.toml` file](https://docs.pytest.org/en/latest/reference/customize.html#pyproject-toml).

Run the package test suite with

```bash
poetry run pytest  # -vv --cov=packagename --cov-report=xml
```

## Documentation

[Sphinx](https://www.sphinx-doc.org/en/master/index.html) is recommended to generate the project's documentation.

Sphinx is in charge of building the documentation and generating HTML output, but also PDF, epub, ...

- The documentation configuration file is located at `docs/conf.py`.
- The source files of the documentation are simply  `.rst` (reStructuredText) or `.md` (Markdown) files. However we suggest using reST markup to keep the same syntax and format as used for writing [Python docstings](https://devguide.python.org/documenting/).

### Install documentation dependencies

Install `docs` extras dependencies, see `[tool.poetry.extras]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry install -E docs
  # poetry install --extras "docs"
  # pip install ".[docs]"
  ```

### Generate the documentation

To generate the documentation locally, i.e., on your machine, you can either use

- basic command

  ```bash
  poetry run sphinx-build -b html docs docs/_build/html
  ```

  and navigate the documentation

  ```bash
  open docs/_build/html/index.html
  ```

- live reload command

  If you have successfully [installed documentation dependencies](#install-documentation-dependencies) then [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) should be available.

  [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) generates the documentation and make a live view available in your browser.

  ```bash
  poetry run sphinx-autobuild docs docs/_build/html
  ```

  ```text
  ....
  build succeeded.

  The HTML pages are in docs/_build/html.
  [sphinx-autobuild] Serving on http://127.0.0.1:8000
  ```

  Changes made to `.rst` files will be reflected live in your favorite browser at <http://127.0.0.1:8000>

**Note:** In both cases, any change made in the source `.py` files or the `docs/conf.py` file require rebuilding the documentation.

### Publish the documentation

TODO

## Packaging and publishing

[Poetry](https://python-poetry.org/) is also of great help to simplify the packaging process

- build your package

  ```bash
  poetry build
  ```

- publish your package on a Package Index (PI)

  - [PyPI](https://pypi.org/) (default), see [Poetry documentation](https://python-poetry.org/docs/repositories/#configuring-credentials)

  ```bash
  poetry config pypi-token.pypi MY_TOKEN
  poetry publish
  ```

  - [TestPyPI](https://test.pypi.org/) it is good practice to first publish on TestPyPI and check the results before publishing on the official PyPI

  - [Poetry documentation](https://python-poetry.org/docs/repositories/#adding-a-repository)
  - <https://test.pypi.org/help/#apitoken>

  ```bash
  poetry config repositories.testpypi https://test.pypi.org/legacy/
  poetry config http-basic.testpypi __token__ MY_TOKEN
  poetry publish -r testpypi
  ```

## Continuous integration

GitHub Actions

github workflows declared as `.github/workflows/*.yml` files.

To be continued ...

## Miscellaneous

Consider reading

- [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [Python naming algorithm](https://melevir.medium.com/python-functions-naming-the-algorithm-74320a18278d)
