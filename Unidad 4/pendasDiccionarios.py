import pandas as pd
import numpy as np

unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2}
unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
unidades_2017 = {"Ag":3, "Au":2, "Cu":4, "Pt":1}

unidades = pd.DataFrame([unidades_2015, unidades_2016, unidades_2017],
                       index = [2015, 2016, 2017])

print(unidades)