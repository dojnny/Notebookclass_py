# Donny Tang: Assignment 10.1 Your Own Class
# This is a simple program that mimics what a Notebook does.
class Notebook:
# Set Class variable as Brand and Number of Pages
    __number_of_pages = 100

    def __init__(self, brand, title = ""):
        # Initialize a notebook object with a required brand and an optional title.
        self.__open = False
        self.__pages = ['' for i in range(self.__number_of_pages)]
        self.__current_page = None
        self.__title = title
        self.__brand = brand

    def get_brand(self):
        # Get the notebook's brand.
        return self.__brand

    def set_page_number(self, page_num):
        # Set's the current page to a number, checking if the notebook was previously open. If not, prints an error.

        # If the notebook is closed, we print an error and return
        if self.__open == False:
            print('You cant turn the page because the notebook is closed')
            return
        self.__current_page = page_num
        

    def get_page_number(self):
        # Get the current page in the notebook.
        return self.__current_page

    def set_title(self, title):
        # Set the notebook's title to a desired one.
        self.__title = title
        
    def open(self):
        # Opens the notebook and sets the current page to 1.
        # Sets current_page to 1 and sets open to true

        self.__open = True
        self.__current_page = 1

    def close(self):
        # Closes the notebook and returns none for current page.
        # Sets current_page to None and sets open to false
        self.__open = False
        self.__current_page = None

    def turn_to_next_page(self):
        # Sets current page to next page, checking if the notebook is open. If not, prints an error.

        # Error handling if the notebook was closed
        if self.__open == False:
            print('You cant turn the page because the notebook is closed')
            return

        # If current page is greater than number of pages, increase page count by 1
        if self.__current_page < self.__number_of_pages:
            self.__current_page = self.__current_page + 1

        # Include else statement and print statement if user ever hits line 100.
        else:
            print('You are already on page %s, which is the last one' % self.__current_page)

    def turn_to_previous_page(self):
        # Sets current page to the previous value.

        # Check if notebook is open, if not print error message.
        if self.__open == False:
            print("You can't turn the previous page because the notebook is closed")
            return

        # If current page is greater than 1 page, decrease page count by 1.
        if self.__current_page > 1:
            self.__current_page = self.__current_page - 1
        # Include else statement and print statement if user is ever on first page.
        else:
            print('You are already on page 1')

    def write(self, text):
        # Check if notebook is open, if not print error message.
        # If the notebook was closed, handle the error
        if self.__open == False:
            print('You cant write because the notebook is closed')
            return
        # Use if statement to create empty array and set equal to text
        if self.__pages[self.__current_page - 1] == '':
            self.__pages[self.__current_page - 1] = text
        # Adds word to end of current page at new line
        else:
            self.__pages[self.__current_page - 1] += '\n' + text

    def read(self):
        # Check if notebook is open, if not print error message.

        # Error handling if the notebook was closed
        if self.__open == False:
            print("You can't read because the notebook is closed")
            return
        
        # Handling a finished notebook,
        if self.__current_page == self.__number_of_pages:
            print('Book finished')
            return

        # Handling blank pages
        if self.__pages[self.__current_page - 1] == '':
            print(self.__current_page +1 , ': [blank]')
            return

        # Printing a non blank and non final page of an opened notebook
        print(self.__pages[self.__current_page - 1])
    
    def word_count(self, word):
        # This function returns the amount of words in a notebook, iterating over each page.
        
        # Set word_count to 0
        word_count = 0
        # Use a for loop to interate through each page in pages.
        for page in self.__pages:
            # Add the count of occurrence of each word in that page to total word count
            word_count += page.count(word)
        # Return word_count
        return word_count
      
    def read_book(self):
        # Read an entire opened notebook, from start to finish, saving the page position .
        # at which the function was called, and returning the notebook to that page once it is finished. Gives an error if the notebook is closed.

        # Error handling for closed books
        if self.__open == False:
            print("You can't read the entire notebook because the notebook is closed")
            return

        print(self.__title)
        # Save the position when the function was called
        bookmark = self.get_page_number()
        # Go to the beginning (Page 1)
        self.set_page_number(1)
        # Use a for loop to iterate through entire book
        for i in range(self.__number_of_pages - 1):
            # Reads entire book and turns 99 pages
            self.read()
            self.turn_to_next_page()
        self.read()
        # Return to the bookmark position
        self.set_page_number(bookmark)
    

def main():
    # Initialize Notebook    
    notebook = Notebook("Walter White")
    notebook.set_title('The Best Cook')

    # Attempt to read closed book
    notebook.read()

    # Open the notebook
    notebook.open()

    # Attempt to read an open book
    notebook.read()

    # Print and access the current page number
    print(notebook.get_page_number())

    # Set the page number to an arbitrary value inside the range (100)
    notebook.set_page_number(10)
    print(notebook.get_page_number())
    notebook.open()
    notebook.read_book()

    # Change current page number
    notebook.turn_to_previous_page()
    notebook.turn_to_next_page()

    # Ask the user to turn the page
    user_direction_input = input("Go to the previous or next page? (type p/n):")
    if user_direction_input == "p":
        notebook.turn_to_previous_page()
    elif user_direction_input == "n":
        notebook.turn_to_next_page()
    else:
        print("Invalid direction!")

    # Write to the notebook
    notebook.write('Boba')
    notebook.write('Hello World')
    user_input = input("Enter some class notes to add to the page: ")
    notebook.write(user_input)

    notebook.read()
    notebook.turn_to_next_page()
    notebook.close()
    notebook.write('Something')
    # Look for count of the word ‘Hello’ in all pages of notebook
    print(str(notebook.word_count("Hello")))
    notebook.read_book()

if __name__ == "__main__":
    main()