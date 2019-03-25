import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://www.ibbi.gov.in/orders/nclt"
html = urlopen(url)

print(html)