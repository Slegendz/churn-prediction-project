import re
import pandas as pd

def convert_columns_to_snake_case(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert all column names of a DataFrame to snake_case.

    Steps:
    - Strip leading/trailing spaces
    - Convert to lowercase
    - Replace non-alphanumeric characters with '_'
    - Remove multiple underscores
    - Remove leading/trailing underscores

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: DataFrame with updated column names
    """

    def to_snake_case(col):
        col = col.strip()
        col = col.lower()
        col = re.sub(r"[^\w]+", "_", col)
        col = re.sub(r"_+", "_", col)
        return col.strip("_")

    df.columns = [to_snake_case(col) for col in df.columns]
    return df