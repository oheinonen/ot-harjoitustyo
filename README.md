# Budgeting application 
This repository contains budgeting application made for Univerity of Helsinki course [Ohjelmistotekniikka](https://courses.helsinki.fi/fi/tkt20002)

Purpose of this application is that the users can keep track on their expenses. The application can have multiple users, each having their own expenses.


## Documentation 
- [Architecture](https://github.com/oheinonen/ot-harjoitustyo/blob/master/documentation/architecture.md)
- [Working time records](https://github.com/oheinonen/ot-harjoitustyo/blob/master/documentation/working_time_records.md)
- [Requirements specification](https://github.com/oheinonen/ot-harjoitustyo/blob/master/documentation/requirement_specification.md)
- [Changelog](https://github.com/oheinonen/ot-harjoitustyo/blob/master/documentation/changelog.md)
- [Instructions for use](https://github.com/oheinonen/ot-harjoitustyo/blob/master/documentation/instructions.md)
- [Testing](https://github.com/oheinonen/ot-harjoitustyo/blob/master/documentation/testing.md)


## Releases
- [Week 5 pre-release](https://github.com/oheinonen/ot-harjoitustyo/releases/tag/week5)
- [Week 6 pre-release](https://github.com/oheinonen/ot-harjoitustyo/releases/tag/week6)
- [Final release](https://github.com/oheinonen/ot-harjoitustyo/releases/tag/final_release)

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

Test pylint
```bash
poetry run invoke lint
```
