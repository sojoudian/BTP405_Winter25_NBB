import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
rainfall = [75, 60, 100, 125, 175, 200, 225, 210, 180, 140, 90, 80]

# Plotting
plt.figure(figsize=(10, 6))  # Set figure size
plt.bar(months, rainfall, color="skyblue", edgecolor="black")

# Adding labels and title
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall Distribution", fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout for better fit

# Show the plot
plt.show()
