from sportsreference.nfl.roster import Player , Roster
from sportsreference.nfl.teams import Teams

from sportsreference.nfl.boxscore import Boxscore
from sportsreference.nfl.schedule import Schedule

import pprint

# DOCUMENTAION
#https://sportsreference.readthedocs.io/en/stable/nfl.html#roster


def main():
    arr = GetAllTeamsInNFL()

    print('Welcome to the stat spread!\n')
    print('1: Find stats of a certain team')
    print('2: Compare team stats')
    print()

    option = input('Please choose an option: ')

    if option =='1':
        TeamSatCheck(arr)

    elif option == '2':
        CompareTeams(arr)

def AllPlayersInTeam( Team_ID ):

    #("Team ID" ,"YEAR", PLAYER ID/NAME -> True/False)
    playerIds = []
    team = Roster(Team_ID , "2020" , True)
    for player in team.players:
        playerIds.append(player)
    return playerIds

def GetAllTeamsInNFL():
    teamsArr = []
    NFLteams = Teams("2020")

    for team in NFLteams:
        # print(team.name)
        # print(team.abbreviation)
        # print()
        teamsArr.append(team)

    return teamsArr
    
def TeamSatCheck(arr):

        print('\n\nTeam name abbreviations\n')
        for x in range(0,len(arr) , 1 ):
            print('{}: {} ----> {}'.format(x , arr[x].name , arr[x].abbreviation)   )
        
        
        option = int(input('Please choose an option using the numbers: '))


        ChosenTeam = arr[option]
        chosenId = arr[option].abbreviation
        


        print('\n\n***PLAYERS***\n')
        chosen_player_ids = AllPlayersInTeam(chosenId) #grabbing all players from team
        PlayerObjects = [] #player objects in a list
        for y in range(0 , len(chosen_player_ids) , 1):
            player = Player( chosen_player_ids[y] )
            PlayerObjects.append(player)
            print(player.name)



        #team stats
        # print('{} -- {}'.format( 'dataframe' , ChosenTeam.dataframe) )
        print('\n\n\t{} -- {}'.format( 'abbreviation' , ChosenTeam.abbreviation) )
        print('\t{} -- {}'.format( 'defensive_simple_rating_system' , ChosenTeam.defensive_simple_rating_system) )
        print('\t{} -- {}'.format( 'first_downs' , ChosenTeam.first_downs) )
        print('\t{} -- {}'.format( 'first_downs_from_penalties' , ChosenTeam.first_downs_from_penalties) )
        print('\t{} -- {}'.format( 'fumbles' , ChosenTeam.fumbles) )
        print('\t{} -- {}'.format( 'games_played' , ChosenTeam.games_played) )
        print('\t{} -- {}'.format( 'interceptions' , ChosenTeam.interceptions) )
        print('\t{} -- {}'.format( 'losses' , ChosenTeam.losses) )
        print('\t{} -- {}'.format( 'margin_of_victory' , ChosenTeam.margin_of_victory) )
        print('\t{} -- {}'.format( 'name' , ChosenTeam.name) )
        print('\t{} -- {}'.format( 'offensive_simple_rating_system' , ChosenTeam.offensive_simple_rating_system) )
        print('\t{} -- {}'.format( 'pass_attempts' , ChosenTeam.pass_attempts) )
        print('\t{} -- {}'.format( 'pass_completions' , ChosenTeam.pass_completions) )
        print('\t{} -- {}'.format( 'pass_first_downs' , ChosenTeam.pass_first_downs) )
        print('\t{} -- {}'.format( 'pass_net_yards_per_attempt' , ChosenTeam.pass_net_yards_per_attempt) )
        print('\t{} -- {}'.format( 'pass_touchdowns' , ChosenTeam.pass_touchdowns) )
        print('\t{} -- {}'.format( 'pass_yards' , ChosenTeam.pass_yards) )
        print('\t{} -- {}'.format( 'penalties' , ChosenTeam.penalties) )
        print('\t{} -- {}'.format( 'percent_drives_with_points' , ChosenTeam.percent_drives_with_points) )
        print('\t{} -- {}'.format( 'percent_drives_with_turnovers' , ChosenTeam.percent_drives_with_turnovers) )
        print('\t{} -- {}'.format( 'plays' , ChosenTeam.plays) )
        print('\t{} -- {}'.format( 'points_against' , ChosenTeam.points_against) )
        print('\t{} -- {}'.format( 'points_contributed_by_offense' , ChosenTeam.points_contributed_by_offense) )
        print('\t{} -- {}'.format( 'points_difference' , ChosenTeam.points_difference) )
        print('\t{} -- {}'.format( 'points_for' , ChosenTeam.points_for) )
        print('\t{} -- {}'.format( 'post_season_result' , ChosenTeam.post_season_result) )
        print('\t{} -- {}'.format( 'rank' , ChosenTeam.rank) )
        print('\t{} -- {}'.format( 'rush_attempts' , ChosenTeam.rush_attempts) )
        print('\t{} -- {}'.format( 'rush_first_downs' , ChosenTeam.rush_first_downs) )
        print('\t{} -- {}'.format( 'rush_touchdowns' , ChosenTeam.rush_touchdowns) )
        print('\t{} -- {}'.format( 'rush_yards' , ChosenTeam.rush_yards) )
        print('\t{} -- {}'.format( 'rush_yards_per_attempt' , ChosenTeam.rush_yards_per_attempt) )
        print('\t{} -- {}'.format( 'simple_rating_system' , ChosenTeam.simple_rating_system) )
        print('\t{} -- {}'.format( 'strength_of_schedule' , ChosenTeam.strength_of_schedule) )
        print('\t{} -- {}'.format( 'turnovers' , ChosenTeam.turnovers) )
        print('\t{} -- {}'.format( 'win_percentage' , ChosenTeam.win_percentage) )
        print('\t{} -- {}'.format( 'wins' , ChosenTeam.wins) )
        print('\t{} -- {}'.format( 'yards' , ChosenTeam.yards) )
        print('\t{} -- {}'.format( 'yards_from_penalties' , ChosenTeam.yards_from_penalties) )
        print('\t{} -- {}'.format( 'yards_per_play' , ChosenTeam.yards_per_play) )
        # print('\t{} -- {}'.format( 'roster' , ChosenTeam.roster) )
        # print('\t{} -- {}'.format( 'schedule' , str( ChosenTeam.schedule ) ) )


        # Trying to add all the functions of Player into stats dictionary

        # for plObject in range(len(PlayerObjects)):
        #     iteration = PlayerObjects[plObject]

