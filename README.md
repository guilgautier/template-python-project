# template-python-project

[![CI](https://github.com/guilgautier/template-python-project/actions/workflows/ci.yml/badge.svg)](https://github.com/guilgautier/template-python-project/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/guilgautier/template-python-project/branch/main/graph/badge.svg?token=9O6RRKUA3S)](https://codecov.io/gh/guilgautier/template-python-project)
<!-- [![Documentation Status](https://readthedocs.org/projects/template-python-project/badge/?version=latest)](https://template-python-project.readthedocs.io/en/latest/?badge=latest) -->
[![docs-build](https://github.com/guilgautier/template-python-project/actions/workflows/docs.yml/badge.svg)](https://github.com/guilgautier/template-python-project/actions/workflows/docs.yml)
[![docs-page](https://img.shields.io/badge/docs-latest-blue)](https://guilgautier.github.io/template-python-project/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/guilgautier/template-python-project/blob/main/notebooks/)

- [template-python-project](#template-python-project)
  - [Development environment](#development-environment)
    - [WARNING for conda users](#warning-for-conda-users)
    - [IDE: Visual Studio Code](#ide-visual-studio-code)
    - [Project and dependency management](#project-and-dependency-management)
    - [Manage Python versions](#manage-python-versions)
    - [Virtual environment](#virtual-environment)
      - [Note](#note)
      - [Running your classical commands in a poetry virtual environment](#running-your-classical-commands-in-a-poetry-virtual-environment)
  - [Dependency management](#dependency-management)
    - [Define main (non-optional) dependencies](#define-main-non-optional-dependencies)
    - [Define optional dependencies](#define-optional-dependencies)
    - [Define extra dependencies](#define-extra-dependencies)
    - [Define development dependencies](#define-development-dependencies)
  - [Installation](#installation)
    - [Install the package as a dependency](#install-the-package-as-a-dependency)
    - [Install in editable mode and potentially contribute to the project](#install-in-editable-mode-and-potentially-contribute-to-the-project)
      - [Editable install with `poetry`](#editable-install-with-poetry)
      - [Editable install with `pip`](#editable-install-with-pip)
        - [Install extras dependencies](#install-extras-dependencies)
  - [Testing](#testing)
    - [Run tests using VSCode](#run-tests-using-vscode)
  - [Debugging files and tests using VSCode](#debugging-files-and-tests-using-vscode)
  - [Documentation](#documentation)
    - [Install documentation dependencies](#install-documentation-dependencies)
    - [Configure the documentation](#configure-the-documentation)
    - [Generate the documentation locally](#generate-the-documentation-locally)
    - [Build and publish the documentation online](#build-and-publish-the-documentation-online)
      - [GitHub pages](#github-pages)
      - [Read the Docs](#read-the-docs)
  - [Packaging and publishing](#packaging-and-publishing)
    - [Build the package](#build-the-package)
    - [Publish the package on a Package Index (PI)](#publish-the-package-on-a-package-index-pi)
      - [TestPyPI](#testpypi)
      - [PyPI](#pypi)
  - [Continuous integration](#continuous-integration)
    - [Test installation of the package and run tests](#test-installation-of-the-package-and-run-tests)
    - [Code coverage with Codecov](#code-coverage-with-codecov)
  - [Miscellaneous](#miscellaneous)

This repository may serve as a template for scientific projects developed in [Python](https://www.python.org/) using [`poetry`](https://python-poetry.org/).

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

### Project and dependency management

> [`poetry`](https://python-poetry.org/) Python Packaging And Dependency Management Made Easy

`poetry` is recommended for its simplicity to manage Python projects in many ways and make them meet the Python packaging standards.

1. Read [WARNING for conda users](#warning-for-conda-users),
2. See [`poetry`'s installation instructions](https://python-poetry.org/docs/#installation),
3. Check your `poetry` version

    ```bash
    poetry --version
    ```

If you get an error, please check [python-poetry/poetry/issues/507](https://github.com/python-poetry/poetry/issues/507)

### Manage Python versions

As mentioned on [`poetry`'s documentation](https://python-poetry.org/docs/managing-environments/)

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

With [`poetry`](https://python-poetry.org/) creating/activating a virtual environment is fairly simple, see also the

(please read [WARNING for conda users](#warning-for-conda-users))

```bash
# conda deactivate for conda users
poetry shell  # the (virtual-environment-name) flag should appear
```

#### Note

In this template project, as defined in the [poetry.toml](./poetry.toml) file, running `poetry shell` will create a new/activate the virtual environment named `(.venv)` at the root of the project in a `.venv` folder.
See also [`poetry`'s documentation](https://python-poetry.org/docs/configuration#virtualenvscreate).

If you [don’t want `poetry` to manage my virtual environments. Can I disable it?](https://python-poetry.org/docs/faq/#i-dont-want-poetry-to-manage-my-virtual-environments-can-i-disable-it)

#### Running your classical commands in a poetry virtual environment

[Prepend `poetry run`](https://python-poetry.org/docs/basic-usage/#using-poetry-run) to your classical commands (e.g. `poetry run pytest`) to make sure they are executed in the virtual environment.

See examples in the following sections

- [Testing](#testing),
- [Documentation](#generate-the-documentation).

## Dependency management

[`poetry`](https://python-poetry.org/) is recommended for its dependency management capabilities.

On top of installing a given dependency (like `pip` would do), `poetry` also [resolves dependencies' version](https://python-poetry.org/docs/basic-usage/#installing-dependencies) (like `conda` would do, but faster).
The result of the resolution procedure is stored in the [`poetry.lock`](./poetry.lock) file.

[`poetry`](https://python-poetry.org/docs/pyproject/) makes use of the [`pyproject.toml`](./pyproject.toml) file to define and manage your project (metadata, dependencies, etc.).
Note that, in a near future, see, e.g., [PEP 621](https://www.python.org/dev/peps/pep-0621/), the [`pyproject.toml`](./pyproject.toml) file is meant to replace `setup.py`, `setup.cfg`, etc.

### Define main (non-optional) dependencies

See [`[tool.poetry.dependencies]`](https://python-poetry.org/docs/pyproject#dependencies-and-dev-dependencies) in [`pyproject.toml`](./pyproject.toml)

```bash
poetry add numpy
# poetry add "packagename[extra1,extra2]"
poetry remove numpy
```

### Define optional dependencies

See [`[tool.poetry.dependencies]`](https://python-poetry.org/docs/pyproject#dependencies-and-dev-dependencies) in [`pyproject.toml`](./pyproject.toml)

```bash
poetry add jupyter --optional
# poetry add "packagename[extra1,extra2]" --optional
poetry remove jupyter
```

### Define extra dependencies

[Optional dependencies](#define-optional-dependencies) can be combined to define package extra dependencies, see [`[tool.poetry.extras]`](https://python-poetry.org/docs/pyproject#extras) in [`pyproject.toml`](./pyproject.toml).

See also [install extras dependencies](#install-extras-dependencies).

### Define development dependencies

See [`[tool.poetry.dev-dependencies]`](https://python-poetry.org/docs/pyproject#dependencies-and-dev-dependencies) in [`pyproject.toml`](./pyproject.toml)

```bash
poetry add black --dev
# poetry add "packagename[extra1,extra2]" --dev
poetry remove black --dev
```

## Installation

### Install the package as a dependency

- If your project is already available on [PyPI](https://pypi.org/),

    ```bash
    poetry add packagename
    # pip install packagename
    poetry add "packagename[extra1,extra2]"
    # pip install "packagename[extra1,extra2]"
    ```

- Otherwise, install the latest version from source (which might be broken)

  ```bash
  poetry add git+https://github.com/USERNAME/REPOSITORY_NAME.git
  # pip install git+https://github.com/USERNAME/REPOSITORY_NAME.git
  ```

> [To depend on a library located in a local directory or file, you can use the path property](https://python-poetry.org/docs/dependency-specification/#path-dependencies)

See also [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/) optional commands.

### Install in editable mode and potentially contribute to the project

#### Editable install with `poetry`

Your package can be installed in **editable** mode along with

- main (non-optional) dependencies, see `[tool.poetry.dependencies]` in [`pyproject.toml`](./pyproject.toml)
- development dependencies, `[tool.poetry.dev-dependencies]` in [`pyproject.toml`](./pyproject.toml)

```bash
git clone https://github.com/USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME
# activate your virtual environment or run
# poetry shell  # to create/activate local .venv (see poetry.toml)
poetry install  # main and dev dependencies are installed
# poetry install --no-dev  # to avoid installing the development dependencies
```

#### Editable install with `pip`

Your package can be installed in **editable** mode along with

- main (non-optional) dependencies, see `[project] dependencies` in [`pyproject.toml`](./pyproject.toml)
- development dependencies, `[project.optional-dependencies]` in [`pyproject.toml`](./pyproject.toml)

To do so,

- Run

  ```bash
  git clone https://github.com/USERNAME/REPOSITORY_NAME.git
  cd REPOSITORY_NAME
  ```

- Activate your virtual environment

- Modify the `[build-system]` section in [`pyproject.toml`](./pyproject.toml) to

  ```toml
  [build-system]
  requires = ["setuptools", "setuptools-scm"]
  build-backend = "setuptools.build_meta"
  ```

- Finally, run

  ```bash
  pip install --editable .
  # pip install --editable ".[extra1, extras2]"  # to install extra dependencies
  ```

See also [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/) optional commands.

##### Install extras dependencies

- With `poetry`, dependencies [defined as extra dependencies](#define-extra-dependencies) in the `[tool.poetry.extras]` section of the [`pyproject.toml`](./pyproject.toml), simply run

  ```bash
  poetry install --extras "name1 name2"
  # poetry install -E name1 -E name2
  ```

  See also [`poetry`'s documentation](https://python-poetry.org/docs/pyproject/#extras).

- With `pip`, dependencies [defined as extra dependencies](#define-extra-dependencies) in the `[project.optional-dependencies]` section of the [`pyproject.toml`](./pyproject.toml), simply run

  ```bash
  pip install ".[extra1, extras2]"
  ```

  See also [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/) optional commands.

## Testing

> The [`pytest`](https://docs.pytest.org/en/6.2.x/) framework makes it easy to write small tests, yet scales to support complex functional testing.

The unit tests of the package are declared in [`tests/test_*.py`](./tests/) files as `test_*` functions with a simple `assert` statement.

The configuration of `pytest` is defined in the [`[tool.pytest.ini_options]` section of the `pyproject.toml` file](https://docs.pytest.org/en/latest/reference/customize.html#pyproject-toml).

Run the package test suite with

```bash
# poetry shell  # to create/activate local .venv (see poetry.toml)
# poetry install  # install main (non-optional) and development dependencies
poetry run pytest
```

**Note:** In this project [`pytest`](https://docs.pytest.org/en/stable/contents.html) and [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/) are listed as `[tool.poetry.dev-dependencies]` in [`pyproject.toml`](./pyproject.toml).
These dev-dependencies are installed as such when `poetry install` was run.

### Run tests using VSCode

See the [Testing](https://code.visualstudio.com/docs/python/testing) section of the VSCode documentation.

## Debugging files and tests using VSCode

The configuration file [.vscode/launch.json](.vscode/launch.json) contains two configurations for debugging

1. Python generic files
2. Python unit-test files

For more details, see the VSCode documentation

- [Debugging](https://code.visualstudio.com/docs/python/debugging),
- [Debug Tests](https://code.visualstudio.com/docs/python/testing#_debug-tests).

## Documentation

> [Sphinx](https://www.sphinx-doc.org/en/master/index.html)  is a tool that makes it easy to create intelligent and beautiful documentation.

Sphinx is in charge of building the documentation and generating HTML output, but also PDF, epub, ...

The source files of the documentation are simply  `.rst` (reStructuredText) or `.md` (Markdown) files. However we suggest using the reST markup to keep the same syntax and format as used for writing [Python docstings](https://devguide.python.org/documenting/).

### Install documentation dependencies

Install `docs` extras dependencies, see `[tool.poetry.extras]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry shell  # to create/activate local .venv (see poetry.toml)
  poetry install -E docs
  # poetry install --extras "docs"
  # pip install ".[docs]"
  ```

### Configure the documentation

The configuration file is located at [`docs/conf.py`](./docs/conf.py).

- Edit the metadata of the package defined in [`docs/conf.py`](./docs/conf.py),
- See also the [sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html)

### Generate the documentation locally

To generate the documentation locally, i.e., on your machine,

```bash
# poetry shell  # to create/activate local .venv (see poetry.toml)
# poetry install -E docs
poetry run sphinx-build -b html docs docs/_build/html
```

and navigate the documentation

```bash
open docs/_build/html/index.html
```

**Important:** Any change made in the source `.py` files or the [`docs/conf.py`](./docs/conf.py) file require rebuilding the documentation.

### Build and publish the documentation online

Choose either

- [GitHub pages](#github-pages) (default), or
- [Read the Docs](#read-the-docs).

#### GitHub pages

The documentation can be built according to the GitHub workflow [.github/workflows/docs.yml](.github/workflows/docs.yml) and deployed from the `gh-pages` branch via GitHub pages at
[https://your-username.github.io/template-python-project](https://guilgautier.github.io/template-python-project).

To make this work automatically, follow the simple steps below (only once!)

1. Push you latest changes

   - a `gh-pages` branch will be automatically created/updated.

2. On your GitHub repository
   - Go to Settings -> Pages -> Source
     - select branch: `gh-pages`
     - select folder: `/root`

#### Read the Docs

> [Read the Docs](https://readthedocs.org/) simplifies software documentation by automating building, versioning, and hosting of your docs for you.

After [linking your project with Read the Docs](https://docs.readthedocs.io/en/stable/intro/import-guide.html), you can configure Read the Docs to build and deploy the documentation of the package at [https://repository-name.readthedocs.io/en/latest/](https://template-python-project.readthedocs.io/en/latest/), either automatically or manually.

See also the [`.readthedocs.yaml`](./.readthedocs.yaml) configuration file.

## Packaging and publishing

[`poetry`](https://python-poetry.org/) is also of great help to simplify the packaging process.

### Build the package

<https://python-poetry.org/docs/libraries#packaging>

```bash
poetry build
```

See also [PyPA's `build` package](https://pypa-build.readthedocs.io/en/stable/).

### Publish the package on a Package Index (PI)

#### TestPyPI

It is good practice to first publish on [TestPyPI](https://test.pypi.org/) and check the results before publishing on the official [PyPI](https://pypi.org/), see [PyPI](#pypi) section.

- [`poetry` documentation](https://python-poetry.org/docs/repositories/#adding-a-repository)
- [`poetry` configure credentials](https://python-poetry.org/docs/repositories/#configuring-credentials)
- [TestPyPI token](https://test.pypi.org/help/#apitoken)

 ```bash
 poetry config repositories.testpypi https://test.pypi.org/legacy/
 poetry config http-basic.testpypi __token__ MY_TOKEN
 poetry publish -r testpypi
 ```

- Check the results <https://test.pypi.org/project/packagename/>
- Check [your package installation from TestPyPI](https://packaging.python.org/guides/using-testpypi/#using-testpypi-with-pip)

 ```bash
 # create a new virtual environment and run
 pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ packagename
 ```

See also [PyPA `twine` package](https://twine.readthedocs.io/en/latest/).

#### PyPI

[PyPI](https://pypi.org/) is the official Python Package Index

> [By default, `poetry` is configured to use the PyPI repository, for package installation and publishing.is the default repository](https://python-poetry.org/docs/repositories/#using-the-pypi-repository)

- [`poetry` publish to PyPI](https://python-poetry.org/docs/libraries/#publishing-to-pypi)
- [`poetry` configure credentials](https://python-poetry.org/docs/repositories/#configuring-credentials)
- [PyPI token](https://pypi.org/help/#apitoken)

  ```bash
  poetry config pypi-token.pypi MY_TOKEN
  poetry publish
  ```

- Check the results <https://pypi.org/project/packagename/>
- Check your package installation from PyPI

  ```bash
  # create a new virtual environment and run
  pip install packagename
  ```

See also [PyPA `twine` package](https://twine.readthedocs.io/en/latest/).

## Continuous integration

> [GitHub Actions](https://github.com/features/actions) makes it easy to automate all your software workflows, now with world-class CI/CD. Build, test, and deploy your code right from GitHub. Make code reviews, branch management, and issue triaging work the way you want.

GitHub workflows declared as [`.github/workflows/*.yml`](./.github/workflows) files.

### Test installation of the package and run tests

See the corresponding sections in the
[`.github/workflows/ci.yml`](./.github/workflows/ci.yml)

### Code coverage with Codecov

- See the corresponding section in the
[`.github/workflows/ci.yml`](./.github/workflows/ci.yml)
- [codecov](https://docs.codecov.com/docs/)
- [codecov-action](https://github.com/codecov/codecov-action)

## Miscellaneous

Consider reading

- [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [Python naming algorithm](https://melevir.medium.com/python-functions-naming-the-algorithm-74320a18278d)
