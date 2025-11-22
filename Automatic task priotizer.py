import datetime

def compute_priority(task):
    today = datetime.date.today()
    days_left = (task["deadline"] - today).days

    urgency = max(0, 1 - (days_left / 30))
    importance = task["importance"] / 5
    effort_score = 1 - (task["effort"] / 480)
    dep_score = task["dependencies"] / 5

    score = (0.4 * urgency +
             0.3 * importance +
             0.15 * effort_score +
             0.1 * dep_score)

    return score


def prioritize_tasks(task_list):
    for task in task_list:
        task["score"] = compute_priority(task)

    return sorted(task_list, key=lambda x: x["score"], reverse=True)


# ---------------------------
#   USER INPUT SECTION
# ---------------------------

tasks = []
n = int(input("Enter number of tasks: "))

for i in range(n):
    print(f"\n--- Task {i+1} ---")

    name = input("Task name: ")

    # deadline input (YYYY-MM-DD)
    deadline_str = input("Enter deadline (YYYY-MM-DD): ")
    year, month, day = map(int, deadline_str.split("-"))
    deadline = datetime.date(year, month, day)

    importance = int(input("Importance (1-5): "))
    effort = int(input("Effort in minutes (0-480): "))
    dependencies = int(input("Dependencies count (0-5): "))

    task = {
        "name": name,
        "deadline": deadline,
        "importance": importance,
        "effort": effort,
        "dependencies": dependencies
    }

    tasks.append(task)

# ---------------------------
#   DISPLAY PRIORITIZED LIST
# ---------------------------

result = prioritize_tasks(tasks)

print("\n\n===== PRIORITIZED TASK LIST =====")
for t in result:
    print(f"{t['name']}  -->  Score: {t['score']:.3f}")
