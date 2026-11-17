# 📊 Sales Data Analyzer

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Dependencies](https://img.shields.io/badge/dependencies-none-lightgrey)

A lightweight Python project that computes basic sales statistics (totals and averages) from in-memory data structures. Built to practice core Python fundamentals: functions, loops, lists, dictionaries and formatted output.

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [▶️ Usage](#️-usage)
- [🖥️ Sample Output](#️-sample-output)
- [🎯 What I Practiced](#-what-i-practiced)
- [🔮 Possible Improvements](#-possible-improvements)
- [👤 Author](#-author)

---

## ✨ Features

- 📅 **Weekly analysis**: total and average sales over a 7-day period (Monday–Sunday)
- 🛍️ **Per-product analysis**: aggregate sales across product categories (Laptops, Smartphones, TVs, Smartwatches)
- 🧮 **Reusable functions**: `total_sales()` and `average_sales()` operate on any numeric list
- 🧾 **Readable output**: results printed with f-string formatting
- 📦 **Zero dependencies**: runs on the Python standard library only

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python 3.6+ | Core language |
| 📚 Standard library | Built-ins only (`sum`, `len`, `print`) |

---

## 📁 Project Structure

```text
.
├── sales_data.py       # Weekly sales: total & average
├── sales_data_v2.py    # Product sales (dict): total
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- 🐍 [Python 3.6+](https://www.python.org/downloads/)
- 🔧 [Git](https://git-scm.com/)

### Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

---

## ▶️ Usage

Run the weekly sales analysis:

```bash
python sales_data.py
```

Run the product sales analysis:

```bash
python sales_data_v2.py
```

To use your own data, edit the values at the top of each script:

```python
# sales_data.py: [Mon, Tue, Wed, Thu, Fri, Sat, Sun]
sales_data = [230, 200, 310, 290, 400, 150, 180]

# sales_data_v2.py
sales = {
    "Laptops": 4800,
    "Smartphones": 6900,
    "TVs": 9000,
    "Smartwatches": 8700,
}
```

---

## 🖥️ Sample Output

**`sales_data.py`**

```text
Sales data for week: [230, 200, 310, 290, 400, 150, 180].
Total sales is: 1760.
Average sales is: 251.42857142857142.
```

**`sales_data_v2.py`**

```text
Total products cost in sub-branch is: 29400.
```

---

## 🎯 What I Practiced

- ✅ Defining and calling functions with parameters and return values
- ✅ Iterating over lists with `for` loops
- ✅ Working with dictionaries (`.values()`) and built-ins (`sum`, `len`)
- ✅ String formatting with f-strings
- ✅ Structuring a small project and documenting it for GitHub


## 🔮 Possible Improvements

- [ ] 📈 Add min/max day and best/worst product
- [ ] 📂 Load data from CSV/JSON instead of hardcoded values
- [ ] 🧪 Add unit tests with `pytest`
- [ ] 🖥️ Add a CLI with `argparse`
- [ ] 📊 Visualize results with `matplotlib`


⭐ If you found this project useful, consider giving it a star!
