import os
import matplotlib.pyplot as plt
from src.optimizer import ResourceOptimizer

# this script is separate from main.py, it just reuses the same data
# to draw a chart instead of printing text

csv_path = os.path.join("data", "processed_schools.csv")

optimizer = ResourceOptimizer(csv_path)
categories = optimizer.load_categories()

# build the labels (ex: "Primaire Public") and their students/room ratio
labels = [f"{cat.level} {cat.sector}" for cat in categories]
ratios = [cat.get_students_per_room() for cat in categories]

# color each bar red if overcrowded, green otherwise
colors = []
for cat in categories:
    if cat.get_status() == "Overcrowded":
        colors.append("red")
    elif cat.get_status() == "Light Load":
        colors.append("green")
    else:
        colors.append("orange")

plt.figure(figsize=(9, 5))
plt.bar(labels, ratios, color=colors)
plt.title("Students per Classroom by Education Category (Morocco 2024-2025)")
plt.xlabel("Category")
plt.ylabel("Students per Room")
plt.xticks(rotation=20)
plt.tight_layout()

os.makedirs("data", exist_ok=True)
plt.savefig("data/status_chart.png")
print("Chart saved to data/status_chart.png")

plt.show()
