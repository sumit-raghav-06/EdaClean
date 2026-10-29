from pathlib import Path
import pandas as pd
class Pipeline:
    def __init__(self, source):
        self.source = source
    def run(self):
        if not Path(self.source).is_file():
            print(f"Error: File not found:{self.source}")
            return
        df=pd.read_csv(self.source)
        print(f"EdaClean is processing:{self.source}")
        print("\nDataset preview:")
        print(df.head())
        print("\nTotal rows:", len(df))
        print("Total columns:",len(df.columns))

        #Calculate a data-quality score

        # CURRENT CODE ONLY MEASURES COMPLETENESS ONLY
        
        print("\nMissing values per column:")
        print(df.isnull().sum())
        print("\nDuplicate rows:",df.duplicated().sum())
        missing_values=df.isnull().sum().sum()
        total_cells = df.size

        if total_cells > 0:
            completeness_score = ((total_cells - missing_values) / total_cells) * 100
        else:
            completeness_score = 100.0
        print("\nCompleteness score:", round(completeness_score,2), "%")