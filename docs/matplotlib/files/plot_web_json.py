
import numpy as np
import matplotlib.pyplot as plt
import json
from urllib.request import urlopen
from pathlib import Path


def plot_weather(title, url):
    """Plots the weather data from the given url and gives it the given title.

    Args:
        title (str): The title of the plot.
        url (str): The url of the API that provides weather data.

    Returns:
        None
    """

    with urlopen(url) as response:
        source = response.read()
    data = json.loads(source)
    dates_list = data["daily"]["time"]
    max_list = data["daily"]["temperature_2m_max"]
    min_list = data["daily"]["temperature_2m_min"]
    xAxis = dates_list
    tmax = max_list
    tmin = min_list
    plt.grid(True)
    plt.xlabel('Date')
    plt.ylabel('Temperature (\N{DEGREE SIGN}C)')
    plt.title(title)
    ## plot lines##
    plt.plot(xAxis, tmax, color='red', marker='o', label = "Max Temp")
    plt.plot(xAxis, tmin, color='blue', marker='x', label = "Min Temp")
    # Set the bottom limit of y-axis to 0
    plt.ylim(bottom=0)
    # format dates so they are angled to fit
    plt.gcf().autofmt_xdate()
    plt.legend()
    # Get the directory of the current file
    currfile_dir = Path(__file__).parent
    # Replace spaces in title with underscores to create filename for saving figure
    filename = title.replace(" ", "_") 
    filepath = currfile_dir / (f"{filename}.png")
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    plt.savefig(filepath, dpi=600)
    # Show plot
    plt.show()


def main():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-37.81&longitude=144.96&daily=temperature_2m_max,temperature_2m_min&timezone=Australia%2FSydney"
    title = "Melb Temp forecast Jul 2023"
    plot_weather(title, url)


if __name__ == '__main__':
    main()
