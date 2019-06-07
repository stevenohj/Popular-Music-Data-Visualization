# Musical-Time-Machine
Popular Music Artists Data Visualization

Description:
This simple data visualization app will show you what the music scene was like for a specific date in the past or today. A bubble visualization will be generated with each bubble representing a musical artist who had a song in Spotify's top 200 streamed songs on the given date. The size of each artist's bubble depends on how many streams their songs in the top 200 had, so the more top 200 streams an artist had, the larger their bubble.

Spotify_Charts_Scraper.py:
A web scraper built with Python's BeautifulSoup library, that extracts data from Spotify Charts. Given a date, the artist, track title, and number of streams will be scraped for each of the top 200 streamed songs on Spotify on that day. Python's pandas library is used to write the data a panda dataframe.

music_data_bubble_plot.py:
Using Python's numpy, matplotlib, pandas, and math libraries, the scraped data in a panda dataframe is used to create the bubble data visualization. functions such as overlaps() and is_cutoff() makes sure that each artist's bubble does not over lap with another artist's bubble and is also not cutoff by the edge of the visualization. The color and location of each bubble is randomized, and the label for each artist's bubble is also sized according to the number of streams the artist had.

main.py:
This file runs the app. It creates a simple GUI made with Python's Tkinter library that takes user input for the date. Spotify_Charts_Scraper.py and music_data_bubble_plot.py is imported and called to get the data and create the data visualization.
