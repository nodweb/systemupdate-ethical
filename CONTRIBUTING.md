# Contributing Guide

Thank you for contributing to SystemUpdate – Ethical Research Edition.

## Code Quality (Backend)

- Black (format): `black .`
- isort (imports): `isort .`
- Flake8 (lint): `flake8 .`
- MyPy (types): `mypy .`
- Tests + coverage (must be >=80%): `pytest -q --cov=app --cov-report=term --cov-report=xml --cov-fail-under=80`

Install dev tools:

```
pip install -r backend/requirements.txt -r backend/requirements-dev.txt
```

Pre-commit (optional, recommended):

```
pre-commit install
pre-commit run --all-files
```

## CI
- Backend CI runs Black/isort/Flake8/MyPy and pytest with coverage >=80%.
- Coverage XML is uploaded as an artifact.

## Branching & Commits
- Use feature branches; squash merge.
- Conventional commits, e.g. `ci(backend): ...`, `test(backend): ...`, `feat(android): ...`.

