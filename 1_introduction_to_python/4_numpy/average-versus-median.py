"""
Average versus median
You now know how to use numpy functions to get a better feeling for your data. It basically comes down to importing numpy and then calling several simple functions on the numpy arrays:

import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)
The baseball data is available as a 2D numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers.

Instructions

Create numpy array np_height_in that is equal to first column of np_baseball.
Print out the mean of np_height_in.
Print out the median of np_height_in.
"""
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in=np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

"""
An average height of 1586 inches, that doesn't sound right, does it? However, the median does not seem affected by the outliers: 74 inches makes perfect sense. It's always a good idea to check both the median and the mean, to get an idea about the overall distribution of the entire dataset.
"""
