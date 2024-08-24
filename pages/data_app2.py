import numpy as np
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
import scipy as sp
import statsmodels.api as sm
import matplotlib.pyplot as plt

def page2():
    st.title("Further analysis")
    st.write("This will show results of regressions and other key data test")