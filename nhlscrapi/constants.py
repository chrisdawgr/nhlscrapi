
"""Module level constants specifying available data"""

from datetime import datetime as dt

MIN_SEASON = 2008
"""Oldest season currently supported"""

MAX_SEASON = dt.today().year if dt.today().month < 10 else dt.today().year + 1
"""Year of the most recent season. Seasons are denoted by the year in which they end, i.e. 2013-2014 is denoted 2014"""

GAME_CT_DICT = {
  2008: 1230,
  2009: 1230,
  2010: 1230,
  2011: 1230,
  2012: 1230,
  2013: 720,
  2014: 1230,
  2015: 1230,
  2016: 1230
}

MISS_REG_GAMES = [
  "20030001",
  "20030002",
  "20030003",
  "20030004",
  "20030005",
  "20030006",
  "20030007",
  "20030008",
  "20030009",
  "20030010",
  "20030011",
  "20030012",
  "20030013",
  "20030014",
  "20030015",
  "20030016",
  "20030017",
  "20030018",
  "20030019",
  "20030020",
  "20030021",
  "20030022",
  "20030023",
  "20030024",
  "20030025",
  "20030026",
  "20030027",
  "20030028",
  "20030029",
  "20030030",
  "20030031",
  "20030032",
  "20030033",
  "20030034",
  "20030035",
  "20030036",
  "20030037",
  "20030038",
  "20030039",
  "20030040",
  "20030041",
  "20030042",
  "20030043",
  "20030044",
  "20030045",
  "20030046",
  "20030047",
  "20030048",
  "20030049",
  "20030050",
  "20030051",
  "20030052",
  "20030053",
  "20030054",
  "20030055",
  "20030056",
  "20030057",
  "20030058",
  "20030059",
  "20030060",
  "20030061",
  "20030062",
  "20030063",
  "20030064",
  "20030065",
  "20030066",
  "20030067",
  "20030068",
  "20030069",
  "20030070",
  "20030071",
  "20030072",
  "20030073",
  "20030074",
  "20030075",
  "20030076",
  "20030077",
  "20030078",
  "20030079",
  "20030080",
  "20030081",
  "20030082",
  "20030083",
  "20030084",
  "20030085",
  "20030086",
  "20030087",
  "20030088",
  "20030089",
  "20030090",
  "20030091",
  "20030092",
  "20030093",
  "20030094",
  "20030095",
  "20030096",
  "20030097",
  "20030098",
  "20030099",
  "20030100",
  "20030101",
  "20030102",
  "20030103",
  "20030104",
  "20030105",
  "20030106",
  "20030107",
  "20030108",
  "20030109",
  "20030110",
  "20030111",
  "20030112",
  "20030113",
  "20030114",
  "20030115",
  "20030116",
  "20030117",
  "20030118",
  "20030119",
  "20030120",
  "20030121",
  "20030122",
  "20030123",
  "20030124",
  "20030125",
  "20030126",
  "20030127",
  "20030134",
  "20030135",
  "20030582",
  "20030598",
  "20030872",
  "20040010",
  "20040251",
  "20040453",
  "20040456",
  "20040482",
  "20040802",
  "20060018",
  "20060140",
  "20060298",
  "20060458",
  "20060974",
  "20071024",
  "20090259",
  "20090409",
  "20091077",
  "20100081",
  "20100827",
  "20100836",
  "20100857",
  "20100863",
  "20100874",
  "20110429",
  "20120259"
]
"""Regular season games without RTSS data on NHL.com. Format:: YYYYNNNN where YYYY is the four digit year and NNNN the four digit game number. """

MISS_PLAYOFF_GAMES = [
  "20040134"
  "20060233"
]
"""Playoff games without RTSS data on NHL.com. Format:: YYYYNNNN where YYYY is the four digit year and NNNN the four digit game number. """

