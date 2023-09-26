#! python3
"""
Program:        getWeather.py
Description:    simple python script to get a Weather Network report for a city in the U.S. or Canada.
                ',' required between city and province / state / territory 2 letter abbreviation.

Author:         Mike Lynch
"""

import webbrowser, sys, logging, pyperclip

# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

provinces = {
    "on": "ontario",
    "qc": "quebec",
    "ns": "nova-scotia",
    "nb": "new-brunswick",
    "mb": "manitoba",
    "bc": "british-columbia",
    "pe": "prince-edward-island",
    "sk": "saskatchewan",
    "ab": "alberta",
    "nl": "newfoundland-and-labrador",
    "nt": "northwest-territories",
    "yt": "yukon",
    "nu": "nunavut",
}

states = {
    "al": "alabama",
    "ak": "alaska",
    "az": "arizona",
    "ar": "arkansas",
    "ca": "california",
    "co": "colorado",
    "ct": "connecticut",
    "de": "delaware",
    "fl": "florida",
    "ga": "georgia",
    "hi": "hawaii",
    "id": "idaho",
    "il": "illinois",
    "in": "indiana",
    "ia": "iowa",
    "ks": "kansas",
    "ky": "kentucky",
    "la": "louisiana",
    "me": "maine",
    "md": "maryland",
    "ma": "massachusetts",
    "mi": "michigan",
    "mn": "minnesota",
    "ms": "mississippi",
    "mo": "missouri",
    "mt": "montana",
    "ne": "nebraska",
    "nv": "nevada",
    "nh": "new hampshire",
    "nj": "new jersey",
    "nm": "new mexico",
    "ny": "new york",
    "nc": "north carolina",
    "nd": "north dakota",
    "oh": "ohio",
    "ok": "oklahoma",
    "or": "oregon",
    "pa": "pennsylvania",
    "ri": "rhode island",
    "sc": "south carolina",
    "sd": "south dakota",
    "tn": "tennessee",
    "tx": "texas",
    "ut": "utah",
    "vt": "vermont",
    "va": "virginia",
    "wa": "washington",
    "vw": "west virginia",
    "wi": "wisconsin",
    "wy": "wyoming",
    "dc": "district of columbia",
    "as": "american samoa",
    "gu": "guam",
    "mp": "northern mariana islands",
    "pr": "puerto rico",
    "vi": "u.s. virgin islands"
}

if len(sys.argv) > 1:
    # get weather from command line
    location = ' '.join(sys.argv[1:])
else:
    location = pyperclip.paste()

location = location.split(',')

logging.debug('weather location is %s', location)

if location[1].lower() not in provinces or location[1].lower() not in states:
    assert location[1] in provinces or location[1] in states, ("Error. Provide a proper 2 letter province or territory "
                                                               "code.")
if location[1] in provinces:
    webbrowser.open(f'https://www.theweathernetwork.com/ca/weather/{provinces[location[1].lower()]}/{location[0].lower()}')
if location[1] in states:
    webbrowser.open(f'https://www.theweathernetwork.com/us/weather/{states[location[1].lower()]}/{location[0].lower()}')

#TODO: add Mexico
#TODO: add World
