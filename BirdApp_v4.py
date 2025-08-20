import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import streamlit as st

import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.set_page_config(layout = "wide")

st.title("Breeding Bird Survey Data")
st.link_button("Data Available Here", "https://zenodo.org/records/14161736")

# Creating a dropdown menu with options for bird species

species = st.selectbox("Select the species you are interested in:", ['Arctic Tern', 'Alexandrine Parakeet', 'Atlantic Puffin', 'Australian Shelduck', 'Bar-headed Goose', 'Bar-tailed Godwit', 'Barn Swallow',
                                                                     'Barnacle Goose', 'Black Kite', 'Black Swan', 'Black Tern', 'Black-headed Gull', 'Black-legged Kittiwake', 'Bluethroat', "Blyth's Reed Warbler",
                                                                     'Bohemian Waxwing', 'Brant Goose', 'Brent Goose (Dark-bellied - bernicla)', 'Canada Goose', 'Carrion Crow', 'Carrion x Hooded Crow', 'Coal Tit',
                                                                     'Cockatiel', 'Common Blackbird', 'Common Buzzard', 'Common Chiffchaff', 'Common Cuckoo', 'Common Grasshopper Warbler', 'Common Gull',
                                                                     'Common Kestrel', 'Common Kingfisher', 'Common Linnet', 'Common Loon', 'Common Merganser', 'Common Moorhen', 'Common Murre', 
                                                                     'Common Nightingale', 'Common Pheasant', 'Common Redpoll', 'Common Redshank', 'Common Redstart', 'Common Reed Bunting', 'Common Reed Warbler',
                                                                     'Common Ringed Plover', 'Common Sandpiper', 'Common Shelduck', 'Common Snipe', 'Common Starling', 'Common Swift', 'Common Tern',
                                                                     'Common Whitethroat', 'Common Wood Pigeon', 'Common/Lesser Redpoll', 'Corn Bunting', 'Crested Tit', 'Curlew Sandpiper', 'Dartford Warbler',
                                                                     'Domestic Greylag Goose', 'Domestic Mallard', 'Dunnock', 'Egyptian Goose', 'Eurasian Blackcap', 'Eurasian Blue Tit', 'Eurasian Bullfinch', 
                                                                     'Eurasian Chaffinch', 'Eurasian Collared Dove', 'Eurasian Coot', 'Eurasian Curlew', 'Eurasian Eagle-Owl', 'Eurasian Hoopoe', 'Eurasian Jay',
                                                                     'Eurasian Magpie', 'Eurasian Nuthatch', 'Eurasian Oystercatcher', 'Eurasian Siskin','Eurasian Skylark','Eurasian Sparrowhawk','Eurasian Teal',
                                                                     'Eurasian Tree Sparrow', 'Eurasian Treecreeper', 'Eurasian Woodcock', 'Eurasian Wren', 'Eurasian Wryneck', 'European Bee-eater',
                                                                     'European Golden Plover', 'European Goldfinch', 'European Green Woodpecker', 'European Greenfinch', 'European Herring Gull',
                                                                     'European Pied Flycatcher', 'European Robin', 'European Rock Pipit', 'European Serin', 'European Shag', 'European Stonechat',
                                                                     'European Turtle Dove', 'Falcated Duck', 'Feral Pigeon', 'Ferruginous Duck', 'Gadwall', 'Garden Warbler', 'Glaucous Gull', 'Goldcrest',
                                                                     'Golden Pheasant', 'Great Black-backed Gull', 'Great Cormorant', 'Great Crested Grebe', 'Great Grey Shrike', 'Great Skua',
                                                                     'Great Spotted Woodpecker', 'Great Tit', 'Greater Scaup', 'Greater White-fronted Goose', 'Grey Heron', 'Grey Partridge', 'Grey Plover',
                                                                     'Grey Wagtail', 'Greylag Goose', "Harris's Hawk", 'Helmeted Guineafowl', 'Hooded Crow', 'House Sparrow', 'Iceland Gull', 'Indian Peafowl',
                                                                     'Jack Snipe', 'Kentish Plover', "Lady Amherst's Pheasant", 'Lapland Longspur', 'Lesser Black-backed Gull', 'Lesser Redpoll', 'Lesser Scaup',
                                                                     'Lesser Spotted Woodpecker', 'Lesser Whitethroat', 'Little Egret', 'Little Grebe', 'Little Gull', 'Little Owl', 'Little Stint',
                                                                     'Long-tailed Duck', 'Long-tailed Tit', 'Mallard', 'Mandarin Duck', 'Manx Shearwater', 'Marsh Sandpiper', 'Marsh Tit', 'Meadow Pipit',
                                                                     'Mistle Thrush', 'Muscovy Duck', 'Mute Swan', 'Nene', 'Northern Fulmar', 'Northern Gannet', 'Northern Lapwing', 'Northern Raven',
                                                                     'Northern Wheatear', 'Parasitic Jaeger', 'Pink-footed Goose', 'Pomarine Jaeger', 'Purple Heron', 'Razorbill', 'Red Crossbill', 'Red Knot', 
                                                                     'Red-breasted Goose', 'Red-breasted Merganser', 'Red-crested Pochard', 'Red-legged Partridge', 'Red-rumped Swallow', 'Red-tailed Hawk', 
                                                                     "Reeves's Pheasant", 'Ring Ouzel', 'Ring-necked Duck', 'Rock Dove', 'Rock Ptarmigan', 'Rook', 'Rose-ringed Parakeet', 'Rosy Starling',
                                                                     'Ruddy Duck', 'Ruddy Shelduck', 'Ruddy Turnstone', "Sabine's Gull", 'Sand Martin', 'Sanderling', 'Sandwich Tern', 'Scottish Crossbill',
                                                                     'Sedge Warbler', 'Short-toed Treecreeper', 'Snow Goose', 'Song Thrush', 'Spotted Flycatcher', 'Spotted Redshank', 'Stock Dove', 'Swan Goose',
                                                                     'Tawny Owl', 'Tree Pipit', 'Tufted Duck', 'Tundra Swan', 'Unidentified crossbill', 'Water Pipit', 'Water Rail', 'Western House Martin',
                                                                     'Western Jackdaw', 'Western Yellow Wagtail', 'Whinchat', 'White Stork', 'White Wagtail', 'White-cheeked Pintail',
                                                                     'White-fronted Goose (Greenland - flavirostris)', 'White-throated Dipper', 'Willow Ptarmigan', 'Willow Tit', 'Willow Warbler', 'Wood Duck',
                                                                     'Wood Warbler', 'Woodchat Shrike', 'Woodlark', 'Yellowhammer', 'Zitting Cisticola'])

