import requests
import sys

def get_employee_todo_progress(employee_id):
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()
    
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todo_data = todo_response.json()

    completed_tasks = [task for task in todo_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_data)

    print(f"Employee {user_data['name']} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")

 
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
