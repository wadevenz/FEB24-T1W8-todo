import csv

def add_todo(file_name):
    todo_name = input("Enter a todo item: ")
    # with blocks close files automatically
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print("Remove todo")

def mark_todo(file_name):
    print ("Mark todo")

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
