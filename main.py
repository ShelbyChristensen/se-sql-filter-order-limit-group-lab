import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1
# Replace None with your code
df_no_moons = pd.read_sql("""
SELECT * FROM planets
WHERE moons = 0;
""", conn1)

# STEP 2
# Replace None with your code
df_name_seven = pd.read_sql("""
SELECT name, mass FROM planets
WHERE LENGTH(name) = 7;
""", conn1)

##### Part 2: Advanced Filtering #####

# STEP 3
df_mass = pd.read_sql("""
SELECT name, mass FROM planets
WHERE mass <= 1.00;
""", conn1)

# STEP 4
df_mass_moon = pd.read_sql("""
SELECT * FROM planets
WHERE moons >= 1 AND mass < 1.00;
""", conn1)

# STEP 5
df_blue = pd.read_sql("""
SELECT name, color FROM planets
WHERE color LIKE '%blue%';
""", conn1)

##### Part 3: Ordering and Limiting #####

# STEP 0

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6
# Replace None with your code
df_hungry = None

# STEP 7
# Replace None with your code
df_hungry_ages = None

# STEP 8
# Replace None with your code
df_4_oldest = None


##### Part 4: Aggregation #####

# STEP 0

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9
# Replace None with your code
df_ruth_years = None

# STEP 10
# Replace None with your code
df_hr_total = None


##### Part 5: Grouping and Aggregation #####

# STEP 11
# Replace None with your code
df_teams_years = None

# STEP 12
# Replace None with your code
df_at_bats = None


conn1.close()
conn2.close()
conn3.close()