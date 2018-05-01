# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

baseline = 15

minimum_detectable_effect = 100*5./15

sample_size_per_variant = 870

yellowstone_weeks_observing = sample_size_per_variant/507.

bryce_weeks_observing = sample_size_per_variant/250.

print("Baseline:")
print(baseline)
print('\n')

print("Sample Size")
print(sample_size_per_variant)
print('\n')

print("Min. Detectable Effect:")
print(minimum_detectable_effect)
print('\n')

print("Weeks at Yellowstone:")
print(yellowstone_weeks_observing)
print('\n')

print("Weeks at Bryce:")
print(bryce_weeks_observing)
