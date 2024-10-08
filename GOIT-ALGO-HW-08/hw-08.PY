import pickle
import AdressBook

def save_data(book, filename ="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()

    # Основний цикл програми

    save_data(book)  # Викликати перед виходом з програми