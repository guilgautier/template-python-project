# template-python-project

[![CI](https://github.com/guilgautier/template-python-project/actions/workflows/main.yml/badge.svg)](https://github.com/guilgautier/template-python-project/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/guilgautier/template-python-project/branch/main/graph/badge.svg?token=9O6RRKUA3S)](https://codecov.io/gh/guilgautier/template-python-project)

- [template-python-project](#template-python-project)
  - [Development environment](#development-environment)
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

  - main (non-optional) dependencies

  See `[tool.poetry.dependencies]` in [`pyproject.toml`](pyproject.toml)

  ```bash
  poetry add numpy
  poetry remove numpy
  ```

- optional dependencies

  See `[tool.poetry.dependencies]` in [`pyproject.toml`](pyproject.toml)

  ```bash
  poetry add jupyter --optional
  poetry remove jupyter
  ```

  Optional dependencies can then be combined to define package [extra dependencies](#install-extras-dependencies).

- development dependencies

  See `[tool.poetry.dev-dependencies]` in [`pyproject.toml`](pyproject.toml)

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

  - main (non-optional) dependencies, see tool.poetry.dependencies in [`pyproject.toml`](pyproject.toml)
  - dev dependencies, `[tool.poetry.dev-dependencies]` in [`pyproject.toml`](pyproject.toml)

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

See also `[tool.poetry.extras]` in [`pyproject.toml`](pyproject.toml) and [Poetry's documentation](https://python-poetry.org/docs/pyproject/#extras).

## Testing

The [`pytest`](https://docs.pytest.org/en/6.2.x/) framework is recommended to make it easy to write small tests, yet scales to support complex functional testing.

**Note:** `pytest` and `pytest-cov` are listed as development dependencies, and installed as such when `poetry install` was run

The unit tests of the package are declared in `tests/test_*.py` files as `test_*` functions with a simple `assert` statement.

The configuration of `pytest` is defined in the [`[tool.pytest.ini_options]` section of the `pyproject.toml` file](https://docs.pytest.org/en/latest/reference/customize.html#pyproject-toml).

To run the package test suite, simply execute

```bash
poetry run pytest  # -vv --cov=packagename --cov-report=xml
```

## Documentation

[Sphinx](https://www.sphinx-doc.org/en/master/index.html) is recommended to generate the project's documentation.

Sphinx is in charge of building the documentation and generating HTML output, but also PDF, epub, ...

- The documentation configuration file is located at `docs/conf.py`.
- The source files of the documentation are simply  `.rst` (reStructuredText) or `.md` (Markdown) files. However we suggest using reST markup to keep the same syntax and format as used for writting [Python docstings](https://devguide.python.org/documenting/).

### Install documentation dependencies

- Install `docs` extras dependencies, see `[tool.poetry.extras]` in [`pyproject.toml`](pyproject.toml)

  ```bash
  poetry install -E docs
  # poetry install --extras "docs"
  # pip install ".[docs]"
  ```

### Generate the documentation

You can either use

- basic command

  ```bash
  sphinx-build -b html docs docs/_build/
  ```

  and navigate the documentation

  ```bash
  open docs/_build/html/index.html
  ```

- live reload command

  If you have successfully [installed documentation dependencies](#install-documentation-dependencies) then [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) should be available.

  [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) generates the documentation and make a live view available in your browser.

  ```bash
  sphinx-autobuild docs docs/_build/html
  ```

  ```
  ....
  build succeeded.

  The HTML pages are in docs/_build/html.
  [sphinx-autobuild] Serving on http://127.0.0.1:8000
  ```

  Changes made to `.rst` files will be reflected live in your favorite browser at <http://127.0.0.1:8000>

**Note:** In both cases, any change made in the source `.py` files or the `docs/conf.py` file require rebuiling the documentation.

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

## Miscellaneous

Consider reading

- [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [Python naming algorithm](https://melevir.medium.com/python-functions-naming-the-algorithm-74320a18278d)
