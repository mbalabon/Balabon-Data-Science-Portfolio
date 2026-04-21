# Streamlit App: Spotify Track Analysis App

## Project Overview

This project is an interactive data exploration app built using Streamlit. It analyzes a [Spotify tracks dataset from Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) and allows users to filter, explore, and visualize music data.

The goal of this project is to make it easy to explore patterns in Spotify track characteristics such as popularity, danceability, energy, and explicit content. By using interactive filters and visualizations, users can better understand how different features relate to each other.

This project demonstrates how data can be explored and visualized using Python tools like pandas, seaborn, and matplotlib.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Dataset Description

The dataset contains information about Spotify tracks across many genres.

Key variables include:

- track_name – name of the song
- artists – artist(s) of the track
- track_genre – genre classification
- popularity – popularity score (0–100)
- danceability – how suitable a track is for dancing (0–1)
- energy – intensity and activity level (0–1)
- explicit – whether the track contains explicit content

Each row represents one track.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Features of the App

### Dataset Exploration
Displays the full dataset
Shows dataset shape (rows and columns)
Displays column data types

### Interactive Filtering

Users can filter the dataset in multiple ways:

Genre selection (dropdown)
<img width="714" height="432" alt="Screenshot 2026-04-20 at 10 43 26 PM" src="https://github.com/user-attachments/assets/8a7ec7cb-6a2c-45ba-97a9-a5509a9c317f" />

Explicit vs. non-explicit tracks
<img width="717" height="195" alt="Screenshot 2026-04-20 at 10 43 50 PM" src="https://github.com/user-attachments/assets/d4e7747f-5f74-44ed-a160-507adc7fc4d6" />

Popularity range (slider)
<img width="738" height="124" alt="Screenshot 2026-04-20 at 10 44 16 PM" src="https://github.com/user-attachments/assets/8463efc2-2a3d-4f46-896c-8a10b119d07b" />

Danceability range (slider)
<img width="724" height="129" alt="Screenshot 2026-04-20 at 10 44 23 PM" src="https://github.com/user-attachments/assets/07bbe280-de39-4501-9227-7efdf3f238ff" />

These filters allow users to dynamically explore subsets of the data.

### Important Variables Display

The app highlights key variables in separate columns:

- Track name
- Artist
- Genre
- Danceability
- Energy

This makes it easier to quickly scan important information.

### Summary Statistics

The app provides summary statistics (mean, min, max, etc.) for the filtered dataset using pandas 

``` 
.describe()
```
݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Visualizations

The app includes several visualizations to explore relationships in the data:

1. Popularity by Explicitness (Boxplot)
Compares popularity distributions between explicit and non-explicit tracks
<img width="698" height="562" alt="Screenshot 2026-04-20 at 10 40 22 PM" src="https://github.com/user-attachments/assets/832d961b-688d-4548-95e0-a94e095aab3b" />

2. Danceability vs Energy (Scatterplot)
Shows the relationship between danceability and energy
<img width="694" height="544" alt="Screenshot 2026-04-20 at 10 40 40 PM" src="https://github.com/user-attachments/assets/6ab990c6-4b6d-4b34-9b22-f9320c797ea8" />

3. Average Popularity by Explicitness (Barplot)
Compares average popularity between explicit and non-explicit tracks
<img width="694" height="553" alt="Screenshot 2026-04-20 at 10 41 00 PM" src="https://github.com/user-attachments/assets/805e0f29-132b-4c05-b9a5-d0d1f04fd970" />

These visualizations update dynamically based on the selected filters.

#### From exploring the dataset, users can observe:

- Popularity varies widely across tracks and genres
- Explicit and non-explicit tracks may show different popularity patterns
- Danceability and energy show a relationship, but not perfectly linear
- Filtering reveals patterns that are not obvious in the full dataset head-on

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Tools and Libraries Used

This project uses Python and the following libraries:

- pandas
- seaborn
- matplotlib
- streamlit

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## How to Run This Project

#### Requirements

Make sure you have Python installed and install the required libraries above.

#### Run the app

From your project folder, in the terminal run:
``` 
streamlit run your_filename.py
``` 

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Project Purpose

This project demonstrates:

- how to build an interactive data app
- how to filter and explore real-world datasets
- how visualization helps reveal patterns in data

It highlights how tools like Streamlit can turn a static dataset into an interactive experience.

₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## References

[Kaggle Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)

[Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)
