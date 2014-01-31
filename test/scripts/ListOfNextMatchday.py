'''
Created on 31.01.2014

@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1

'''

import suds
import sys
import locale

locale.setlocale(locale.LC_ALL, '')

## Define League
LEAGUE_NAME = "bl1"
LEAGUE_SAISON = "2013"
LEAGUE_ID = 623

## SOAP Interface
URL = "http://www.openligadb.de/Webservices/Sportsdata.asmx?WSDL"

## Create client
client = suds.client.Client(URL)

## Get Current Group
try:
    group = client.service.GetCurrentGroup(LEAGUE_NAME).groupOrderID
except AttributeError:
    print "n/A"
    sys.exit(1)

## Get Match-List
try:
    matches = client.service.GetMatchdataByGroupLeagueSaison(group, LEAGUE_NAME, LEAGUE_SAISON).Matchdata
except AttributeError:
    print "n/A"
    sys.exit(1)

## iteration
for match in matches:
    if match.matchResults:
        goals =  "[{0}:{1}]".format(match.matchResults.matchResult[0].pointsTeam1, match.matchResults.matchResult[0].pointsTeam2)
    else:
        goals = "[N/A]"
    print """{start_time} - {goals} - {team1} vs. {team2}""".format(team1=match.nameTeam1.encode("utf-8"),
        team2=match.nameTeam2.encode("utf-8"), 
        goals=goals, start_time=match.matchDateTime.strftime("%a, %H:%M Uhr"))
