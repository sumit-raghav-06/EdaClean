import pandas as pd
class Pipeline:
    def __init__(self, source):
        self.source = source
    def run(self):
        df=pd.read_csv(self.source)
        print(f"EdaClean is processing:{self.source}")
        print("\nDataset preview:")
        print(df.head())
        print("\nTotal rows:", len(df))
        print("Total columns:",len(df.columns))
        print("\nMissing values per column:")
        print(df.isnull().sum())
        print("\nDuplicate rows:",df.duplicated().sum())