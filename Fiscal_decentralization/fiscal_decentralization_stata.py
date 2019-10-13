import pandas as pd
df_path = "/Users/aaronforbes/for-date-science/raw_data/fiscal_decentralization/fiscal_decentralization_stata_file.dta"
df = None
with open(df_path, "r") as f:
    df = pd.read_stata(f)
    print df
