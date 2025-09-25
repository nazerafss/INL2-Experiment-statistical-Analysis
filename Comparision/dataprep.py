import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Programmer IDs
programmer = list(range(1, 11))

# Time taken for each program
prog1_time = [104, 102, 159, 168, 150, 151, 111, 105, 137, 124]
prog2_time = [71.3, 110, 178, 153, 120, 174, 94.9, 86.1, 115, 175]

# IDE assignments according to Table 1
ide_prog1 = ["IDE-A", "IDE-B", "IDE-A", "IDE-A", "IDE-B", "IDE-B", "IDE-A", "IDE-B", "IDE-A", "IDE-B"]
ide_prog2 = ["IDE-B", "IDE-A", "IDE-B", "IDE-B", "IDE-A", "IDE-A", "IDE-B", "IDE-A", "IDE-B", "IDE-A"]

# Combine into a long-format DataFrame
data = pd.DataFrame({
    "Programmer": programmer*2,
    "Program": ["Prog-1"]*10 + ["Prog-2"]*10,
    "IDE": ide_prog1 + ide_prog2,
    "Time": prog1_time + prog2_time
})

print(data.head(20))
# Compute mean time per IDE
mean_times = data.groupby("IDE")["Time"].mean().reset_index()

# Bar plot
plt.figure(figsize=(6,4))
sns.barplot(x="IDE", y="Time", data=mean_times, palette="pastel")
plt.title("Average Development Time by IDE")
plt.ylabel("Average Time (minutes)")
plt.show()