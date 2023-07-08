
import numpy as np
import matplotlib.pyplot as plt
import json
from urllib.request import urlopen
from datetime import datetime, timedelta
from pathlib import Path


def plot_weather_temperatures(title, url):
    """Plots the weather data from the given url and gives it the given title.

    Args:
        title (str): The title of the plot.
        url (str): The url of the API that provides weather data.

    Returns:
        None
    """
    # Open the URL and read its content
    with urlopen(url) as response:
        source = response.read()
    # Load the content as a JSON object
    data = json.loads(source)
    # Extract the list of dates from the "daily" key of the JSON object
    dates_list = data["daily"]["time"]
    # Extract the list of maximum temperatures from the "daily" key of the JSON object
    tmax = data["daily"]["temperature_2m_max"]
    # Extract the list of minimum temperatures from the "daily" key of the JSON object
    tmin = data["daily"]["temperature_2m_min"]
    # Convert the dates in dates_list to datetime objects
    dates_list = [datetime.strptime(date, "%Y-%m-%d") for date in dates_list]
    # plot lines with x, y, colour, markers, labels for legend
    plt.plot(dates_list, tmax, color='darkred', marker='o', label = "Max Temp")
    plt.plot(dates_list, tmin, color='blue', marker='x', label = "Min Temp")
    # Set the offset values for the x and y coordinates of the temperature labels
    x_offset = timedelta(days=0.2)
    max_offset = 0.7
    min_offset = -1.2
    # Label the maximum temperatures
    for x, y in zip(dates_list, tmax):
        plt.text(x - x_offset, y + max_offset, f"{y:.1f}", color="darkred", fontsize=8)
    # Label the minimum temperatures
    for x, y in zip(dates_list, tmin):
        plt.text(x - x_offset, y + min_offset, f"{y:.1f}", color="blue", fontsize=8)
    # Set the bottom limit of the y-axis to the minimum of 0 and 2 units below the minimum temperature,
    # and set the top limit of the y-axis to 2 units above the maximum temperature
    plt.ylim(bottom=min(0, min(tmin) - 2), top=max(tmax) + 2)
    # Set the y ticks to be every 2 units
    ymin = min(0, min(tmin) - 2)
    ymax = max(tmax) + 2
    plt.yticks(np.arange(ymin, ymax, 2))
    # format dates so they are angled to fit
    plt.gcf().autofmt_xdate()
    # Set the font size of the x-axis labels to 10 points
    plt.tick_params(axis='x', labelsize=8)
    # add a grid
    plt.grid(True)
    # add axis title labels
    plt.xlabel('Date', fontsize=14)
    # \N{DEGREE SIGN} si the escape sequence for unicode name for the degree symbol
    plt.ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize=14)
    # add plot title
    plt.title(title,fontsize=18)
    # place legend at lower right
    plt.legend(loc="lower right")
    # Get the directory of the current file
    currfile_dir = Path(__file__).parent
    # Replace spaces in title with underscores to create filename for saving figure
    filename = title.replace(" ", "_")
    # build the image file path
    filepath = currfile_dir / (f"{filename}.png")
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    plt.savefig(filepath, dpi=600)
    # Show plot
    plt.show()


def plot_melb_temp_7day():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-37.81&longitude=144.96&daily=temperature_2m_max,temperature_2m_min&timezone=Australia%2FSydney"
    title = "Melb Temp forecast Jul 2023"
    plot_weather_temperatures(title, url)


if __name__ == '__main__':
    plot_melb_temp_7day()
