import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=["Dist_norm"])
st.write(data.head())

fig, ax = plt.subplot()
n_bins = st.number_input(
    Lable = "Choisir le nombre de bins",
    min_value=10,
    max_value=100,
    value=30
)
ax.hist(data.Dist_norm,bins=n_bins)
graph_title = st.text_input(
    label = "Titre du graphique",
    )
plt.title(graph_title)
st.pyplot(fig)
