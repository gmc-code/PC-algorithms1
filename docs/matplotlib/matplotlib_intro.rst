====================================================
Matplotlib basics
====================================================

| Matplotlib is a python library for creating static, animated, and interactive visualizations in Python.

----

Basic plots
---------------

.. code-block:: python

    x = list(range(0,6))
    y = list(range(0,12,2))

    # Resize your Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
    plt.figure(figsize=(8,5), dpi=100)

    # Line 1

    # Keyword Argument Notation
    #plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

    # Shorthand notation
    # fmt = '[color][marker][line]'
    plt.plot(x,y, 'b^--', label='2x')

    ## Line 2

    # select interval we want to plot points at
    x2 = np.arange(0,4.5,0.5)

    # Plot part of the graph as line
    plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')

    # Plot remainder of graph as a dot
    plt.plot(x2[5:], x2[5:]**2, 'r--')

    # Add a title (specify font parameters with fontdict)
    plt.title('Lines Graph!', fontdict={'fontname': 'Arial', 'fontsize': 24})

    # X and Y labels
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # X, Y axis Tickmarks (scale of your graph)
    plt.xticks([0,1,2,3,4,])
    #plt.yticks([0,2,4,6,8,10])

    # Add a legend
    plt.legend()

    # Save figure (dpi 300 is good when saving so graph has high resolution)
    plt.savefig('mygraph.png', dpi=300)

    # Show plot
    plt.show()