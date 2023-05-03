import pandas as pd
from typing import List

# pd.DataFrame
sample_df = pd.DataFrame(
    {"sub": [50, 51, 52, 53, 54, 55, 56], "parent": [54, 55, 54, 56, 51, 0, 0]}
)


def find_master(df: pd.DataFrame, sub: int, level: int = 0) -> List:
    """
    Return [master, level]. If the sub is the highest, return [sub, 0]
    """
    parent = df.loc[df["sub"] == sub, "parent"].values[0]

    if parent == 0:
        return [sub, level]
    else:
        return find_master(df, parent, level + 1)


# test
print(find_master(sample_df, 50))
print(find_master(sample_df, 55))
