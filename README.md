
# 🔁 Doubly Linked List in Python — With Randomized Operations

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange)

> Fully interactive terminal-based **Doubly Linked List** in Python — supports insertions, deletions, searching, and random position operations using a custom `node` and `linkedList` class structure.

---

## 💡 Features

- 🔂 Insert at beginning, end, or at a **random position**
- ❌ Delete from start, end, or randomly
- 🔍 Search for elements
- 🔄 Fully bidirectional — supports `.next` and `.prev`
- 🎯 All inputs validated
- 😈 Errors gracefully handled

---

## 📦 Installation & Usage

### 📁 Clone this Repository

```bash
git clone https://github.com/nishuR31/doubleLinkedlist.git
cd doubleLinkedList
````

### ▶️ Run the Program

```bash
python file.py
```

---

## 🧠 Menu Options

```
1: Insert at beginning
2: Insert at end
3: Insert at random position
4: Delete from start
5: Delete from last
6: Delete randomly
7: Display the list
8: Search for an element
0: Exit
```

---

## 📂 Project Structure

```
📁 doubleLinkedList/
├── 📄 doubleLinkedlist.py   # Main Python code
└── 📄 README.md               # This file
```

---

## 🧬 Behind the Scenes

* **Node Class**: Stores `data`, `next`, and `prev`
* **LinkedList Class**:

  * `insertFirst`, `insertLast`, `insertRandom`
  * `delFirst`, `delLast`, `delRandom`
  * `search`, `display`
* Random positions determined using `random.randint`
* User-friendly messages and retry prompts on all failures

---

## 🖼️ Demo Preview

> Terminal output after inserting and deleting nodes:

```
None <= 10 => <= 20 => <= 42 => None
10 removed from first
42 inserted at index 1
```

---

## ❗ Gotchas Handled

* Empty list operations
* Insertion/deletion when list has only one node
* Invalid input recovery
* Consistent pointer linkage (`prev`, `next`) maintained

---

## 🧠 Learnings

If you're learning **data structures**, this project is perfect for:

* Understanding pointers and memory flow
* Simulating memory address linkage using Python objects
* Practicing object-oriented thinking

---

## 📜 License

This project is under the [MIT License](LINCENSE)

---

## ✨ Author

Made with 💻 by [Nishu](https://github.com/nishuR31)

```
