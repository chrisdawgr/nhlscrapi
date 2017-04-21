import requests
import sys
from lxml.html import fromstring
from lxml.html import tostring
import lxml
from lxml import etree
from nhlscrapi.scrapr.teamnameparser import team_abbr_parser
from nhlscrapi.constants import TEAM_TO_ABB as ABB

sys.path.append('..')

class getGameSummary(object):
  """docstring for getGameSummary"""
  def __init__(self, game_key):
    super(getGameSummary, self).__init__()
    self.game_key = game_key
    self.html_src = None
    self.url = None
    self.PP = None
    self.teams = None

  def getUrl(self):
    seas, gt, num = self.game_key.to_tuple()
    __domain = 'http://www.nhl.com/'
    url = [ __domain, "scores/htmlreports/", str(seas-1), str(seas),
                "/", "GS", "0", str(gt), ("%04i" % (num)), ".HTM" ]
    url = ''.join(url)
    self.url = url

  def __open(self):
    self.getUrl()
    req = None
    try:
      req = requests.get(self.url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
      })
      html_src = req.text
    except Exception as e:
      print e
      print "error getting html: getGameSummary"
      html_src = "error"
    print self.url
    self.html_src = fromstring(html_src)

  def parseSummary(self):
    teams = {}
    PP = {}
    EV = {}
    self.__open()
    lx_doc = self.html_src

    main = lx_doc.xpath('//*[@id="MainTable"]')[0]
    text_file = open("Output.txt", "w")
    text_file.write(etree.tostring(main, pretty_print=True))
    text_file.close()
    away_team = main.find('.//table[@id="Visitor"]')
    away_team = away_team.findall('.//td[@align="center"]')[-1].text
    home_team = main.find('.//table[@id="Home"]')
    home_team = home_team.findall('.//td[@align="center"]')[-1].text
    teams['home'] = ABB[home_team]
    teams['away'] = ABB[away_team]
    PP[teams['home']] = 0
    PP[teams['away']] = 0
    EV[teams['home']] = 0
    EV[teams['away']] = 0

    scr_summ = main.xpath('child::tr[4]//tr')

    for r in scr_summ:
      if r.get('class') in ['oddColor','evenColor']:
        tds = r.xpath('./td')
        scr = [td.xpath('text()') for td in tds[:8]]
        try:
          if scr[3][0] == 'EV':
            EV[team_abbr_parser(scr[4][0])] += 1
        except Exception:
          continue
        try:
          if scr[3][0] == 'PP':
            PP[team_abbr_parser(scr[4][0])] += 1
        except Exception:
          continue
    pen_sum = main.find('.//table[@id="PenaltySummary"]')
    test = pen_sum.findall('.//table')
    tbl_list = []
    txtList = ["1.txt","2.txt","3.txt","4.txt","5.txt","6.txt","7.txt","8.txt"]
    i = 0
    for t in test:
      if len(t.xpath('.//td[text()="TOT (PN-PIM)"]')) == 1:
        if len(t.xpath('.//td[text()="Power Plays (Goals-Opp./PPTime)"]'))!=0:
          s = lxml.html.tostring(t)
          text_file = open(txtList[i], "w")
          i += 1
          text_file.write(s)
          text_file.close()
          tbl_list.append(t)
    #test:
    a_pen = tbl_list[0].findall('.//td[@align="left"]')
    h_pen = tbl_list[1].findall('.//td[@align="left"]')
    away_pen = a_pen[-1].text
    home_pen = h_pen[-1].text
    away_pen = int(away_pen[away_pen.index('-')+1:away_pen.index('/')])
    home_pen = int(home_pen[home_pen.index('-')+1:home_pen.index('/')])

    PP[teams['home']] = (home_pen,PP[teams['home']])
    PP[teams['away']] = (away_pen,PP[teams['away']])
    self.PP = PP
    self.EV = EV
    self.teams = teams