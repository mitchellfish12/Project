import random
TEAM=str(2)
CONF=str(2)
DIV=str(2)
POS=str(2)
HT=str(2)
AGE=str(2)
NUM=str(2)
sp = str(0)

players = ["Lebron James", "Kevin Durant", "Mikal Bridges", "Kelly Oubre Jr.", "Kevin Huerter", "Jalen Green", "Cade Cunningham", "Josh Christopher", "Russell Westbrook", "Anthony Davis", "Klay Thompson", "Kennedy Chandler", "Giannis Antetokounmpo", "Steph Curry", "Joel Embiid", "Luka Doncic", "Nikola Jokic", "Seth Curry", "Tobias Harris", "James Harden", "Jimmy Butler", "Christian Wood", "Shai-Gilgeous Alexander", "Luke Kennard", "Jose Alverado", "Jayson Tatum", "Julius Randle", "Dejounte Murray", "Trae Young", "Tyler Herro", "Tyrese Maxey", "Devin Booker", "Jae Crowder", "Eric Gordon", "Aaron Gordon", "Zach Lavine", "Keldon Johnson", "Karl Anthony-Towns", "TJ Warren", "Miles Bridges", "Gordon Hayward", "Montrez Harrell", "Pascal Siakam", "Kawhi Leonard", "Paul George", "Jaylen Brown", "Bradley Beal", "Damian Lillard", "Deaaron Fox", "Ja Morant"]


def select_player(p):
    global sp
    sp = random.choice(players)
    #print (sp)

select_player(players)


  
if sp == "Lebron James":
    TEAM = "Lakers"
    CONF = "Western"
    DIV = "Pacific"
    POS = "SF"
    HT = "6-9"
    AGE = "37"
    NUM = "6"
elif sp == "Kevin Durant":
    TEAM = 'Nets'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'PF'
    HT = '6-10'
    AGE = '34'
    NUM = '7'
elif sp == "Mikal Bridges":
    TEAM = 'Suns'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'SF'
    HT = '6-6'
    AGE = '26'
    NUM = '25'
elif sp == "Kelly Oubre Jr.":
    TEAM = 'Hornets'
    CONF = 'Eastern'
    DIV = 'Southeast'
    POS = 'SF'
    HT = '6-7'
    AGE = '26'
    NUM = '12'
elif sp == "Kevin Huerter":
    TEAM = 'Kings'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'SG'
    HT = '6-7'
    AGE = '24'
    NUM = '3'
elif sp == "Jalen Green":
    TEAM = 'Rockets'
    CONF = 'Western'
    DIV = 'Southwest'
    POS = 'SG'
    HT = '6-4'
    AGE = '20'
    NUM = '0'                    
elif sp == "Cade Cunningham":
    TEAM ='Pistons'
    CONF = 'Eastern'
    DIV = 'Central'
    POS = 'PG'
    HT = '6-6'
    AGE = '21'
    NUM = '2'
elif sp == "Josh Christopher":
    TEAM = 'Rockets'
    CONF = 'Western'
    DIV = 'Southwest'
    POS = 'SG'
    HT = '6-5'
    AGE = '20'
    NUM = '9'
elif sp == "Russell Westbrook":
    TEAM = 'Lakers'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'PG'
    HT = '6-3'
    AGE = '33'
    NUM = '0'
elif sp == "Demar Derozan":
    TEAM = 'Bulls'
    CONF = 'Eastern'
    DIV = 'Central'
    POS = 'SF'
    HT = '6-6'
    AGE = '33'
    NUM = '11'
elif sp == "Klay Thompson":
    TEAM = 'Warriors'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'SG'
    HT = '6-6'
    AGE = '32'
    NUM = '11'
elif sp == "Kennedy Chandler":
    TEAM = 'Grizzlies'
    CONF = 'Western'
    DIV = 'Southwest'
    POS = 'PG'
    HT = '6-0'
    AGE = '20'
    NUM = '0'
