#from google.colab import drive, files # specific to Google Colab
#import plotly.express as px # visualization
import pandas as pd # data manipulation
import io

file_dir = ''

# read in api key file
#df_api_keys = pd.read_csv(file_dir + 'api_keys.csv')

# get keys
#mapbox_api_key = df_api_keys.loc[df_api_keys['API'] =='mapbox']['KEY'].iloc[0] # replace this with your own key

# upload
#uploaded = files.upload()

# get file name
#file_name = list(uploaded.keys())[0]

# read file
#df_upload = pd.read_csv(io.BytesIO(uploaded[file_name]))
df_upload = pd.read_csv('dataset_airbnb-scraper_2025-03-09_20-55-48-977.csv')
print('Num of rows:', len(df_upload))
print('Num of columns:', len(df_upload.columns))

# view elements in first row
#df_upload.iloc[0]

# list all columns
print(df_upload.columns)

# cities
#df_grp_cities = df_upload.groupby(by=['address'])['name'].count().reset_index()\
#  .rename(columns={'name': 'count'})\
#  .sort_values(by=['count'], ascending=False)
#df_grp_cities['percent'] = (df_grp_cities['count'] / df_grp_cities['count'].sum()) * 100
#df_grp_cities

# filter on Siesta Key, Florida
#df = df_upload.loc[df_upload['address'] == 'Siesta Key, Florida, United States']
#print('Num of rows:', len(df))
#df.head()

# room type
#df_grp_rm_type = df.groupby(by=['roomType'])['name'].count().reset_index()\
#  .rename(columns={'name': 'count'})\
#  .sort_values(by=['count'], ascending=False)
#df_grp_rm_type['percent'] = round((df_grp_rm_type['count'] / df_grp_rm_type['count'].sum()) * 100, 2)
#df_grp_rm_type

# star count & avg price amount
#df.groupby('stars')\
#  .agg({'name':'count','pricing/rate/amount':'mean'}).reset_index()\
#  .rename(columns={'name': 'count'})\
#  .sort_values(by=['count'], ascending=False)

# view number of guests
#fig = px.histogram(df, x="numberOfGuests", nbins=10)
#fig.show()

# daily price
#fig = px.histogram(df, x="pricing/rate/amount")
#fig.show()

# daily price by number of guests
#fig = px.scatter(df, x="pricing/rate/amount", y="numberOfGuests")
#fig.show()

# take a single example to test logic of getting listing id
#test_url = df['url'].iloc[0]
#print('Test URL:', test_url)
#print('Listing ID:', test_url.split('/')[-1])

# create plot dataframe
#df_plot = df.copy()
# feature #1 - listing id
#df_plot['listing_id'] = df_plot.apply(lambda x: x['url'].split('/')[-1], axis=1)
# feature #2 - header (listing id + listing name)
#df_plot['header'] = df_plot.apply(lambda x: x['listing_id'] + ' - ' + x['name'], axis=1)
#df_plot['header'].head()

# set mapbox key
#px.set_mapbox_access_token(mapbox_api_key)
# create scatter plot
#fig = px.scatter_mapbox(
#    df_plot,
#    lat="location/lat",
#    lon="location/lng",
#    color="pricing/rate/amount",
#    size="numberOfGuests",
#    color_continuous_scale=px.colors.cyclical.Edge,
#    hover_name="header",
#    zoom=13
#)
# modify height to show all of siesta key (town specific)
#fig.update_layout(
#    height=800
#)
#fig.show()

# view single listing
#df_single_list = df_plot.loc[df_plot['listing_id'] == '38351053']
# get URL to view listing photos and detail
#print('Listing URL:', df_single_list['url'].iloc[0])
# view df
#df_single_list

# # download file
# df.to_csv('output.csv', index=False)
# files.download('output.csv')