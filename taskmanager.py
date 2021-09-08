import datetime

#def function, main menu
#if admin, has a 2 more options
#otherwise if user not admin, has fewer options
#use if statements to take user to another function

def main_menu():
    if username == "admin":

        print("\nPlease select from one of the following options \nr: register user \na: add task \nva: view all tasks \nvm: view my tasks \ngr: generate reports \nds: display statistics \ne: exit ")
        user_option = input("Enter r/a/va/vm/gr/ds/e: ")
    
    else:

        print("\nPlease select from one of the following options \na: add task \nva: view all tasks \nvm: view my tasks \ne: exit ")
        user_option = input("Enter a/va/vm/e: ")    

    if username == "admin" and user_option == "r":

        reg_user()
   

    if user_option == "a":

        add_task()


    if user_option == "va":

        view_all()

    
    if user_option == "vm":

        view_mine()    
                

    if user_option == "ds" and username == "admin":
    
        display_stats()

    if user_option == "gr" and username == "admin":

        generate_reports()

#open user text file to append
#ask user for new username and pw
#confirm pw
#add new user and pw to text file and close file
#print 'user has been added' to let user know new user has been added

def reg_user():
    file2 = open('user.txt', 'a')

    new_username = input("Enter new username: ")
    while new_username in user_dict:
        print("This user already exists. ")
        new_username = input("Enter new username: ")
        
    else:
        new_password = input("Enter a password: ")
        confirm_pw = input("Re-enter password: ")

        if new_password == confirm_pw:
            file2.write(new_username +", ")
            file2.write(new_password +"\n")

    file2.close()                    

    print("New user has been added. ")

#open task text file
#ask the user who task is assigned to
#if assigned to a user not in user dict(see below for details on dict)
#ask to assign a user in the dict
#ask user to input details for task
#write the collected info to task file and close file
#print to let user know task has been added 



def add_task():
    file3 = open('tasks.txt', 'a')
    
    task_user = input("Enter the username for who this task is assigned: ")
    while task_user not in user_dict:
        print("This user is not registered. ")
        task_user = input("Enter the username for who this task is assigned: ")
    else:
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter a discription of the task: ")
        date_today = datetime.date.today()
        task_duedate = input("Enter the due date of the task yyyy-mm-dd: ")
        task_complete = "No"

        file3.write(task_user + ", " + task_title + ", " + task_description + ", " + str(date_today) + ", " + task_duedate + ", " + task_complete + "\n")

        file3.close()

        print("Your task has been added. ")    

#open tasks text file
#using split() function, separate info from the text file
#print info from text file in a user friendly manner


def view_all():
    with open('tasks.txt', 'r+') as f:
        for line in f:
            x = line.split(",")
            print(f"User: " + x[0] + "\n" + "Task title: " + x[1] + "\n" + "Task description: " + x[2] + "\n" + "Task assigned on: " + x[3] + "\n" + "Task due on: " + x[4] + "\n" + "Task complete?: " + x[5] + "\n")

#open task file and read text
#use split() function to separate each new line of text
#text becomes list and if the last item of list is empty, remove item
#using for loop separate each task into a dict
#use counter function to number each task
#for user logged in, print dict for user in a user frienly manner 


def view_mine():

    f = open('tasks.txt', 'r+')
    text = f.read()
    f.close()
    text_list = text.split("\n")
    if text_list[-1] == "" or "\n":
        text_list.remove(text_list[-1])
    

    counter = 0 
    for line in text_list:
        counter = counter + 1
        x = line.split(",")
        vm_dict = {"Task: ": counter,
                   "User: ": x[0],
                   "Task title: ": x[1],
                   "Task description: ": x[2],
                   "Task assigned on: ": x[3],
                   "Task due on: ": x[4],
                   "Task complete?: ": x[5]}

        for k, v in vm_dict.items():
            if vm_dict["User: "] == username:
                print(k,v)

    #user can enter a task number to edit their task
    #-1 takes user back to main menu (using elif)
    #using if statements, give user different option to edit task
    #use replace() function to change items
    #cast text list back to str
    #open txt file and replace the text in file to new text
    #use w function to write the new text into the file 
                
    orig_user_select = int(input("To select a task enter the task number, or enter -1 to return to the main menu: "))

    user_select = (orig_user_select -1)
    if orig_user_select != -1:
        
        user_edit = input(f"To mark task {user_select+1} as complete, enter 'Y', or enter 'E' to edit: ")
        
        if user_edit == "Y":
            for line in text_list:
                text_list[user_select] = text_list[user_select].replace(text_list[user_select][-2:], "yes")
                break
            print(f"Task {orig_user_select} has been marked as complete. ")
            print(text_list)             
        elif user_edit == "E":
            user_date_name = input("To reassign the task to another user enter 'U' or to change the due date enter 'D': ")
            if user_date_name == "U":
                new_name = input(f"Enter the username task {user_select+1} is being reassigned to: ")
                for line in text_list:
                    text_list[user_select] = text_list[user_select].replace(username, new_name)
                    break
            if user_date_name == "D":
                new_date = input("Enter new due date yyyy-mm-dd: ")
                for line in text_list:
                    text_list[user_select] = text_list[user_select].replace(text_list[user_select][-14:-4], new_date)
                    break

        text_str = "\n".join(text_list)

        f1 = open('tasks.txt', 'r')
        new_text = f1.read()
        new_text = new_text.replace(new_text, text_str)
        f1.close()

        f1 = open('tasks.txt', 'w')
        f1.write(new_text + "\n")
        f1.close()
        
        
    elif orig_user_select == -1:
        main_menu()
    
