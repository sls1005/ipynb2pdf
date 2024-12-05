#!/usr/bin/env python
# -*- coding: ASCII -*-
# Python 3 is recommended for interpreting this.
import pdfkit
import atexit
import socket
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

def am_online():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('8.8.8.8', 443))
    except OSError:
        return False
    except:
        return False
    finally:
        s.close()
    return True

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

if am_online():
    if input("[!] You seem to be online rather than offline. Are you sure to continue? [y/N]") not in ('Y', 'y'):
        print("Exiting...")
        exit(1)

atexit.register(callback)

html, _ = HTMLExporter().from_filename(input_file_name)
print("Writing to '%s'..." % output_file_name)
pdfkit.from_string(html, output_file_name)
