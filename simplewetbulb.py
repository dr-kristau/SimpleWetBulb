import click
import numpy as np

@click.command()
@click.option('--temp', prompt='temperature (ºC)', type=click.FLOAT)
@click.option('--humid', prompt='relative humidity (%)', type=click.FLOAT)
def cli(temp, humid): 
    wetbulb = calc_wetbulb(temp, humid)
    heatindex = calc_heatindex(temp, humid)
    dewpoint = calc_dewpoint(temp, humid)
    textwbt = f"wet-bulb temperature (ºC): {np.format_float_positional(wetbulb, 0, True, True, '-')}"
    texthi = f"heat index (ºC): {np.format_float_positional(heatindex, 0, True, True, '-')}"
    textdp = f"dew point (ºC): {np.format_float_positional(dewpoint, 0, True, True, '-')}"
    
    if np.less_equal(wetbulb, fartoCelc(80)):
       click.echo(click.style(textwbt, fg='white'))
       click.echo(click.style(texthi, fg='white'))
       click.echo(click.style(textdp, fg='white'))
    elif np.less_equal(wetbulb, fartoCelc(85)):
       click.echo(click.style(textwbt, fg='green'))
       click.echo(click.style(texthi, fg='green'))
       click.echo(click.style(textdp, fg='green'))
    elif np.less_equal(wetbulb, fartoCelc(88)):
       click.echo(click.style(textwbt, fg='yellow'))
       click.echo(click.style(texthi, fg='yellow'))  
       click.echo(click.style(textdp, fg='yellow'))
    elif np.less_equal(wetbulb, fartoCelc(90)):
       click.echo(click.style(textwbt, fg='red')) 
       click.echo(click.style(texthi, fg='red'))  
       click.echo(click.style(textdp, fg='red'))  
    elif np.greater(wetbulb, fartoCelc(90)):
       click.echo(click.style(textwbt, bold=True, bg='white', fg='black')) 
       click.echo(click.style(texthi, bold=True, bg='white', fg='black')) 
       click.echo(click.style(textdp, bold=True, bg='white', fg='black'))    
       
def fartoCelc(tempF):
    return (tempF - 32)/1.8
    
def celctoFar(tempC):
    return (tempC * 1.8) + 32     
       
def calc_wetbulb(temp, humid):
    return temp * np.arctan(0.151977 * np.power((humid + 8.313659), (1/2))) + np.arctan(temp + humid) - np.arctan(humid - 1.676331) + 0.00391838 * np.power(humid, (3/2)) * np.arctan(0.023101 * humid) - 4.686035
        
def calc_heatindex(temp, humid):
    tempF = celctoFar(temp)
    hitemp = 61.0+((tempF-68.0)*1.2)+(humid*0.094)
    hifinal = 0.5*(tempF+hitemp)
    
    hi = hifinal
    
    if np.greater(hifinal, 79):
        hi = -42.379+2.04901523*tempF+10.14333127*humid-0.22475541*tempF*humid-6.83783*(np.power(10.0, -3))*(np.power(tempF, 2))-5.481717*(np.power(10.0, -2))*(np.power(humid, 2))+1.22874*(np.power(10.0, -3))*(np.power(tempF, 2))*humid+8.5282*(np.power(10.0, -4))*tempF*(np.power(humid, 2))-1.99*(np.power(10.0, -6))*(np.power(tempF, 2))*(np.power(humid,2))
        if np.less_equal(humid, 13) and np.greater_equal(tempF, 80.0) and np.less_equal(tempF, 112.0):
            adj1 = (13.0-humid)/4.0
            adj2 = np.sqrt((17.0-np.absolute(tempF-95.0))/17.0)
            adj = adj1 * adj2
            hi = hi - adj
        elif np.greater(humid, 85.0) and np.greater_equal(tempF, 80.0) and np.less_equal(tempF, 87.0):
            adj1 = (humid-85.0)/10.0
            adj2 = (87.0-tempF)/5.0
            adj = adj1 * adj2
            hi = hi + adj
            
    return fartoCelc(hi)
    
def calc_dewpoint(temp, humid):
    h = (np.log10(humid)-2)/0.4343 + (17.62*temp)/(243.12+temp) 
    return 243.12*h/(17.62-h)   


