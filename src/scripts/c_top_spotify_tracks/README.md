## Task 2: Spotify Top Tracks

Using the Spotify Top Tracks dataset from Kaggle, Write a Glue ETL job that will:

1. Read the data from Data Catalog
    - The source data should be stored in a S3 bucket
    - Schema of this source data should crawled and stored in the Data Catalog, using the Glue Crawler.
2. Create a DynamicFrame from the source data
3. Apply Mappings, change column names and data types as needed
4. Convert the DynamicFrame to a Spark DataFrame
5. Apply transformations to the Spark DataFrame
    - Filter out any songs that do not have a year in the release date
    - If the song has multiple artists, add commas between the artist names
    - Make sure the song name is in title case
    - Validate the Album Image URL is a valid URL

Reference:
Data Source: https://www.kaggle.com/datasets/joebeachcapital/top-10000-spotify-songs-1960-now
