import pandas as pd

# Data preparation
programmer = list(range(1, 11))
prog1_time = [104, 102, 159, 168, 150, 151, 111, 105, 137, 124]
prog2_time = [71.3, 110, 178, 153, 120, 174, 94.9, 86.1, 115, 175]
ide_prog1 = ["IDE-A", "IDE-B", "IDE-A", "IDE-A", "IDE-B", "IDE-B", "IDE-A", "IDE-B", "IDE-A", "IDE-B"]
ide_prog2 = ["IDE-B", "IDE-A", "IDE-B", "IDE-B", "IDE-A", "IDE-A", "IDE-B", "IDE-A", "IDE-B", "IDE-A"]

data = pd.DataFrame({
    "Programmer": programmer*2,
    "Program": ["Prog-1"]*10 + ["Prog-2"]*10,
    "IDE": ide_prog1 + ide_prog2,
    "Time": prog1_time + prog2_time
})

# Descriptive statistics
desc_stats = data.groupby("IDE")["Time"].agg(['count','mean','median','std','min','max'])
print(desc_stats)

