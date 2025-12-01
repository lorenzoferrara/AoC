import numpy as np
import pandas as pd
import re
import copy
import time
from typing import List, Tuple

# type = "input"
type='example'
# type='example_1'

with open(type + ".txt", "r") as file:
    lines = file.readlines()

print(lines)