#open task and user overview files
#rad the data and print it out 
          
def display_stats():
   
    f1 = open('task_overview.txt', 'r')
    f1text = f1.read()
    f1.close()
    print(f1text)

    f2 = open('user_overview.txt', 'r')
    f2text = f2.read()
    f2.close()
    print(f2text)

#like above, open tasks file, change text from str to list
#using len(), determine num of tasks
#for incomp/comp, use for loop to check if line ends with yes/no
#if yes and to comp list, if no add line to incomp list
#if overdue, use incomp list to check if date is ovedue
#use len() function to check how many items in each list
#calculate percentages
#using multi string, write text as str to file


def generate_reports():

    f = open('tasks.txt', 'r+')
    text = f.read()
    f.close()
    text_list = text.split("\n")
    if text_list[-1] == "":
        text_list.remove(text_list[-1])
  

    num_of_tasks = len(text_list)

    
    incomp = []
    for line in text_list:
        if line.endswith("No") or line.endswith("no"):
            incomp = incomp + line.split("\n")
    
    num_of_incomp = len(incomp)


    comp = []
    for line in text_list:
        if line.endswith("Yes") or line.endswith("yes"):
            comp = comp + line.split("\n")
    
    num_of_comp = len(comp)


    incomp_overdue = []
    today_date = str(datetime.date.today())
    for line in incomp:
        date_list = line[-14:-4]
        if date_list < today_date:
            incomp_overdue = incomp_overdue + line.split("\n")

    num_incomp_overdue = len(incomp_overdue)

    perc_incomp = round(((num_of_incomp / num_of_tasks) * 100),2)
    perc_overdue = round(((num_incomp_overdue / num_of_tasks) * 100),2)
    
    
    text_overview_tasks = f"""Total number of tasks: {num_of_tasks}
Total number of completed tasks: {num_of_comp}
Total number of incomplete tasks: {num_of_incomp}
Total number of overdue tasks: {num_incomp_overdue}
Percentage of tasks incomplete: {perc_incomp}%
Percentage of tasks overdue: {perc_overdue}%
"""
    f1 = open('task_overview.txt', 'w')
    f1.write(text_overview_tasks)
    f1.close()


#for user overview, similar to above but get text from user file
#len() function to determine num of users
#use for loop and count function to determine how many tasks user is assigned
#add user and num of tasks assigned to dict
#cast dict to str to write into text user overview file
#use similar method to determine which user has tasks comp/incomp or overdue 

    f2 = open('user.txt', 'r+')
    user_text = f2.read()
    f2.close()
    user_text_list = user_text.split("\n")
    if user_text_list[-1] == "" or "\n":
        user_text_list.remove(user_text_list[-1])

    num_of_users = len(user_text_list)
    

    user_task_dict = {}
    for item in user_text_list:
        name = item.split(",")
        count = sum(line.count(name[0]) for line in text_list)
        user_task_dict[name[0]] = count
    user_tasks_overview = str(user_task_dict)


    user_perc_dict = {}
    for key in user_task_dict:
        user_perc_dict[key] = round((user_task_dict[key] / num_of_tasks) * 100,2)
    user_perc_overview = str(user_perc_dict)
                
    comp_user_dict = {}
    for item in comp:
        name = item.split(",")
        count = sum(line.count(name[0]) for line in comp)
        comp_user_dict[name[0]] = count
    

    final_comp_dict = {}
    for key in comp_user_dict:
        final_comp_dict[key] = round((comp_user_dict[key] / user_task_dict[key]) * 100,2)
    user_comp_overview = str(final_comp_dict)

    incomp_user_dict = {}
    for item in incomp:
        name = item.split(",")
        count = sum(line.count(name[0]) for line in incomp)
        incomp_user_dict[name[0]] = count

    final_incomp_dict = {}
    for key in incomp_user_dict:
        final_incomp_dict[key] = round((incomp_user_dict[key] / user_task_dict[key]) * 100,2)
    user_incomp_overview = str(final_incomp_dict)

    overdue_user_dict = {}
    for item in incomp_overdue:
        name = item.split(",")
        count = sum(line.count(name[0]) for line in incomp_overdue)
        overdue_user_dict[name[0]] = count

    final_overdue_dict = {}
    for key in overdue_user_dict:
        final_overdue_dict[key] = round((overdue_user_dict[key] / user_task_dict[key]) * 100,2)
    user_overdue_overview = str(final_overdue_dict)
    
    
    text_user_overview = f"""The total number of users registered: {num_of_users}
The total number of tasks: {num_of_tasks}
The number of tasks assigned to each user:
{user_tasks_overview}
% of total tasks assigned to each user:
{user_perc_overview}
% of tasks user has completed:
{user_comp_overview}
% of tasks user has yet to complete:
{user_incomp_overview}
% of tasks assigned that are overdue:
{user_overdue_overview}"""

    f3 = open('user_overview.txt', 'w')
    f3.write(text_user_overview)
    f3.close()

#create empty dict, user_dict
#open user txt file and add names from text file to dict
#when user logs in, if username in dict , ask user for pw
#if username not in dict, user will be asked for a valid username
#after logged in, begin by calling main_menu function 
  
user_dict = {}

file1 = open('user.txt', 'r+')

for line in file1:
    key = line.split()[0].strip(",")
    value = line.split()[1]
    user_dict[key] = value
    
file1.close()
print(user_dict)

username = input("Enter your username: ")


while username not in user_dict:
    username = input("Enter your username: ")
else:
    password = input("Enter your password: ")
    while password != user_dict[username]:
        password = input("Enter your password: ")
    else:
        print("\nWelcome to Task Manager")

main_menu()



        
        
