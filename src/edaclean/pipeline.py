import pandas as pd
class Pipeline:
    def __init__(self, source):
        self.source = source
    def run(self):
        df=pd.read_csv(self.source)
        print(f"EdaClean is processing:{self.source}")
        print("\nDataset preview:")
        print(df.head())
        print("\ntotal rows :", len(df))
        print("total columns:",len(df.columns))