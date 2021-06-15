# Parlament-schema

Schema and validator for the data of Parlament de Catalunya. The validator is written in python.

## Validate

To launch the validator, the only requisite is lxml.

```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements
```

After the installation simply

```
python validate.py parlament.xml parlament.xsd
```
