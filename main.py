from dataclasses import dataclass
from typing import List, Dict

import random




@dataclass
class Team:
    num: int
    name: str
    overall: int




TEAMS: Dict[str, Team] = {"Boston": Team(1, "Celtics",91), 
"Brooklyn": Team(2, "Nets", 95), "Denver": Team(3, "Nuggets", 90), "Golden State": Team(4, "Warriors", 88),
 "Los Angeles": Team(5, "Lakers", 93), "Milwaukee": Team(6, "Bucks", 92),
  "Phoenix": Team(7, "Suns", 93), "Toronto": Team(8, "Raptors", 85),
  "Minnesota": Team(9, "Timberwolves", 85),
"Portland": Team(10, "Trail Blazers", 87),
"LA": Team(11, "Clippers", 92),
 "Philadelphia": Team(12, "76ers", 90),
  "Chicago": Team(13, "Bulls", 83),
"New York": Team(14, "Knicks", 80),
 "Oklahoma City": Team(15, "Thunder",80 ),
 "Miami": Team(16, "Heat", 84),
 "San Antonio": Team(17, "Spurs", 78),
 "Charlotte": Team(18, "Hornets", 77),
 "Houston": Team(19, "Rockets", 78),
 "Dallas": Team(20, "Mavericks", 86),
 "Orlando": Team(21, "Magic", 79),
"Utah": Team(22, "Jazz", 89),
 "Memphis": Team(23, "Grizzlies", 85),
"Washington": Team(24, "Wizards", 83),
"Alanta": Team(25, "Hawks",80 ), "New Orleans": Team(26, "Pelicans", 78), "Cleveland": Team(27, "Cavaliers", 73), "Detroit": Team(28, "Pistons", 65), "Indiana": Team(29, "Pacers", 73), "Sacramento": Team(30, "Kings", 73)
}


@dataclass
class Player:
    pshot: int
    pdunk: int
    playup: int
    pmidr: int
    preb: int

@dataclass
class Opposition:
    oshot: int
    odunk: int
    olayup: int
    omidr: int
    oreb: int


@dataclass
class Stat:
    win: int
    loss: int

@dataclass
class User:
    team: str
    player: str
    possession: str
    opponent: str
    opponentplayer: str
    

@dataclass
class Overall:
    shooting: int
    dunk: int
    layup: int
    midrange: int
    rebound: int



