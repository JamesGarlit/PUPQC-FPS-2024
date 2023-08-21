import subprocess

def commit_and_push(message):
    subprocess.run(["git", "add", "."])  # Stage all changes
    subprocess.run(["git", "commit", "-m", message])  # Commit changes with the provided message
    subprocess.run(["git", "push"])  # Push changes to remote repository

def pull_changes():
    subprocess.run(["git", "pull"])  # Pull changes from remote repository

def create_tag(tag_name, tag_message):
    subprocess.run(["git", "tag", "-a", tag_name, "-m", tag_message])  # Create a new tag

if __name__ == "__main__":
    print("Python Web Development Version Control Script")
    
    while True:
        print("\nOptions:")
        print("1. Commit and Push Changes")
        print("2. Pull Changes")
        print("3. Create Version Tag")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            commit_message = input("Enter commit message: ")
            commit_and_push(commit_message)
        elif choice == "2":
            pull_changes()
        elif choice == "3":
            tag_name = input("Enter tag name: ")
            tag_message = input("Enter tag message: ")
            create_tag(tag_name, tag_message)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")
