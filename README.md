# zpa-dmeo-pvalues

A short description of the product analytics project.

## Installation

To install the python package for this project
(`zpa_demo`), run:

```bash
$ uv sync
```

then use `uv run` to run python scripts.

## Testing

To run the tests for this project, run:

```bash
$ make test
```

## Standards

This project makes use of [ruff](https://beta.ruff.rs/docs/) to automatically format
code. It is recomended to configure your IDE to automatically run these formatters on
saving of files; see the
[documentation](https://code.visualstudio.com/docs/python/editing) for doing so
when using VSCode.

If using `make` on your system you can run

```bash
$ make format
```

to run the formatters.

For linting, this project uses [ruff](https://beta.ruff.rs/docs/).
The configuration file (pyproject.toml) includes the settings determining which rules
are applied. Again linting should be configured to be flagged directly by the
IDE, however it is possible to manually run linting across the project by running

```bash
$ make lint
```

Where not covered by `ruff`, code should be compliant with the
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
In particular, docstrings should use this style guide in order to make use of
the automatic documentation provided by Sphinx.

## Project Organization

```
├── Makefile           <- Makefile with commands like `make data` or `make test`
├── README.md          <- The top-level README for developers using this project
├── requirements.txt   <- The requirements file for building the environment
├── pyproject.toml     <- Project configuration
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── notebooks          <- Jupyter notebooks
│
└── src/zpa_demo  <- Source code for use in this project
   ├── __init__.py    <- Makes src a Python module
   │
   ├── data           <- Scripts to download or generate data
   │   └── make_dataset.py
   │
   ├── features       <- Scripts to turn raw data into features for modeling
   │   └── build_features.py
   │
   ├── models         <- Scripts to train models and then use trained models to make
   │   │                 predictions
   │   ├── predict_model.py
   │   └── train_model.py
   │
   └── visualisation  <- Scripts to create exploratory and results oriented visualisations
       └── visualise.py
```

---

<p><small>Project based on the <a target="_blank" href="https://github.com/philzestyai/product-analytics-cookiecutter">cookiecutter product analytics project template</a>.</small></p>
