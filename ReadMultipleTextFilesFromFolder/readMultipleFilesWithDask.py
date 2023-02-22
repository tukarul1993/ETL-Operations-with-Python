import dask.dataframe as dd
ddf = dd.read_csv(f"D:\Python\ETL Operations with Python\Files\TextFiles\*.csv")

df = ddf.compute()
print(df)
"""
Dask takes care of the file listing operation and doesn’t require you to perform it manually. 
Dask makes it a lot easier to read and write multiple files compared to pandas.

Dask is also designed to handle large datasets without erroring out like pandas.

Dask splits up data into partitions so it can be processed in parallel. 
It also allows for computations to be performed in a streaming manner without loading all the data in memory 
at once.

Dask computations can be scaled up to use all the cores of a single machine or scaled out to leverage a 
cluster of multiple computers in parallel. Dask is a good option whenever you’re facing pandas related
scaling issues.

"""