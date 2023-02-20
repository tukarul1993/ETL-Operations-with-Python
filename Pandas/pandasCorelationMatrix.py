import pandas as pd
import numpy as np
# DataFrame with some random values
df = pd.DataFrame(np.random.randint(0,100, size=(100, 6)), columns=list('ABCDEF'))
print(df.head())
print(df.corr())