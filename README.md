python-openligadb-api
=========================

This is a python wrapper class for the openligadb.de api.

 http://www.openligadb.de/Webservices/Sportsdata.asmx
 
___________________________________________________

**Please donate to "DQ6mBVyuboTGwS8JYW11oHwXtxsjNAzkzi" [DOGECOIN]** 

!["Dogecoin Donation QR-Code"](http://github.com/Dirrot/python-openligadb-api/blob/master/img/donation-qr-code.png?raw=true)

___________________________________________________
 
_Methods_
* info
* getAvailGroups
* getAvailLeagues
* getAvailLeaguesBySports
* getAvailSports
* getCurrentGroup
* getCurrentGroupOrderID
* getGoalGettersByLeagueSaison
* getGoalsByLeagueSaison
* getGoalsByMatch
* getLastChangeDateByGroupLeagueSaison
* getLastChangeDateByLeagueSaison
* getLastMatch
* getLastMatchByLeagueTeam
* getMatchByMatchID
* getMatchdataByGroupLeagueSaison
* getMatchdataByGroupLeagueSaisonJSON
* getMatchdataByLeagueDateTime
* getMatchdataByLeagueSaison
* getMatchdataByTeams
* getNextMatch
* getNextMatchByLeagueTeam
* getTeamsByLeagueSaison
___________________________________________________

Here's an example:

```python
from OpenLigaDbApi import API
from datetime import datetime, date, time

if __name__ == '__main__':
    
    '''Sport: Soccer'''
    sportID = "1"
    '''Shortcut of league'''
    leagueShortcut = "bl1"
    '''ID of 1. Fussball Bundesliga 2013/2014'''
    leagueId = "623"
    '''Season of league'''
    leagueSaison = "2013"
    '''No. of matchday'''
    groupOrderID = "1"
    '''ID of Bayern Muenchen'''
    teamID1 = "40"
    '''ID of Borussia Moenchengladbach'''
    teamID2 = "87"
    '''Bayern Muenchen - Borussia Moenchengladbach'''
    matchID = "23711"
    '''Startdate of 1.BL 2013'''
    fromDateTime = datetime.combine(datetime(2013, 8, 9),time(0, 0 ,0))
    '''Enddate'''
    toDateTime = datetime.combine(date.today(),time(0, 0, 0))
     
    api = API()
    
    info = api.info()
    print "Info: ", info

    availGroups = api.getAvailGroups(leagueShortcut, leagueSaison)
    print "Available Groups: ", availGroups
    
    availLeagues = api.getAvailLeagues()
    print "Available Leagues: ", availLeagues
    
    availLeaguesBySports = api.getAvailLeaguesBySports(sportID)
    print "Available Leagues By Sports: ", availLeaguesBySports
    
    availSports = api.getAvailSports()
    print "Available Sports: ", availSports
    
    currentGroup = api.getCurrentGroup(leagueShortcut)
    print "Current Group: ", currentGroup
    
    currentGroupOrderID = api.getCurrentGroupOrderID(leagueShortcut)
    print "Current Group Order ID: ", currentGroupOrderID
    
    goalGettersByLeagueSaison = api.getGoalGettersByLeagueSaison(leagueShortcut, leagueSaison)
    print "Goal Getters By League Saison: ", goalGettersByLeagueSaison
    
    goalsByLeagueSaison = api.getGoalsByLeagueSaison(leagueShortcut, leagueSaison)
    print "Goals By League Saison: ", goalsByLeagueSaison
    
    goalsByMatch = api.getGoalsByMatch(matchID)
    print "Goals By Match: ", goalsByMatch
    
    lastChangeDataByGroupLeagueSaison = api.getLastChangeDateByGroupLeagueSaison(groupOrderID, leagueShortcut, leagueSaison)
    print "Last Change Data By Group League Saison: ", lastChangeDataByGroupLeagueSaison
    
    lastChangeDataByLeagueSaison = api.getLastChangeDateByLeagueSaison(leagueShortcut, leagueSaison)
    print "Last Change Data By League Saison: ", lastChangeDataByLeagueSaison
    
    lastMatch = api.getLastMatch(leagueShortcut)
    print "Last Match: ", lastMatch
    
    lastMatchByLeagueTeam = api.getLastMatchByLeagueTeam(leagueId, teamID1)
    print "Last Match By League Team: ", lastMatchByLeagueTeam
    
    matchByMatchID = api.getMatchByMatchID(matchID)
    print "Match By MatchID: ", matchByMatchID
    
    matchdataByGroupLeagueSaison = api.getMatchdataByGroupLeagueSaison(groupOrderID, leagueShortcut, leagueSaison)
    print "Match Data By Group League Saison: ", matchdataByGroupLeagueSaison
    
    matchdataByGroupLeagueSaisonJSON = api.getMatchdataByGroupLeagueSaisonJSON(groupOrderID, leagueShortcut, leagueSaison)
    print "Match Data By Group League Saison JSON: ", matchdataByGroupLeagueSaisonJSON
    
    matchdataByLeagueDateTime = api.getMatchdataByLeagueDateTime(fromDateTime, toDateTime, leagueShortcut)
    print "Match Data By League Date Time: ", matchdataByLeagueDateTime
    
    matchdataByLeagueSaison = api.getMatchdataByLeagueSaison(leagueShortcut, leagueSaison)
    print "Match Data By League Saison: ", matchdataByLeagueSaison
    
    matchdataByTeams = api.getMatchdataByTeams(teamID1, teamID2)
    print "Match Data By Teams: ", matchdataByTeams
    
    nextMatch = api.getNextMatch(leagueShortcut)
    print "Next Match: ", nextMatch
    
    nextMatchByLeagueTeam = api.getNextMatchByLeagueTeam(leagueId, teamID1)
    print "Next Match By League Team: ", nextMatchByLeagueTeam
    
    teamsByLeagueSaison = api.getTeamsByLeagueSaison(leagueShortcut, leagueSaison)
    print "Teams By League Saison: ", teamsByLeagueSaison
```
