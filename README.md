# wit-vcs-python

🔧 A basic version control system (VCS) implemented in Python, inspired by Git and built for learning purposes.

## 📌 Project Overview

`wit` is a simplified version control system developed as part of a Python course. It allows you to track changes in files, create commits, revert to previous versions, and view history — all through a clean command-line interface (CLI) powered by `Click` and object-oriented programming.

🔗 GitHub Repository: [https://github.com/Naomi-Bnayahu/wit-vcs-python](https://github.com/Naomi-Bnayahu/wit-vcs-python)

---

## 🚀 Supported Commands

### `wit init`
Initializes a new `.wit` folder in the current directory. This folder stores all version data. If it already exists, an error is shown.

### `wit add <file>`
Stages a specific file for the next commit. Only added files will be tracked in the next commit.

### `wit commit -m "message"`
Creates a new commit with all staged files. A message is required to describe the changes made.

### `wit log`
Displays the history of commits, including their IDs, timestamps, and messages.

### `wit status`
Checks whether there are changes that haven’t yet been committed (e.g., files that were modified but not committed).

### `wit checkout <commit_id>`
Reverts the working directory to the state of a previous commit by its ID.

---

## ⚙️ Technologies Used

- **Python 3.10+**
- **Click** for command-line interface (CLI)
- **Object-Oriented Programming** (OOP)
- Built-in modules like `os`, `shutil`, `pathlib` for filesystem management

---

## ▶️ Getting Started

1. **Clone the repository:**
```bash
git clone https://github.com/Naomi-Bnayahu/wit-vcs-python.git
cd wit-vcs-python
````

2. **Install required packages:**

```bash
pip install click
```

3. **Run CLI commands:**

```bash
python main.py init
python main.py add myfile.txt
python main.py commit -m "Initial commit"
python main.py log
python main.py status
python main.py checkout <commit_id>
```

---

## 💡 Possible Extensions

* 📁 **Directory tracking**: Enhance the system to support tracking entire folders, including file moves, deletions, and nested structures.

---

## 👩‍💻 Developed By

* **Naomi Bnayahu**
* Course: Introduction to Python

