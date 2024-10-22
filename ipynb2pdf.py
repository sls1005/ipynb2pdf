#!/usr/bin/env python
# -*- coding: ASCII -*-
# Python 3 is recommended for interpreting this.
import pdfkit
import atexit
from nbconvert import HTMLExporter
from sys import argv
from os.path import exists

usage = "Usage: ipynb2pdf.py <file>"
input_file_name = ''
output_file_name = ''

def callback():
    if output_file_name != '':
        if exists(output_file_name):
            print("'%s' generated!\n" % output_file_name)

if len(argv) == 1:
    exit(usage)

for a in argv[1:]:
    if a in ('-h', '--help'):
        exit(usage)
    else:
        input_file_name = a

if input_file_name.endswith('.ipynb'):
    i = input_file_name.index('.ipynb')
    output_file_name = input_file_name[:i] + '.pdf'
else:
    output_file_name = input_file_name + '.pdf'

if exists(output_file_name):
    exit("[Error] '%s' already exists." % output_file_name)
elif not exists(input_file_name):
    exit("[Error] '%s' doesn't exist." % input_file_name)

atexit.register(callback)

html, _ = HTMLExporter().from_filename(input_file_name)
print("Writing to '%s'..." % output_file_name)
pdfkit.from_string(html, output_file_name)
