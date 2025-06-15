# Singly Linked List in Python

This project demonstrates a basic implementation of a **singly linked list** using Python and object-oriented programming principles.

## 📌 Features

- Node creation and linking
- Add elements to the start or end
- Insert after a specific element
- Delete by:
  - Position (1-based index)
  - First or last element
  - Specific value
- Search for a value
- Get the total number of nodes
- Iterable support for easy traversal

## 📂 Files

- `linked_list.py`: Contains the full implementation and sample usage code.

## 🛠️ Methods Included

| Method | Description |
|--------|-------------|
| `append(data)` | Add a node at the end |
| `prepend(data)` | Add a node at the start |
| `insert_after(target, data)` | Insert a node after a node with given value |
| `remove_nth(pos)` | Delete node at position (1-based index) |
| `delete_first()` | Remove the first node |
| `delete_last()` | Remove the last node |
| `remove_val(value)` | Delete node by value |
| `show()` | Print the list |
| `size()` | Return number of nodes |
| `find(value)` | Search for a value and return its index |
| `__iter__()` / `__next__()` | Support iteration using for-loops |

## ▶️ Sample Output

```python
5 -> 10 -> 20 -> 25 -> 30 -> 40
5 -> 10 -> 25 -> 30 -> 40
5 -> 10 -> 30 -> 40
10 -> 30
Found 30 at: 2
Total nodes: 2
Next item: 10
Next item: 30
