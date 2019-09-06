class Room(obejct):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(directions, None)

    def add_paths(self, paths):
        self.paths.update(paths)

hogsmeade = Room("Hogsmeade", 
"""

The prisinors from Azbaban have escaped and you and you fellow Aurors have been tasked with rallying them up and turning them into the Ministry of Magic.
You are hurrying about Hogsmeade, trying to stay safe while capturing the rebels. 

You burst into Zonko's in time to catch an escaped convict attempting to steal all opf the gold out of the safe.
You take aim to disarm him as he draws a stolen wand to your chest. 
YOu have to choose: LAY DOWN your wand or DISARM the prisonor.
""")

three_bromsticks = Room("Three Broomsticks", 
"""
You successfully disarm the rebel, secure the stolen wand, and capture the prisonor.
You cast Petrificous Totalus, making it easier for you to drag him along to the Three Broomsticks, Auror gathering spot.
As you approach the Three Broomsticks, you can tell something is off. 
It is eeriely quiet, and none of your team appears to have arrived. 

You look inside, and you see your team silenced and hanging from the ceiling from their feet, a Death Eater trick.
There are escaped convicts enjoyinh butterbeer by the gallon. laughing as they torture the captured Aurors.  
YOu bring your prisonor to the front door, about to burst in when you see there is a magical lock on it. 
It requires a four digit code, and getting it wrong three times would result in complete annihalation of the city. 
""")

courtyard = Room("Courtyard",
"""
You correctly enter the code and charge into the Three Broomsticks.
The convicts become silent, then scramble to get their wands. 
Too late for them, as you have already released your group and conjured their wands back to them.
You gather all of the convicts, and bring them outside to go to the dspoist point. 

As you go to the Portkey, stormy clouds gather in the skies, and lightening blinds you.
You gather yourself just in time to see a crowd of Death Eaters descend from the sky. 
In front is Draco Malfoy, the newest leader, eager to avenge his parents death. 
He advises you to turn over the convicts to him, or suffer a painful fate. 
The Portkey starts quivering, just out of reach. 
Ten more seconds, and you wil fail your mission.
You must either GIVE IN the Malfoy's threats, or RISK making it to the Portkey in time for travel.
""")

the_house = Room("The House",
"""
You touch the Portkey just in time, traveling fasted than the speed of light. 
You arrive at the deposit point to be greeted by the greatest Auror of all, Nyphadora Tonks. 
She thanks you for your hard work, and send the prisonors back to Azkaban, equipped with more security than ever.
She asks if you would like to head another mission, this time delivering socks to free houseelves.
yes or no?
""")

the_end_yes = Room("The End",
"""
You agree to another mission. 
Tonks presents another Portkey and a sack of socks.
She wishes you luck on your journey, and advises that all freed elves will find roo, board, and work at Hogwarts.
""")

the_end_no = Room("The End",
"""
You decline another mission.
She lets you know that her door will always be open when you want work.
You Apparate to your house, and settle in your favorite chair with an ice cold Butterbeer.
""")

the_house.add_paths({
    'yes': the_end_yes,
    'no': the_end_no
})

generic_death = Room("death", "You died.")

courtyard.add_paths({
    'give in': generic_death,
    'risk': the_house
})

three_broomsticks.add_paths({
    '*': generic_death,
    '3825': courtyard
})

hogsmeade.add_paths({
    'lay down': generic_death,
    'disarm': three_brommsticka
})

START = 'hogsmeade'

def load_room(name):
    """

    There is a potentail security problem here.
    Who gets to set the name?
    Can that expose a vaiable?

    """
    return globals().get(name)

def name_room(room):
    """

    Same possible security problem.
    What's a better solution than this globals lookup?

    """
    for key, value in globals().items():
        if value == room:
            return key