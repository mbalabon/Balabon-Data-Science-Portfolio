#Import tools

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("★ Spotify Track Analysis")
st.write("This app analyzes a Spotify tracks dataset from Kaggle.")

st.subheader("★ Exploring the Spotify Dataset")

# Load Spotify CSV file
df = pd.read_csv("basic_streamlit_app/data/spotify_dataset.csv")

st.write("Here's the data:")
st.dataframe(df)

st.write("Dataset shape (rows, columns):", df.shape)
st.write("Column types:")
st.write(df.dtypes)

#Filter Spotify Tracks
st.subheader("★ Filtering the Spotify Dataset")

#Filter Spotify Tracks by genre
genre = st.selectbox("Select a genre", df["track_genre"].unique())
filtered_df = df[df["track_genre"] == genre]

st.write(f"Tracks in genre: {genre}")
st.dataframe(filtered_df)

# Filter by Explicitness
explicit_category = st.selectbox("Explicit?", ["All", "Explicit only", "Non-explicit only"])

if explicit_category == "Explicit only":
    filtered_df = filtered_df[filtered_df["explicit"] == True]
elif explicit_category == "Non-explicit only":
    filtered_df = filtered_df[filtered_df["explicit"] == False]

st.write("Explicitness:")
st.dataframe(filtered_df)

# Filter by popularity (slider)
popularity_range = st.slider("Slide me", 
                             min_value=0, 
                             max_value=100, 
                             value=(0, 100)
)

filtered_df = filtered_df[
    (filtered_df["popularity"] >= popularity_range[0]) &
    (filtered_df["popularity"] <= popularity_range[1])
]

st.write(f"Popularity range: {popularity_range}")
st.dataframe(filtered_df)

#Filter by danceability (slider)
danceability_range = st.slider("Slide me", 
                               min_value=0.0, 
                               max_value=1.0, 
                               value=(0.0, 1.0)
)
filtered_df = filtered_df[
    (filtered_df["danceability"] >= danceability_range[0]) &
    (filtered_df["danceability"] <= danceability_range[1])
]
st.write(f"Danceability range: {danceability_range}")
st.dataframe(filtered_df)

#Columns 
st.subheader("★ Important Variables")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.write("Track Name")
    st.dataframe(filtered_df[["track_name"]])

with col2:
    st.write("Artist")
    st.dataframe(filtered_df[["artists"]])

with col3:
    st.write("Genre")
    st.dataframe(filtered_df[["track_genre"]])

with col4:
    st.write("Danceability")
    st.dataframe(filtered_df[["danceability"]])

with col5:
    st.write("Energy")
    st.dataframe(filtered_df[["energy"]])

st.subheader("★ Summary Statistics")
st.write(filtered_df.describe())

#Graphs
st.subheader("★ Visuals")

#Boxplot for popularity by explicitness
st.write("Popularity by Explicitness (Boxplot)")
plt.figure()
box_plot1 = sns.boxplot(data=filtered_df,
                        x="explicit",
                        y="popularity")

plt.title("Popularity by Explicitness")
plt.xlabel("Explicit")
plt.ylabel("Popularity")

st.pyplot(box_plot1.get_figure())

# Scatterplot for danceability vs energy
st.write("Danceability vs Energy (Scatterplot)")
plt.figure()
scatter_plot1 = sns.scatterplot(data=filtered_df,
                                x="danceability",
                                y="energy")

plt.title("Danceability vs Energy")
plt.xlabel("Danceability")
plt.ylabel("Energy")

st.pyplot(scatter_plot1.get_figure())

# Barplot for average popularity by explicitness
st.write("Average Popularity by Explicitness (Barplot)")
plt.figure()
bar_plot1 = sns.barplot(data=filtered_df,
                        x="explicit",
                        y="popularity")

plt.title("Average Popularity by Explicitness")
plt.xlabel("Explicit")
plt.ylabel("Popularity")

st.pyplot(bar_plot1.get_figure())