# SimpleWetBulb

Calculates the wet-bulb temperature, heat index, and dew point from a given temperature in degrees Celcius or degrees Fahrenheit and the relative humidity. The calculations are taken from the following authoritative sources:

1. Wet-bulb temperature: Stoll formula (2011, DOI:https://doi.org/10.1175/JAMC-D-11-0143.1) 
2. Heat index: The National Oceanic and Atmospheric Administration of the US (https://www.wpc.ncep.noaa.gov/html/heatindex.shtml)
3. Dew point: Magnus  formula  [Sonntag90] (http://irtfweb.ifa.hawaii.edu/~tcs3/tcs3/Misc/Dewpoint_Calculation_Humidity_Sensor_E.pdf)

The output is color-coded according to the following ranges of wet-bulb temperature:

- white text: no risk (<=80ºF, <=26.66ºC)
- green text: low risk (<=85ºF, <=29.44ºC)
- yellow text: moderate risk (<=88ºF, <=31.11ºC)
- red text: high risk (<=90ºF, <=32.22ºC)
- black background, white text, bold: extreme risk (>90ºF, >32.22ºC)

These ranges are taken from [the US National Weather Service](https://www.weather.gov/tsa/wbgt):

<table bgcolor="#333399" border="1">
	<tbody>
		<tr>
			<td align="center" colspan="3"><font color="white" size="+2">Suggested Actions and Impact Prevention</font></td>
		</tr>
		<tr>
			<td width="137">
			<div align="center"><font color="#FFFFFF" size="4"><strong>WBGT(F)</strong></font></div>
			</td>
			<td width="170">
			<div align="center"><font color="#FFFFFF" size="4"><strong>Effects</strong></font></div>
			</td>
			<td width="296">
			<div align="center"><font color="#FFFFFF" size="4"><strong>Precautionary Actions</strong></font></div>
			</td>
		</tr>
		<tr>
			<td><strong><font color="#FFFFFF">&lt; 80 </font></strong></td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td><strong><font color="#FFFFFF">80-85 </font></strong></td>
			<td><strong><font color="#FFFFFF">Working or exercising in direct sunlight will stress your body after 45 minutes. </font></strong></td>
			<td><strong><font color="#FFFFFF">Take at least 15 minutes of breaks each hour if working or exercising in direct sunlight </font></strong></td>
		</tr>
		<tr>
			<td><strong><font color="#FFFFFF">85-88 </font></strong></td>
			<td><strong><font color="#FFFFFF">Working or exercising in direct sunlight will stress your body after 30 minutes. </font></strong></td>
			<td><strong><font color="#FFFFFF">Take at least 30 minutes of breaks each hour if working or exercising in direct sunlight </font></strong></td>
		</tr>
		<tr>
			<td><strong><font color="#FFFFFF">88-90 </font></strong></td>
			<td><strong><font color="#FFFFFF">Working or exercising in direct sunlight will stress your body after 20 minutes. </font></strong></td>
			<td><strong><font color="#FFFFFF">Take at least 40 minutes of breaks each hour if working or exercising in direct sunlight </font></strong></td>
		</tr>
		<tr>
			<td><strong><font color="#FFFFFF">&gt;90 </font></strong></td>
			<td><strong><font color="#FFFFFF">Working or exercising in direct sunlight will stress your body after 15 minutes. </font></strong></td>
			<td><strong><font color="#FFFFFF">Take at least 45 minutes of breaks each hour if working or exercising in direct sunlight </font></strong></td>
		</tr>
	</tbody>
</table>

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
$ simplewetbulb --temp 30 --humid 30 --input ºC
```
