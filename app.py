import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI Dashboard")

df = pd.read_csv("netflix_titles.csv")


st.header("Dataset Overview")
st.write(df.head())

# Data Cleaning
st.header("Data Cleaning")
st.write(df.isnull().sum())


st.header("Key Metrics")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Rows", df.shape[0])

with col2:
    st.metric("Total Columns", df.shape[1])



st.sidebar.header("Filters")

content_type = st.sidebar.selectbox(
    "Select Type",
    df["type"].dropna().unique()
)

filtered_df = df[df["type"] == content_type]

st.header("Filtered Data")
st.dataframe(filtered_df.head())
...
st.header("Filtered Data")
st.dataframe(filtered_df.head())



st.header("Movies vs TV Shows")

fig1 = px.pie(
    df,
    names="type",
    title="Content Distribution"
)

st.plotly_chart(fig1)

st.header("Content Released by Year")

fig2 = px.histogram(
    df,
    x="release_year",
    title="Content Released by Year"
)

st.plotly_chart(fig2)
st.header("Ratings Distribution")

rating_count = df["rating"].value_counts().reset_index()
rating_count.columns = ["rating", "count"]

fig3 = px.bar(
    rating_count,
    x="rating",
    y="count",
    title="Ratings Distribution"
)

st.plotly_chart(fig3)
st.header("Top 10 Countries")

country_count = df["country"].value_counts().head(10).reset_index()
country_count.columns = ["country", "count"]

fig4 = px.bar(
    country_count,
    x="country",
    y="count",
    title="Top 10 Countries"
)

st.plotly_chart(fig4)
st.header("Content Added by Year")

year_count = df["release_year"].value_counts().reset_index()
year_count.columns = ["year", "count"]

fig5 = px.line(
    year_count,
    x="year",
    y="count",
    title="Content Trend"
)

st.plotly_chart(fig5)
st.header("Key Insights")

st.write("""
• Movies are more common than TV Shows.
• Most content was released after 2015.
• Some countries contribute significantly more content.
• Netflix content grew rapidly in recent years.
""")