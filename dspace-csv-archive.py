#!/usr/bin/python3

import os, sys

from dspacearchive import DspaceArchive

from zipcompressor import ZipCompressor

if len(sys.argv) == 2 and '--help' in sys.argv:
	print("\n")
	print("  -z    creara un archivo zip desde la carpeta output al finalizar")
	print("\n")
	sys.exit()

if len(sys.argv) > 3:
	print("Usa: ./dspace-csv-archive.py /path/to/input/file.csv [--option]\n")
	print(" --help    Para informacion de los comandos\n")
	sys.exit()

input_file = sys.argv[1]
input_base_path = os.path.dirname(input_file)

archive = DspaceArchive(input_file)
archive.write("./output")

if '-z' in sys.argv:
	ZipCompressor()
