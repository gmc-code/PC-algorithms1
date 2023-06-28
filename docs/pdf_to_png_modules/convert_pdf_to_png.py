"""
Paste in a pdf file path to convert the pdf to a png @GMC 2023
"""
import pathlib
import magick_pdf_to_png
import wand_pdf_to_png

# pdf_file_path = input("Enter a windows full file path to a pdf: ")

# a raw r string is used since backslashes are normally escape characters
# paste in windows pdf full file path
pasted_pdf_file_path = r"C:\PC_RTD_GITHUB\PC-algorithms\docs\maths_python\files\flow_chart_add_fractions.pdf"

# get file path object
pdf_file_path = pathlib.PureWindowsPath(pasted_pdf_file_path)
# use magick or wand -- comment or uncomment to choose
magick_pdf_to_png.pdf_to_png(pdf_file_path)
# wand_pdf_to_png.pdf_to_png(pdf_file_path)
