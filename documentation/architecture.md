``` mermaid 

classDiagram
    class Expense{
        id
        name
        value
        category
        date
        owner
    }
    class User{
        username
        password
    }
    Expense "*" --|> "1" ExpenseRepository
    Expense "*" --|> "1" User
    User "*" --|> "1" UserRepository
    ExpenseService  --|> "*" Expense
    ExpenseService  --|> "*" User
    ExpenseService  --|>  ExpenseRepository
    ExpenseService  --|>  UserRepository
    Ui "1" --|> "1" ExpenseService

```
