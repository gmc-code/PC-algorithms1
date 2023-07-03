====================================================
Matplotlib fonts
====================================================

| Matplotlib availbale fonts can be viewed via hte python script below.

.. raw:: html

    <p style='font-family:Adobe Devanagari; font-size: 24px;'>Adobe Devanagari</p>
.. raw:: html

    <p style='font-family:Agency FB; font-size: 24px;'>Agency FB</p>
.. raw:: html

    <p style='font-family:Algerian; font-size: 24px;'>Algerian</p>
.. raw:: html

    <p style='font-family:Arial; font-size: 24px;'>Arial</p>
.. raw:: html

    <p style='font-family:Arial Rounded MT Bold; font-size: 24px;'>Arial Rounded MT Bold</p>
.. raw:: html

    <p style='font-family:Bahnschrift; font-size: 24px;'>Bahnschrift</p>
.. raw:: html

    
.. code-block:: python

    import matplotlib.font_manager
    import webbrowser

    def make_html(fontname):
        return "<p>{font}: <span style='font-family:{font}; font-size: 24px;'>{font}</p>".format(font=fontname)

    code = "\n".join([make_html(font) for font in sorted(set([f.name for f in matplotlib.font_manager.fontManager.ttflist]))])

    # Save the generated HTML to a file
    with open('fonts.html', 'w') as f:
        f.write("<div style='column-count: 2;'>{}</div>".format(code))

    # Open the saved HTML file in the default web browser
    webbrowser.open('fonts.html')
