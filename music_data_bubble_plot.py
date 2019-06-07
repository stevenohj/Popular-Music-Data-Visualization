import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd


def overlaps(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
    min_distance_allowed = z1 + z2
    return distance < min_distance_allowed + 2


def is_cutoff(x, y, z):
    return ((x - z) < 0) or ((y - z) < 0) or ((x + z) > 450) or ((y + z) > 450)


def random_color():
    r, g, b = 0, 0, 0
    while (r < 100 or g < 100 or b < 100):
        r = np.random.randint(0, 255)
        g = np.random.randint(0, 255)
        b = np.random.randint(0, 255)

    return (r / 255, g / 255, b / 255)


def calc_font_size(z, min, max):
    max -= min
    z -= min
    font_size = 10 * z / max
    return font_size + 5


# WORK IN PROGRESS
"""def display_song_table(artist,songlist):
    songlist.sort(key=lambda song: song[1])
    titles = []
    counts = []
    for title, streams in songlist:
        title.append(title)
        counts.append(streams)
    song_table = plt.table(counts,rowLabels=titles,colLabels=['Number of Streams This Day'])"""


def display_artist_bubbles(music_panda):

    artists = []

    x = [0] * len(music_panda.index)
    y = [0] * len(music_panda.index)
    z = [0] * len(music_panda.index)
    colors = [(0, 0, 0)] * len(music_panda.index)

    first_one = True
    count = 0

    for index, row in music_panda.iterrows():

        x_point = np.random.rand() * 450
        y_point = np.random.rand() * 450
        z[count] = math.sqrt(row['streamcount'] / 1000 / math.pi)
        colors[count] = random_color()
        artists.append((row['artist'], row['songs']))

        if first_one:
            x[count] = x_point
            y[count] = y_point
            while is_cutoff(x[0], y[0], z[0]):
                x[count] = np.random.rand() * 450
                y[count] = np.random.rand() * 450
            first_one = False
            count += 1
            continue

        checking_index = 0
        while checking_index < count:
            if overlaps(x_point, y_point, z[count], x[checking_index], y[checking_index], z[checking_index]) or is_cutoff(x_point, y_point, z[count]):
                x_point = np.random.rand() * 450
                y_point = np.random.rand() * 450
                checking_index = 0
            else:
                checking_index += 1

        x[count] = x_point
        y[count] = y_point
        count += 1

    fig, ax = plt.subplots()

    # change default range so that new circles will work
    ax.set_xlim((0, 450))
    ax.set_ylim((0, 450))

    for i in range(len(music_panda.index)):
        ax.add_artist(plt.Circle((x[i], y[i]), z[i], color=colors[i]))
        ax.annotate(artists[i][0], xy=(x[i] - (z[i] / 2), y[i]), fontsize=calc_font_size(z[i], z[-1], z[0]), fontweight='bold')
    """for artist, point in artist_points.items():
        plt.annotate(artist, point)"""
    plt.suptitle('Most Popular Artists on this Day', fontsize=20, fontweight='bold')
    plt.axis("off")
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.show()

    # WORK IN PROGRESS
    """if event.button_release_event:
    artist = event.artist
    xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
    x, y = artist.get_xdata(), artist.get_ydata()
    ind = event.ind"""


# display_artist_bubbles(pd.read_csv('Spotify_Charts_us_daily_2019-05-25.csv'))
