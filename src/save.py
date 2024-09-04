import pandas as pd
import datetime


now = datetime.datetime.now()
outputFile = f"/Users/thuptenwangpo/Downloads/masterAttendanceSheet{now}.csv"
good = "masterAttendanceSheet/masterAttendance"
test = "testFiles/masterAttendanceTest.csv"


#### CHANGE THE BELOW FROM GOOD TO TEST OR VICE VERSA AS NECESSARY
df = pd.read_csv(f"/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/{test}")


if __name__ == "__main__":
    df.to_csv(outputFile, index=True)
    print("csv saved to downloads")