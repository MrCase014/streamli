import streamlit as st
import pandas as pd
import numpy as np


data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=["Dist_nom"])