# Displaying the selected option - could remove at a later stage
st.header(f"Showing Results for: {species}")

## Create a graph of the species population rank
# Step 1: Load data from CSV
species_counts_over_time = pd.read_csv('species_counts_over_time.csv')
species_counts_over_time['rank'] = species_counts_over_time.groupby('year')['total_obs'].rank(method='dense', ascending=False)

# Create two columns
col1, col2 = st.columns(2)

# Display graphs in the columns
with col1:
    def species_time_series(species_name):
    # Find the subset of the data for the given species
        temp_species_info = species_counts_over_time[species_counts_over_time['English_name'] == species_name].copy()

    # Calculate 5-year moving average on the 'value' column
        temp_species_info['5y_average'] = temp_species_info['total_obs'].rolling(window=5, min_periods=1).mean()
    
        st.line_chart(data=temp_species_info, x='year', y=['total_obs', '5y_average'], x_label='Year', y_label='Number Observed')
        return

    st.header(f"{species} Sightings Over Time")
    species_time_series(species)

    def species_rank(species_name):
        temp_species_df = species_counts_over_time[species_counts_over_time['English_name'] == species_name].copy()

        st.line_chart(data=temp_species_df, x='year', y='rank', x_label='Year', y_label='Rank')
        return
    
    st.header(f"{species} Rank Over Time*")
    species_rank(species)
    st.write('*The most common species is ranked at position 1, then species are in descending order by annual sightings.')

with col2:

    ## Implementing a Folium Heatmap for the species...
    # Step 1: Load data from CSV
    count_by_location = pd.read_csv('count_by_location.csv')

    # Step 2: Convert pandas DataFrame to GeoDataFrame
    gdf = gpd.GeoDataFrame(count_by_location,
                       geometry=gpd.points_from_xy(count_by_location.ETRS89Long, count_by_location.ETRS89Lat),       # create a geometry column from the longitude and latitude
                       crs="EPSG:4326")                                                                              # this is the standard coordinate system for latitude/longitude coordinates

    # Step 3: Function which creates heatmap for the species selected
    def species_heatmap(species_name):
        # Find the subset of the data for the given species
        species_df = gdf[gdf['English_name'] == species_name]
    
        # Create a base map centered around mean lat/lon
        m = folium.Map(location = [species_df['ETRS89Lat'].mean(), species_df['ETRS89Long'].mean()], zoom_start=5)

        # Create list of [lat, lon] for heatmap points
        heat_data = species_df[['ETRS89Lat', 'ETRS89Long', 'total_obs']].values.tolist()      # add the total_obs for weightings
    
        # Add heatmap layer (on top of map around species centroid)
        HeatMap(heat_data).add_to(m)

        return m

    # Step 4: Define the map based on the species using our function
    folium_map = species_heatmap(species)

    # Step 5: Render the folium map in Streamlit
    st.header(f"Heatmap for sighting locations of {species}")
    st_folium(folium_map, width=800, height=800)