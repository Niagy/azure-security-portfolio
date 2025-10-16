# Exercise: Try Bash 🐚

## 🧭 Overview

This exercise introduced the basics of using **Bash** in **Azure Cloud Shell**, a browser-accessible terminal that allows you to manage Azure resources without local setup.  

The goal was to practice navigating directories, managing files, using command history, and leveraging autocompletion — all within the context of Azure Cloud Shell.

---

## 🧰 Skills Learned

- Basic **Bash navigation commands** (`ls`, `pwd`, `cd`)
- Viewing **hidden files and directories** (`ls -a`)
- Understanding **special files** like `.bashrc`, `.bash_history`, and `.profile`
- Using **command recall** (↑ ↓ arrows) and **autocompletion** (Tab)
- Viewing command manuals with **`man`**
- Reading files with **`cat`**
- Navigating directories and relative paths (`.`, `..`, `~`)

---

## 🧑‍💻 Commands Practiced

```bash
# List files and subdirectories
ls

# Show current working directory
pwd

# Show all (including hidden) files
ls -a

# Read the contents of a file
cat .azure/commands/2020-01-29.21-56-35.login.103.log

# Display manual/help page for a command
man cat

# Change directory
cd ~
cd .azure/commands/
cd ..

```

## Screenshots
[Screenshot](./screenshots/Screenshot%202025-10-16%20121010.png)

[Screenshot](./screenshots/Screenshot%202025-10-16%20124721.png)

[Screenshot](./screenshots/Screenshot%202025-10-16%20124902.png)

[Screenshot](./screenshots/Screenshot%202025-10-16%20124952.png)

[Screenshot](./screenshots/Screenshot%202025-10-16%20125108.png)

[Screenshot](./screenshots/Screenshot%202025-10-16%20125139.png)

## 🧩 Key Takeaways
Azure Cloud Shell provides a convenient way to manage Azure resources without local installation.

The Bash shell is powerful for automation, file management, and cloud operations.

Understanding hidden configuration files helps in customizing your Linux environment.

Autocompletion and command history drastically improve terminal efficiency.

## 🌐 Related Links
[Azure Cloud Shell Documentation](https://learn.microsoft.com/azure/cloud-shell/overview)

[Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)

[Azure Learn Module – Try Bash](https://learn.microsoft.com/en-us/training/modules/bash-introduction/4-exercise-try-bash)

## 🏁 Reflection
This exercise reinforced my understanding of Bash fundamentals and how Azure Cloud Shell simplifies Linux administration in the cloud.
I now feel more confident navigating and manipulating files directly in Azure’s CLI environment, which will be essential for tasks in VM management, automation scripts, and Azure resource configuration.

Author: John Niagwan
Date Completed: 16/10/2025