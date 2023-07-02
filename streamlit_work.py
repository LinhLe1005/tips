import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import datetime

with st.sidebar:
    st.markdown("Author: **:blue[Tan Do]**")
    st.write("Date: ", datetime.date(2023, 7, 3))
    st.text("Description: This serves as an illustration \n for an Interactive Web Application \n for Python Project 2.")

st.title("Tips")
st.markdown("We analyze the :blue[tips] data set available in the plotly.express package.")

st.divider()

df = px.data.tips()

st.header("Original data set")
st.text("The first 10 rows of the data set is displayed below.")
st.write(df.head(10))

st.header("Tip versus total bill")
st.text("We explore the relation between the amount of tip and the total bill.")

tab1, tab2 = st.tabs(["General scatter plot", "Counts"])
with tab1:
    col1, col2 = st.columns([1,3])
    with col1:
        by_what = st.radio(
            "Choose a category:",
            ('sex', 'smoker', 'day', 'time', 'size'),
            key = "r1")
    with col2:
        fig1 = px.scatter(df, x = "total_bill", y = "tip", color = by_what,
                  labels={"total_bill": "total bill"},
                  size = "tip", title = "Amount of tip versus total bill")
        st.plotly_chart(fig1, theme = "streamlit", use_container_width=True)
with tab2:
    by_what_2 = st.radio(
            "Choose a category:",
            ('sex', 'smoker', 'day', 'time', 'size'),
            horizontal = True,
            key = "r2")
    
    tbr = st.slider("Choose a range for total bill:", 
                    df['total_bill'].min(), df['total_bill'].max(), (25.0, 45.0)
                    )
    st.write("Total bill range:", tbr)

    dff = df[(df['total_bill'] >= tbr[0]) & (df['total_bill'] <= tbr[1])]
    df2 = pd.crosstab(index=dff[by_what_2], columns="count")
    df3 = pd.crosstab(index=dff[by_what_2], columns="percentage", normalize=True) * 100
    df3a = df3.apply(lambda x: round(x,1))
    df3b = df3a.astype(str).apply(lambda x: x + '%')

    col1, col2 = st.columns(2)
    with col1:
        fig2 = px.bar(df2, x = df2.index, y = "count", text_auto = True, title = "In frequency")
        st.plotly_chart(fig2, theme=None, use_container_width=True)
    with col2:
        #fig3 = px.bar(df3, x = df3.index, y = "percentage", text = df3b["percentage"])
        fig3 = px.pie(df2, values = "count", names = df2.index, hole = 0.4, title = "In percentage")
        st.plotly_chart(fig3, theme=None, use_container_width=True)
    
    
