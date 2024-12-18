# Scenario

The 'Man of the Match' award of a 50-over cricket match is decided by computing points earned by players. 
The points are calculated on the basis of the following rules:

## Batting

● 1 point for 2 runs scored
● Additional 5 points for a half-century
● Additional 10 points for a century
● 2 points for strike rate (runs/balls faced) of 80-100
● Additional 4 points for strike rate>100
● 1 point for hitting a boundary (four) and 2 points for over boundary (six)

## Bowling

● 10 points for each wicket
● Additional 5 points for three wickets in innings
● Additional 10 points for 5 wickets or more in innings
● 4 points for economy rate (runs given per over) between 3.5 and 4.5
● 7 points for an economy rate between 2 and 3.5
● 10 points for an economy rate less than 2

## Fielding

● 10 points each for catch/stumping/run out
The performance of each player is stored in a dictionary object. Displayed below is data for 5
players.

```py

p1={'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0,'balls':119, 'field':0}
p2={'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2,'balls':112, 'field':0}
p3={'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10,'runs':71, 'field':1}
p4={'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10,'runs':45, 'field':0}
p5={'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34,'field':0}

```

## Problem Statement

Assuming that these are the top 5 performers, write a Python program to decide the player with the highest points. 
Develop separate functions to compute batting and bowling points and save them in a module. 
These functions should be imported into the main code.

