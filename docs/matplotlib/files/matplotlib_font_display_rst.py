import matplotlib.font_manager as mfm


def make_rst(fontname):
    return f".. raw:: html\n\n    <p style='font-family:{fontname}; font-size: 24px;'>{fontname}</p>\n"


code = "".join([make_rst(font) for font in sorted(set([f.name for f in mfm.fontManager.ttflist]))])

# Save the generated RST to a file
with open('fonts.rst', 'w') as f:
    f.write(code)