OVERALLSTAT: Dict[str,Overall] = { "Jrue Holiday": Overall(3, 4, 2, 2, 3), #bucks1
"Khris Middleton": Overall(2, 2, 2, 2, 5), 
"Pj Tucker": Overall( 7, 6, 4, 4, 3), 
"Giannis Antetokumpo": Overall(6, 2, 2, 3, 2), 
"Brook Lopez": Overall(6, 2, 2, 3, 2),
#celtics2
"Marcus Smart": Overall(4, 3, 2, 2, 5), 
"Jalen Brown": Overall(2, 3, 2, 2, 5), 
"Josh Richardson": Overall(2, 4, 3, 3, 5),
"Jayson Tatum": Overall(3, 2, 2, 2, 3),
"Robin Williams II": Overall(7, 4, 3, 6, 3),
#clippers3
"Patrick Beverly": Overall(5, 4, 2, 3, 3),
"Paul George": Overall(3, 2, 2, 2, 3), 
"Kawhi Leonard": Overall(3, 2, 2, 2, 3), 
"Marcus Moris Sr.": Overall(6, 3, 3, 5, 2), 
"Ivaci Zubac": Overall(10, 5, 5, 6, 2),
#Trail Blazers4
"Damien Lillard": Overall(2, 2, 2, 2, 5),
"Cj McCollum": Overall(4, 3, 3, 2, 5),
"Norman Powell": Overall(6, 4, 3, 5, 4),
"Robert Covington": Overall(7, 5, 5, 5, 3),
"Jusef Nurkic": Overall(4, 3, 2, 3, 2),
#Suns5
"Chris Paul": Overall(2, 8, 2, 2, 6),
"Devin Booker": Overall(2, 4, 2, 3, 6),
"Mikal Bridges": Overall(5, 2, 2, 4, 4),
"Jae Crowder": Overall(4, 3, 3, 4, 3),
"Deandre Ayton": Overall(5, 2, 2, 3, 2),
#Warriors6
"Stephen Curry": Overall(2, 9, 2, 3, 6),
"Klay Thompson": Overall(2, 8, 2, 3, 6),
"Andrew Wiggins": Overall(4, 2, 2, 3, 5),
"Draymond Green": Overall(4, 2, 3, 3, 5),
"James Wiseman": Overall(7, 4, 3, 7, 2),
#Raptors7
"Kyle Lowry": Overall(3, 7, 3, 3, 7),
"Fred Vanfleet": Overall(3, 3, 4, 3, 4),
"OG Anunoby": Overall(5, 3, 3, 4, 3),
"Pacal Siakam": Overall(3, 4, 3, 4, 3),
"Khem Birch": Overall(8, 3, 4, 4, 3),
#Nuggets8
"Jamal Murray": Overall(2, 4, 2, 2, 5),
"Will Barton": Overall(4, 3, 3, 3, 5),
"Michael Porter Jr.": Overall(2, 3, 2, 3, 3),
"Aaron Gordon": Overall(4, 2, 3, 3, 4),
"Nikola Jokic": Overall(3, 2, 2, 2, 2),
#Nets9
"Kyrie Irving": Overall(2, 5, 2, 2, 6),
"James Harden": Overall(2, 4, 2, 2, 9),
"Kevin Durant": Overall(2, 2, 2, 2, 2),
"Blake Griffin": Overall(4, 2, 2, 2, 2),
"Lamarcus Aldridge": Overall(3, 2, 2, 2, 2),
#Timberwolves10
"D'Angelo Russel": Overall(3, 4, 2, 2, 4),
"Anthony Edwards": Overall(4, 2, 2, 3, 4),
"Josh Okogie": Overall(4, 3, 3, 4, 3),
"Jaden McDaniels": Overall(4, 3, 3, 4, 3),
"Karl Anthony-Towns": Overall(3, 2, 2, 2, 2),
#Lakers11
"Russell Westbrook": Overall(4, 2, 2, 2, 4),
"Alex Carusso": Overall(4, 3, 3, 4, 4),
"Lebron James": Overall(2, 2, 2, 2, 2),
"Anthony Davis": Overall(3, 2, 2, 3, 2),
"Andre Drummond": Overall(5, 2, 2, 3, 2),
#76ers12
"Ben Simmons": Overall( 10, 2, 2, 5, 2),
"Seth Curry": Overall( 2, 3, 3, 3, 6),
"Furkan Korkmaz": Overall( 4, 3, 3, 3, 4),
"Tobias Harris": Overall( 3, 3, 3, 3, 3),
"Joel Embiid": Overall( 3, 2, 2, 2, 2),
#Bulls13
"Lonzo Ball": Overall( 3, 4, 2, 2, 5),
"Zach LaVine": Overall( 2, 2, 2, 3, 4),
"DeMar DeRozan": Overall( 3, 3, 2, 2, 4),
"Patrick Williams": Overall( 5, 3, 3, 3, 2),
"Nikola Vucevic": Overall( 3, 2, 2, 3, 2),
#Cavaliers14
"Darius Garland": Overall( 4, 3, 3, 3, 5),
"Collin Sexton": Overall( 2, 3, 3, 3, 6),
"Isaac Okoro": Overall( 4, 3, 3, 3, 3),
"Kevin Love": Overall( 2, 3, 2, 3, 2),
"Evan Mobley": Overall( 4, 4, 3, 3, 2),
#Grizzlies15
"Ja Morant": Overall( 3, 3, 2, 2, 5),
"Dillon Brooks": Overall( 4, 3, 3, 4, 2),
"Kyle Anderson": Overall( 3, 3, 4, 3, 2),
"Jaret Jackson Jr.": Overall( 5, 3, 3, 3, 2),
"Steven Adams": Overall( 6, 2, 2, 5, 2),
#Hawks16
"Trae Young": Overall( 2, 6, 3, 2, 8),
"Bogdan Bogdanovic": Overall( 3, 4, 2, 4, 3),
"Kevin Huerter": Overall( 4, 3, 2, 3, 3),
"John Collins": Overall( 4, 3, 3, 3,2),
"Clint Capela": Overall( 6, 3, 2, 5, 2),
#Heat17
"Tyler Herro": Overall( 2, 5, 3, 2, 8),
"Duncan Robinson": Overall( 4, 3, 3, 2, 3),
"Jimmy Butler": Overall( 3, 2, 2, 2, 4),
"Markieff Morris": Overall( 5, 2, 2, 4, 2),
"Bam Adebayo": Overall( 3, 2, 2, 3, 2),
#Hornets18
"LaMelo Ball": Overall( 3, 4, 3, 3, 4),
"Terry Rozier": Overall( 5, 4, 3, 4, 4),
"Gordon Hayward": Overall( 2, 2, 2, 3, 5),
"P.J. Washington": Overall( 5, 3, 3, 4, 2),
"Mason Plumlee": Overall( 4, 2, 3, 3, 2),
#Jazz19
"Mike Conley": Overall( 3, 2, 2, 2, 7),
"Donavan Mitchell": Overall( 2, 2, 2, 2, 6),
"Bojan Bogdanovic": Overall( 4, 3, 3, 3, 2),
"Royce O'Neale": Overall( 5, 4, 4, 4, 2),
"Rudy Gobert": Overall( 4, 2, 2, 2, 2),
#Kings20
"DeArron Fox": Overall( 2, 4, 3, 2, 6),
"Buddy Hield": Overall( 2, 4, 3, 3, 6),
"Harrison Barnes": Overall( 3, 2, 2, 2, 3),
"Marvin Bagley III": Overall( 4, 2, 2, 3, 2),
"Richaun Holmes": Overall( 6, 4, 4, 4, 2),
#Knicks21
"Kemba Walker": Overall( 2, 3, 2, 2, 8),
"Evan Founier": Overall( 2, 4, 3, 2, 7),
"RJ Barrett": Overall( 2, 3, 3, 3, 3),
"Julius Randle": Overall( 3, 2, 2, 2, 3),
"Mitchell Robinson": Overall( 4, 3, 3, 3, 2),
#Magic22
"Cole Anthony": Overall( 4, 3, 3, 3, 6),
"Gary Harris": Overall( 3, 3, 3, 3, 3),
"Dwayne Bacon": Overall( 4, 3, 3, 3, 4),
"James Ennis III": Overall( 5, 4, 3, 3, 2),
"Wendell Carter Jr.": Overall( 6, 3, 3, 5, 2),
#Mavericks23
"Luka Doncic": Overall( 2, 2, 2, 2, 8),
"Tim Hardaway Jr.": Overall( 2, 2, 3, 3, 4),
"Dorian Finney-Smith": Overall( 4, 3, 3, 4, 3),
"Kristaps Porzingus": Overall( 3, 3, 3, 3, 3),
"Dwight Powell": Overall( 4, 3, 3, 3, 2),
#Pacers24
"Malcolm Brogdon": Overall( 3, 3, 3, 3, 6),
"Caris LeVert": Overall( 2, 3, 3, 3, 7),
"T.J. Warren": Overall( 4, 3, 3, 4, 3),
"Domantas Sabonis": Overall( 3, 3, 3, 3, 4),
"Myles Turner": Overall( 4, 3, 3, 4, 3),
#Pelicans25
"Nickeil Alexander-Walker": Overall( 3, 3, 3, 4, 6),
"Devonte' Graham": Overall( 3, 3, 3, 4, 6),
"Brandon Ingram": Overall( 3, 3, 3, 3, 3),
"Zion Williamson": Overall( 4, 2, 2, 5, 2),
"Jonas Valanciunas": Overall( 4, 3, 3, 3, 2),
#Pistons26
"Killian Hayes": Overall( 3, 3, 3, 4, 6),
"Cade Cunningham": Overall( 4, 4, 4, 4, 4),
"Saddiq Bey": Overall( 5, 4, 3, 4, 3),
"Jerami Grant": Overall( 3, 4, 3, 5, 4),
"Isaiah Stewart": Overall( 5, 3, 3, 5, 2),
#Rockets27
"John Wall": Overall( 3, 2, 2, 3, 4),
"Kevin Porter Jr.": Overall( 3, 3, 3, 4, 5),
"Jalen Green": Overall( 4, 3, 3, 4, 2),
"Daniel Theis": Overall( 4, 3, 2, 4, 2),
"Christian Wood": Overall( 5, 3, 2, 4, 2),
#Spurs28
"Dejounte Murray": Overall( 3, 3, 3, 3, 6),
"Derrick White": Overall( 4, 3, 3, 4, 5),
"Devin Vassell": Overall( 4, 3, 2, 4, 5),
"Keldon Johnson": Overall( 3, 3, 2, 4, 2),
"Jakob Poeltl": Overall( 5, 3, 3, 4, 2),
#Wizards29
"Spencer Dinwiddie": Overall( 3, 2, 2, 3, 4),
"Bradley Beal": Overall( 2, 2, 2, 2, 5),
"Kyle Kuzma": Overall( 3, 3, 3, 3, 4),
"Rui Hachimura": Overall( 4, 2, 2, 3, 3),
"Thomas Bryant ": Overall( 5, 4, 4, 3, 2),
#Thunder30
"Shai Gilgeous-Alexander": Overall( 2, 3, 3, 2, 6),
"Luguentz Dort": Overall( 3, 3, 3, 3, 4),
"Aleksej Pokusevski": Overall( 4, 3, 3, 4, 3),
"Darius Bazley": Overall( 4, 3, 3, 4, 5),
"Isaiah Roby": Overall( 5, 3, 2, 4, 2),
}





