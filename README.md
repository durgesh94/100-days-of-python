# 100-days-of-python
## Learning and Mastering Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
### Day-01
- Printing Practice
- Debugging Practice
- Variable Naming 

### Day-02
- Data Types
- Numbers
- Operations
- Type Converstion
- f-Strings

### Day-03
- Conditional Statement
- Logical Operators
- Code Blocks and Scope

### Day-04
- Randomisation
  - Read the official docs: [Click here](https://docs.python.org/3/library/random.html)
- Module
- Python List

### Day-05
- For Loops
  ```
    for item in list_of_items:
      #Do something to each item
  ```
- Range and Code Blocks
  ```
    for number in range(a, b):
      print(number)
  ```
- Projects
  - FizzBuzz
  - Password Generator

### Day-06
- Indentation
- Functions
  - Build-in Functions
    ``` 
      print()
      len()
      type()
    ```
  - User-defined Functions
    ```
      def my_fun():
        #do something
    
      my_fun()
    ```
- While Loops
  ```
  while something_is_true:
    #Do something repeatedly
  ```
- Projects
  - Escaping the Maze 

### Day-07
- Projects
  - Hangman 
    - Flow Chart

### Day-08
- Functions with Inputs
  ```
  def my_fun(something):
    #Do with this something
    #Then do this
    #Finally do this
  
  my_fun(123)
  ```
- Positional vs. Keyword Arguments
  ``` 
  # Positional Arguments
  def my_fun(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c
  
  my_fun(1, 2, 3)
  ```
  ```
  # Keyword Arguments
  def my_fun(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c
  
  my_fun(a=1, b=2, c=3) 
  ```
- Projects
  - Love Calculator
  - Life in Weeks
  - Caesar Cipher

### Day-09
- Dictionary
  ```
  {"key": "value"}
  ```
- Nesting Lists and Dictionaries
  ```
  travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 4
    },
    "India": {
        "cities_visited": ["Pune", "Mumbai", "Bangalore", "Chennai"],
        "total_visits": 12
    }
  }
  print(travel_log["France"]["total_visits"]) # output: 4
  print(travel_log["India"]["cities_visited"][0]) # output: Pune
  ```
- Projects
  - Grading 
  - Auction

### Day-10
- Docstrings
- Functions with Outputs
  ``` 
  def my_fun():
    result = 5 + 2
    return result
  
  output = my_fun()
  ```
- Projects
  - Calculator
  - Leap Year