TEAMS_BY_ABBR = {
  'ANA': 'Anaheim Ducks', # (1993-94 - present)
  'ARI': 'Arizona Coyotes', # (2014-15 - present)
  'ATF': 'Atlanta Flames', # (1972-73 - 1979-80)
  'ARL': 'Atlanta Trashers', # (1999-00 - 2010-11)
  'BOS': 'Boston Bruins', # (1925-26 - present)
  'BKN': 'Brooklyn Americans', # (1941-1942)
  'BUF': 'Buffalo Sabres', # (1970-71 - present)
  'CGY': 'Calgary Flames', # (1980-81 - present)
  'CLF': 'California Golden Seals', # (1970-71 - 1975-76)
  'CAR': 'Carolina Hurricanes', # (1997-98 - present)
  'CHI': 'Chicago Blackhawks', # (1926-27 - present)
  'CLE': 'Cleveland Barons', # (1976-77 - 1977-78)
  'COR': 'Colorado Rockies', # (1976-77 - 1981-82)
  'COL': 'Colorado Avalanche', # (1995-96 - present)
  'CBJ': 'Columbus Blue Jackets', # (2000-01 - present)
  'DAL': 'Dallas Stars', # (1993-94 - present)
  'DTC': 'Detroit Cougars', # (1926-27 - 1929-30)
  'DTF': 'Detroit Falcons', # (1930-31 - 1931-32)
  'DET': 'Detroit Red Wings', # (1932-33 - present)
  'EDM': 'Edmonton Oilers', # (1979-80 - present)
  'FLA': 'Florida Panthers', # (1993-94 - present)
  'HAM': 'Hamilton Tigers', # (1920-21 - 1924-25)
  'HAR': 'Hartford Whalers', # (1979-80 - 1996-97)
  'KC': 'Kansas City Scouts', # (1974-75 - 1975-76)
  'LA': 'Los Angeles Kings', # (1967-68 - present)
  'MIN': 'Minnesota Wild', # (2000-01 - present)
  'MNS': 'Minnesota North Stars', # (1967-68 - 1992-93)
  'MTL': 'Montreal Canadiens', # (1917-18 - present)
  'MTM': 'Montreal Maroons', # (1924-25 - 1937-38)
  'MTW': 'Montreal Wanderers', # (1917-18)
  'NSH': 'Nashville Predators', # (1998-99 - present)
  'NJ': 'New Jersey Devils', # (1982-83 - present)
  'NYA': 'New York Americans', # (1925-26 - 1940-41)
  'NYI': 'New York Islanders', # (1972-73 - present)
  'NYR': 'New York Rangers', # (1926-27 - present)
  'OAK': 'Oakland Seals', # (1967-68 - 1969-70)
  'PHI': 'Philadelphia Flyers', # (1967-68 - present)
  'PHQ': 'Philadelphia Quakers', # (1930-31)
  'PHO': 'Phoenix Coyotes', # (1996-97 - 2013-14)
  'PIT': 'Pittsburgh Penguins', # (1967-68 - present)
  'PIP': 'Pittsburgh Pirates', # (1925-26 - 1929-30)
  'OTT': 'Ottawa Senators', # (1992-93 - present)
  'OTS': 'Ottawa Senators (orig)', # (1917-18 - 1930-31, 1932-33 - 1933-34)
  'QUE': 'Quebec Nordiques', # (1979-80 - 1994-95)
  'QUB': 'Quebec Bulldogs', # (1919-20)
  'STL': 'St Louis Blues', # (1967-68 - present)
  'STE': 'St Louis Eagles', # (1934-35)
  'SJ': 'San Jose Sharks', # (1991-92 - present)
  'TB': 'Tampa Bay Lightning', # (1992-93 - present)
  'TOR': 'Toronto Maple Leafs', # (1926-27 - present)
  'TRA': 'Toronto Arenas', # (1917-18 - 1918-19)
  'TRS': 'Toronto St Pats', # (1919-20 - 1925-26)
  'VAN': 'Vancouver Canucks', # (1970-71 - present)
  'WSH': 'Washington Capitals', # (1974-75 - present)
  'WIJ': 'Winnipeg Jets (orig)', # (1st) (1979-80 - 1995-96)
  'WPG': 'Winnipeg Jets', # (2011-12 - present)
}


