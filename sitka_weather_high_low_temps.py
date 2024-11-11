import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

def read_weather_data(filename):
  """Reads weather data from a CSV file and returns dates, highs, and lows.

  Args:
      filename: The path to the CSV file.

  Returns:
      A tuple of three lists: dates, high temperatures, and low temperatures.
  """

  dates, highs, lows = [], [], []
  try:
      with open(filename) as f:
          reader = csv.reader(f)
          header_row = next(reader)  # Skip the header row

          for row in reader:
              try:
                  current_date = datetime.strptime(row[2], '%Y-%m-%d')
                  high = int(row[5])
                  low = int(row[6])
                  dates.append(current_date)
                  highs.append(high)
                  lows.append(low)
              except (ValueError, IndexError) as e:
                  print(f"Error processing row: {row}. Error: {e}")
  except FileNotFoundError:
      print(f"File not found: {filename}")

  return dates, highs, lows

def plot_data(data, label, color):
  """Plots the provided data on a graph with a specified label and color.

  Args:
      data: The list of data points to plot (e.g., high temperatures).
      label: The label for the data series.
      color: The color to use for the line.
  """

  plt.plot(dates, data, color=color, label=label)

# Use the full path to the CSV file
filename = 'C:\\Users\\mteso\\Downloads\\sitka_weather\\sitka_weather_2018_simple.csv'

# Read weather data
dates, highs, lows = read_weather_data(filename)

# Display welcome message and menu options
print("Welcome to the Sitka Weather Data Analyzer!")
print("Select an option:")
print("  - 'h': View High Temperatures")
print("  - 'l': View Low Temperatures")
print("  - 'e': Exit")

while True:
  # Get user input
  choice = input("Enter your choice (h, l, or e): ").lower()

  # Process user choice
  if choice == 'h':
    plot_data(highs, "Daily High Temperatures", "red")
  elif choice == 'l':
    plot_data(lows, "Daily Low Temperatures", "blue")
  elif choice == 'e':
    print("Exiting...")
    sys.exit()  # Exit the program using sys.exit()
  else:
    print("Invalid choice. Please select 'h', 'l', or 'e'.")

  # Format and display the plot
  plt.title("Daily Temperatures - 2018", fontsize=16)
  plt.xlabel("Date", fontsize=12)
  plt.ylabel("Temperature (F)", fontsize=12)
  plt.xticks(rotation=45)
  plt.grid(True)
  plt.legend()
  plt.tight_layout()
  plt.show()