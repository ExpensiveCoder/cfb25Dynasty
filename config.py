

# Arrays to hold the heading of the tracked stats (General, Passing, Rushing, Receiving, Defense, Blocking, Kicking)
PASSING_STATS = ['RATING', 'YARDS', 'TD', 'INT', 'LONG', 'SACKS', 'COMP', 'ATT', 'COMP%', 'YPA', 'GP', 'DP']
RUSHING_STATS = ['CAR', 'YARDS', 'AVG', 'TD', 'AVG G', 'FUMB', 'BTK', 'LONG', '20+', 'GP', 'DP']
RECEIVING_STATS = ['REC', 'YARDS', 'AVG', 'AVG G', 'TD', 'RAC', 'LONG', 'GP', 'DP']
DEFENSE_STATS = ['SOLO', 'ASSISTS', 'TAK', 'TFL', 'SACK', 'INT', 'INT YDS', 'INT AVG', 'INT LG', 'DEFL', 'CTHA', 'FFUMB', 'TD', 'GP', 'DP']
BLOCK_STATS = ['SACK', 'GP', 'DP']
KICK_STATS = ['FGM', 'FGA', 'FG%', 'FG LNG', 'FG BLK', 'XPM', 'XPA', 'XP%', 'XPB', 'FGM29', 'FGA29', 'FGM39', 'FMA39', 'FGM39', 'FGA39', 'FGM49', 'FGA49', 'FGM50+', 'FGA50+', 'KO', 'TB', 'GP']
PUNT_STATS = ['PUNTS', 'YARDS', 'AVG', 'NET YDS', 'NET AVG', 'BLOCK', 'IN20', 'TB', 'LONG', 'GP']
KR_STATS = ['KR', 'YARDS', 'AVG', 'TD', 'LONG', 'GP']
PR_STATS = ['PR', 'YARDS', 'AVG', 'TD', 'LONG', 'GP']

# TODO: Arrays to hold the heading of the ratings tracked per position group (QB, )
QB_RAT = ['OVR', 'SPD', 'ACC', 'AGI', 'COD', 'STR', 'AWR', 'THP', 'SAC', 'MAC', 'DAC', 'RUN', 'TUP',
          'CAR', 'BCV', 'BTK', 'TRK', 'SFA', 'SPM', 'JKM', 'BSK', 'PAC', 'IBL', 'STA', 'TGH', 'INJ']
HB_RAT = ['OVR', 'SPD', 'ACC', 'AGI', 'COD', 'STR', 'AWR', 'CAR', 'BCV', 'BTK', 'TRK', 'SFA', 'SPM',
          'JKM', 'CTH', 'CIT', 'SPC', 'SRR', 'MRR', 'DRR', 'RLS', 'PBK', 'PBP', 'PBF', 'RBK', 'RBP',
          'RBF', 'LBK', 'IBL', 'RET', 'STA', 'TGH', 'INJ']
WR_RAT = ['OVR', 'SPD', 'ACC', 'AGI', 'COD', 'STR', 'AWR', 'CTH', 'CIT', 'SPC', 'SRR', 'MRR', 'DRR',
          'RLS', 'JMP', 'CAR', 'BCV', 'BTK', 'TRK', 'SFA', 'SPM', 'JKM', 'RBK', 'IBL', 'RET', 'STA',
          'TGH', 'INJ']
TE_RAT = ['OVR', 'SPD', 'ACC', 'AGI', 'COD', 'STR', 'AWR', 'CTH', 'CIT', 'SPC', 'SRR', 'MRR', 'DRR',
          'RLS', 'PBK', 'PBP', 'PBF', 'RBK' ,'RBP', 'RBF', 'LBK', 'IBL', 'CAR', 'BTK', 'TRK', 'SFA',
          'SPM', 'JKM', 'JMP', 'STA', 'TGH', 'INJ']

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