elif sp == "Giannis Antetokounmpo":
    TEAM = 'Bucks'
    CONF = 'Eastern'
    DIV = 'Central'
    POS = 'PF'
    HT = '6-11'
    AGE = '27'
    NUM = '34'
elif sp == "Steph Curry":
    TEAM = 'Warriors'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'PG'
    HT = '6-2'
    AGE = '34'
    NUM = '30'
elif sp == "Joel Embiid":
    TEAM = 'Sixers'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'C'
    HT = '7-0'
    AGE = '28'
    NUM = '21'
elif sp == "Luka Doncic":
    TEAM = 'Mavericks'
    CONF = 'Eastern'
    DIV = 'Southwest'
    POS = 'PG'
    HT = '6-7'
    AGE = '23'
    NUM = '77'
elif sp == "Nikola Jokic":
    TEAM = 'Nuggets'
    CONF = 'Western'
    DIV = 'Northwest'
    POS = 'C'
    HT = '6-11'
    AGE = '27'
    NUM = '15'
elif sp == "Seth Curry":
    TEAM = 'Nets'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'PG'
    HT = '6-2'
    AGE = '32'
    NUM = '30'
elif sp == "Tobias Harris":
    TEAM = 'Sixers'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'PF'
    HT = '6-7'
    AGE = '30'
    NUM = '12'
elif sp == "James Harden":
    TEAM = 'Sixers'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'SG'
    HT = '6-5'
    AGE = '33'
    NUM = '1'
elif sp == "Jimmy Butler":
    TEAM = 'Heat'
    CONF = 'Eastern'
    DIV = 'Southeast'
    POS = 'SF'
    HT = '6-7'
    AGE = '33'
    NUM = '22'
elif sp == "Christian Wood":
    TEAM = 'Mavericks'
    CONF = 'Western'
    DIV = 'Southwest'
    POS = 'C'
    HT = '6-10'
    AGE = '27'
    NUM = '35'
elif sp == "Shai-Gilgeous Alexander":
    TEAM = 'Thunder'
    CONF = 'Western'
    DIV = 'Northwest'
    POS = 'SG'
    HT = '6-6'
    AGE = '24'
    NUM = '2'
elif sp == "Luke Kennard":
    TEAM = 'Clippers'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'SG'
    HT = '6-5'
    AGE = '26'
    NUM = '5'
elif sp == "Jose Alverado":
    TEAM = 'Pelicans'
    CONF = 'Eastern'
    DIV =  'Southwest'
    POS = 'PG'
    HT = '6-0'
    AGE = '24'
    NUM = '15'
elif sp == "Jayson Tatum":
    TEAM = 'Celtics'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'SF'
    HT = '6-8'
    AGE = '24'
    NUM = '0'
elif sp == "Julius Randle":
    TEAM = 'Knicks'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'PF'
    HT = '6-8'
    AGE = '27'
    NUM = '30'
elif sp == "Dejounte Murray":
    TEAM = 'Hawks'
    CONF = 'Eastern'
    DIV = 'Southeast'
    POS = 'PG'
    HT = '6-4'
    AGE = '26'
    NUM = '5'
elif sp == "Trae Young":
    TEAM = 'Hawks'
    CONF = 'Eastern'
    DIV = 'Southeast'
    POS = 'PG'
    HT = '6-1'
    AGE = '24'
    NUM = '11'
elif sp == "Tyler Herro":
    TEAM = 'Heat'
    CONF = 'Eastern'
    DIV = 'Southeast'
    POS = 'SG'
    HT = '6-5'
    AGE = '22'
    NUM = '14'
elif sp == "Tyrese Maxey":
    TEAM = 'Sixers'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'PG'
    HT = '6-2'
    AGE = '21'
    NUM = '0'
elif sp == "Devin Booker":
    TEAM = 'Suns'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'SG'
    HT = '6-5'
    AGE = '25'
    NUM = '1'
