# Instructions of use
## Setup

1. Install dependencies with command
```bash
poetry install
```


2. Execute initialization with command

```bash
poetry run invoke build
```

3. Start application with command

```bash
poetry run invoke start
```

## Login
The application opens into the login view. Here user can login by writing existing username and password to corresponding fields and clicking "Login" button

![Screenshot from 2022-05-03 18-30-50](https://user-images.githubusercontent.com/65664408/166485715-b6183516-bc42-4eb5-bf83-2865e922e873.png)



## Creating new account
User can move to create user view from login view by clicking 'Create user button'. In this view user can create new account by writing username and password to corresponding fields and clicking "Create user" button. Username must be between 4 and 99 characters.
![Screenshot from 2022-05-03 18-30-26](https://user-images.githubusercontent.com/65664408/166485769-4b225c55-b423-49d9-bdcc-26cb04698b98.png)


## Add new category
After succesfull login, user sees the main view. In the main view user can add new category by writing it's name to the field and clicking "Add category button"

![Screenshot from 2022-05-03 18-31-27](https://user-images.githubusercontent.com/65664408/166485675-bfe32d66-56a2-4fba-ade7-71d16eba2f9b.png)

## Adding new expense 
In the main view, user can also add new expense by writing its name and value to corresponding fields and choosing category. After that user must click "Add new expense" button to save the new expense.

![Screenshot from 2022-05-03 18-31-51](https://user-images.githubusercontent.com/65664408/166485654-2084c800-73a5-41dc-9898-7b5ed4a32194.png)

## Remove or update existing expense
User can choose expense in the expense list. Clicking "Delete" deletes selected expense. User can also click "update" button.

![Screenshot from 2022-05-15 21-18-17](https://user-images.githubusercontent.com/65664408/168487860-a5e3558e-72ab-42cf-8ca0-d1d08ce268c3.png)

That shows the expense view, where user can change some of the expense information and save it by clicking "Update!" button.

![Screenshot from 2022-05-03 18-32-22](https://user-images.githubusercontent.com/65664408/166485516-108cf062-a305-457e-818e-3db4f4e99688.png)

## Show expenses of on category
User can see all expenses belonging to one category by choosing category from category list and clickin "View"

![Screenshot from 2022-05-15 21-23-15](https://user-images.githubusercontent.com/65664408/168488088-b5137a86-a24b-47b3-9ab0-526a2848123b.png)

That shows the category view, where user can review expenses belonging to that category and update / remove them
![Screenshot from 2022-05-15 21-23-26](https://user-images.githubusercontent.com/65664408/168488093-ec076af2-63e2-495d-ba34-a3407909e866.png)
