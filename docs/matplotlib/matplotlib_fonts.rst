====================================================
Matplotlib fonts
====================================================

| Matplotlib available fonts can be viewed via the python script below.


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

----

Fonts
-------

.. raw:: html

    <p>
    <span style='font-family:Adobe Devanagari; font-size: 24px;'>Adobe Devanagari</span>--
    <span style='font-family:Agency FB; font-size: 24px;'>Agency FB</span>--
    <span style='font-family:Algerian; font-size: 24px;'>Algerian</span>--
    <span style='font-family:Arial; font-size: 24px;'>Arial</span>--
    <span style='font-family:Arial Rounded MT Bold; font-size: 24px;'>Arial Rounded MT Bold</span>--
    <span style='font-family:Bahnschrift; font-size: 24px;'>Bahnschrift</span>--
    <span style='font-family:Baskerville Old Face; font-size: 24px;'>Baskerville Old Face</span>--
    <span style='font-family:Bauhaus 93; font-size: 24px;'>Bauhaus 93</span>--
    <span style='font-family:Bell MT; font-size: 24px;'>Bell MT</span>--
    <span style='font-family:Berlin Sans FB; font-size: 24px;'>Berlin Sans FB</span>--
    <span style='font-family:Berlin Sans FB Demi; font-size: 24px;'>Berlin Sans FB Demi</span>--
    <span style='font-family:Bernard MT Condensed; font-size: 24px;'>Bernard MT Condensed</span>--
    <span style='font-family:Blackadder ITC; font-size: 24px;'>Blackadder ITC</span>--
    <span style='font-family:Bodoni MT; font-size: 24px;'>Bodoni MT</span>--
    <span style='font-family:Book Antiqua; font-size: 24px;'>Book Antiqua</span>--
    <span style='font-family:Bookman Old Style; font-size: 24px;'>Bookman Old Style</span>--
    <span style='font-family:Bookshelf Symbol 7; font-size: 24px;'>Bookshelf Symbol 7</span>--
    <span style='font-family:Bradley Hand ITC; font-size: 24px;'>Bradley Hand ITC</span>--
    <span style='font-family:Britannic Bold; font-size: 24px;'>Britannic Bold</span>--
    <span style='font-family:Broadway; font-size: 24px;'>Broadway</span>--
    <span style='font-family:Brush Script MT; font-size: 24px;'>Brush Script MT</span>--
    <span style='font-family:Calibri; font-size: 24px;'>Calibri</span>--
    <span style='font-family:Californian FB; font-size: 24px;'>Californian FB</span>--
    <span style='font-family:Calisto MT; font-size: 24px;'>Calisto MT</span>--
    <span style='font-family:Cambria; font-size: 24px;'>Cambria</span>--
    <span style='font-family:Candara; font-size: 24px;'>Candara</span>--
    <span style='font-family:Castellar; font-size: 24px;'>Castellar</span>--
    <span style='font-family:Centaur; font-size: 24px;'>Centaur</span>--
    <span style='font-family:Century; font-size: 24px;'>Century</span>--
    <span style='font-family:Century Gothic; font-size: 24px;'>Century Gothic</span>--
    <span style='font-family:Century Schoolbook; font-size: 24px;'>Century Schoolbook</span>--
    <span style='font-family:Chiller; font-size: 24px;'>Chiller</span>--
    <span style='font-family:Colonna MT; font-size: 24px;'>Colonna MT</span>--
    <span style='font-family:Comic Sans MS; font-size: 24px;'>Comic Sans MS</span>--
    <span style='font-family:Consolas; font-size: 24px;'>Consolas</span>--
    <span style='font-family:Constantia; font-size: 24px;'>Constantia</span>--
    <span style='font-family:Cooper Black; font-size: 24px;'>Cooper Black</span>--
    <span style='font-family:Copperplate Gothic Bold; font-size: 24px;'>Copperplate Gothic Bold</span>--
    <span style='font-family:Copperplate Gothic Light; font-size: 24px;'>Copperplate Gothic Light</span>--
    <span style='font-family:Corbel; font-size: 24px;'>Corbel</span>--
    <span style='font-family:Courier New; font-size: 24px;'>Courier New</span>--
    <span style='font-family:Curlz MT; font-size: 24px;'>Curlz MT</span>--
    <span style='font-family:DejaVu Sans; font-size: 24px;'>DejaVu Sans</span>--
    <span style='font-family:DejaVu Sans Display; font-size: 24px;'>DejaVu Sans Display</span>--
    <span style='font-family:DejaVu Sans Mono; font-size: 24px;'>DejaVu Sans Mono</span>--
    <span style='font-family:DejaVu Serif; font-size: 24px;'>DejaVu Serif</span>--
    <span style='font-family:DejaVu Serif Display; font-size: 24px;'>DejaVu Serif Display</span>--
    <span style='font-family:Dubai; font-size: 24px;'>Dubai</span>--
    <span style='font-family:Ebrima; font-size: 24px;'>Ebrima</span>--
    <span style='font-family:Edwardian Script ITC; font-size: 24px;'>Edwardian Script ITC</span>--
    <span style='font-family:Elephant; font-size: 24px;'>Elephant</span>--
    <span style='font-family:Engravers MT; font-size: 24px;'>Engravers MT</span>--
    <span style='font-family:Eras Bold ITC; font-size: 24px;'>Eras Bold ITC</span>--
    <span style='font-family:Eras Demi ITC; font-size: 24px;'>Eras Demi ITC</span>--
    <span style='font-family:Eras Light ITC; font-size: 24px;'>Eras Light ITC</span>--
    <span style='font-family:Eras Medium ITC; font-size: 24px;'>Eras Medium ITC</span>--
    <span style='font-family:Felix Titling; font-size: 24px;'>Felix Titling</span>--
    <span style='font-family:Footlight MT Light; font-size: 24px;'>Footlight MT Light</span>--
    <span style='font-family:Forte; font-size: 24px;'>Forte</span>--
    <span style='font-family:Franklin Gothic Book; font-size: 24px;'>Franklin Gothic Book</span>--
    <span style='font-family:Franklin Gothic Demi; font-size: 24px;'>Franklin Gothic Demi</span>--
    <span style='font-family:Franklin Gothic Demi Cond; font-size: 24px;'>Franklin Gothic Demi Cond</span>--
    <span style='font-family:Franklin Gothic Heavy; font-size: 24px;'>Franklin Gothic Heavy</span>--
    <span style='font-family:Franklin Gothic Medium; font-size: 24px;'>Franklin Gothic Medium</span>--
    <span style='font-family:Franklin Gothic Medium Cond; font-size: 24px;'>Franklin Gothic Medium Cond</span>--
    <span style='font-family:Freestyle Script; font-size: 24px;'>Freestyle Script</span>--
    <span style='font-family:French Script MT; font-size: 24px;'>French Script MT</span>--
    <span style='font-family:Gabriola; font-size: 24px;'>Gabriola</span>--
    <span style='font-family:Gadugi; font-size: 24px;'>Gadugi</span>--
    <span style='font-family:Garamond; font-size: 24px;'>Garamond</span>--
    <span style='font-family:Georgia; font-size: 24px;'>Georgia</span>--
    <span style='font-family:Gigi; font-size: 24px;'>Gigi</span>--
    <span style='font-family:Gill Sans MT; font-size: 24px;'>Gill Sans MT</span>--
    <span style='font-family:Gill Sans MT Condensed; font-size: 24px;'>Gill Sans MT Condensed</span>--
    <span style='font-family:Gill Sans MT Ext Condensed Bold; font-size: 24px;'>Gill Sans MT Ext Condensed Bold</span>--
    <span style='font-family:Gill Sans Ultra Bold; font-size: 24px;'>Gill Sans Ultra Bold</span>--
    <span style='font-family:Gill Sans Ultra Bold Condensed; font-size: 24px;'>Gill Sans Ultra Bold Condensed</span>--
    <span style='font-family:Gloucester MT Extra Condensed; font-size: 24px;'>Gloucester MT Extra Condensed</span>--
    <span style='font-family:Goudy Old Style; font-size: 24px;'>Goudy Old Style</span>--
    <span style='font-family:Goudy Stout; font-size: 24px;'>Goudy Stout</span>--
    <span style='font-family:HGGothicE; font-size: 24px;'>HGGothicE</span>--
    <span style='font-family:HGGothicM; font-size: 24px;'>HGGothicM</span>--
    <span style='font-family:HGGyoshotai; font-size: 24px;'>HGGyoshotai</span>--
    <span style='font-family:HGKyokashotai; font-size: 24px;'>HGKyokashotai</span>--
    <span style='font-family:HGMaruGothicMPRO; font-size: 24px;'>HGMaruGothicMPRO</span>--
    <span style='font-family:HGMinchoB; font-size: 24px;'>HGMinchoB</span>--
    <span style='font-family:HGMinchoE; font-size: 24px;'>HGMinchoE</span>--
    <span style='font-family:HGSeikaishotaiPRO; font-size: 24px;'>HGSeikaishotaiPRO</span>--
    <span style='font-family:HGSoeiKakugothicUB; font-size: 24px;'>HGSoeiKakugothicUB</span>--
    <span style='font-family:HGSoeiKakupoptai; font-size: 24px;'>HGSoeiKakupoptai</span>--
    <span style='font-family:HGSoeiPresenceEB; font-size: 24px;'>HGSoeiPresenceEB</span>--
    <span style='font-family:Haettenschweiler; font-size: 24px;'>Haettenschweiler</span>--
    <span style='font-family:Harlow Solid Italic; font-size: 24px;'>Harlow Solid Italic</span>--
    <span style='font-family:Harrington; font-size: 24px;'>Harrington</span>--
    <span style='font-family:High Tower Text; font-size: 24px;'>High Tower Text</span>--
    <span style='font-family:HoloLens MDL2 Assets; font-size: 24px;'>HoloLens MDL2 Assets</span>--
    <span style='font-family:Impact; font-size: 24px;'>Impact</span>--
    <span style='font-family:Imprint MT Shadow; font-size: 24px;'>Imprint MT Shadow</span>--
    <span style='font-family:Informal Roman; font-size: 24px;'>Informal Roman</span>--
    <span style='font-family:Ink Free; font-size: 24px;'>Ink Free</span>--
    <span style='font-family:Javanese Text; font-size: 24px;'>Javanese Text</span>--
    <span style='font-family:Jokerman; font-size: 24px;'>Jokerman</span>--
    <span style='font-family:Juice ITC; font-size: 24px;'>Juice ITC</span>--
    <span style='font-family:Kristen ITC; font-size: 24px;'>Kristen ITC</span>--
    <span style='font-family:Kunstler Script; font-size: 24px;'>Kunstler Script</span>--
    <span style='font-family:Leelawadee; font-size: 24px;'>Leelawadee</span>--
    <span style='font-family:Leelawadee UI; font-size: 24px;'>Leelawadee UI</span>--
    <span style='font-family:Lucida Bright; font-size: 24px;'>Lucida Bright</span>--
    <span style='font-family:Lucida Calligraphy; font-size: 24px;'>Lucida Calligraphy</span>--
    <span style='font-family:Lucida Console; font-size: 24px;'>Lucida Console</span>--
    <span style='font-family:Lucida Fax; font-size: 24px;'>Lucida Fax</span>--
    <span style='font-family:Lucida Handwriting; font-size: 24px;'>Lucida Handwriting</span>--
    <span style='font-family:Lucida Sans; font-size: 24px;'>Lucida Sans</span>--
    <span style='font-family:Lucida Sans Typewriter; font-size: 24px;'>Lucida Sans Typewriter</span>--
    <span style='font-family:Lucida Sans Unicode; font-size: 24px;'>Lucida Sans Unicode</span>--
    <span style='font-family:MS Gothic; font-size: 24px;'>MS Gothic</span>--
    <span style='font-family:MS Outlook; font-size: 24px;'>MS Outlook</span>--
    <span style='font-family:MS Reference Sans Serif; font-size: 24px;'>MS Reference Sans Serif</span>--
    <span style='font-family:MS Reference Specialty; font-size: 24px;'>MS Reference Specialty</span>--
    <span style='font-family:MT Extra; font-size: 24px;'>MT Extra</span>--
    <span style='font-family:MV Boli; font-size: 24px;'>MV Boli</span>--
    <span style='font-family:Magneto; font-size: 24px;'>Magneto</span>--
    <span style='font-family:Maiandra GD; font-size: 24px;'>Maiandra GD</span>--
    <span style='font-family:Malgun Gothic; font-size: 24px;'>Malgun Gothic</span>--
    <span style='font-family:Marlett; font-size: 24px;'>Marlett</span>--
    <span style='font-family:Matura MT Script Capitals; font-size: 24px;'>Matura MT Script Capitals</span>--
    <span style='font-family:Microsoft Himalaya; font-size: 24px;'>Microsoft Himalaya</span>--
    <span style='font-family:Microsoft JhengHei; font-size: 24px;'>Microsoft JhengHei</span>--
    <span style='font-family:Microsoft New Tai Lue; font-size: 24px;'>Microsoft New Tai Lue</span>--
    <span style='font-family:Microsoft PhagsPa; font-size: 24px;'>Microsoft PhagsPa</span>--
    <span style='font-family:Microsoft Sans Serif; font-size: 24px;'>Microsoft Sans Serif</span>--
    <span style='font-family:Microsoft Tai Le; font-size: 24px;'>Microsoft Tai Le</span>--
    <span style='font-family:Microsoft Uighur; font-size: 24px;'>Microsoft Uighur</span>--
    <span style='font-family:Microsoft YaHei; font-size: 24px;'>Microsoft YaHei</span>--
    <span style='font-family:Microsoft Yi Baiti; font-size: 24px;'>Microsoft Yi Baiti</span>--
    <span style='font-family:MingLiU-ExtB; font-size: 24px;'>MingLiU-ExtB</span>--
    <span style='font-family:Mistral; font-size: 24px;'>Mistral</span>--
    <span style='font-family:Modern No. 20; font-size: 24px;'>Modern No. 20</span>--
    <span style='font-family:Mongolian Baiti; font-size: 24px;'>Mongolian Baiti</span>--
    <span style='font-family:Monotype Corsiva; font-size: 24px;'>Monotype Corsiva</span>--
    <span style='font-family:Myanmar Text; font-size: 24px;'>Myanmar Text</span>--
    <span style='font-family:Niagara Engraved; font-size: 24px;'>Niagara Engraved</span>--
    <span style='font-family:Niagara Solid; font-size: 24px;'>Niagara Solid</span>--
    <span style='font-family:Nirmala UI; font-size: 24px;'>Nirmala UI</span>--
    <span style='font-family:OCR A Extended; font-size: 24px;'>OCR A Extended</span>--
    <span style='font-family:OCRB; font-size: 24px;'>OCRB</span>--
    <span style='font-family:Old English Text MT; font-size: 24px;'>Old English Text MT</span>--
    <span style='font-family:Onyx; font-size: 24px;'>Onyx</span>--
    <span style='font-family:Palace Script MT; font-size: 24px;'>Palace Script MT</span>--
    <span style='font-family:Palatino Linotype; font-size: 24px;'>Palatino Linotype</span>--
    <span style='font-family:Papyrus; font-size: 24px;'>Papyrus</span>--
    <span style='font-family:Parchment; font-size: 24px;'>Parchment</span>--
    <span style='font-family:Perpetua; font-size: 24px;'>Perpetua</span>--
    <span style='font-family:Perpetua Titling MT; font-size: 24px;'>Perpetua Titling MT</span>--
    <span style='font-family:Playbill; font-size: 24px;'>Playbill</span>--
    <span style='font-family:Poor Richard; font-size: 24px;'>Poor Richard</span>--
    <span style='font-family:Pristina; font-size: 24px;'>Pristina</span>--
    <span style='font-family:Rage Italic; font-size: 24px;'>Rage Italic</span>--
    <span style='font-family:Ravie; font-size: 24px;'>Ravie</span>--
    <span style='font-family:Roboto; font-size: 24px;'>Roboto</span>--
    <span style='font-family:Rockwell; font-size: 24px;'>Rockwell</span>--
    <span style='font-family:Rockwell Condensed; font-size: 24px;'>Rockwell Condensed</span>--
    <span style='font-family:Rockwell Extra Bold; font-size: 24px;'>Rockwell Extra Bold</span>--
    <span style='font-family:STIXGeneral; font-size: 24px;'>STIXGeneral</span>--
    <span style='font-family:STIXNonUnicode; font-size: 24px;'>STIXNonUnicode</span>--
    <span style='font-family:STIXSizeFiveSym; font-size: 24px;'>STIXSizeFiveSym</span>--
    <span style='font-family:STIXSizeFourSym; font-size: 24px;'>STIXSizeFourSym</span>--
    <span style='font-family:STIXSizeOneSym; font-size: 24px;'>STIXSizeOneSym</span>--
    <span style='font-family:STIXSizeThreeSym; font-size: 24px;'>STIXSizeThreeSym</span>--
    <span style='font-family:STIXSizeTwoSym; font-size: 24px;'>STIXSizeTwoSym</span>--
    <span style='font-family:Script MT Bold; font-size: 24px;'>Script MT Bold</span>--
    <span style='font-family:Segoe MDL2 Assets; font-size: 24px;'>Segoe MDL2 Assets</span>--
    <span style='font-family:Segoe Print; font-size: 24px;'>Segoe Print</span>--
    <span style='font-family:Segoe Script; font-size: 24px;'>Segoe Script</span>--
    <span style='font-family:Segoe UI; font-size: 24px;'>Segoe UI</span>--
    <span style='font-family:Segoe UI Emoji; font-size: 24px;'>Segoe UI Emoji</span>--
    <span style='font-family:Segoe UI Historic; font-size: 24px;'>Segoe UI Historic</span>--
    <span style='font-family:Segoe UI Symbol; font-size: 24px;'>Segoe UI Symbol</span>--
    <span style='font-family:Showcard Gothic; font-size: 24px;'>Showcard Gothic</span>--
    <span style='font-family:SimSun; font-size: 24px;'>SimSun</span>--
    <span style='font-family:SimSun-ExtB; font-size: 24px;'>SimSun-ExtB</span>--
    <span style='font-family:Sitka Small; font-size: 24px;'>Sitka Small</span>--
    <span style='font-family:Snap ITC; font-size: 24px;'>Snap ITC</span>--
    <span style='font-family:Stencil; font-size: 24px;'>Stencil</span>--
    <span style='font-family:Sylfaen; font-size: 24px;'>Sylfaen</span>--
    <span style='font-family:Symbol; font-size: 24px;'>Symbol</span>--
    <span style='font-family:Tahoma; font-size: 24px;'>Tahoma</span>--
    <span style='font-family:Tempus Sans ITC; font-size: 24px;'>Tempus Sans ITC</span>--
    <span style='font-family:Times New Roman; font-size: 24px;'>Times New Roman</span>--
    <span style='font-family:Trebuchet MS; font-size: 24px;'>Trebuchet MS</span>--
    <span style='font-family:Tw Cen MT; font-size: 24px;'>Tw Cen MT</span>--
    <span style='font-family:Tw Cen MT Condensed; font-size: 24px;'>Tw Cen MT Condensed</span>--
    <span style='font-family:Tw Cen MT Condensed Extra Bold; font-size: 24px;'>Tw Cen MT Condensed Extra Bold</span>--
    <span style='font-family:Verdana; font-size: 24px;'>Verdana</span>--
    <span style='font-family:Viner Hand ITC; font-size: 24px;'>Viner Hand ITC</span>--
    <span style='font-family:Vivaldi; font-size: 24px;'>Vivaldi</span>--
    <span style='font-family:Vladimir Script; font-size: 24px;'>Vladimir Script</span>--
    <span style='font-family:Webdings; font-size: 24px;'>Webdings</span>--
    <span style='font-family:Wide Latin; font-size: 24px;'>Wide Latin</span>--
    <span style='font-family:Wingdings; font-size: 24px;'>Wingdings</span>--
    <span style='font-family:Wingdings 2; font-size: 24px;'>Wingdings 2</span>--
    <span style='font-family:Wingdings 3; font-size: 24px;'>Wingdings 3</span>--
    <span style='font-family:Yu Gothic; font-size: 24px;'>Yu Gothic</span>--
    <span style='font-family:Yu Mincho; font-size: 24px;'>Yu Mincho</span>--
    <span style='font-family:ZWAdobeF; font-size: 24px;'>ZWAdobeF</span>--
    <span style='font-family:cmb10; font-size: 24px;'>cmb10</span>--
    <span style='font-family:cmex10; font-size: 24px;'>cmex10</span>--
    <span style='font-family:cmmi10; font-size: 24px;'>cmmi10</span>--
    <span style='font-family:cmr10; font-size: 24px;'>cmr10</span>--
    <span style='font-family:cmss10; font-size: 24px;'>cmss10</span>--
    <span style='font-family:cmsy10; font-size: 24px;'>cmsy10</span>--
    <span style='font-family:cmtt10; font-size: 24px;'>cmtt10</span>
    </p>


