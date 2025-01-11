import pandas as pd
import datetime

## file save details
now = datetime.datetime.now()
repoPath = "/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/"
test = "testFiles/masterAttendanceTest.csv"

main = "masterAttendanceSheet/masterAttendanceSheetFall2024.csv"
outputFile = f"/Users/thuptenwangpo/Downloads/masterAttendanceSheet{now}.csv"


df = pd.read_csv(f"{repoPath}{main}")


if __name__ == "__main__":
    df.to_csv(outputFile, index=True)
    print(f"csv saved to downloads as: {outputFile}")