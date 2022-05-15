# Requirement specification
## Purpose of the application
Puprose of this application is that the users can keep track on their expenses and income. The application can have multiple users, each having their own expenses and income.  

## Users
There are only one type of users, normal users.

## User interface
UI has five different views: LoginView, CreateUserView, MainView, ExpenseView and CategoryView. MainView shows everything in one place; all expenses and all categories of logged in user. ExpenseView shows information of one Expense and is tool for user o update its information. CategoryView shows a list of all expenses of a logged in user in a chosen category

## Functionalities
### Before signing in
- [x] The user can create and account 
  - [x] The username must be unique and between 4 and 99 characters
- [x] The user can log in 
  - [x] Log in is done by giving username and correct password to the login form 
  - [x] If the username doesn't exist or the password isn't correct, the application shows an error
### After signing in
- [x] The user can see own expenses 
  - [x] The expenses can be listed by category 
- [x] The user can add new expense 
  - [x] Expense includes name, category, date and amount 
- [x] The user can add new cost category 
- [x] The user can update expense 
- [x] The user can remove expense 
- [x] The user can remove a cost category 
- [x] The user can log out 

## Development ideas
- Show some visualization of expenses
- Add recurring costs
- Add incomes
