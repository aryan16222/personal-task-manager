# Task Manager

#### Video Demo: https://youtu.be/dctPxxvKOfA?feature=shared

#### Description:

Task Manager is a simple Python program that allows users to create, view, and delete tasks in a to-do list. It is a command-line application that makes it easy to manage tasks without any distractions.

The main features of the program are:
- Users can **add tasks** by typing in a task name.
- Users can **view all tasks** in the list at any time.
- Users can **remove tasks** once they've been completed.

### Files in the Project:
- `project.py`: This is the main Python file. It contains functions such as `add_task()`, `view_tasks()`, and `remove_task()`.
- `test_project.py`: This file contains tests for the functions in `project.py`, ensuring the program works as expected. We used `pytest` to test the add, remove, and view functionalities.
- `requirements.txt`: Lists any external Python libraries used by the project. (Currently empty, as no external libraries were used).

### Design Choices:
I chose to use a simple **in-memory list** to store tasks, which makes it easy to get started. However, this means tasks are not saved between program runs. In the future, I could implement file storage or a database to persist tasks.

The interface is text-based and interactive, asking users to input commands for adding, viewing, and removing tasks.

Future updates could include:
- **Saving tasks to a file** so that they persist between sessions.
- **Adding priorities** to tasks, where higher-priority tasks are listed first.
- **Allowing users to mark tasks as complete** without removing them.
- ### **3. Saving and Testing Your README.md File:**

Once you've written your README.md, save the file and **preview it** to make sure it looks good. 

- In **VSCode**, click on the **Preview** button to see the rendered version.
- If everything looks good, **save the file**.

---

### **4. Submit the README.md File:**

After creating your README.md file, **commit it** to your GitHub repository along with the rest of your code, then move on to **Step 3**: Submitting the project!

---

### **Markdown Syntax Reference** (just in case):

Here are a few quick examples of Markdown syntax:

- **Headers**: Use `#` for headers. The number of `#` symbols corresponds to the header level.
  - `# Header 1` (largest)
  - `## Header 2`
  - `### Header 3` (smaller)
- **Bold**: `**bold text**` → **bold text**
- **Italic**: `*italic text*` → *italic text*
- **Lists**: 
  - Unordered (bullet points): 
    ```markdown
    - Item 1
    - Item 2
    ```
  - Ordered (numbered):
    ```markdown
    1. First item
    2. Second item
    ```

---

### **Conclusion:**

- Your README.md is your project’s **documentation**.
- It should describe what your project does, how it works, what files are in it, and any important design decisions.
- It should be **clear**, **thorough**, and **well-written**.
- **Take your time** with this file because it’s an important part of your final proje
