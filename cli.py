from db import initialize_database
from author import Author
from article import Article

def start_cli():
    while True:
        print("\n=== Magazine CLI ===")
        print("1. Manage Authors")
        print("2. Manage Articles")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            manage_authors()
        elif choice == "2":
            manage_articles()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

def manage_authors():
    while True:
        print("\n-- Authors --")
        print("1. Create Author")
        print("2. List Authors")
        print("3. Delete Author")
        print("4. View Author's Articles")
        print("5. Back")
        choice = input("Option: ")

        if choice == "1":
            try:
                name = input("Enter name: ")
                author = Author.create(name)
                print(f"Created author: {author.name}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            for a in Author.get_all():
                print(f"{a.id}: {a.name}")
        elif choice == "3":
            id = input("Enter author ID: ")
            author = Author.find_by_id(int(id))
            if author:
                author.delete()
                print("Deleted.")
            else:
                print("Author not found.")
        elif choice == "4":
            id = input("Enter author ID: ")
            author = Author.find_by_id(int(id))
            if author:
                articles = author.get_articles()
                for art in articles:
                    print(f"{art.id}: {art.title} - {art.content}")
            else:
                print("Author not found.")
        elif choice == "5":
            break

def manage_articles():
    while True:
        print("\n-- Articles --")
        print("1. Create Article")
        print("2. List Articles")
        print("3. Delete Article")
        print("4. Back")
        choice = input("Option: ")

        if choice == "1":
            try:
                title = input("Title: ")
                content = input("Content: ")
                author_id = int(input("Author ID: "))
                if not Author.find_by_id(author_id):
                    print("Author not found.")
                    continue
                article = Article.create(title, content, author_id)
                print(f"Created article: {article.title}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            for a in Article.get_all():
                print(f"{a.id}: {a.title} - {a.content} (Author ID: {a.author_id})")
        elif choice == "3":
            id = input("Enter article ID: ")
            article = Article.find_by_id(int(id))
            if article:
                article.delete()
                print("Deleted.")
            else:
                print("Article not found.")
        elif choice == "4":
            break

if __name__ == "__main__":
    initialize_database()
    start_cli()
