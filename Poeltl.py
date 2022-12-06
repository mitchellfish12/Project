import tkinter
from tkinter import *
from prettytable import PrettyTable
import Playersdatabase
from Playersdatabase import select_player
from Playersdatabase import players

from Playersdatabase import TEAM
from Playersdatabase import CONF
from Playersdatabase import DIV
from Playersdatabase import POS
from Playersdatabase import HT
from Playersdatabase import AGE
from Playersdatabase import NUM
from Playersdatabase import sp

remaining_attempts = 9
root = tkinter.Tk()
root.title("Poeltl")
root.geometry("1000x1000")

Poeltltable = PrettyTable(["TEAM", "CONF", "DIV", "POS", "HT", "AGE", "NUM"])

GTEAM = str(2)
GCONF = str(2)
GDIV = str(2)
GPOS = str(2)
GHT = str(2)
GAGE = str(2)
GNUM = str(2)


instructions = tkinter.Label(root, text = "Welcome to Poeltl! The NBA guessing game! Enter a player name below.")
instructions.pack()
remaining_attemptsLabel = tkinter.Label(root, text = "Press enter to start", font = ("Helvetica", 12))
remaining_attemptsLabel.pack()       
guess = tkinter.Entry(root)
guess.pack()
guess.focus_set()
labels = tkinter.Label(root)
labels.pack()
scom = tkinter.Label(root)
scom.pack()
roo = tkinter.Label(root)
roo.pack()
ro = tkinter.Label(root)
ro.pack()
r = tkinter.Label(root)
r.pack()
piggy = tkinter.Label(root)
piggy.pack()
pigg = tkinter.Label(root)
pigg.pack()
pig = tkinter.Label(root)
pig.pack()
pi = tkinter.Label(root)
pi.pack()
p = tkinter.Label(root)
p.pack()
mess = tkinter.Label(root)
mess.pack()


