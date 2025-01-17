import os
import pandas as pd

def evaluate_offensive_performance(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Calculate average yards per drive
    avg_yards_per_drive = data.groupby('Offense')['Yards'].mean()

    # Calculate scoring efficiency (percentage of scoring drives)
    scoring_efficiency = data.groupby('Offense')['Scoring'].mean() * 100

    # Calculate average plays per drive
    avg_plays_per_drive = data.groupby('Offense')['Plays'].mean()

    # Combine metrics into a single DataFrame
    offensive_metrics = pd.DataFrame({
        'Avg Yards per Drive': avg_yards_per_drive,
        'Scoring Efficiency (%)': scoring_efficiency,
        'Avg Plays per Drive': avg_plays_per_drive
    })

    # Sort by scoring efficiency for better readability
    offensive_metrics = offensive_metrics.sort_values(by='Scoring Efficiency (%)', ascending=False)

    return offensive_metrics

# File path to the dataset
file_path = './data/driveData.csv'

# Evaluate offensive performance
offensive_metrics = evaluate_offensive_performance(file_path)

# Display the results
print("Offensive Performance Metrics:")
print(offensive_metrics)

# Ensure the output directory exists
output_dir = './resultData.csv'
os.makedirs(output_dir, exist_ok=True)

# Save the results to a CSV file
output_path = os.path.join(output_dir, 'offensive_metrics.csv')
offensive_metrics.to_csv(output_path)
print(f"Metrics saved to {output_path}")
