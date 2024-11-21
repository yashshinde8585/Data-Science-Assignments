import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame manually or read from a CSV file
data = {
    'Date': ['03-10-16', '04-10-16', '05-10-16', '06-10-16', '07-10-16'],
    'Close': [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime for better plotting
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')

# Plot the closing values
plt.plot(df['Date'], df['Close'], marker='o', linestyle='-', color='g')

# Customize the grid
plt.grid(True, linestyle='-', linewidth=0.5, color='blue')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.title('Closing Values of Alphabet Inc. (Oct 3, 2016 - Oct 7, 2016)')

# Rotate the date labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()
