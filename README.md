# CLI ToDo List

## Introduction
A neat little todo list for your cli, made with python! You can add, list, remove and clear your tasks!

I mainly made this to learn about git and github!

## Installation

To get the program on your computer, you:

1. Clone the repo

```bash
git clone https://github.com/Rikemannen/todo-list
```

2. Move to the directory:

```bash
cd todo-list
```

3. Install requirements

```bash
pip install -r requirements.txt
```

4. Run it!

```bash
python list.py -h
```

## How to use

Really simple to use, to add a task:

```bash
python list.py -a "Empty Dishwasher"
```

But nobody likes doing that, so we delete it:

```bash
python list.py -r 1
```

or:

```bash
python list.py -r "empty"
```

The script matches both numbers, as in which order, and text.

Don't know what tasks you have?

```bash
python list.py -l
```

too much stuff...

```bash
python list.py -c
```

## Contribute?

Sure, contributions are welcome!

1. Fork the repo
2. Create a branch
3. Make your (awesome) additions/changes
4. Commit to your fork
5. Push to your branch
6. Open a pull request!

Thanks for supporting! :D

## License

Do whatever you wish, I do not care.
(The repo has the unlicense-license)