import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id','age'])


data = [[1, 19], [2, 13], [3, 20]]
df = createDataframe(data)
print(df)