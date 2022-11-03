import pandas as pd
from pandas_profiling import ProfileReport


if __name__ == '__main__':
    df = pd.read_csv('data/raw/heart_cleveland_upload.csv')
    profile = ProfileReport(df, title="Pandas Profiling Report")
    profile.to_file('references/report.html')

