import requests

url = "https://jsonplaceholder.typicode.com/todos?userId=1"
response = requests.get(url)


if response.status_code == 200:
    todos = response.json()

    user_id = 1
    total_tasks = len(todos)
    completed_tasks = 0

    for todo in todos:
        if todo.get("completed", False):
            completed_tasks += 1

    pending_tasks = total_tasks - completed_tasks
    completion_rate = (completed_tasks / total_tasks) * 100

    if completion_rate >= 80:
        project_status = "EXCELLENT"
    elif completion_rate >= 50:
        project_status = "GOOD"
    else:
        project_status = "NEEDS_FOCUS"

    print("API Request Status: Success")
    print("User ID:", user_id)
    print("Total Tasks:", total_tasks)
    print("Completed Tasks:", completed_tasks)
    print("Pending Tasks:", pending_tasks)
    print("Completion Rate: {:.2f}%".format(completion_rate))
    print("Project Status:", project_status)

else:
    print("API Request Status: Failed")
    print("Error: Could not fetch data. Status code:", response.status_code)
