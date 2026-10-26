# MIMO Communications Lab

Python library and hands-on tutorials for the MIMO Communications course at TU
Dresden. Reusable mathematical models and signal-processing algorithms will be
accompanied by interactive notebooks and numerical experiments. This initial
scaffold contains docstring-only placeholders; algorithms and notebooks are not
implemented yet. The Python package is `mimolab`.

## Structure

```text
mimo-communications-lab/
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── AGENTS.md
├── lectures/
├── src/mimolab/
│   ├── __init__.py
│   ├── channels.py
│   ├── p2p.py
│   ├── mu_uplink.py
│   ├── mu_downlink.py
│   ├── estimation.py
│   ├── detection.py
│   ├── massive.py
│   ├── distributed.py
│   └── metrics.py
├── notebooks/
├── tests/
├── examples/
└── docs/
```

`src/mimolab/` holds reusable algorithms independently of plotting and
presentation. `notebooks/` will hold interactive explanations and course
exercises; exercise-specific parameters and student work belong there.
`examples/` is reserved for standalone usage scripts, `docs/` for supporting
documentation, and `tests/` for automated checks. Empty directories contain
`.gitkeep` files so Git retains them.

`lectures/` contains the authoritative LaTeX manuscripts `01`–`06` and shared
`math_notation.tex`, `acronyms.tex`, and `preamble.tex` definitions in one flat
directory. These sources are separate from the installable Python package.
Implementations follow their system models, notation, dimensions, and energy
normalization; documentation and tests should retain useful equation labels.
Do not edit the manuscripts unless explicitly requested. Finalized replacements
will be supplied separately. Generated lecture PDFs and build artifacts do not
belong in the repository.

## Installation

Install Python **3.12 or newer**, including pip and venv, and Git to clone the
repository. From the repository root, create a virtual environment:

```sh
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on Linux/macOS:

```sh
source .venv/bin/activate
```

Install in editable mode so source changes are available without reinstalling:

```sh
python -m pip install -e .
```

NumPy and SciPy are runtime dependencies. Install optional Matplotlib,
JupyterLab, and ipykernel dependencies for notebook work:

```sh
python -m pip install -e ".[notebooks]"
python -m jupyter lab
```

## Development and validation

Install pytest and run the initial import checks:

```sh
python -m pip install -e ".[dev]"
python -m pytest
```

Install both optional groups with `python -m pip install -e ".[notebooks,dev]"`.
Tests import the installed package without adding `src/` to the test path.
A successful editable install followed by pytest validates initial packaging.
See [AGENTS.md](AGENTS.md) for mathematical, programming, and testing conventions.

## License

MIT; see [LICENSE](LICENSE). Copyright (c) 2026 Ahmad Nimr.
Repository: [ahmadnimr/mimo-communications-lab](https://github.com/ahmadnimr/mimo-communications-lab).
