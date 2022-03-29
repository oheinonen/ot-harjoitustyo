# Budgeting application 
This repository contains budgeting application made for Univerity of Helsinki course (Ohjelmistotekniikka)[https://courses.helsinki.fi/fi/tkt20002]
Purpose of this application is that the users can keep track on their expenses and income. The application can have multiple users, each having their own expenses and income.


## Documentation 
- [Working time records](https://github.com/oheinonen/ot-harjoitustyo/blob/master/documentation/working_time_records.md)
- [Requirements specification](https://github.com/oheinonen/ot-harjoitustyo/blob/master/documentation/requirement_specification.md)
- [Changelog](https://github.com/oheinonen/ot-harjoitustyo/blob/master/documentation/changelog.md)

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

## Terminal commands
Run the application
```bash
poetry run invoke start
```
Run tests
```bash
poetry run invoke test
```

Create test coverage report
```bash
poetry run invoke coverage-report
```