def CompareTeams(arr):
        #first team
        print('\n\nPlease Choose First Team To Compare\n')
        for x in range(0,len(arr) , 1 ):
            print('{}: {} ----> {}'.format(x , arr[x].name , arr[x].abbreviation)   )
        option1 = int(input('Please choose an option using the numbers: '))

         #second team
        print('\n\nPlease Choose Scond Team To Compare\n')
        for x in range(0,len(arr) , 1 ):
            print('{}: {} ----> {}'.format(x , arr[x].name , arr[x].abbreviation)   )
        option2 = int(input('Please choose an option using the numbers: '))


        TeamOne = arr[option1]
        TeamTwo = arr[option2]

        team_ONE_Stats =  []
        team_TWO_Stats =  []



        attributes = [

            # 'abbreviation' ,
            # 'dataframe' ,
            'defensive_simple_rating_system' ,
            'first_downs' ,
            'first_downs_from_penalties' ,
            # 'fumbles' ,
            'games_played' ,
            'interceptions' ,
            # 'losses' ,
            'margin_of_victory' ,
            # 'name' ,
            'offensive_simple_rating_system' ,
            # 'pass_attempts' ,
            'pass_completions' ,
            'pass_first_downs' ,
            'pass_net_yards_per_attempt' ,
            'pass_touchdowns' ,
            'pass_yards' ,
            # 'penalties' ,
            'percent_drives_with_points' ,
            # 'percent_drives_with_turnovers' ,
            'plays' ,
            # 'points_against' ,
            'points_contributed_by_offense' ,
            'points_difference' ,
            'points_for' ,
            'post_season_result' ,
            'rank' ,
            # 'roster' ,
            # 'rush_attempts' ,
            'rush_first_downs' ,
            'rush_touchdowns' ,
            'rush_yards' ,
            'rush_yards_per_attempt' ,
            # 'schedule' ,
            'simple_rating_system' ,
            # 'strength_of_schedule' ,
            # 'turnovers' ,
            'win_percentage' ,
            'wins' ,
            'yards' ,
            'yards_from_penalties' ,
            'yards_per_play' ,

        ]







        # team_ONE_Stats.append(TeamOne.abbreviation)
        # team_ONE_Stats.append(TeamOne.dataframe)
        team_ONE_Stats.append(TeamOne.defensive_simple_rating_system)
        team_ONE_Stats.append(TeamOne.first_downs)
        team_ONE_Stats.append(TeamOne.first_downs_from_penalties)
        # team_ONE_Stats.append(TeamOne.fumbles)
        team_ONE_Stats.append(TeamOne.games_played)
        team_ONE_Stats.append(TeamOne.interceptions)
        # team_ONE_Stats.append(TeamOne.losses)
        team_ONE_Stats.append(TeamOne.margin_of_victory)
        # team_ONE_Stats.append(TeamOne.name)
        team_ONE_Stats.append(TeamOne.offensive_simple_rating_system)
        # team_ONE_Stats.append(TeamOne.pass_attempts)
        team_ONE_Stats.append(TeamOne.pass_completions)
        team_ONE_Stats.append(TeamOne.pass_first_downs)
        team_ONE_Stats.append(TeamOne.pass_net_yards_per_attempt)
        team_ONE_Stats.append(TeamOne.pass_touchdowns)
        team_ONE_Stats.append(TeamOne.pass_yards)
        # team_ONE_Stats.append(TeamOne.penalties)
        team_ONE_Stats.append(TeamOne.percent_drives_with_points)
        # team_ONE_Stats.append(TeamOne.percent_drives_with_turnovers)
        team_ONE_Stats.append(TeamOne.plays)
        # team_ONE_Stats.append(TeamOne.points_against)
        team_ONE_Stats.append(TeamOne.points_contributed_by_offense)
        team_ONE_Stats.append(TeamOne.points_difference)
        team_ONE_Stats.append(TeamOne.points_for)
        team_ONE_Stats.append(TeamOne.post_season_result)
        team_ONE_Stats.append(TeamOne.rank)
        # team_ONE_Stats.append(TeamOne.roster)
        # team_ONE_Stats.append(TeamOne.rush_attempts)
        team_ONE_Stats.append(TeamOne.rush_first_downs)
        team_ONE_Stats.append(TeamOne.rush_touchdowns)
        team_ONE_Stats.append(TeamOne.rush_yards)
        team_ONE_Stats.append(TeamOne.rush_yards_per_attempt)
        # team_ONE_Stats.append(TeamOne.schedule)
        team_ONE_Stats.append(TeamOne.simple_rating_system)
        # team_ONE_Stats.append(TeamOne.strength_of_schedule)
        # team_ONE_Stats.append(TeamOne.turnovers)
        team_ONE_Stats.append(TeamOne.win_percentage)
        team_ONE_Stats.append(TeamOne.wins)
        team_ONE_Stats.append(TeamOne.yards)
        team_ONE_Stats.append(TeamOne.yards_from_penalties)
        team_ONE_Stats.append(TeamOne.yards_per_play)






        # team_TWO_Stats.append(TeamTwo.abbreviation)
        # team_TWO_Stats.append(TeamTwo.dataframe)
        team_TWO_Stats.append(TeamTwo.defensive_simple_rating_system)
        team_TWO_Stats.append(TeamTwo.first_downs)
        team_TWO_Stats.append(TeamTwo.first_downs_from_penalties)
        # team_TWO_Stats.append(TeamTwo.fumbles)
        team_TWO_Stats.append(TeamTwo.games_played)
        team_TWO_Stats.append(TeamTwo.interceptions)
        # team_TWO_Stats.append(TeamTwo.losses)
        team_TWO_Stats.append(TeamTwo.margin_of_victory)
        # team_TWO_Stats.append(TeamTwo.name)
        team_TWO_Stats.append(TeamTwo.offensive_simple_rating_system)
        # team_TWO_Stats.append(TeamTwo.pass_attempts)
        team_TWO_Stats.append(TeamTwo.pass_completions)
        team_TWO_Stats.append(TeamTwo.pass_first_downs)
        team_TWO_Stats.append(TeamTwo.pass_net_yards_per_attempt)
        team_TWO_Stats.append(TeamTwo.pass_touchdowns)
        team_TWO_Stats.append(TeamTwo.pass_yards)
        # team_TWO_Stats.append(TeamTwo.penalties)
        team_TWO_Stats.append(TeamTwo.percent_drives_with_points)
        # team_TWO_Stats.append(TeamTwo.percent_drives_with_turnovers)
        team_TWO_Stats.append(TeamTwo.plays)
        # team_TWO_Stats.append(TeamTwo.points_against)
        team_TWO_Stats.append(TeamTwo.points_contributed_by_offense)
        team_TWO_Stats.append(TeamTwo.points_difference)
        team_TWO_Stats.append(TeamTwo.points_for)
        team_TWO_Stats.append(TeamTwo.post_season_result)
        team_TWO_Stats.append(TeamTwo.rank)
        # team_TWO_Stats.append(TeamTwo.roster)
        # team_TWO_Stats.append(TeamTwo.rush_attempts)
        team_TWO_Stats.append(TeamTwo.rush_first_downs)
        team_TWO_Stats.append(TeamTwo.rush_touchdowns)
        team_TWO_Stats.append(TeamTwo.rush_yards)
        team_TWO_Stats.append(TeamTwo.rush_yards_per_attempt)
        # team_TWO_Stats.append(TeamTwo.schedule)
        team_TWO_Stats.append(TeamTwo.simple_rating_system)
        # team_TWO_Stats.append(TeamTwo.strength_of_schedule)
        # team_TWO_Stats.append(TeamTwo.turnovers)
        team_TWO_Stats.append(TeamTwo.win_percentage)
        team_TWO_Stats.append(TeamTwo.wins)
        team_TWO_Stats.append(TeamTwo.yards)
        team_TWO_Stats.append(TeamTwo.yards_from_penalties)
        team_TWO_Stats.append(TeamTwo.yards_per_play)


        Score1 = 0
        Score2 = 0
        tied = 0
        NoneCheck = 0
        for x in range(0 , len(team_ONE_Stats) , 1):
            if team_ONE_Stats[x] == None:
                NoneCheck = x
                team_ONE_Stats[x] = 0
                team_TWO_Stats[x] = 0


            if float(team_ONE_Stats[x]) > float(team_TWO_Stats[x]):
                Score1 += 1
            elif  float(team_TWO_Stats[x]) > float(team_ONE_Stats[x]):
                Score2 += 1
            else:
                tied += 1


        for x in range(len(attributes)):
            print('\n**{}**\n{}\n{}\n'.format(attributes[x] , team_ONE_Stats[x] , team_TWO_Stats[x]))


        
        print('\nComparison Results\n {} scored: {}\n {} scored: {}\nTies: {}'.format( TeamOne.name,Score1 , TeamTwo.name,Score2 , tied))


        if Score1>Score2:
            print('{} Win!'.format(TeamOne.name))
        else:
            print('{} Win!'.format(TeamTwo.name))

#helper functions
def add(dict, key, value):
    dict[key] = value 



main()