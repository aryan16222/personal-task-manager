# test_project.py

from project import add_task, complete_task, save_tasks, load_tasks

def test_add_task():
    tasks = []
    add_task(tasks, "Buy milk")
    assert tasks == ["Buy milk"]

def test_complete_task():
    tasks = ["Buy milk", "Do homework"]
    complete_task(tasks, 0)
    assert tasks == ["Do homework"]

def test_save_and_load_tasks(tmp_path):
    filename = tmp_path / "tasks.txt"
    tasks = ["Buy milk", "Do homework"]
    save_tasks(tasks, filename)
    loaded = load_tasks(filename)
    assert loaded == ["Buy milk", "Do homework"]
