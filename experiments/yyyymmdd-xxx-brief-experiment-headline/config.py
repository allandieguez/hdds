import os
import sys


# Directory

## Root
ROOT_DIR = os.path.abspath(os.path.join(os.path.abspath(os.path.curdir), '..', '..'))

## Base
DATA_DIR = os.path.join(ROOT_DIR, 'data')
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')
EXPT_DIR = os.path.join(ROOT_DIR, 'experiments')
SOURCE_DIR = os.path.join(ROOT_DIR, 'src')

# Enable Local Sources 
if SOURCE_DIR not in sys.path:
    sys.path.append(SOURCE_DIR)
