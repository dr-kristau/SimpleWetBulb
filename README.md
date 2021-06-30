# SimpleWetBulb

This script uses the Stoll formula (2011, DOI:https://doi.org/10.1175/JAMC-D-11-0143.1) to estimate the wet-bulb temperature from the temperature in celcius and the relative humidity.

To test the script, you can make a new virtualenv and then install simplewetbulb:

```
$ virtualenv venv
$ . venv/bin/activate
$ pip install --editable .
```

It should now be available:

```
$ simplewetbulb
```
