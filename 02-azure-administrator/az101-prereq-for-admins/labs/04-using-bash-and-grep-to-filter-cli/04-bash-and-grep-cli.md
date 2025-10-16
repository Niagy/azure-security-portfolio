# Exercise: Use Bash and grep to Filter CLI Output 🔍  

---

## 🧭 Overview  

This exercise demonstrated how to use **Bash** in combination with the **Azure CLI** to filter and refine command output efficiently.  

You learned how to apply the **pipe (`|`)** operator to pass command results between tools, and how to use **`grep`** to extract relevant information from large data sets.  

This practice is essential for system administrators and cloud engineers who regularly work with command-line data in Azure environments.  

---

## 🧰 Skills Learned  

- Using **`grep`** to filter text-based command output  
- Applying **regular expressions** for pattern matching  
- Combining **Azure CLI** with Bash utilities for automation  
- Leveraging **pipes (`|`)** to chain commands  
- Extracting specific Azure VM SKU details from CLI output  

---

## 🧑‍💻 Commands Practiced  

```bash
# List all available VM SKUs in the West US region
az vm list-skus --location westus --output table

# Filter VM SKUs to show only those containing "DS"
az vm list-skus --location westus --output table | grep DS

# Use a regular expression to show only DS V2 series SKUs
az vm list-skus --location westus --output table | grep DS.*_v2
```

---

## Screenshots
![Screenshots](./screenshots/Screenshot%202025-10-16%20161222.png)
![Screenshots](./screenshots/Screenshot%202025-10-16%20161540.png)

---

## 🧩 Key Takeaways

* **Piping (`|`)** connects commands, letting one tool’s output become another’s input.
* **`grep`** is a powerful text filter — ideal for narrowing down CLI results.
* **Regular expressions (regex)** enhance pattern matching capabilities beyond simple keywords.
* Combining **Bash** and **Azure CLI** simplifies data exploration and troubleshooting workflows.
* Efficient command-line filtering saves time and reduces manual searching through large outputs.

---

## 🌐 Related Links

* [Azure CLI Documentation](https://learn.microsoft.com/cli/azure/)
* [grep Command Reference](https://man7.org/linux/man-pages/man1/grep.1.html)
* [Azure VM Sizes](https://learn.microsoft.com/azure/virtual-machines/sizes)
* [Microsoft Learn: Use Bash and grep to Filter CLI Output](https://learn.microsoft.com/training/)

---

## 🏁 Reflection

This exercise showed how powerful simple command combinations can be.
By integrating **Bash** utilities with **Azure CLI**, I can quickly extract meaningful insights from large datasets, improving efficiency in managing cloud resources.

The use of `grep` with regular expressions is especially valuable for automating repetitive tasks and parsing outputs in scripts.

---

**Author:** John Niagwan
**Date Completed:** 16/10/2025