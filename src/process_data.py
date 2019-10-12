import pandas as pd

# Fist look for the most turistic agebs
# Describe the inclucion is this agebs
# Describe the population in this agebs

turistic_codes = ['721111', '722110', '722411']

denue = pd.read_csv('data/denue_inegi_72_.csv')

turistic = denue.loc[denue.codigo_act.isin(turistic_codes)]

turistic['cve_ent'] = turistic.cve_ent.map(lambda x: str(x).zfill(2))
turistic['cve_mun'] = turistic.cve_mun.map(lambda x: str(x).zfill(3))
turistic['ageb_h'] = turistic.cve_ent + turistic.cve_mun + turistic.ageb
most_turistic = turistic.groupby(['ageb_h']).count().id.reset_index().sort_values(desc=False)

turistic_agebs = most_turistic[:-20].ageb_h.tolist()

# TODO: Create Turistic metric

# TODO: Look for this agebs in the INEGI data
# TODO: Create density metric

# TODO: Look for the muns of this ageb in the CNBV data
# TODO: Create inclussion metric

# TODO: Create necesity metric
# TODO: Order and expose results
# You are DONE go home!

