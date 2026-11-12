# 🔐 Strong Password Assistant

A Python-based interactive password assistant designed to help users create stronger and more complex passwords.

Instead of simply checking an existing password, this program guides users through password requirements, analyzes password complexity, detects predictable patterns, and helps them create a stronger password.

## ✨ Features

- **Interactive CLI:** A simple and user-friendly command-line interface.
- **Password Length Validation:** Requires passwords to meet a minimum length.
- **Character Diversity:** Encourages using uppercase letters, lowercase letters, numbers, and special characters.
- **Pattern Detection:** Identifies common sequential patterns such as `123`, `1234`, and `abcd`.
- **Repetition Detection:** Checks for excessive character repetition.
- **Custom Scoring Algorithm:** Evaluates password complexity using a weighted scoring system.
- **Password Feedback:** Provides suggestions when password requirements are not met.
- **Cross-Session Interaction:** Allows users to restart the password creation process.

## ⚙️ Password Evaluation

The program assigns different scores to password characters:

| Character Type | Score |
|---|---:|
| Lowercase Letters | +1 |
| Uppercase Letters | +1.5 |
| Numbers | +1.5 |
| Special Characters | +2 |

It also checks for:
- Passwords containing only numbers.
- Passwords containing only one letter case.
- Common sequential patterns.
- Excessive character repetition.
- Minimum password length.

## 🚀 Getting Started

### Requirements
- Python 3.x

### Installation

Clone the repository:

```bash
git clone https://github.com/endjackcho/Strong-Password-Assistant.git
```

Navigate to the project directory:

```bash
cd Strong-Password-Assistant
```

Run the application:

```bash
python main.py
```

## 💻 Example

```text
>>>> Welcome !
- I wanna help you to create a Strong Password !
Are you ready ?

>> yes

Enter your password : abc123

>> Enter Stronger Password use more number, UpperCase words and Special Characters !

Enter your password : MyStr0ng!Pass2026

>> Great !
- Your strong Password : MyStr0ng!Pass2026
```

## 🛠️ Technologies

- Python
- OS Module
- String Manipulation
- Conditional Logic
- Loops
- Custom Scoring Algorithms

## 🎯 Project Goals

This project was created to improve Python programming skills through practical implementation of:

- Input validation
- String analysis
- Algorithm design
- Logical conditions
- Interactive CLI applications

---

**Developed by [endjackcho](https://github.com/endjackcho)**
