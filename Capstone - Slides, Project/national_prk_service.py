# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

species = pd.read_csv('c:/users/kalei/documents/python/data analysis/biodiversity/species.csv', delimiter = ',')

# Print species.head() to get a sample of species dataframe
print(species.head())
print('\n')

# Count the number of species
species_count = species.scientific_name.nunique()
print(species_count)
print('\n')

# List the different categories of species
species_type = species['category'].unique()
print(species_type)
print('\n')

# List the different conservation statuses
conservation_statuses = species.conservation_status.unique()
print(conservation_statuses)
print('\n')

# Count how many species (scientific names) falls into each conservation_status
# Here, we are not concerned with the nulls
conservation_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print(conservation_counts)
print('\n')

# Fill the species dataframe with 'No Intervention' instead of the Nan or None 
# that it is using
species.fillna('No Intervention', inplace = True)

# Now, count how many species fall into each conservation_status
# This will display the new numbers for 'No Intervention'
conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print(conservation_counts_fixed)
print('\n')

# sort values by scientific_name
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')

# ------------------- Bar Chart --------------------
# figure size
plt.figure(figsize=(10,4))

# create an axis to be used for x ticks later
ax = plt.subplot()

# create bar chart whose heights are the scientific name
# column of protection_counts
plt.bar(range(len(protection_counts.scientific_name)),protection_counts.scientific_name)

# create an x-tick for each bar
ax.set_xticks(range(len(protection_counts.conservation_status)))

# label each x-tick with the conservation_status from
# protection_counts
ax.set_xticklabels(protection_counts.conservation_status)

# label y-axis
plt.ylabel('Number of Species')
# title
plt.title('Conservation Status by Species')

# plt.savefig('c:/users/kalei/documents/python/data analysis/biodiversity/conserv_stat.png')

plt.show()

# ----------- PIVOT TABLE -----------
# Create a new column in species called is_protected, 
# which is True if conservation_status is not equal to 'No
# Intervention', and False otherwise.
species['is_protected'] = species.conservation_status.apply(\
lambda x: 'True'\
 if x != 'No Intervention'\
 else 'False')

# group by category (mammal, fish, etc) and new column
# (is_protected)
category_counts = species.groupby(['category','is_protected']).scientific_name.nunique().reset_index()

print(category_counts.head())
print('\n')

# create a pivot table for category_counts
# be sure to reset_index()
category_pivot = category_counts.pivot(columns='is_protected', index='category', 
values='scientific_name').reset_index()

print(category_pivot)
print('\n')

# rename False and True columns using .columns
category_pivot.columns = ['category', 'not_protected', 'protected']

# add a new column, named percent_protected
category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

print(category_pivot)
print('\n')

# Contingency Table I
# 					protected | not protected
# ---------+--------------------+-----------
# Mammal   |   30     |    146
# Bird     |	 75			|    413

contingency = [[30, 146],
               [75, 413]]

chi2, pval, dof, expected = chi2_contingency(contingency)
print("Chi-squared Test - Mammal v. Bird")
print (pval)
print('\n')

# Contingency Table II
# 					protected | not protected
# ---------+--------------------+-----------
# Reptile   |   5      |    73
# Mammal    |	  30		 |    146

contingency2 = [[5, 73],
                [30, 146]]

chi2, pval_reptile_mammal, dof, expected = chi2_contingency(contingency2)
print("Chi-squared Test - Reptile v. Mammal")
print (pval_reptile_mammal)
print('\n')
