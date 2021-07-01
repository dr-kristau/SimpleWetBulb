# SimpleWetBulb

Calculates the wet-bulb temperature, heat index, and dew point from a given temperature in degrees Celcius and the relative humidity. The calculations are taken from the following authoritative sources:

Wet-bulb temperature: Stoll formula (2011, DOI:https://doi.org/10.1175/JAMC-D-11-0143.1) 
Heat index: The National Oceanic and Atmospheric Administration of the US (https://www.wpc.ncep.noaa.gov/html/heatindex.shtml)
Dew point: Magnus  formula  [Sonntag90] (http://irtfweb.ifa.hawaii.edu/~tcs3/tcs3/Misc/Dewpoint_Calculation_Humidity_Sensor_E.pdf)

The output is color-coded:
- white text: no risk (<=80ºF, <=26.66ºC)
- green text: low risk (<=85ºF, <=29.44ºC)
- yellow text: moderate risk (<=88ºF, <=31.11ºC)
- red text: high risk (<=90ºF, <=32.22ºC)
- black background, white text, bold, blinking: extreme risk (>90ºF, >32.22ºC)

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
