import pandas as pd
import polars as pl
import time


t0 = time.time()

df = pd.read_csv("input.txt", header=None, sep="   ")
df.columns = ["D1", "D2"]

df = pl.from_pandas(df)
df = df.with_columns([pl.col("D1").sort(), pl.col("D2").sort()]).with_columns(
    [(pl.col("D2") - pl.col("D1")).alias("diff")]
)


print("Result 1:   ", df.get_column("diff").sum())
print("PART II...")

right_list = df.get_column("D1").unique().to_list()

df_sim = df.select("D2").filter(pl.col("D2").is_in(right_list)).group_by("D2").len()
df_res = (
    df.select("D1")
    .join(df_sim, left_on="D1", right_on="D2")
    .with_columns([(pl.col("D1") * pl.col("len")).alias("similarity_score")])
)
res_num = df_res.get_column("similarity_score").sum()

print(df_res)
print(f"{res_num=}")

print(f"Execution time: {time.time() - t0}")
