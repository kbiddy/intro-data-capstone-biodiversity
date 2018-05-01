# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('c:/users/kalei/documents/python/data analysis/biodiversity/species.csv', delimiter = ',')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv('c:/users/kalei/documents/python/data analysis/biodiversity/observations.csv', delimiter = ',')
print(observations.head())
print('\n')

# Use apply and a lambda function to create a new column 
# in species called is_sheep which is True if the
# common_names contains 'Sheep', and False otherwise.
species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)

print(species.head())
print('\n')

# Select the rows of species where is_sheep is True and save
# it to the variable species_is_sheep.
species_is_sheep = species[(species['is_sheep'] == True)]
print(species_is_sheep)
print('\n')

# Select the rows of species where is_sheep is True and
# category is Mammal. Save the results to the variable
# sheep_species.
sheep_species = species[(species.is_sheep == True) & (species.category == 'Mammal')]
print(sheep_species)
print('\n')

# merge the dataframe sheep_species with observations
sheep_observations = pd.merge(sheep_species, observations)
print(sheep_observations.head())
print('\n')

# How many total sheep sightings (across all three species)
# were made at each national park? Use groupby to get the
# sum of observations for each park_name.
# this is the total number of sheep observed in each park
# over the past 7 days.
obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
print(obs_by_park)
print('\n')

# ---------- Bar Chart ------------
plt.figure(figsize=(16,4))

# Create an axes object called ax using plt.subplot.
ax = plt.subplot()

# Create a bar chart whose heights are equal to observations
# column of obs_by_park.
plt.bar(range(len(obs_by_park.observations)),obs_by_park.observations)

# Create an x-tick for each of the bars.
ax.set_xticks(range(len(obs_by_park.park_name)))

# Label each x-tick with the label from park_name in
# obs_by_park
ax.set_xticklabels(obs_by_park.park_name)

# Label the y-axis Number of Observations
plt.ylabel("Number of Observations")

plt.title("Observations of Sheep per Week")

# plt.savefig('c:/users/kalei/documents/python/data analysis/biodiversity/sheep_sightings.png')

plt.show()
