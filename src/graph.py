import matplotlib.pyplot as plt
import pandas as pd
import os

# File path to the master attendance sheet
file_path = "/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/masterAttendanceSheet/masterAttendanceSheetFall2024.csv"

def plot_attendance_pie_chart(attendance_counts, save_path):
    # Create pie chart
    plt.figure(figsize=(10, 8))
    attendance_counts.plot.pie(
        autopct='%1.1f%%',
        startangle=140,
        legend=False,
        title="Distribution of Attendance Across Events (Excluding Total Attendance)"
    )
    plt.ylabel('')  # Remove default ylabel
    plt.savefig(save_path, bbox_inches='tight')  # Save the chart
    plt.show()

if __name__ == "__main__":
    if not os.path.exists(file_path):
        print(f"File not found at {file_path}. Please check the path and try again.")
    else:
        # Read the master attendance sheet
        master_df = pd.read_csv(file_path, index_col=0)
        
        # Ensure the 'Event Attendance' row exists
        if 'Event Attendance' not in master_df.index:
            print("The 'Event Attendance' row is missing in the file.")
        else:
            # Extract attendance counts for pie chart
            attendance_counts = master_df.loc['Event Attendance']
            
            # Exclude "Total Attendance" if it exists in the columns
            if "Total Attendance" in attendance_counts:
                attendance_counts = attendance_counts.drop("Total Attendance")
            
            # File path for saving the chart
            ##### change for appropriate semester
            save_path = "attendance_distribution/attendance_pie_chart_fall2024.png"
            
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            # Plot and save the pie chart
            plot_attendance_pie_chart(attendance_counts, save_path)
            
            print(f"Pie chart saved as {save_path}.")
