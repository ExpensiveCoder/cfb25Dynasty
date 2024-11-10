# Configuration file to store static information (stat categories, rating categories, position archetype, etc)

# TODO: Arrays to hold the heading of the tracked stats (General, Passing, Rushing, Receiving, Defense, Blocking, Kicking)
GEN_STATS = ['GP (Games Played)', 'DP (Downs Played)']
PASSING_STATS = ['RATING', 'YARDS', 'TD', 'INT', 'LONG', 'SACKS', 'COMP', 'ATT', 'COMP%', 'YPA']
RUSHING_STATS = []
RECEIVING_STATS = []
DEFENSE_STATS = ['SOLO', 'ASSISTS', 'TAK', 'TFL', 'SACK', 'INT', 'INT YDS', 'INT AVG', 'INT LG', 'DEFL', 'CTHA', 'FFUMB', 'TD']
BLOCK_STATS = []
KICK_STATS = []

# TODO: Arrays to hold the heading of the ratings tracked per position group (QB, )
QB_RAT = ['OVR', 'SPD', 'ACC', 'AGI', 'COD', 'STR', 'AWR', 'THP', 'SAC', 'MAC', 'DAC', 'RUN', 'TUP',
          'CAR', 'BCV', 'BTK', 'TRK', 'SFA', 'SPM', 'JKM', 'BSK', 'PAC', 'IBL', 'STA', 'TGH', 'INJ']
HB_RAT = []
DE_RAT = ['OVR', 'SPD', 'ACC', 'AGI', 'COD', 'STR', 'AWR', 'PRC', 'PMV', 'FMV', 'BSH',
          'TAK', 'POW', 'PUR', 'ZCV', 'MCV', 'CTH', 'JMP', 'IBL', 'STA', 'TGH', 'INJ']
OLB_RAT = ['OVR', 'SPD', 'ACC', 'AGI', 'COD', 'STR', 'AWR', 'PRC', 'TAK', 'POW', 'BSH', 'PMV',
           'FMV', 'PUR', 'MCV', 'ZCV', 'PRS', 'CTH', 'JMP', 'IBL', 'STA', 'TGH', 'INJ']


# Arrays to hold the Archetypes for each position
QB_ARC = ['Field General', 'Scrambler', 'Improvisor']
HB_ARC = ['Elusive Back', 'Receiving Back', 'Power Back']
FB_ARC = ['Blocking', 'Utility']
WR_ARC = ['Deep Threat', 'Route Runner', 'Physical']
TE_ARC = ['Blocking', 'Vertical Threat', 'Possession']
OL_ARC = ['Agile', 'Pass Protector', 'Power']
DL_ARC = ['Speed Rusher', 'Power Rusher', 'Run Stopper']
OLB_ARC = ['Speed Rusher', 'Power Rusher', 'Pass Coverage', 'Run Stopper']
MLB_ARC = ['Field General', 'Pass Coverage', 'Run Stopper']
CB_ARC = ['Man To Man', 'Zone', 'Slot']
SAFE_ARC = ['Zone', 'Hybrid', 'Run Support']
KICK_ARC = ['Power', 'Accurate']
