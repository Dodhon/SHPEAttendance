import pandas as pd
import os

def process_emails(emails):
    return [email.lower() for email in emails]
def getFiles(path="/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/attendanceFormResponses/"):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]

def createMasterAttendance(files):
    masterDf = pd.DataFrame()
    for file in files:
        df = pd.read_csv(file)

        event_name = os.path.splitext(os.path.basename(file))[0]

        emailCol = next((col for col in df.columns if "email" in col.lower()), None)
        if emailCol:
            df.rename(columns={emailCol: "Email"}, inplace=True)
        else:
            print(f"Warning: No email column found in {file}. Skipping...")
            continue 

        df['Email'] = process_emails(df['Email'])
        df['Event'] = event_name  
        masterDf = pd.concat([masterDf, df[['Email', 'Event']]], ignore_index=True)

    return masterDf

def createBinaryMatrix(masterDf):
    binaryMatrix = masterDf.pivot_table(index='Email', columns='Event', aggfunc='size', fill_value=0)
    binaryMatrix = binaryMatrix.applymap(lambda x: 1 if x > 0 else 0)
    return binaryMatrix

if __name__ == "__main__":
    files = getFiles()
    master_attendance = createMasterAttendance(files)
    binaryMatrix = createBinaryMatrix(master_attendance)

    output_file = "/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/masterAttendanceSheet/masterAttendance.csv"
    binaryMatrix.to_csv(output_file, index=True)
    print(f"Binary attendance matrix saved to {output_file}")