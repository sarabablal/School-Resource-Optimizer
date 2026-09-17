import os
from src.optimizer import ResourceOptimizer


def main():
    csv_path = os.path.join("data", "processed_schools.csv")

    optimizer = ResourceOptimizer(csv_path)
    all_categories = optimizer.load_categories()
    overcrowded, light_load = optimizer.partition_categories()

    total_count = len(all_categories)
    overcrowded_count = len(overcrowded)
    light_count = len(light_load)
    balanced_count = total_count - (overcrowded_count + light_count)

    print(" MOROCCAN EDUCATION RESOURCE EVALUATION REPORT ")
    print(f" Total Categories Evaluated : {total_count}")
    print(f" 🔴 Overcrowded             : {overcrowded_count}")
    print(f" 🟡 Light Load              : {light_count}")
    print(f" 🔵 Balanced                : {balanced_count}")

    print("\nOVERCROWDED CATEGORIES (HIGH PRIORITY):")
    if overcrowded:
        for cat in overcrowded:
            print(
                f"  - [{cat.category_id}] {cat.level} {cat.sector:<8} | Students: {cat.students:<10} | Rooms: {cat.rooms:<8} | Students/Room: {cat.get_students_per_room():.1f}"
            )
    else:
        print("None!")

    print("\nLIGHT LOAD CATEGORIES:")
    if light_load:
        for cat in light_load:
            print(
                f"  - [{cat.category_id}] {cat.level} {cat.sector:<8} | Students: {cat.students:<10} | Rooms: {cat.rooms:<8} | Students/Room: {cat.get_students_per_room():.1f}"
            )
    else:
        print("None!")


if __name__ == "__main__":
    main()
