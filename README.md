# template-python-project

- [template-python-project](#template-python-project)
  - [Development environment](#development-environment)
  - [Dependency management](#dependency-management)

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
    poetry install --extras <name>
    # or equivalently poetry install -E <name>
  ```
