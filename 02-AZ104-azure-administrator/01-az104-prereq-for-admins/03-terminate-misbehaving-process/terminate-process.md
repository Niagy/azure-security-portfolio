# Exercise: Terminate a Misbehaving Process ⚙️  

---

## 🧭 Overview  

This exercise covered how to identify and terminate problematic processes in a **Linux** environment using **Bash** commands.  
You learned how to locate a process with `ps` and `grep`, and safely terminate it using `kill`.  

This is an essential skill for system administrators who need to keep systems stable and performant when rogue processes consume excessive CPU or memory.  

---

## 🧰 Skills Learned  

- Identifying active processes using `ps`  
- Filtering process output with `grep`  
- Understanding process IDs (PIDs)  
- Sending signals to processes using `kill`  
- Using `vi` to create and edit files in Linux  
- Managing background jobs in Bash (`&`)  

---

## 🧑‍💻 Commands Practiced  

```bash
# Return to home directory
cd ~

# Create and edit a Python script with vi
vi bad.py

# Example content inside bad.py
i = 0
while i == 0:
    pass

# Save and exit vi
:wq

# Run the program in the background
python3 bad.py &

# View running processes containing 'python'
ps -ef | grep python

# List all available kill signals
kill -l

# Terminate a process using SIGKILL (replace PROCESS_ID with actual ID)
kill -9 PROCESS_ID

# Verify process termination
ps -ef | grep python
```

---

## Screenshot
![Screenshot](./screenshots/Screenshot%202025-10-16%20152550.png)

---

## 🧩 Key Takeaways

* **`ps`** provides detailed process information, including process IDs and CPU usage.
* **`grep`** helps filter process lists to find specific programs quickly.
* **`kill`** can send different signals; `SIGKILL (9)` forcefully terminates a process.
* Background jobs (`&`) continue running after returning to the shell prompt.
* Understanding how to handle **misbehaving or zombie processes** is critical for maintaining system health.

---

## 🌐 Related Links

* [Linux ps Command Reference](https://man7.org/linux/man-pages/man1/ps.1.html)
* [Linux kill Command Reference](https://man7.org/linux/man-pages/man1/kill.1.html)
* [Azure Cloud Shell Overview](https://learn.microsoft.com/azure/cloud-shell/overview)
* [Microsoft Learn: Terminate a Misbehaving Process](https://learn.microsoft.com/training/)

---

## 🏁 Reflection

This exercise taught me how to effectively manage and terminate problematic processes in a Linux system.
I now understand how to identify CPU-intensive tasks, issue kill signals, and confirm successful termination.
This skill is vital for real-world system administration and cloud operations, ensuring stable and responsive environments.

---

**Author:** John Niagwan
**Date Completed:** 16/10/2025