"""
some file operations. 
"""
import os
import sys

path = os.getcwd()  # path

def read_text(path:str, mode="r", is_print=False, size=None):
	with open(path, mode) as f:
		if size == None:
			result = f.read()
		else:
			result = f.read(size)
		
		if is_print:
			print(result)
