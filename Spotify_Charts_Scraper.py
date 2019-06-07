import requests
from bs4 import BeautifulSoup
import calendar
import pandas as pd
import datetime


# RETURNS THE 2-DIGIT NUMBER REPRESENTATION OF THE GIVEN MONTH
def get_month_num_formatted(month_name):
    months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    month_name = month_name.capitalize()
    return months[month_name]

# CHANGE DATE TO PROPER FORMAT FOR WEEKLY DATE STARTING ON FRIDAYS


def adjust_weekly_dates(year, month, day):
    weekdayNum = calendar.weekday(year, int(get_month_num_formatted(month)), day)
    if weekdayNum < 4:
        weekdayNum = weekdayNum + 3
    else:
        weekdayNum -= 4

    print(weekdayNum)
    # if weekdayNum == 0:
    #    weekdayNum = 7

    # CHECK TO SEE IF THE PREVIOUS FRIDAY WAS IN THE PREVIOUS MONTH AND IF SO, ADJUST ACCORDINGLY
    if weekdayNum >= day:

        if month == 'January':
            month = 'December'
            weekdayNum -= day
            day = 31 - weekdayNum
            year -= 1

        elif month == 'February':
            month = 'January'
            weekdayNum -= day
            day = 31 - weekdayNum

        elif month == 'March':
            month = 'February'
            weekdayNum -= day
            if calendar.isleap(year):
                day = 29 - weekdayNum
            else:
                day = 28 - weekdayNum

        elif month == 'April':
            month = 'March'
            weekdayNum -= day
            day = 31 - weekdayNum

        elif month == 'May':
            month = 'April'
            weekdayNum -= day
            day = 30 - weekdayNum

        elif month == 'June':
            month = 'May'
            weekdayNum -= day
            day = 31 - weekdayNum

        elif month == 'July':
            month = 'June'
            weekdayNum -= day
            day = 30 - weekdayNum

        elif month == 'August':
            month = 'July'
            weekdayNum -= day
            day = 31 - weekdayNum

        elif month == 'September':
            month = 'August'
            weekdayNum -= day
            day = 31 - weekdayNum

        elif month == 'October':
            month = 'September'
            weekdayNum -= day
            day = 30 - weekdayNum

        elif month == 'November':
            month = 'October'
            weekdayNum -= day
            day = 31 - weekdayNum

        else:
            month = 'November'
            weekdayNum -= day
            day = 30 - weekdayNum

    else:
        day -= weekdayNum

    return str(year) + '-' + num_month[month] + '-' + str(day) + '--' + str(year) + '-' + num_month[month] + '-' + str(day + 7)


# GETS THE CODE FOR GIVEN COUNTRY TO INCLUDE IN URL
def get_country_code(country):
    codes = {
        'All Countries': 'global',
        'United States': 'us',
        'United Kingdom': 'gb',
        'Argentina': 'ar',
        'Austria': 'at',
        'Australia': 'au',
        'Belgium': 'be',
        'Bulgaria': 'bg',
        'Bolivia': 'bo',
        'Brazil': 'br',
        'Canada': 'ca',
        'Chile': 'cl',
        'Colombia': 'co',
        'Costa Rica': 'cr',
        'Czech Republic': 'cz',
        'Germany': 'de',
        'Denmark': 'dk',
        'Dominican Republic': 'do',
        'Ecuador': 'ec',
        'Estonia': 'ee',
        'Finland': 'fi',
        'France': 'fr',
        'Greece': 'gr',
        'Guatemala': 'gt',
        'Hong Kong': 'hk',
        'Honduras': 'hn',
        'Hungary': 'hu',
        'Indonesia': 'id',
        'Ireland': 'ie',
        'Israek': 'il',
        'India': 'in',
        'Iceland': 'is',
        'Italy': 'it',
        'Japan': 'jp',
        'Lithuania': 'lt',
        'Luxembourg': 'lu',
        'Latvia': 'lv',
        'Malta': 'mt',
        'Mexico': 'mx',
        'Malaysia': 'my',
        'Nicaragua': 'ni',
        'Netherlands': 'nl',
        'Norway': 'no',
        'New Zealand': 'nz',
        'Panama': 'pa',
        'Peru': 'pe',
        'Philippines': 'ph',
        'Poland': 'pl',
        'Portugal': 'pt',
        'Paraguay': 'py',
        'Romania': 'ro',
        'El Salvador': 'sv',
        'Singapore': 'sg',
        'Slovakia': 'sk',
        'South Africa': 'za',
        'Sweden': 'se',
        'Switzerland': 'ch',
        'Taiwan': 'tw',
        'Thailand': 'th',
        'Turkey': 'tr',
        'Uruguay': 'uy',
        'Vietnam': 'vn'
    }
    return codes[country]


def scrape_music_data(year, month, day, country='United States', period='daily'):

    # WORK IN PROGRESS
    """if period == 'weekly':
                    date = adjust_weekly_dates(year, month, day)
                else:
                    date = str(year) + '-' + get_month_num_formatted(month) + '-' + str(day)"""
    if day < 10:
        date = str(year) + '-' + get_month_num_formatted(month) + '-' + '0' + str(day)
    else:
        date = str(year) + '-' + get_month_num_formatted(month) + '-' + str(day)
    d = datetime.datetime.today()
    if (year == d.year and int(get_month_num_formatted(month)) == d.month and day == d.day):
        date = 'latest'

    url = 'https://spotifycharts.com/regional/' + get_country_code(country) + '/' + period.lower() + '/' + date
    # print(url)
    webpage_response = requests.get(url)

    webpage = webpage_response.content
    # print(webpage)
    soup = BeautifulSoup(webpage, "html.parser")

    music_data_dic = {}

    for song in soup.select(".chart-table")[0].tbody.find_all("tr"):
        track = song.select(".chart-table-track")[0].get_text()
        track = track.split("by ")
        track_title = track[0].strip('\n')
        # print(track_title)
        artist = track[1].strip('\n')
        # print(artist)
        streamcount = int(song.select(".chart-table-streams")[0].get_text().replace(',', ''))

        # print(streamcount)

        if artist not in music_data_dic.keys():
            music_data_dic[artist] = [0, []]

        music_data_dic[artist][0] += streamcount
        music_data_dic[artist][1].append((track_title, streamcount))

    pd_data = []
    for key, val in music_data_dic.items():
        pd_data.append([key, val[0], val[1]])

    music_df = pd.DataFrame(pd_data, columns=['artist', 'streamcount', 'songs'])

    music_df = music_df.sort_values(by='streamcount', ascending=False)
    music_df = music_df.reset_index(drop=True)

    # UNCOMMENT TO SAVE DATAFRAME AS CSV
    """csv_path = 'Spotify_Charts_' + get_country_code(country) + '_' + period.lower() + '_' + date + '.csv'
    music_df.to_csv(csv_path)"""
    return music_df
