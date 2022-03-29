# Requirement specification
## Purpose of the application
Puprose of this application is that the users can keep track on their expenses and income. The application can have multiple users, each having their own expenses and income.  

## Users
There are only one type of users, normal users.

## Functionalities
### Before signing in
- The user can create and account
  - The username must be unique and between 4 and 99 characters
- The user can log in
  - Log in is done by giving username and correct password to the login form
  - If the username doesn't exist or the password isn't correct, the application shows an error
### After signing in
- The user can see own expenses/income
  - Later the expenses can be listed eg. via category 
    - and maybe with a graph?
- The user can add new expense/income
  - Expense includes at least name, category, date and amount
  - Later recurring expenses could be added
- The user can add new cost category
- The user can remove expense/income
- The user can remove a cost category
- The user can log out