elif sp == "Jae Crowder":
    TEAM = 'Suns'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'SF'
    HT = '6-6'
    AGE = '32'
    NUM = '99'
elif sp == "Eric Gordon":
    TEAM = 'Houston'
    CONF = 'Western'
    DIV = 'Southwest'
    POS = 'SG'
    HT = '6-3'
    AGE = '33'
    NUM = '10'
elif sp == "Aaron Gordon":
    TEAM = 'Nuggets'
    CONF = 'Western'
    DIV = 'Northwest'
    POS = 'PF'
    HT = '6-8'
    AGE = '27'
    NUM = '50'
elif sp == "Zach Lavine":
    TEAM = 'Bulls'
    CONF = 'Eastern'
    DIV = 'Central'
    POS = 'SG'
    HT = '6-5'
    AGE = '27'
    NUM = '8'
elif sp == "Keldon Johnson":
    TEAM = 'Spurs'
    CONF = 'Western'
    DIV = 'Southwest'
    POS = 'SF'
    HT = '6-5'
    AGE = '22'
    NUM = '3'
elif sp == "Karl Anthony-Towns":
    TEAM = 'Timberwolves'
    CONF = 'Western'
    DIV = 'Northwest'
    POS = 'C'
    HT = '6-11'
    AGE = '26'
    NUM = '34'
elif sp == "TJ Warren":
    TEAM = 'Nets'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'SF'
    HT = '6-8'
    AGE = '29'
    NUM = '12'
elif sp == "Miles Bridges":
    TEAM = 'Hornets'
    CONF = 'Eastern'
    DIV = 'Southeast'
    POS = 'SF'
    HT = '6-6'
    AGE = '24'
    NUM = '0'
elif sp == "Gordon Hayward":
    TEAM = 'Hornets'
    CONF = 'Eastern'
    DIV = 'Southeast'
    POS = 'SF'
    HT = '6-7'
    AGE = '32'
    NUM = '20'
elif sp == "Montrez Harrell":
    TEAM = 'Sixers'
    CONF = 'Eastern'
    DIV = 'Southeast'
    POS = 'C'
    HT = '6-7'
    AGE = '28'
    NUM = '5'
elif sp == "Pascal Siakam":
    TEAM = 'Raptors'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'PF'
    HT = '6-9'
    AGE = '28'
    NUM = '43'
elif sp == "Kawhi Leonard":
    TEAM = 'Clippers'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'SF'
    HT = '6-7'
    AGE = '31'
    NUM = '2'
elif sp == "Paul George":
    TEAM = 'Clippers'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'SG'
    HT = '6-8'
    AGE = '32'
    NUM = '13'
elif sp == "Jaylen Brown":
    TEAM = 'Celtics'
    CONF = 'Eastern'
    DIV = 'Atlantic'
    POS = 'SG'
    HT = '6-6'
    AGE = '25'
    NUM = '7'
elif sp == "Bradley Beal":
    TEAM = 'Wizards'
    CONF = 'Eastern'
    DIV = 'Southeast'
    POS = 'SG'
    HT = '6-4'
    AGE = '29'
    NUM = '3'
elif sp == "Damian Lillard":
    TEAM = 'Trailblazers'
    CONF = 'Western'
    DIV = 'Northwest'
    POS = 'PG'
    HT = '6-2'
    AGE = '32'
    NUM = '0'
elif sp == "Deaaron Fox":
    TEAM = 'Kings'
    CONF = 'Western'
    DIV = 'Pacific'
    POS = 'PG'
    HT = '6-3'
    AGE = '24'
    NUM = '5'
elif sp == "Ja Morant":
    TEAM = 'Grizzlies'
    CONF = 'Western'
    DIV = 'Southwest'
    POS = 'PG'
    HT = '6-3'
    AGE = '23'
    NUM = '12'


#print (TEAM, CONF, DIV, POS, HT, AGE, NUM)



    
