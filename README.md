# template-python-project

[![CI](https://github.com/guilgautier/template-python-project/actions/workflows/main.yml/badge.svg)](https://github.com/guilgautier/template-python-project/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/guilgautier/template-python-project/branch/main/graph/badge.svg?token=9O6RRKUA3S)](https://codecov.io/gh/guilgautier/template-python-project)

- [template-python-project](#template-python-project)
  - [Development environment](#development-environment)
    - [WARNING for conda users](#warning-for-conda-users)
    - [IDE: Visual Studio Code](#ide-visual-studio-code)
    - [Install Poetry](#install-poetry)
    - [Manage Python versions](#manage-python-versions)
    - [Virtual environment](#virtual-environment)
      - [Note](#note)
  - [Dependency management](#dependency-management)
  - [Installation](#installation)
    - [Install as a dependency](#install-as-a-dependency)
    - [Install from source and potentially contribute to the project](#install-from-source-and-potentially-contribute-to-the-project)
    - [Install extras dependencies](#install-extras-dependencies)
  - [Testing](#testing)
    - [Run tests using VSCode](#run-tests-using-vscode)
  - [Debugging](#debugging)
  - [Documentation](#documentation)
    - [Install documentation dependencies](#install-documentation-dependencies)
    - [Configure the documentation](#configure-the-documentation)
    - [Generate the documentation](#generate-the-documentation)
    - [Publish the documentation](#publish-the-documentation)
  - [Packaging and publishing](#packaging-and-publishing)
  - [Continuous integration](#continuous-integration)
    - [Test installation of the package and run tests](#test-installation-of-the-package-and-run-tests)
    - [Code coverage with Codecov](#code-coverage-with-codecov)
  - [Miscellaneous](#miscellaneous)

This repository may serve as a template for scientific projects developed in [Python](https://www.python.org/) using [Poetry](https://python-poetry.org/).

## Development environment

### WARNING for conda users

If you have [`Anaconda`](https://www.anaconda.com/) or [`Miniconda`](https://docs.conda.io/en/latest/miniconda.html) installed,

1. **DISABLE** the auto-activation of the base environment

    ```bash
    conda config --set auto_activate_base false
    ```

2. **ALWAYS DEACTIVATE** your conda environment before running any of the following commands

    ```bash
    conda deactivate
    ```

### IDE: Visual Studio Code

[Visual Studio Code (VSCode)](https://code.visualstudio.com/) is recommended to simplify your coding experience.

The [.vscode](./.vscode) directory contains a list of suggested extensions together with the corresponding settings.
You can place it at the root of your project workspace.

See also the [vscode-workflow](https://github.com/guilgautier/vscode-workflow) repository.

### Install Poetry

> [Poetry](https://python-poetry.org/) Python Packaging And Dependency Management Made Easy

Poetry is recommended for its simplicity to manage your Python project in many ways and make it meet the Python packaging standards.

1. Read [WARNING for conda users](#warning-for-conda-users),
2. See [Poetry's installation instructions](https://python-poetry.org/docs/#installation),
3. Check your `poetry` version

    ```bash
    poetry --version
    ```

If you get an error, please check [python-poetry/poetry/issues/507](https://github.com/python-poetry/poetry/issues/507)

### Manage Python versions

As mentioned on [Poetry's documentation](https://python-poetry.org/docs/managing-environments/)

> To easily switch between Python versions, it is recommended to use [`pyenv`](https://github.com/pyenv/) or similar tools.
>
> For instance, if your project is Python 2.7 only, a standard workflow would be:
>
> ```bash
> # cd path-to-your-project
> pyenv install 2.7.15
> pyenv local 2.7.15  # Activate Python 2.7 for the current project
> poetry install
> ```

See also the [Real Python's tutorial "Intro to `pyenv`"](https://realpython.com/intro-to-pyenv/).

### Virtual environment

> A [virtual environment](https://docs.python.org/3/tutorial/venv.html) is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

It is always good practice to work in a virtual environment, isolated from your other Python projects.

With [Poetry](https://python-poetry.org/) creating/activating a virtual environment is fairly simple (please read [WARNING for conda users](#warning-for-conda-users))

```bash
# conda deactivate for conda users
poetry shell  # a (.venv) flag should appear
```

To make sure your classical commands are executed in the virtual environment, e.g., `pytest`, prepend `poetry run ...`

See also

- [Testing](#testing),
- [Documentation](#generate-the-documentation).

#### Note

In this template project, a virtual environment will be created at the root of the project in a `.venv` folder, as defined in the [poetry.toml](./poetry.toml) file, see also [Poetry's documentation](https://python-poetry.org/docs/configuration#virtualenvscreate).

If you [don’t want `poetry` to manage my virtual environments. Can I disable it?](https://python-poetry.org/docs/faq/#i-dont-want-poetry-to-manage-my-virtual-environments-can-i-disable-it)

## Dependency management

[Poetry](https://python-poetry.org/) is recommended for its dependency management capabilities.
On top of installing a given package (like `pip` can do), Poetry also resolves dependencies' version to preserve compatibility.

Dependencies specified in the [`pyproject.toml`](./pyproject.toml) (according to [PEP 518](https://www.python.org/dev/peps/pep-0518/#file-format)) can be declared in the following way.

- Install main (non-optional) dependencies

  See `[tool.poetry.dependencies]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry add numpy
  # poetry add "packagename[extra1,extra2]"
  poetry remove numpy
  ```

- Install optional dependencies

  See `[tool.poetry.dependencies]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry add jupyter --optional
  # poetry add "packagename[extra1,extra2]" --optional
  poetry remove jupyter
  ```

  Optional dependencies can then be combined to define package [extra dependencies](#install-extras-dependencies).

- Install development dependencies

  See `[tool.poetry.dev-dependencies]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry add black --dev
  # poetry add "packagename[extra1,extra2]" --dev
  poetry remove black --dev
  ```

## Installation

### Install as a dependency

- If your project is already available on [PyPI](https://pypi.org/),

  ```bash
  poetry add packagename
  # equivalent to pip install packagename
  poetry add "packagename[extra1,extra2]"
  # equivalent to pip install "packagename[extra1,extra2]"
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

  Note that, from the current [`pyproject.toml`](./pyproject.toml) file, it is **not** possible to install the project in editable mode ~~`pip install -e .`~~.
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

> The [`pytest`](https://docs.pytest.org/en/6.2.x/) framework makes it easy to write small tests, yet scales to support complex functional testing.

**Note:** In this project `pytest` and `pytest-cov` are listed as development dependencies, and installed as such when `poetry install` was run.

The unit tests of the package are declared in [`tests/test_*.py`](./tests/) files as `test_*` functions with a simple `assert` statement.

The configuration of `pytest` is defined in the [`[tool.pytest.ini_options]` section of the `pyproject.toml` file](https://docs.pytest.org/en/latest/reference/customize.html#pyproject-toml).

Run the package test suite with

```bash
poetry run pytest  # -vv --cov=packagename --cov-report=xml
```

### Run tests using VSCode

See the [Testing](https://code.visualstudio.com/docs/python/testing) section of the VSCode documentation.

## Debugging

The configuration file [.vscode/launch.json](.vscode/launch.json) contains two configurations for debugging

1. Python generic
2. Python test files

For more details, check out the documentation

- [Debugging](https://code.visualstudio.com/docs/python/debugging),
- [Debug Tests](https://code.visualstudio.com/docs/python/testing#_debug-tests).

## Documentation

> [Sphinx](https://www.sphinx-doc.org/en/master/index.html)  is a tool that makes it easy to create intelligent and beautiful documentation.

Sphinx is in charge of building the documentation and generating HTML output, but also PDF, epub, ...

The source files of the documentation are simply  `.rst` (reStructuredText) or `.md` (Markdown) files. However we suggest using reST markup to keep the same syntax and format as used for writing [Python docstings](https://devguide.python.org/documenting/).

### Install documentation dependencies

Install `docs` extras dependencies, see `[tool.poetry.extras]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry install -E docs
  # poetry install --extras "docs"
  # pip install ".[docs]"
  ```

### Configure the documentation

The configuration file is located at [`docs/conf.py`](./docs/conf.py).

- Edit the metadata of the package defined in [`docs/conf.py`](./docs/conf.py),
- See also the [sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html)

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

  [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) generates the documentation and makes a live view available in your browser.

  Changes made to `.rst` files will be reflected live in your favorite browser at <http://127.0.0.1:8000>.

  ```bash
  poetry run sphinx-autobuild docs docs/_build/html
  ```

  ```text
  ....
  build succeeded.

  The HTML pages are in docs/_build/html.
  [sphinx-autobuild] Serving on http://127.0.0.1:8000
  ```

**Important:** In both cases, any change made in the source `.py` files or the [`docs/conf.py`](./docs/conf.py) file require rebuilding the documentation.

### Publish the documentation

> [Read the Docs](https://readthedocs.org/) simplifies software documentation by automating building, versioning, and hosting of your docs for you.

After [linking your project with Read the Docs](https://docs.readthedocs.io/en/stable/intro/import-guide.html), you can configure Read the Docs to deploy the documentation of the package at <https://packagename.readthedocs.io/>, automatically or manually.

## Packaging and publishing

[Poetry](https://python-poetry.org/) is also of great help to simplify the packaging process

- build your package

  ```bash
  poetry build
  ```

- publish your package on a Package Index (PI)

  - [TestPyPI](https://test.pypi.org/) it is good practice to first publish on TestPyPI and check the results before publishing on the official [PyPI](https://pypi.org/) (see next bullet)

    - [Poetry documentation](https://python-poetry.org/docs/repositories/#adding-a-repository)
    - [Poetry configure credentials](https://python-poetry.org/docs/repositories/#configuring-credentials)
    - [TestPyPI token](https://test.pypi.org/help/#apitoken)

    ```bash
    poetry config repositories.testpypi https://test.pypi.org/legacy/
    poetry config http-basic.testpypi __token__ MY_TOKEN
    poetry publish -r testpypi
    ```

  - [PyPI](https://pypi.org/) (default)

    - [Poetry publish to PyPI](https://python-poetry.org/docs/libraries/#publishing-to-pypi)
    - [Poetry configure credentials](https://python-poetry.org/docs/repositories/#configuring-credentials)
    - [PyPI token](https://pypi.org/help/#apitoken)

    ```bash
    poetry config pypi-token.pypi MY_TOKEN
    poetry publish
    ```

## Continuous integration

> [GitHub Actions](https://github.com/features/actions) makes it easy to automate all your software workflows, now with world-class CI/CD. Build, test, and deploy your code right from GitHub. Make code reviews, branch management, and issue triaging work the way you want.

GitHub workflows declared as [`.github/workflows/*.yml`](./.github/workflows) files.

### Test installation of the package and run tests

TODO

### Code coverage with Codecov

TODO

## Miscellaneous

Consider reading

- [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [Python naming algorithm](https://melevir.medium.com/python-functions-naming-the-algorithm-74320a18278d)