def run_game(event):
    global GTEAM
    global GCONF
    global GDIV
    global GPOS
    global GHT
    global GAGE
    global GNUM
    global TEAM, CONF, DIV, POS, HT, AGE, NUM
    global guess
    global remaining_attempts
    global roo, ro, r, piggy, pigg, pig, pi, p, scom
    guess.focus_set()
    if remaining_attempts == 0:
        MESS = tkinter.Label(mess, text = "Better luck next time! The correct answer was" + sp)
        mess.pack()
        quit()
    else:
        if guess.get().title() == "Lebron James":
            GTEAM = 'Lakers'
            GCONF = "Western"
            GDIV = "Pacific"
            GPOS = "SF"
            GHT = "6-9"
            GAGE = "37"
            GNUM = "6"


        elif guess.get().title() == "Kevin Durant":
            GTEAM = 'Nets'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'PF'
            GHT = '6-10'
            GAGE = '34'
            GNUM = '7'

        elif guess.get().title() == "Mikal Bridges":
            GTEAM = 'Suns'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'SF'
            GHT = '6-6'
            GAGE = '26'
            GNUM = '25'
            
        elif guess.get().title() == "Kelly Oubre Jr.":
            GTEAM = 'Hornets'
            GCONF = 'Eastern'
            GDIV = 'Southeast'
            GPOS = 'SF'
            GHT = '6-7'
            GAGE = '26'
            GNUM = '12'
            
        elif guess.get().title() == "Kevin Huerter":
            GTEAM = 'Kings'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'SG'
            GHT = '6-7'
            GAGE = '24'
            GNUM = '3'
            
        elif guess.get().title() == "Jalen Green":
            GTEAM = 'Rockets'
            GCONF = 'Western'
            GDIV = 'Southwest'
            GPOS = 'SG'
            GHT = '6-4'
            GAGE = '20'
            GNUM = '0'
            
        elif guess.get().title() == "Cade Cunningham":
            GTEAM ='Pistons'
            GCONF = 'Eastern'
            GDIV = 'Central'
            GPOS = 'PG'
            GHT = '6-6'
            GAGE = '21'
            GNUM = '2'
            
        elif guess.get().title() == "Josh Christopher":
            GTEAM = 'Rockets'
            GCONF = 'Western'
            GDIV = 'Southwest'
            GPOS = 'SG'
            GHT = '6-5'
            GAGE = '20'
            GNUM = '9'
            
        elif guess.get().title() == "Russell Westbrook":
            GTEAM = 'Lakers'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'PG'
            GHT = '6-3'
            GAGE = '33'
            GNUM = '0'
            
        elif guess.get().title() == "Demar Derozan":
            GTEAM = 'Bulls'
            GCONF = 'Eastern'
            GDIV = 'Central'
            GPOS = 'SF'
            GHT = '6-6'
            GAGE = '33'
            GNUM = '11'
            
        elif guess.get().title() == "Klay Thompson":
            GTEAM = 'Warriors'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'SG'
            GHT = '6-6'
            GAGE = '32'
            GNUM = '11'
            
        elif guess.get().title() == "Kennedy Chandler":
            GTEAM = 'Grizzlies'
            GCONF = 'Western'
            GDIV = 'Southwest'
            GPOS = 'PG'
            GHT = '6-0'
            GAGE = '20'
            GNUM = '0'
            
        elif guess.get().title() == "Giannis Antetokounmpo":
            GTEAM = 'Bucks'
            GCONF = 'Eastern'
            GDIV = 'Central'
            GPOS = 'PF'
            GHT = '6-11'
            GAGE = '27'
            GNUM = '34'
            
        elif guess.get().title() == "Steph Curry":
            GTEAM = 'Warriors'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'PG'
            GHT = '6-2'
            GAGE = '34'
            GNUM = '30'
            
        elif guess.get().title() == "Joel Embiid":
            GTEAM = 'Sixers'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'C'
            GHT = '7-0'
            GAGE = '28'
            GNUM = '21'
            
        elif guess.get().title() == "Luka Doncic":
            GTEAM = 'Mavericks'
            GCONF = 'Eastern'
            GDIV = 'Southwest'
            GPOS = 'PG'
            GHT = '6-7'
            GAGE = '23'
            GNUM = '77'
            
        elif guess.get().title() == "Nikola Jokic":
            GTEAM = 'Nuggets'
            GCONF = 'Western'
            GDIV = 'Northwest'
            GPOS = 'C'
            GHT = '6-1'
            GAGE = '27'
            GNUM = '15'
            
        elif guess.get().title() == "Seth Curry":
            GTEAM = 'Nets'
            GCONF = 'Eastern'
            GDIV = 'Atlntic'
            GPOS = 'PG'
            GHT = '6-2'
            GAGE = '32'
            GNUM = '30'
            
        elif guess.get().title() == "Tobias Harris":
            GTEAM = 'Sixers'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'PF'
            GHT = '6-7'
            GAGE = '30'
            GNUM = '12'
            
        elif guess.get().title() == "James Harden":
            GTEAM = 'Sixers'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'SG'
            GHT = '6-5'
            GAGE = '33'
            GNUM = '1'
            
        elif guess.get().title() == "Jimmy Butler":
            GTEAM = 'Heat'
            GCONF = 'Eastern'
            GDIV = 'Southeast'
            GPOS = 'SF'
            GHT = '6-7'
            GAGE = '33'
            GNUM = '22'
            
        elif guess.get().title() == "Christian Wood":
            GTEAM = 'Mavericks'
            GCONF = 'Western'
            GDIV = 'Southwest'
            GPOS = 'C'
            GHT = '6-10'
            GAGE = '27'
            GNUM = '35'
            
        elif guess.get().title() == "Shai-Gilgeous Alexander":
            GTEAM = 'Thunder'
            GCONF = 'Western'
            GDIV = 'Northwest'
            GPOS = 'SG'
            GHT = '6-6'
            GAGE = '24'
            GNUM = '2'
            
        elif guess.get().title() == "Luke Kennard":
            GTEAM = 'Clippers'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'SG'
            GHT = '6-5'
            GAGE = '26'
            GNUM = '5'
            
        elif guess.get().title() == "Jose Alverado":
            GTEAM = 'Pelicans'
            GCONF = 'Eastern'
            GDIV =  'Southwest'
            GPOS = 'PG'
            GHT = '6-0'
            GAGE = '24'
            GNUM = '15'
            
        elif guess.get().title() == "Jayson Tatum":
            GTEAM = 'Celtics'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'SF'
            GHT = '6-8'
            GAGE = '24'
            GNUM = '0'
            
        elif guess.get().title() == "Julius Randle":
            GTEAM = 'Knicks'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'PF'
            GHT = '6-8'
            GAGE = '27'
            GNUM = '30'
            
        elif guess.get().title() == "Dejounte Murray":
            GTEAM = 'Hawks'
            GCONF = 'Eastern'
            GDIV = 'Southeast'
            GPOS = 'PG'
            GHT = '6-4'
            GAGE = '26'
            GNUM = '5'
            
        elif guess.get().title() == "Trae Young":
            GTEAM = 'Hawks'
            GCONF = 'Eastern'
            GDIV = 'Southeast'
            GPOS = 'PG'
            GHT = '6-1'
            GAGE = '24'
            GNUM = '11'
            
        elif guess.get().title() == "Tyler Herro":
            GTEAM = 'Heat'
            GCONF = 'Eastern'
            GDIV = 'Southeast'
            GPOS = 'SG'
            GHT = '6-5'
            GAGE = '22'
            GNUM = '14'
            
        elif guess.get().title() == "Tyrese Maxey":
            GTEAM = 'Sixers'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'PG'
            GHT = '6-2'
            GAGE = '21'
            GNUM = '0'
            
        elif guess.get().title() == "Devin Booker":
            GTEAM = 'Suns'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'SG'
            GHT = '6-5'
            GAGE = '25'
            GNUM = '1'
            
        elif guess.get().title() == "Jae Crowder":
            GTEAM = 'Suns'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'SF'
            GHT = '6-6'
            GAGE = '32'
            GNUM = '99'
            
        elif guess.get().title() == "Eric Gordon":
            GTEAM = 'Houston'
            GCONF = 'Western'
            GDIV = 'Southwest'
            GPOS = 'SG'
            GHT = '6-3'
            GAGE = '33'
            GNUM = '10'
            
        elif guess.get().title() == "Aaron Gordon":
            GTEAM = 'Nuggets'
            GCONF = 'Western'
            GDIV = 'Northwest'
            GPOS = 'PF'
            GHT = '6-8'
            GAGE = '27'
            GNUM = '50'
            
        elif guess.get().title() == "Zach Lavine":
            GTEAM = 'Bulls'
            GCONF = 'Eastern'
            GDIV = 'Central'
            GPOS = 'SG'
            GHT = '6-5'
            GAGE = '27'
            GNUM = '8'
            
        elif guess.get().title() == "Keldon Johnson":
            GTEAM = 'Spurs'
            GCONF = 'Western'
            GDIV = 'Southwest'
            GPOS = 'SF'
            GHT = '6-5'
            GAGE = '22'
            GNUM = '3'
            
        elif guess.get().title() == "Karl Anthony-Towns":
            GTEAM = 'Timberwolves'
            GCONF = 'Western'
            GDIV = 'Northwest'
            GPOS = 'C'
            GHT = '6-11'
            GAGE = '26'
            GNUM = '34'
            
        elif guess.get().title() == "TJ Warren":
            GTEAM = 'Nets'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'SF'
            GHT = '6-8'
            GAGE = '29'
            GNUM = '12'
            
        elif guess.get().title() == "Miles Bridges":
            GTEAM = 'Hornets'
            GCONF = 'Eastern'
            GDIV = 'Southeast'
            GPOS = 'SF'
            GHT = '6-6'
            GAGE = '24'
            GNUM = '0'
            
        elif guess.get().title() == "Gordon Hayward":
            GTEAM = 'Hornets'
            GCONF = 'Eastern'
            GDIV = 'Southeast'
            GPOS = 'SF'
            GHT = '6-7'
            GAGE = '32'
            GNUM = '20'
            
        elif guess.get().title() == "Montrez Harrell":
            GTEAM = 'Sixers'
            GCONF = 'Eastern'
            GDIV = 'Southeast'
            GPOS = 'C'
            GHT = '6-7'
            GAGE = '28'
            GNUM = '5'
            
        elif guess.get().title() == "Pascal Siakam":
            GTEAM = 'Raptors'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'PF'
            GHT = '6-9'
            GAGE = '28'
            GNUM = '43'
            
        elif guess.get().title() == "Kawhi Leonard":
            GTEAM = 'Clippers'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'SF'
            GHT = '6-7'
            GAGE = '31'
            GNUM = '2'
            
        elif guess.get().title() == "Paul George":
            GTEAM = 'Clippers'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'SG'
            GHT = '6-8'
            GAGE = '32'
            GNUM = '13'
            
        elif guess.get().title() == "Jaylen Brown":
            GTEAM = 'Celtics'
            GCONF = 'Eastern'
            GDIV = 'Atlantic'
            GPOS = 'SG'
            GHT = '6-6'
            GAGE = '25'
            GNUM = '7'
            
        elif guess.get().title() == "Bradley Beal":
            GTEAM = 'Wizards'
            GCONF = 'Eastern'
            GDIV = 'Southeast'
            GPOS = 'SG'
            GHT = '6-4'
            GAGE = '29'
            GNUM = '3'
            
        elif guess.get().title() == "Damian Lillard":
            GTEAM = 'Trailblazers'
            GCONF = 'Western'
            GDIV = 'Northwest'
            GPOS = 'PG'
            GHT = '6-2'
            GAGE = '32'
            GNUM = '0'
            
        elif guess.get().title() == "Deaaron Fox":
            GTEAM = 'Kings'
            GCONF = 'Western'
            GDIV = 'Pacific'
            GPOS = 'PG'
            GHT = '6-3'
            GAGE = '24'
            GNUM = '5'
            
        elif guess.get().title() == "Ja Morant":
            GTEAM = 'Grizzlies'
            GCONF = 'Western'
            GDIV = 'Southwest'
            GPOS = 'PG'
            GHT = '6-3'
            GAGE = '23'
            GNUM = '12'
        if guess.get().title() == sp:
            MESS = tkinter.Label(mess, text = "You solved it in" + 9 - remaining_attempts + "guess.get().title()es")
            mess.pack()
        else:
            remaining_attempts -= 1
            remaining_attemptsLabel.config(text = "Remaining attempts: " + str(remaining_attempts))                                           
        if remaining_attempts < 8:
            guess.delete(0, tkinter.END)
            if GTEAM == TEAM:
                c1 = 'green'
                cc1 = 'black'
            elif GCONF == CONF:
                c1 = 'yellow'
                cc1 = 'black'
            else:
                c1 = 'black'
                cc1 = 'white'
            if GCONF == CONF:
                c2 = 'green'
                cc2 = 'black'
            else:
                c2 = 'black'
                cc2 = 'white'
            if GDIV == DIV:
                c3 = 'green'
                cc3 = 'black'
            elif GCONF == CONF and GDIV != DIV:
                c3 = 'yellow'
                cc3 = 'black'
            else:
                c3 = 'black'
                cc3 = 'white'
            if GPOS == 'PG':
                GPOS = 1
            elif GPOS == 'SG':
                GPOS = 2
            elif GPOS == 'SF':
                GPOS = 3
            elif GPOS == 'PF':
                GPOS = 4
            elif GPOS == 'C':
                GPOS = 5
            if POS == 'PG':
                POS = 1
            if POS == 'SG':
                POS = 2
            if POS == 'SF':
                POS = 3
            if POS == 'PF':
                POS = 4
            if POS == 'C':
                POS = 5
            if GPOS == POS:
                c4 = 'green'
                cc4 = 'black'
            elif -2 < (int(GPOS) - int(POS)) < 2:
                c4 = 'yellow'
                cc4 = 'black'
            else:
                c4 = 'black'
                cc4 = 'white'
            if GPOS == 1:
                GPOS = str('PG')
            if GPOS == 2:
                GPOS = str('SG')
            if GPOS == 3:
                GPOS = str('SF')
            if GPOS == 4:
                GPOS = str('PF')
            if GPOS == 5:
                GPOS = str('C')
            if POS == 1:
                POS = str('PG')
            if POS == 2:
                POS = str('SG')
            if POS == 3:
                POS = str('SF')
            if POS == 4:
                POS = str('PF')
            if POS == 5:
                POS = str('C')
            if GHT == '6-0':
                GHT = 60
            if GHT == '6-1':
                GHT = 61
            if GHT == '6-2':
                GHT = 62
            if GHT == '6-3':
                GHT = 63
            if GHT == '6-4':
                GHT = 64
            if GHT == '6-5':
                GHT = 65
            if GHT == '6-6':
                GHT = 66
            if GHT == '6-7':
                GHT = 67
            if GHT == '6-8':
                GHT = 68
            if GHT == '6-9':
                GHT = 69
            if GHT == '6-10':
                GHT = 70
            if GHT == '6-11':
                GHT = 71
            if GHT == '7-0':
                GHT = 72
            if HT == '6-0':
                HT = 60
            if HT == '6-1':
                HT = 61
            if HT == '6-2':
                HT = 62
            if HT == '6-3':
                HT = 63
            if HT == '6-4':
                HT = 64
            if HT == '6-5':
                HT = 65
            if HT == '6-6':
                HT = 66
            if HT == '6-7':
                HT = 67
            if HT == '6-8':
                HT = 68
            if HT == '6-9':
                HT = 69
            if HT == '6-10':
                HT = 70
            if HT == '6-11':
                HT = 71
            if HT == '7-0':
                HT = 72
            if GHT == HT:
                c5 = 'green'
                cc5 = 'black'
            elif -4 < (int(GHT) - int(HT)) < 4:
                c5 = 'yellow'
                cc5 = 'black'
            else:
                c5 = 'black'
                cc5 = 'white'
            if GHT == 60:
                GHT = str('6-0')
            if GHT == 61:
                GHT = str('6-1')
            if GHT == 62:
                GHT = str('6-2')
            if GHT == 63:
                GHT = str('6-3')
            if GHT == 64:
                GHT = str('6-4')
            if GHT == 65:
                GHT = str('6-5')
            if GHT == 66:
                GHT = str('6-6')
            if GHT == 67:
                GHT = str('6-7')
            if GHT == 68:
                GHT = str('6-8')
            if GHT == 69:
                GHT = str('6-9')
            if GHT == 70:
                GHT = str('6-10')
            if GHT == 71:
                GHT = str('6-11')
            if GHT == 72:
                GHT = str('7-0')
            if HT == 60:
                HT = str('6-0')
            if HT == 61:
                HT = str('6-1')
            if HT == 62:
                HT = str('6-2')
            if HT == 63:
                HT = str('6-3')
            if HT == 64:
                HT = str('6-4')
            if HT == 65:
                HT = str('6-5')
            if HT == 66:
                HT = str('6-6')
            if HT == 67:
                HT = str('6-7')
            if HT == 68:
                HT = str('6-8')
            if HT == 69:
                HT = str('6-9')
            if HT == 70:
                HT = str('6-10')
            if HT == 71:
                HT = str('6-11')
            if HT == 72:
                HT = str('7-0')
            GAGE = int(GAGE)
            AGE = int(AGE)
            if AGE == GAGE:
                c6 = 'green'
                cc6 = 'black'
            elif -6 < (AGE - GAGE) < 6:
                c6 = 'yellow'
                cc6 = 'black'
            else:
                c6 = 'black'
                cc6 = 'white'
            GAGE = str(GAGE)
            AGE = str(AGE)
            GNUM = int(GNUM)
            NUM = int(NUM)
            if NUM == GNUM:
                c7 = 'green'
                cc7 = 'black'
            elif -6 < (NUM - GNUM) < 6:
                c7 = 'yellow'
                cc7 = 'black'
            else:
                c7 = 'black'
                cc7 = 'white'
            GNUM = str(GNUM)
            NUM = str(NUM)
            mem = roo
            if remaining_attempts == 8:
                mm = roo
            elif remaining_attempts == 7:
                mm = ro
            elif remaining_attempts == 6:
                mm = r
            elif remaining_attempts == 5:
                mm = piggy
            elif remaining_attempts == 4:
                mm = pigg
            elif remaining_attempts == 3:
                mm = pig
            elif remaining_attempts == 2:
                mm = pi
            elif remaining_attempts == 1:
                mm = p
            SCOMMYY = tkinter.Label(scom, text = "TEAM", font = ('Times', 50))
            SCOMMYY.pack(side = LEFT, padx = 10)
            SCOMMY = tkinter.Label(scom, text = "CONF", font = ('Times', 50))
            SCOMMY.pack(side = LEFT, padx = 10)
            SCOMM = tkinter.Label(scom, text = "DIV", font = ('Times', 50))
            SCOMM.pack(side = LEFT, padx = 10)
            SCOM = tkinter.Label(scom, text = "POS", font = ('Times', 50))
            SCOM.pack(side = LEFT, padx = 10)
            SCO = tkinter.Label(scom, text = "HT", font = ('Times', 50))
            SCO.pack(side = LEFT, padx = 10)
            SC = tkinter.Label(scom, text = "AGE", font = ('Times', 50))
            SC.pack(side = LEFT, padx = 10)
            S = tkinter.Label(scom, text = "NUM", font = ('Times', 50))
            S.pack(side = LEFT, padx = 10)
            scom.pack()
            label1 = tkinter.Label(mm, text = GTEAM , font = ('Times', 40), fg = cc1, bg = c1)
            label1.pack(side = LEFT, padx = 10)
            label2 = tkinter.Label(mm, text = GCONF, font = ('Times', 40), fg = cc2, bg = c2)
            label2.pack(side = LEFT, padx = 10)
            label3 = tkinter.Label(mm, text = GDIV, font = ('Times', 40), fg = cc3, bg = c3)
            label3.pack(side = LEFT, padx = 10)
            label4 = tkinter.Label(mm, text = GPOS, font = ('Times', 40), fg = cc4, bg = c4)
            label4.pack(side = LEFT, padx = 10)
            label5 = tkinter.Label(mm, text = GHT, font = ('Times', 40), fg = cc5, bg = c5)
            label5.pack(side = LEFT, padx = 10)
            label6 = tkinter.Label(mm, text = GAGE, font = ('Times', 40), fg = cc6, bg = c6)
            label6.pack(side = LEFT, padx = 10)
            label7 = tkinter.Label(mm, text = GNUM, font = ('Times', 40), fg = cc7, bg = c7)
            label7.pack(side = LEFT, padx = 10)
            root.mainloop()
            

root.bind('<Return>', run_game)
guess.focus_set()
root.mainloop()
