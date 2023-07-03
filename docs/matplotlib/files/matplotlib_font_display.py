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
