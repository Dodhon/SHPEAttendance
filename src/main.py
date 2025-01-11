import pandas as pd
import os


## Each attendance forms needs an email question
#################################

## file save details
#change as per semester
sample_semester = "Fall2024"
semester = "Fall2024"
repoPath = "/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/"
fileName = f"masterAttendanceSheet{semester}.csv"
folderName = "masterAttendanceSheet/"
attendanceResponsesFolder = f"/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/attendanceFormResponses{semester}/"

def check_folder_exists():
    if not os.path.exists(attendanceResponsesFolder):
        os.makedirs(attendanceResponsesFolder)
def check_empty_folder():
    dir = os.listdir(attendanceResponsesFolder)
    if len(dir) == 0: 
        return True
    else: 
        return False
    
def process_emails(emails):
    return [email.lower() for email in emails]

def getFiles(path=attendanceResponsesFolder):
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
    binaryMatrix = binaryMatrix.map(lambda x: 1 if x > 0 else 0)
    return binaryMatrix

def add_attendance_stats(binaryMatrix):
    attendance_counts = binaryMatrix.sum(axis=0)
    attendance_counts.name = 'Event Attendance'

    binaryMatrix = pd.concat([pd.DataFrame(attendance_counts).T, binaryMatrix])

    people_counts = binaryMatrix.sum(axis=1)

    binaryMatrix.insert(0, 'Total Attendance', people_counts)

    return binaryMatrix

if __name__ == "__main__":
    check_folder_exists()
    if check_empty_folder() == True:
        print("Attendance folder is empty. Please check that the semester and folder variable are set properly and folders are actually updated with info from attendance forms.")
        
    else:
        files = getFiles()
        master_attendance = createMasterAttendance(files)
        binaryMatrix = createBinaryMatrix(master_attendance)
        binaryMatrix = add_attendance_stats(binaryMatrix) 
        
        outputFile = f"{repoPath}{folderName}{fileName}"
        binaryMatrix.to_csv(outputFile, index=True)
        print(f"Master Attendance Sheet updated/created.")