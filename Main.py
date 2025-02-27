pip install pytrends // import libraries
import pandas as pd
import matplotlib.pyplot as plt
//import pytrends
from pytrends.request import TrendReq
trends=TrendReq()
//Pre processing Step
import time
# Initialize pytrends
trends = TrendReq(hl='en-US', tz=360)

# Prompt the user to enter keywords for trends
user_input = input("Enter keywords (comma-separated) to check trends: ")
keywords = [keyword.strip() for keyword in user_input.split(',')]

# Loop through the keywords to get trends data for each
for keyword in keywords:
    trends.build_payload(kw_list=[keyword])
    data = trends.interest_by_region()
    data = data.sort_values(by=keyword, ascending=False)
    data = data.head(10)
    #to print data
    #data
    print(f"Top 10 regions for {keyword}:\n", data, "\n")
    # Pause for 5 seconds between API calls to avoid rate limiting
    time.sleep(5)

#Visualize the bar chart
data.reset_index().plot(x="geoName", y=keyword, figsize=(15, 5), kind="bar")  # Changed y to keyword
plt.title(f"Top 10 regions for {keyword}")
plt.xlabel("Region")
plt.ylabel(f"Interest in {keyword}")
plt.style.use('fivethirtyeight')
plt.show()

//last 3-4 years trend of searches
# Prompt the user to enter a keyword to check trends for the past 3-4 years
keyword = input("Enter a keyword to check Google search trends for the last 3-4 years: ")

# Create a new TrendReq object to avoid overwriting the previous one
pytrends_object = TrendReq(hl='en-US', tz=360)

# Fetch interest over time data for the keyword using the new object
pytrends_object.build_payload(kw_list=[keyword])
trend_data = pytrends_object.interest_over_time()

# Plot the trend data
fig, ax = plt.subplots(figsize=(20, 15))
trend_data[keyword].plot()
plt.style.use('fivethirtyeight')
plt.title(f'Google searches for {keyword} (Past 3-4 years)', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()
