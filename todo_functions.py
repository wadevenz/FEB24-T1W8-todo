import csv

def add_todo(file_name):
    todo_name = input("Enter a todo item: ")
    # with blocks close files automatically
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    todo_name = input("Enter the todo name you want to delete: ")
    # Create a new list
    todo_lists = []
    # Put all the previous items in the new list except the deleted item
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader:
            if (todo_name != row[0]): # row index refers to the 'row' list inside the larger 'reader' list'
                todo_lists.append(row)
            else:
                is_exist = True
    
    if not is_exist:
        print("No item with that name exits")

    # And then rewrite list.csv with new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def mark_todo(file_name):
    todo_name = input("Enter the todo name that you want to mark complete: ")
    todo_lists = []
    with open(file_name, "r") as (f):
        reader = csv.reader(f)
        for row in reader:
            if (todo_name != row[0]):
                todo_lists.append(row)
            else:
                todo_lists.append([row[0], "True"])
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)


def view_todo(file_name):

    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            reader.__next__() # it will skip the first line
            for row in reader:
                if (row[1] == "True"):
                    print(f"{row[0]} is complete")
                else:
                    print(f"{row[0]} is not complete")
                        
    except FileNotFoundError:
        print("the todo file does not exist.")
