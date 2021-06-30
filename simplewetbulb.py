import click
import numpy as np


@click.command()
@click.option('--temp', prompt='temperature (ºC)', type=click.INT)
@click.option('--humid', prompt='relative humidity (%)', type=click.INT)
def cli(temp, humid): 
    wetbulb = temp * np.arctan(0.151977 * np.power((humid + 8.313659), (1/2))) + np.arctan(temp + humid) - np.arctan(humid - 1.676331) + 0.00391838 * np.power(humid, (3/2)) * np.arctan(0.023101 * humid) - 4.686035
    click.echo(f"wetbulb temperature (ºC): {np.format_float_positional(wetbulb, 2)}")


