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
      - [Running your classical commands in a poetry virtual environment](#running-your-classical-commands-in-a-poetry-virtual-environment)
  - [Dependency management](#dependency-management)
    - [Define main (mandatory) dependencies](#define-main-mandatory-dependencies)
    - [Organize your dependencies](#organize-your-dependencies)
      - [Define optional groups](#define-optional-groups)
    - [Define extra dependencies](#define-extra-dependencies)
  - [Installation](#installation)
    - [Install the package as a dependency for another project](#install-the-package-as-a-dependency-for-another-project)
      - [From a repository](#from-a-repository)
        - [From PyPI](#from-pypi)
      - [From a git repository](#from-a-git-repository)
      - [From a local directory](#from-a-local-directory)
    - [Install in editable mode and potentially contribute to the project](#install-in-editable-mode-and-potentially-contribute-to-the-project)
      - [Editable install with `poetry`](#editable-install-with-poetry)
        - [Install group dependencies](#install-group-dependencies)
      - [Editable install with `pip`](#editable-install-with-pip)
        - [Install extras dependencies](#install-extras-dependencies)
  - [Testing](#testing)
    - [Run tests using VSCode](#run-tests-using-vscode)
  - [Debugging files and tests files using VSCode](#debugging-files-and-tests-files-using-vscode)
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

`poetry>=1.2` is recommended for its simplicity to manage Python projects in many ways and make them meet the Python packaging standards.

1. Read [WARNING for conda users](#warning-for-conda-users),
2. See [`poetry`'s installation instructions](https://python-poetry.org/docs/#installation),
3. Check your `poetry` version

    ```bash
    poetry --version
    ```

If you get an error, please check [python-poetry/poetry/issues/507](https://github.com/python-poetry/poetry/issues/507)

### Manage Python versions

To easily switch between Python versions, it is recommended to use [`pyenv`](https://github.com/pyenv/) or similar tools.

> ```bash
> # cd REPOSITORY_NAME
> pyenv install 3.9.8
> pyenv local 3.9.8  # Activate Python 3.9.8 for the current project
> ```

See also the [Real Python's tutorial "Intro to `pyenv`"](https://realpython.com/intro-to-pyenv/).

### Virtual environment

> A [virtual environment](https://docs.python.org/3/tutorial/venv.html) is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

It is always good practice to work in a virtual environment, isolated from your other Python projects.

With [`poetry`](https://python-poetry.org/) creating/activating a virtual environment is fairly simple with the [`poetry shell`](https://python-poetry.org/docs/cli/#shell) command

**Please read [WARNING for conda users](#warning-for-conda-users))**

```bash
# conda deactivate  # for conda users
poetry shell  # create/activate virtual environment (see poetry.toml)
exit  # to exit the virtual environment
```

**Note**

In this template project, as defined in the [poetry.toml](./poetry.toml) file, the command `poetry shell` will create a new/activate the virtual environment named `(.venv)` at the root of the project in a `.venv` folder
See also [`poetry`'s documentation](https://python-poetry.org/docs/configuration#virtualenvscreate).

If you [don’t want `poetry` to manage my virtual environments. Can I disable it?](https://python-poetry.org/docs/faq/#i-dont-want-poetry-to-manage-my-virtual-environments-can-i-disable-it)

#### Running your classical commands in a poetry virtual environment

[Prepend `poetry run`](https://python-poetry.org/docs/basic-usage/#using-poetry-run) to your classical commands (e.g. `poetry run pytest`) to make sure they are executed in the dedicated virtual environment.

See examples in the following sections

- [Testing](#testing),
- [Documentation](#generate-the-documentation).

## Dependency management

[`poetry`](https://python-poetry.org/) is recommended for its dependency management capabilities.

`poetry` makes use of a single file: the [`pyproject.toml`](./pyproject.toml) file.

Nowadays, since [PEP 517](https://peps.python.org/pep-0517/), [PEP 518](https://peps.python.org/pep-0518/), [PEP 660](https://peps.python.org/pep-0660/), [PEP 621](https://peps.python.org/pep-0621/), the [`pyproject.toml`](./pyproject.toml) file is used to define and manage your project metadata, build system, dependencies, packaging options, third party packages configurations, etc.
In particular, it replaces the need for ~~`setup.py`~~, ~~`setup.cfg`~~, ~~`requirements.txt`~~, `~~pytest.ini~~` files.

On top of installing a given dependency (like `pip` would do), `poetry` also resolves dependencies' version (like `conda` would do, but faster).
The result of the resolution procedure is stored in the [`poetry.lock`](./poetry.lock) file.
This guarantees full reproducibility of your project setup!

> Anyone who sets up the project with `poetry` when the file `poetry.lock` is present uses the exact same versions of the dependencies that you are using.

### Define main (mandatory) dependencies

Use the command [`poetry add`](https://python-poetry.org/docs/cli/#add) and check the result in the section `[tool.poetry.dependencies]` of the [`pyproject.toml`](./pyproject.toml) file

```bash
poetry add PACKAGENAME
# poetry add "PACKAGENAME[EXTRANAME1,EXTRANAME2]"
poetry remove PACKAGENAME
```

### Organize your dependencies

> [With `poetry` you can organize your dependencies in groups to manage them in a more granular way](https://python-poetry.org/docs/managing-dependencies/)

To do this, use the command [`poetry add PACKAGENAME --group GROUPNAME`](https://python-poetry.org/docs/managing-dependencies/#adding-a-dependency-to-a-group) and check the result in the corresponding section `[tool.poetry.group.GROUPNAME.dependencies]` of the [`pyproject.toml`](./pyproject.toml) file.

For example, to add [`pytest`](https://docs.pytest.org/) to the `dev` (development) group use

```bash
poetry add pytest --group dev
poetry remove pytest --group dev
```

#### Define optional groups

If you wish to [make a group of dependencies optional](https://python-poetry.org/docs/managing-dependencies/#optional-groups), add the following to the [`pyproject.toml`](./pyproject.toml) file

```bash
[tool.poetry.group.GROUPNAME]
optional = true

# [tool.poetry.group.GROUPNAME.dependencies]
```

See also [install group dependencies](#install-group-dependencies).

### Define extra dependencies

[Single dependecies can also be made optional](#define-optional-dependencies)

```bash
poetry add PACKAGENAME1 --optional
poetry add PACKAGENAME2 --optional
```

and then combined to define [package extra dependencies](https://python-poetry.org/docs/master/pyproject#extras) in the [`pyproject.toml`](./pyproject.toml).

```bash
[tool.poetry.extras]
EXTRANAME = ["PACKAGENAME1", "PACKAGENAME2"]
```

See also [Install the package with extra dependencies](#install-extras-dependencies).

## Installation

### Install the package as a dependency for another project

Use the command [`poetry add`](https://python-poetry.org/docs/cli/#add) which, to some extend, is similar to [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/).

#### From a repository

> By default, Poetry discovers and installs packages from [PyPI](https://pypi.org/).
> This represents most cases and will likely be enough for most users.

If the target package is available from a different source than [PyPI](https://pypi.org/), you can configure poetry and add this new source, see [the documentation](https://python-poetry.org/docs/master/repositories/)

##### From PyPI

When the target project is available on [PyPI](https://pypi.org/)

  ```bash
  poetry add PACKAGENAME
  # pip install PACKAGENAME
  poetry add "PACKAGENAME[EXTRANAME1,EXTRANAME2]"
  # pip install "PACKAGENAME[EXTRANAME1,EXTRANAME2]"
  poetry add --editable "PACKAGENAME[EXTRANAME1,EXTRANAME2]"
  # pip install --editable "PACKAGENAME[EXTRANAME1,EXTRANAME2]"
  ```

#### From a git repository

[When the target project is available online](https://python-poetry.org/docs/master/dependency-specification/#git-dependencies)

  ```bash
  poetry add git+https://github.com/USERNAME/REPOSITORY_NAME.git
  # pip install git+https://github.com/USERNAME/REPOSITORY_NAME.git
  poetry add --editable git+https://github.com/USERNAME/REPOSITORY_NAME.git
  # pip install --editable git+https://github.com/USERNAME/REPOSITORY_NAME.git
  ```

#### From a local directory

[When the target project is located in a specific directory or file](https://python-poetry.org/docs/dependency-specification/#path-dependencies)
poetry add --editable ./my-package/

  ```bash
  poetry add PATH_TO_PACKAGE
  # pip install PATH_TO_PACKAGE
  poetry add --editable PATH_TO_PACKAGE
  # pip install --editable PATH_TO_PACKAGE
  ```

### Install in editable mode and potentially contribute to the project

**By default, dependencies across all non-optional groups will be installed when executing** `poetry install`.

#### Editable install with `poetry`

**By default**, the command [`poetry install`](https://python-poetry.org/docs/cli/#install) **installs the package in editable mode**.

```bash
git clone https://github.com/USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME
poetry shell  # create/activate virtual environment (see poetry.toml)
poetry install  # main + non-optional group dependencies
poetry install --without GROUPNAME # main + non-optional - GROUPNAME dependencies
```

##### Install group dependencies

Optional group dependencies, see [Define optional groups](#define-optional-groups), can be installed using the [`--with`, `--only` flags](https://python-poetry.org/docs/managing-dependencies/#installing-group-dependencies)

```bash
poetry install --with GROUPNAME1 --without GROUPNAME2
poetry install --only GROUPNAME3
```

#### Editable install with `pip`

Consider using [`pip>=21.3.1`](https://pip.pypa.io/en/stable/news/#v21-3-1), when installing packages defined by a `pyproject.toml` file.

  ```bash
  git clone https://github.com/USERNAME/REPOSITORY_NAME.git
  cd REPOSITORY_NAME
  # activate your virtual environment  # e.g. conda activate ENVIRONMENT_NAME
  pip install --editable .
  # pip install --editable ".[EXTRANAME1, EXTRANAME2]"  # to install extra dependencies
  ```

See also the [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/) optional commands.

##### Install extras dependencies

- With `poetry`, dependencies [defined as extra dependencies](#define-extra-dependencies) in the `[tool.poetry.extras]` section of the [`pyproject.toml`](./pyproject.toml), simply run

  ```bash
  poetry install --extras "EXTRANAME1 EXTRANAME2"
  # poetry install -E EXTRANAME1 -E EXTRANAME2
  ```

  See also [`poetry`'s documentation](https://python-poetry.org/docs/pyproject/#extras).

- With `pip`, dependencies [defined as extra dependencies](#define-extra-dependencies) in the `[project.optional-dependencies]` section of the [`pyproject.toml`](./pyproject.toml), simply run

  ```bash
  pip install ".[EXTRANAME1, EXTRANAME2]"
  ```

  See also [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/) optional commands.

## Testing

> The [`pytest`](https://docs.pytest.org/) framework makes it easy to write small tests, yet scales to support complex functional testing.

The unit tests of the package are declared in [`tests/test_*.py`](./tests/) files as `test_*` functions with a simple `assert` statement.

The configuration of `pytest` is defined in the [`[tool.pytest.ini_options]` section of the `pyproject.toml` file](https://docs.pytest.org/en/latest/reference/customize.html#pyproject-toml).

Run the package test suite with

```bash
# poetry shell  # create/activate virtual environment (see poetry.toml)
# poetry install --with dev # install main and development dependencies [tool.poetry.group.dev.dependencies]
poetry run pytest
```

### Run tests using VSCode

See the [Testing](https://code.visualstudio.com/docs/python/testing) section of the VSCode documentation.

## Debugging files and tests files using VSCode

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

Install the documentation dependencies defined under `[tool.poetry.group.docs.dependencies]` in [`pyproject.toml`](./pyproject.toml)

  ```bash
  poetry shell  # create/activate virtual environment (see poetry.toml)
  poetry install --with docs
  # poetry install --only docs
  ```

### Configure the documentation

The configuration file is located at [`docs/conf.py`](./docs/conf.py).

- Edit the metadata of the package documentation defined in [`docs/conf.py`](./docs/conf.py),
- See also the [sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html)

### Generate the documentation locally

To generate the documentation locally, i.e., on your machine,

```bash
# poetry shell  # create/activate virtual environment (see poetry.toml)
# poetry install --with docs
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

The documentation can be built according to the GitHub workflow [.github/workflows/docs.yml](.github/workflows/docs.yml) and deployed from the `gh-pages` branch via GitHub pages at `https://USERNAME.github.io/template-python-project`.

To make this work automatically, follow the simple steps below (only once!)

1. Push you latest changes

   - the `gh-pages` branch will be automatically created/updated once the GitHub workflow [.github/workflows/docs.yml](.github/workflows/docs.yml) is triggered

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

Before publication, [`poetry` can package your project](https://python-poetry.org/docs/libraries#packaging)

```bash
poetry build
```

See also [PyPA's `build` package](https://pypa-build.readthedocs.io/en/stable/).

### Publish the package on a Package Index (PI)

#### TestPyPI

It is good practice to first publish on [TestPyPI](https://test.pypi.org/) and check the results before publishing on the official [PyPI](https://pypi.org/), see [PyPI](#pypi) section.

Let's configure `poetry` to publish your package on [TestPyPI](https://test.pypi.org/)

- [`poetry` documentation](https://python-poetry.org/docs/repositories/#adding-a-repository)
- [`poetry` configure credentials](https://python-poetry.org/docs/repositories/#configuring-credentials)
- [TestPyPI token](https://test.pypi.org/help/#apitoken)

 ```bash
 poetry config repositories.testpypi https://test.pypi.org/legacy/
 poetry config http-basic.testpypi __token__ MY_TOKEN
 # poetry build
 poetry publish --repository testpypi
 ```

- Check the results <https://test.pypi.org/project/packagename/>
- Check [your package installation from TestPyPI](https://packaging.python.org/guides/using-testpypi/#using-testpypi-with-pip)

  ```bash
  # create a new virtual environment and run
  # conda create -n test-install-testpypi python=3.8 pip
  # conda activate test-install-testpypi
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
  # poetry build
  poetry publish
  ```

- Check the results <https://pypi.org/project/packagename/>
- Check your package installation from PyPI

  ```bash
  # create a new virtual environment and run
  # conda create -n test-install-pypi python=3.8 pip
  # conda activate test-install-pypi
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
