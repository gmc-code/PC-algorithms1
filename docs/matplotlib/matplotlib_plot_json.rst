====================================================
Matplotlib plot json
====================================================

| Matplotlib can be used to draw a graph of json data from the web.

----

Straight line graph with parabola
------------------------------------


.. image:: images/Melb_Temp_forecast_Jul_2023.png
    :width: 600
    :align: center

----

Python code
-------------

    
| The python code is below.

.. literalinclude:: files/plot_web_json.py
    :linenos:

----

Code explanation
-------------------

Here is an explanation of each line of the code with all the syntax details:

::

    import numpy as np

This imports the numpy library, which is used for working with arrays and matrices, and gives it the alias np for convenience.

::

    import matplotlib.pyplot as plt

This imports the pyplot module from the matplotlib library, which is used for creating and customizing plots, and gives it the alias plt for convenience.

::

    import json

This imports the json library, which is used for parsing and manipulating data in JSON format.

::

    from urllib.request import urlopen

This imports the urlopen function from the urllib.request module, which is used for opening and reading URLs.

::

    from pathlib import Path

This imports the Path class from the pathlib module, which is used for working with file paths in a cross-platform way.


::

    def plot_weather(title, url):

This defines a function named plot_weather that takes two parameters: title and url. The function will plot the weather data from the given url and give it the given title.

::

    with urlopen(url) as response:

This opens the url as a response object using the urlopen function, and closes it automatically when done.

::

    source = response.read()

This reads the data from the response object and assigns it to a variable named source.

::

    data = json.loads(source)

This parses the data from source using the json.loads function and converts it into a Python dictionary named data.

::

    dates_list = data["daily"]["time"]

This extracts the list of dates from the data dictionary and assigns it to a variable named dates_list.

::

    max_list = data["daily"]["temperature_2m_max"]

This extracts the list of maximum temperatures from the data dictionary and assigns it to a variable named max_list.

::

    min_list = data["daily"]["temperature_2m_min"]

This extracts the list of minimum temperatures from the data dictionary and assigns it to a variable named min_list.

::

    xAxis = dates_list

This assigns the dates_list to a variable named xAxis, which will be used as the x-axis of the plot.

::

    tmax = max_list

This assigns the max_list to a variable named tmax, which will be used as one of the y-axis values of the plot.

::

    tmin = min_list

This assigns the min_list to a variable named tmin, which will be used as another y-axis value of the plot.

::

    plt.grid(True)

This enables a grid on the plot using the plt.grid function with True as an argument.

::

    plt.xlabel('Date')

This sets the label of the x-axis to 'Date' using the plt.xlabel function.

::

    plt.ylabel('Temperature (\N{DEGREE SIGN}C)')

This sets the label of the y-axis to 'Temperature (°C)' using the plt.ylabel function. The \N{DEGREE SIGN} is a Unicode escape sequence for the degree symbol.

::

    plt.title(title)

This sets the title of the plot to the value of title using the plt.title function.

::

    ## plot lines##

This is a comment that indicates that the next two lines are for plotting lines on the graph.

::

    plt.plot(xAxis, tmax, color='red', marker='o', label = "Max Temp")

This plots a line with xAxis as x-values and tmax as y-values using
the plt.plot function. It also specifies some attributes for
the line, such as color='red', marker='o', and label="Max Temp".

::

    plt.plot(xAxis, tmin, color='blue', marker='x', label = "Min Temp")

This plots another line with xAxis as x-values and tmin as y-values using
the plt.plot function. It also specifies some attributes for
the line, such as color='blue', marker='x', and label="Min Temp".

::

    plt.ylim(bottom=0)

This sets the lower limit of
the y-axis to 0 using
the plt.ylim function with bottom=0 as an argument.

::

    plt.gcf().autofmt_xdate()

This gets
the current figure using
the plt.gcf function and then calls
the autofmt_xdate method on it. This method automatically formats
the x-axis labels so that they are angled to fit better on
the plot.

::

    plt.legend()

This adds
a legend to
the plot using
the plt.legend function. The legend will show
the labels of
the lines that were specified earlier in
the plt.plot functions.

::

    currfile_dir = Path(__file__).parent

This creates
a Path object from
the __file__ variable, which is
a special variable that holds
the name of
the current file, and then gets
the parent attribute of
the Path object. This returns
a Path object that represents
the directory of
the current file. This is assigned to
a variable named currfile_dir.

::

    filename = title.replace(" ", "_")

This replaces
all the spaces in
the title with underscores using
the replace method of
the title string and assigns it to
a variable named filename. This will be used as
the name of
the file where
the plot will be saved.

::

    filepath = currfile_dir / (f"{filename}.png")

This creates
a Path object by joining
the currfile_dir and the filename using
the / operator, which is overloaded for Path objects. The filename is formatted as a string with the .png extension using f-strings. This Path object represents the full path of the file where the plot will be saved and is assigned to a variable named filepath.

::

    plt.savefig(filepath, dpi=600)

This saves the plot as an image file using the plt.savefig function with filepath as the first argument and dpi=600 as the second argument. The dpi argument specifies the resolution of the image in dots per inch.

::

    plt.show()

This displays the plot on the screen using the plt.show function.


::

    def main():

This defines a function named main that will be executed when the script runs.

::

    url = "https://api.open-meteo.com/v1/forecast?latitude=-37.81&longitude=144.96&daily=temperature_2m_max,temperature_2m_min&timezone=Australia%2FSydney"

This assigns a string that contains the URL of an API that provides weather data for Melbourne to a variable named url.

::

    title = "Melb Temp forecast Jul 2023"

This assigns a string that contains the title of the plot to a variable named title.

::

    plot_weather(title, url)

This calls the plot_weather function with title and url as arguments.


::

    if __name__ == '__main__':

This checks if the __name__ variable, which is another special variable that holds the name of the current module, is equal to '__main__'. This means that the script is being run directly and not imported by another module.

::

    main()

This calls the main function if the previous condition is true.
