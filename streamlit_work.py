import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import numpy as np


st.title("Tips")

df = px.data.tips()
df2 = pd.crosstab(index=df["sex"], columns="count")
df3 = pd.crosstab(index=df["sex"], columns="percentage", normalize=True, margins = True, margins_name= "Total") * 100
df3a = df3.apply(lambda x: round(x,1))
df3b = df3a.astype(str).apply(lambda x: x + '%')


st.write(df3a.head())


fig1 = px.scatter(df, x = "total_bill", y = "tip", color = "smoker", hover_name="sex", size = "tip")
fig2 = px.bar(df2, x = df2.index, y = "count", text_auto = True)
fig3 = px.bar(df3, x = df3.index, y = "percentage", text = df3b["percentage"])

tab1, tab2 = st.tabs(["scatter", "bar"])
with tab1:
    st.plotly_chart(fig1, theme = "streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig2, theme=None, use_container_width=True)
    st.plotly_chart(fig3, theme=None, use_container_width=True)