def opponent(user: User, opponent_roster: List, face: Opposition)-> str:
    while True:
        opponent = random.randint(1,30)
        for team, k in TEAMS.items():
            if opponent == k.num:
                user.opponent = f"{team} {k.name}"
                with open(f"Roster/{k.name}.txt", "r")as f: 
                    u = f.readlines()
                    for i in u:
                        i = i.strip()
                        opponent_roster.append(i)
                user.opponentplayer = random.choice(opponent_roster)
        for name, s in OVERALLSTAT.items():
                if user.opponentplayer == name:
                        
                    face.oshot = s.shooting
                    face.odunk = s.dunk
                    face.olayup = s.layup
                    face.omidr = s.midrange
                    face.oreb = s.rebound
                    
        if user.opponent != user.team:
                    print(f"\033[34m~ You will be playing against:\n -{user.opponent}: {user.opponentplayer} -\n\033[0m")

                        
                            
                    return user.opponent
        elif user.opponent == user.team:
                    opponent_roster.clear()
                    pass
          
      
  

   


def points(user: User,stat: Stat, face: Opposition, you: Player) -> None: 
    
    print(f"You ({user.player}'s) Stats:\nDunk: {you.pdunk}\nLayup: {you.playup}\nMid-Range Shooting: {you.pmidr}\n3 Point Shooting: {you.pshot}\nRebound: {you.preb}\n")

    print(f"Opponent ({user.opponentplayer}'s) Stats:\nDunk: {face.odunk}\nLayup: {face.olayup}\nMid-Range Shooting: {face.omidr}\n3 Point Shooting: {face.oshot}\nRebound: {face.oreb}\n")
   
    score = 0
    opponent_score = 0
    possession = random.randint(1,2)
    if possession == 1:
        user.possession = "Offense"
    else:
        user.possession = "Defense"
    
    while True:
        if score >= 30 or opponent_score >= 30:
                if opponent_score > score:
                    stat.loss += 1
                    break
                elif score > opponent_score:
                    stat.win += 1
                    break
        elif user.possession == "Offense":
            print(f"{user.team}: {score}")
            print(f"{user.opponent}: {opponent_score}")
            print("\033[33m")
            print(" ____________________________")
            print("|  1. Layup: [2 points]      |")
            print("|  2. Dunk: [2 points]       |")
            print("|  3. Mid-range: [2 points]  |")
            print("|  4. 3 pointer: [3 points]  |")
            print("|____________________________|")
            action = input("\033[0mWhat do you want to do? ")
            
                
            
        
        
            if action == "1":
                chance = random.randint(1,you.playup)
                if chance == 1:
                    print(f"\033[32m{user.player} drives and the layup is good.\033[0m")
                    score += 2
                
                    user.possession = "Defense"
                    
                else:
                    rebound = random.randint(1,you.preb)
                    if rebound == 1:
                        print(f"\033[36m{user.player} misses the layup but he gets his own rebound\033[0m")
                        user.possession == "Offense"
                    else:
                        print(f"\033[31m{user.player} blew the layup\033[0m")
                        user.possession = "Defense"
                   
            elif action == "2":
                chance = random.randint(1,you.pdunk)
                if chance == 1:
                    print(f"\033[32mOOOOOH and a monster jam from {user.player}.\33[0m")
                    score += 2
                    
                    user.possession = "Defense"
                else:
                    rebound = random.randint(1, you.preb)
                    if rebound == 1:
                        print(f"\033[36m{user.player} misses but he gets the rebound\033[0m")
                        user.possession = "Offense"
                        pass
                    else:
                        print(f"\033[31m{user.player} goes for the dunk and misses\033[0m")
                        user.possession = "Defense"
                        pass
                   
            elif action == "3":
                chance = random.randint(1,you.pmidr)
                if chance == 1:
                    print(f"\033[32m{user.player} sinks the mid-range\033[0m")
                    score += 2
                    
                    user.possession = "Defense"
                else:
                    rebound = random.randint(1, you.preb)
                    if rebound == 1:
                        print(f"\033[36m{user.player} misses the mid-range but he gets the rebound\033[0m")
                        user.possession == "Offense"
                    else:
                        print(f"\033[31mThe mid-range is no good from {user.player}\033[0m")
                        user.possession = "Defense"
                    
            elif action == "4":
                chance = random.randint(1,you.pshot)
                if chance == 1:
                    print(f"\033[32mFrom the corner. Puts up a 3. BAAAAAAANG. A long 3 from {user.player}\033[0m")
                    score += 3
                    
                    user.possession = "Defense"
                else:
                    rebound = random.randint(1,you.preb)
                    if rebound == 1:
                        print(f"\033[36m{user.player} misses on the 3 point attempt but he gets the rebound\033[0m")
                        user.possession == "Offense"
                    else:
                        print(f"\033[31mThe 3 point attempt is no good from {user.player}.\033[0m")
                        user.possession = "Defense"

            else:
                print("You can't do that")
        elif user.possession == "Defense":
            opponent_shot = random.randint(1,4)
            
            if opponent_shot == 1:
                chance = random.randint(1,face.olayup)
                if chance == 1:
                    opponent_score += 2
                    
                    print(f"\033[32m{user.opponentplayer} drive in for an easy layup\033[0m")
                    user.possession = "Offense"
                else:
                    rebound = random.randint(1,face.oreb)
                    if rebound == 1:
                        print(f"\033[36m{user.opponentplayer} misses the layup but he gets the rebound\033[0m")
                        user.possession = "Defense"
                    else:
                        print(f"\033[31m{user.opponentplayer} misses the wide open layup\033[0m")
                        user.possession = "Offense"
            elif opponent_shot == 2:
                chance = random.randint(1,face.odunk)
                if chance == 1:
                    opponent_score += 2
                    
                    print(f"\033[32mAn amazing dunk from {user.opponentplayer}\033[0m")
                    user.possession = "Offense"
                else:
                    rebound = random.randint(1,face.oreb)
                    if rebound == 1:
                        print(f"\033[36m{user.opponentplayer} misses the dunk but gets the rebound\033[0m")
                        user.possession = "Defense"
                    else:
                        print(f"\033[31m{user.opponentplayer} goes for the dunk but it bounces off the rim\033[0m")
                        user.possession = "Offense"
            elif opponent_shot == 3:
                chance = random.randint(1,face.omidr)
                if chance == 1:
                    opponent_score += 2
                    
                    print(f"\033[32m{user.opponentplayer} makes the mid-range\033[0m")
                    user.possession = "Offense"
                else:
                    rebound = random.randint(1,face.oreb)
                    if rebound == 1:
                        print(f"\033[36m{user.opponentplayer} misses the mid-range but gets the rebound\033[0m")
                        user.possession = "Defense"
                    else:
                        print(f"\033[31m{user.opponentplayer} just misses the mid-range\033[0m")
                        user.possession = "Offense"
            elif opponent_shot == 4:
                chance = random.randint(1,face.oshot)
                if chance == 1:
                    opponent_score += 3
                    
                    print(f"\033[32m{user.opponentplayer} drills the shot from deep\033[0m")
                    user.possession = "Offense"
                else:
                    rebound = random.randint(1,face.oreb)
                    if rebound == 1:
                        print(f"\033[36m{user.opponentplayer} misses on the 3 point attempt but he gets the rebound\033[0m")
                        user.possession = "Defense"
                    else:
                        print(f"\033[31m{user.opponentplayer} puts up a 3 and it won't go.\033[0m")
                        user.possession = "Offense"
    


