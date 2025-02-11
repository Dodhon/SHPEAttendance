import matplotlib.pyplot as plt
import pandas as pd
import os

def load_attendance_data(semester):
    """Load all attendance form responses for the given semester"""
    folder_path = f"/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/attendanceFormResponses{semester}"
    
    if not os.path.exists(folder_path):
        print(f"Folder not found for {semester}. Please check the semester name and try again.")
        return None
    
    try:
        # Get all CSV files in the folder
        all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
        if not all_files:
            print(f"No CSV files found in {folder_path}")
            return None
        
        # Read each file and store with event name
        events_data = {}
        for file in all_files:
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)
            
            # Find the major column (case insensitive)
            major_col = next((col for col in df.columns if 'major' in col.lower()), None)
            if major_col:
                event_name = os.path.splitext(file)[0]
                events_data[event_name] = df[major_col]
            else:
                print(f"Warning: No major column found in {file}")
        
        return events_data
        
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def process_majors(majors_series):
    """Clean and standardize major names"""
    return majors_series.str.upper().str.strip()

def create_major_distribution_chart(major_counts, title, save_path):
    """Create and save pie chart of major distribution"""
    plt.figure(figsize=(12, 8))
    plt.pie(major_counts.values, 
            labels=[f"{major} ({count})" for major, count in zip(major_counts.index, major_counts.values)],
            autopct='%1.1f%%',
            startangle=90)
    
    plt.title(title)
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()

def print_major_statistics(major_counts, total_students, event_name="Overall"):
    """Print detailed statistics about major distribution"""
    print(f"\nMajor Distribution for {event_name}:")
    for major, count in major_counts.items():
        percentage = count/total_students * 100
        print(f"{major}: {count} students ({percentage:.1f}%)")

def plot_majors_distribution(semester):
    """Create pie charts showing the distribution of majors for the semester and each event"""
    
    # Load data
    events_data = load_attendance_data(semester)
    if events_data is None:
        return
    
    try:
        # Create graphs folder and event-specific subfolder
        graphs_folder = "graphs"
        semester_folder = os.path.join(graphs_folder, f"majors_{semester}")
        os.makedirs(semester_folder, exist_ok=True)
        
        # Process overall distribution
        all_majors = pd.concat(events_data.values())
        cleaned_majors = process_majors(all_majors)
        major_counts = cleaned_majors.value_counts()
        
        # Create and save overall chart
        overall_path = os.path.join(semester_folder, f"majors_distribution_overall_{semester}.png")
        create_major_distribution_chart(
            major_counts, 
            f"Overall Distribution of Majors - {semester}", 
            overall_path
        )
        print(f"\nOverall distribution chart saved as {overall_path}")
        print_major_statistics(major_counts, len(cleaned_majors))
        
        # Process each event separately
        for event_name, majors_data in events_data.items():
            cleaned_event_majors = process_majors(majors_data)
            event_counts = cleaned_event_majors.value_counts()
            
            # Create and save event chart
            event_path = os.path.join(semester_folder, f"majors_distribution_{event_name}.png")
            create_major_distribution_chart(
                event_counts,
                f"Distribution of Majors - {event_name}",
                event_path
            )
            print(f"\nEvent distribution chart saved as {event_path}")
            print_major_statistics(event_counts, len(cleaned_event_majors), event_name)
            
    except Exception as e:
        print(f"Error processing data: {str(e)}")

if __name__ == "__main__":
    semester = input("Enter semester (e.g., Spring2025): ")
    plot_majors_distribution(semester)
