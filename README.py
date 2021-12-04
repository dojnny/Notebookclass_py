https://github.com/dojnny/Notebook_pyclass

# Notebook PyClass - Real World Notebook in Python

## Description of Class
This is a simple program which involves using a Notebook as a real-world object to model for my class. 
For the constructor method, I passed self, and the book brandm and for my class variables, 
I included a fixed brand and number of pages (100 for each notebook). 
For my methods I used real-world common uses of Notebooks, I used examples from the real world such as opening/closing a notebook, reading/writing in a notebook, 
moving to the next or previous page, and turning to an arbitrary page.

## Description of Class and Data Variables

### Class Variables:
Number of pages belongs to the class, it is the class variable.
This means that it is shared by all instances so, because __number_of_pages is set to 100, every instance of the class is going to have that as it's value.

### Data Variables
Open, pages, current pages, title, and brand are all data variables which I created to be used in methods like getters and setters. Since the variables were created under __init__, prefaced with "self.", they belong to the object instance. Some of them, like brand and title can be set with a value on the instance creation, because the constructor's function input values are attached to them.

# Description of Methods
- def get_brand(self): The method get_brand only accepts self as argument as there is no input. The method only returns the fixed class variable of Brand.
- def set_page_number(self, page_num): The method set_page_number accepts itself and the argument page_num. An if statement is being used to check whether the notebook is open and if not, an error message will be printed to the user. Then, page_num is set equal to current speed and returned.
- def get_page_number(self): The method get_page_number accepts itself as an argument and it returns the current page depending on input from the main function.
- def set_title(self, title): The method set_title accepts itself and the argument title. An if statement is being used to check whether the notebook is open and if not, an error message will be printed to the user. Then, the data variable self.___title is set equal to the title and returned to the user.
- def open(self): The method open only accepts itself as the argument. The notebook opens when a boolean value of true is equal to self.__open and set the current_page to 1 as the notebook only has been opened.
- def close(self): The close method is basically the same as the open function as in it only accepts itself as an argument. The notebook closes when a boolean value of false is equal to self.__open. The current_page is also set to none as the notebook is closed.
- def turn_to_next_place(self): The turn_to_next_page method takes in itself as an argument. The method also checks whether the notebook is open using an if statement. An if statement is also used to increase page count if conditions are met. An else statement is included if the user is on page 100 which is the maximum number of pages due to the class variable. 
- def turn_to_previous_page(self): The turn_to_previous_page method takes in itself as an argument. The method also checks whether the notebook is open using an if statement. An if statement is also used to decrease page count if conditions are met. An else statement is included if the user is on page 1.
- def write(self, text): The write method takes in itself and text as an argument. An if statement is used to check whether the notebook is open, and if not, an error message will be printed. An if and else statement is used to append text at the end of a page at a new line.
- def read(self): The read method takes in itself as an argument and an if statement is also used to check whether the notebook is open. Use if statements to read what is on the current page or print a message to the user that “Book Finished”.
- def word_count(self, word): The word_count method takes in itself and word as arguments. The word_count is set to 0 and a for loop is used to iterate through all the words. Then, the program adds the count of occurrences of each word in the certain page.
- def read_book(self): The read_book method takes in itself as the argument. It prints the title given by the user and a for loop is used to iterate through the entire notebook. It will print an error if the book is unopened, and return.

## Demo  

In our main function of our program, we instanciate a notebook object from the Notebook class, then we try opening it so we are able to write on it.
Later on, we test each of the created functions, by getting and setting some of the variables, and also executing some of the object's methods, like reading the whole notebookbook 
(notebook.read_book()). We also promt the user to enter some text to write into a page in the notebook, and we ask the user to navigate the notebook in a desired direction.

To run this demo program, you have to clone the repository, and then execute the python file

    git clone https://github.com/dojnny/Notebook_pyclass.git . # Clone the repository
    python ./class.py # Execute the python file