def convert_stat(user: User, you: Player)-> None:
    for name, s in OVERALLSTAT.items():
            if user.player == name:
                        
                    you.pshot = s.shooting
                    you.pdunk = s.dunk
                    you.playup = s.layup
                    you.pmidr = s.midrange
                    you.preb = s.rebound




def file_opener(user: User)->None:
    players = []
    while True:
        choice = input("~> ")
        for name, k in TEAMS.items():
            if choice in k.name:
                user.team = f"{name} {k.name}"
        try:
            with open(f"Roster/{choice}.txt", "r") as f:
                player = f.readlines()
                
                for p in player:
                    p = p.strip()
                    print(f"- {p}")
                    players.append(p)
            while user.player != name:
                playerchoice = input("Which Player? ~> ")
                for name in players:
                        if playerchoice == name:
                            user.player = name
                            print(f"You have chose Team: {user.team}\nPlayer: {user.player}")
                            return
                else:
                            print("Pick from someone on the team:")

        except FileNotFoundError:
            print("This is not a team.")
       


       
    


def search_roster()-> None:
    while True:
        print("Search through the rosters to get a understanding of who is on what team what stats a player has. (STATS DO HAVE AN AFFECT ON THE GAME)")
        searchroster = input("Search through the rosters?[q] to quit> ")
        
        if searchroster == "q":
            break
        try:
           with open(f"Roster/{searchroster}.txt", "r") as f:
            player = f.readlines()
            print(f"-{searchroster}' STARTING LINEUP- ")
            for p in player:
                p = p.strip()
                for name, s in OVERALLSTAT.items():
                    if p in name:
                        
                        print(f"- {p}:\n     3PS: \033[33m{s.shooting}\033[0m Dunk: \033[33m{s.dunk}\033[0m Lay-up: \033[33m{s.layup}\033[0m Mid-range:\033[33m{s.midrange}\033[0m")
                    
            
        
        except FileNotFoundError:
            print("Team does not exist or is not included.")
              

         




