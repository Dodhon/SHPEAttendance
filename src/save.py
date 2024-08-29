import pandas as pd

outputFile = "/Users/thuptenwangpo/Downloads/masterAttendanceSheet.csv"
df = pd.read_csv("/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/masterAttendanceSheet/masterAttendance.csv")


if __name__ == "__main__":
    df.to_csv(outputFile, index=True)
    print("csv saved to downloads")