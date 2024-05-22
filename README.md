# References

https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://python-poetry.org/docs/pyproject/


# Before uploading any changes, you must first run the unit tests is it exists

cd Logyca\tests
```console
# Pre-requisite
pip install pytest -y
pip show pytest

# Make test
pytest -s
```

# Define version to publish

Change Attribute: setup.py: VERSION

## Definitions for releasing versions
* https://peps.python.org/pep-0440/

    - X.YaN (Alpha release): Identify and fix early-stage bugs. Not suitable for production use.
    - X.YbN (Beta release): Stabilize and refine features. Address reported bugs. Prepare for official release.
    - X.YrcN (Release candidate): Final version before official release. Assumes all major features are complete and stable. Recommended for testing in non-critical environments.
    - X.Y (Final release/Stable/Production): Completed, stable version ready for use in production. Full release for public use.

# Pre-Requisites to Build + Publish

```python
# Create virtual environment
python -m pip install pipenv
# Activate virtual environment
python -m pipenv shell

# Build tool
pip install --upgrade setuptools

# Publish to pypi/Azure DevOps Artifacts tool
pip install --upgrade twine

```

# Build + Publish in https://pypi.org

```console
# be located in the library folder
cd folder/
# then run this in the same folder where setup.py is located.    
python -m build
# Upload to PyPI Production
twine upload dist/* --config-file ../.pypirc --verbose --repository pypi
```

For testing
```console
# be located in the library folder
cd folder/
# Upload to PyPI Develop
twine upload dist/* --config-file ../.pypirc --verbose --repository testpypi
```

# Delete Cache

Powershell
```Powershell
Get-ChildItem -Directory -Recurse -Filter "*.egg-info" | Remove-Item -Force -Recurse
Get-ChildItem -Directory -Recurse -Filter "dist" | Remove-Item -Force -Recurse
```