TEAM_TO_ABB = {
  'Anaheim Ducks' : 'ANA' , # (1993-94 - present)
  'ANAHEIM DUCKS' : 'ANA' , # (1993-94 - present)

  'Arizona Coyotes': 'ARI' , # (2014-15 - present)
  'ARIZONA COYOTES': 'ARI' , # (2014-15 - present)

  'Atlanta Flames': 'ATF', # (1972-73 - 1979-80)
  'ATLANTA FLAMES': 'ATF', # (1972-73 - 1979-80)

  'Atlanta Trashers':'ARL' , # (1999-00 - 2010-11)
  'ATLANTA THRASHERS':'ARL' , # (1999-00 - 2010-11)

  'Boston Bruins':'BOS' , # (1925-26 - present)
  'BOSTON BRUINS':'BOS' , # (1925-26 - present)

  'Brooklyn Americans':'BKN' , # (1941-1942)
  'BROOKLYN AMERICANS':'BKN' , # (1941-1942)

  'Buffalo Sabres':'BUF' , # (1970-71 - present)
  'BUFFALO SABRES':'BUF' , # (1970-71 - present)

  'Calgary Flames':'CGY' , # (1980-81 - present)
  'CALGARY FLAMES':'CGY' , # (1980-81 - present)

  'California Golden Seals':'CLF' , # (1970-71 - 1975-76)
  'California Golden Seals':'CLF' , # (1970-71 - 1975-76)

  'Carolina Hurricanes':'CAR' , # (1997-98 - present)
  'CAROLINA HURRICANES':'CAR' , # (1997-98 - present)

  'Chicago Blackhawks':'CHI' , # (1926-27 - present)
  'CHICAGO BLACKHAWKS':'CHI' , # (1926-27 - present)

  'Cleveland Barons':'CLE' , # (1976-77 - 1977-78)
  'Cleveland Barons':'CLE' , # (1976-77 - 1977-78)

  'Colorado Rockies':'COR' , # (1976-77 - 1981-82)
  'Colorado Rockies':'COR' , # (1976-77 - 1981-82)

  'Colorado Avalanche':'COL' , # (1995-96 - present)
  'COLORADO AVALANCHE':'COL' , # (1995-96 - present)

  'Columbus Blue Jackets':'CBJ' , # (2000-01 - present)
  'COLUMBUS BLUE JACKETS':'CBJ' , # (2000-01 - present)

  'Dallas Stars':'DAL' , # (1993-94 - present)
  'DALLAS STARS':'DAL' , # (1993-94 - present)

  'Detroit Cougars':'DTC' , # (1926-27 - 1929-30)
  'Detroit Cougars':'DTC' , # (1926-27 - 1929-30)

  'Detroit Falcons':'DTF' , # (1930-31 - 1931-32)
  'Detroit Falcons':'DTF' , # (1930-31 - 1931-32)

  'Detroit Red Wings':'DET' , # (1932-33 - present)
  'DETROIT RED WINGS':'DET' , # (1932-33 - present)

  'Edmonton Oilers':'EDM' , # (1979-80 - present)
  'EDMONTON OILERS':'EDM' , # (1979-80 - present)

  'Florida Panthers':'FLA' , # (1993-94 - present)
  'FLORIDA PANTHERS':'FLA' , # (1993-94 - present)

  'Hamilton Tigers':'HAM' , # (1920-21 - 1924-25)
  'Hamilton Tigers':'HAM' , # (1920-21 - 1924-25)

  'Hartford Whalers':'HAR' , # (1979-80 - 1996-97)
  'Hartford Whalers':'HAR' , # (1979-80 - 1996-97)

  'Kansas City Scouts':'KC' , # (1974-75 - 1975-76)
  'Kansas City Scouts':'KC' , # (1974-75 - 1975-76)

  'Los Angeles Kings':'LA' , # (1967-68 - present)
  'LOS ANGELES KINGS':'LA' , # (1967-68 - present)

  'Minnesota Wild':'MIN' , # (2000-01 - present)
  'MINNESOTA WILD':'MIN' , # (2000-01 - present)

  'Minnesota North Stars':'MNS' , # (1967-68 - 1992-93)
  'Minnesota North Stars':'MNS' , # (1967-68 - 1992-93)

  'Montreal Canadiens':'MTL' , # (1917-18 - present)
  'MONTREAL CANADIENS':'MTL' , # (1917-18 - present)

  'Montreal Maroons':'MTM' , # (1924-25 - 1937-38)
  'Montreal Maroons':'MTM' , # (1924-25 - 1937-38)

  'Montreal Wanderers':'MTW' , # (1917-18)
  'Montreal Wanderers':'MTW' , # (1917-18)

  'Nashville Predators':'NSH' , # (1998-99 - present)
  'NASHVILLE PREDATORS':'NSH' , # (1998-99 - present)

  'New Jersey Devils':'NJ' , # (1982-83 - present)
  'NEW JERSEY DEVILS':'NJ' , # (1982-83 - present)

  'New York Americans':'NYA' , # (1925-26 - 1940-41)
  'New York Americans':'NYA' , # (1925-26 - 1940-41)

  'New York Islanders':'NYI' , # (1972-73 - present)
  'NEW YORK ISLANDERS':'NYI' , # (1972-73 - present)

  'New York Rangers':'NYR' , # (1926-27 - present)
  'NEW YORK RANGERS':'NYR' , # (1926-27 - present)

  'Oakland Seals':'OAK' , # (1967-68 - 1969-70)
  'Oakland Seals':'OAK' , # (1967-68 - 1969-70)

  'Philadelphia Flyers':'PHI' , # (1967-68 - present)
  'PHILADELPHIA FLYERS':'PHI' , # (1967-68 - present)

  'Philadelphia Quakers':'PHQ' , # (1930-31)
  'Philadelphia Quakers':'PHQ' , # (1930-31)

  'Phoenix Coyotes':'PHO' , # (1996-97 - 2013-14)
  'PHOENIX COYOTES':'PHO' , # (1996-97 - 2013-14)

  'Pittsburgh Penguins':'PIT' , # (1967-68 - present)
  'PITTSBURGH PENGUINS':'PIT' , # (1967-68 - present)

  'Pittsburgh Pirates':'PIP' , # (1925-26 - 1929-30)
  'Pittsburgh Pirates':'PIP' , # (1925-26 - 1929-30)

  'Ottawa Senators':'OTT' , # (1992-93 - present)
  'OTTAWA SENATORS':'OTT' , # (1992-93 - present)

  'Ottawa Senators (orig)':'OTS' , # (1917-18 - 1930-31, 1932-33 - 1933-34)
  'Ottawa Senators (orig)':'OTS' , # (1917-18 - 1930-31, 1932-33 - 1933-34)

  'Quebec Nordiques':'QUE' , # (1979-80 - 1994-95)
  'Quebec Nordiques':'QUE' , # (1979-80 - 1994-95)

  'Quebec Bulldogs':'QUB' , # (1919-20)
  'Quebec Bulldogs':'QUB' , # (1919-20)

  'St Louis Blues':'STL' , # (1967-68 - present)
  'ST LOUIS BLUES':'STL' , # (1967-68 - present)

  'St Louis Eagles':'STE' , # (1934-35)
  'St Louis Eagles':'STE' , # (1934-35)

  'San Jose Sharks':'SJ' , # (1991-92 - present)
  'SAN JOSE SHARKS':'SJ' , # (1991-92 - present)

  'Tampa Bay Lightning':'TB' , # (1992-93 - present)
  'TAMPA BAY LIGHTNING':'TB' , # (1992-93 - present)

  'Toronto Maple Leafs':'TOR' , # (1926-27 - present)
  'TORONTO MAPLE LEAFS':'TOR' , # (1926-27 - present)

  'Toronto Arenas':'TRA' , # (1917-18 - 1918-19)
  'Toronto Arenas':'TRA' , # (1917-18 - 1918-19)

  'Toronto St Pats':'TRS' , # (1919-20 - 1925-26)
  'Toronto St Pats':'TRS' , # (1919-20 - 1925-26)

  'Vancouver Canucks':'VAN' , # (1970-71 - present)
  'VANCOUVER CANUCKS':'VAN' , # (1970-71 - present)

  'Washington Capitals':'WSH' , # (1974-75 - present)
  'WASHINGTON CAPITALS':'WSH' , # (1974-75 - present)

  'Winnipeg Jets (orig)':'WIJ' , # (1st) (1979-80 - 1995-96)
  'Winnipeg Jets (orig)':'WIJ' , # (1st) (1979-80 - 1995-96)

  'Winnipeg Jets':'WPG' , # (2011-12 - present)
  'WINNIPEG JETS':'WPG' , # (2011-12 - present)
}
