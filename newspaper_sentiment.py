"""
This package is designed to track the sentiment of a newspaper on a given topic over time.

It will be pretty crude, but hopefully sufficient to resolve the argument that inspired this.
"""

# imports
import re, numpy as np, numpy.linalg as nplin, string, operator, bs4, matplotlib.pyplot as plt, scipy.stats as spstat, requests
from senti_classifier import senti_classifier
from future import __division__


