# SimpleWetBulb

This script uses the Stoll formula (2011, DOI:https://doi.org/10.1175/JAMC-D-11-0143.1) to estimate the wet-bulb temperature from the temperature in celcius and the relative humidity.

The output is color-coded:
- white text: no risk (<=80ºF, <=26.66ºC)
- green text: low risk (<=85ºF, <=29.44ºC)
- yellow text: moderate risk (<=88ºF, <=31.11ºC)
- red text: high risk (<=90ºF, <=32.22ºC)
- black backgroud, white text, bold, blinking: extreme risk (>90ºF, >32.22ºC)

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

or:

```
$ simplewetbulb --temp 30 --humid 30
```
