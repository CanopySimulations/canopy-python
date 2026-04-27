# Canopy Python Client

The official Python client for the [Canopy Simulations](https://www.canopysimulations.com/) API.

This package enables Canopy customers to interact with the Canopy platform from Python, for example using Jupyter Notebooks, to run simulations, load results, and manage configurations programmatically.

## Installation

```sh
pip install canopy
```

## Requirements

- Python 3.10 or higher.

## Quick Start

Create a session and load output channels from a study:

```python
import canopy

async with canopy.Session(client_id="<your_client_id>", username="<your_username>") as session:
    study_data = await canopy.load_study(session, "<study_id>", "DynamicLap", ["sRun", "vCar"])
```

You will be prompted for your client secret and password on first use. Alternatively, pass them into the `Session` constructor directly (after retrieving them from a secure location).

### Synchronous Usage

If you cannot use `async/await`, use the synchronous wrapper:

```python
import canopy

with canopy.Session(client_id="<your_client_id>", username="<your_username>") as session:
    study_data = canopy.run(canopy.load_study(session, "<study_id>", "DynamicLap", ["sRun", "vCar"]))
```

## Features

- **Study & Job Loading** — Load study results, job data, scalar results, and vector channel data.
- **Parquet Support** — Channel data is loaded from Parquet files where available for improved performance, with automatic fallback to legacy binary formats.
- **Configuration Management** — Create, find, load, update, and delete simulation configurations.
- **Study Management** — Create, find, load, and delete studies. Wait for studies to complete.
- **Unit Conversion** — Convert results into your preferred units for display.
- **Async & Sync** — All helper functions support `asyncio` for efficient parallel downloads. A synchronous wrapper (`canopy.run`) is provided for environments without async support.
- **Proxy Support** — Configure proxy servers via the `Session` object.

## Examples

See the [Canopy Python Examples](https://github.com/CanopySimulations/canopy-python-examples) repository for detailed usage examples.

## Documentation

- [Full README & Developer Guide](https://github.com/CanopySimulations/canopy-python/)
- [Changelog](https://github.com/CanopySimulations/canopy-python/blob/main/CHANGELOG.md)
- [OpenAPI Client Documentation](https://github.com/CanopySimulations/canopy-python/blob/main/OPENAPI_README.md)

## License

This project is licensed under the [MIT License](https://github.com/CanopySimulations/canopy-python/blob/main/LICENSE.txt).
