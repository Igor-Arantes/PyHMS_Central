
import pandas as pd



Unidade = pd.read_json('http://smp26ocn02:8509/get/data?localtime&airpresok&headvsok&heavprok&heavvlok')

print(Unidade)