def main()-> None:
    opponent_roster: List[str] = []
    user = User("", "", "", "", "")
    stat = Stat(0, 0)
    you = Player(0,0,0,0,0)
    face = Opposition(0,0,0,0,0)
    print("Welcome to the arcade based basketball game. This is a game where you pick a player off of any team and try to defeat your opponent and get to the finals. Be careful who you pick every player has an overall and the overall will affect how you play. Good luck!!!")
    
    print("The players stat is based from 1 to 9. 1 being the best stat (1/1 chance) and 9 meaning they have a 1/9 chance of making a shot.")
    start = input("Press any key to continue or press enter. ")
    if start == "THE END OF THE GAME":
        quit()
    else:
        pass
    
    for name, o in TEAMS.items():
        print(f"{o.num}.\nCity: {name}\nTeam Name: #{o.name},\n{o.overall} OVERALL")
        print("_________________________________")
    search_roster()
    print("Which [Team Name] would you like to be would you like to be?")
    file_opener(user)
    convert_stat(user,you)
   
    while True:

        opponent(user, opponent_roster, face)
        opponent_roster.clear()
        print(f"                   YOUR GAME STATS:\n                   Wins:{stat.win} - Losses:{stat.loss}")
        points(user, stat,face, you)
        if stat.win == 4 and stat.loss == 0:
            print("You are now in the NBA Finals.")
        elif stat.win == 5 and stat.loss == 0:
            print(u"\n\u001b[33mYou have WON THE CHAMPIONSHIP!!\u001b[0m")
            break
        elif stat.loss == 1 and stat.win <4:
            print("You lost one game. We will give you easy mode and let you restart score? ")
            print("Type [reset] to reset. And [continue] without reset.")
            reset = input("> ")
            if reset == "reset":
                stat.win = 0
                stat.loss = 0
            elif reset == "continue":
                pass
            elif reset == "quit":
                break
            else: 
                print("This is not a valid option")
                reset = input("> ")
        elif stat.win == 4 and stat.loss > 1:
            print(f"You lost {stat.loss} games. Hit [Run to try again]")
        elif stat.win + stat.loss == 82:
            print(f"Season: {stat.win} - {stat.loss}")
            break
        
            
        



if __name__ == "__main__":
    main()
