# Hotel-Management 🍽️
Simple Python Menu & UPI Payment System

A beginner‑friendly command‑line script that lets customers:

1. **Browse a multi‑category menu** (starters, Indian food, fast‑food, desserts, drinks, …).
2. **Select items and quantities** interactively.
3. **See a running bill** with totals.
4. **Pay by scanning an auto‑generated UPI QR code** (works with any Indian UPI app).

## 🗃️ Folder Structure

your‑project/

├─ main.py # ← The main python Menu script

└─ upi_qr.png # ← QR code created automatically at checkout

└─ README.md # ← This file

└─ .gitignore

└─ LICENSE

# 🤖 Features

* **Category‑wise menu display** with serial numbers and prices.
* **Flexible ordering** – choose as many categories/items as you like.
* **Real‑time cost calculation**.
* **UPI deep‑link & QR generation** so users pay the exact amount.
* **Fully customizable** menu items, prices, and UPI details (just edit the lists in the code).

# 🛠️ Prerequisites

* Python 3.1+  
* Two Python packages (install once):

```bash
pip install qrcode[pil]  webbrowser  # 'webbrowser' is from the standard library; repeat safe
# qrcode uses Pillow under the hood, so the extra tag [pil] pulls it in automatically.
```

# 🚀 Running the Script
python main.py

***Then follow the on‑screen prompts:**

*For each category the program asks “Order starters? (Yes(y) / No(n))”.*

If you say y:

Enter serial numbers separated by spaces (e.g., 1 4 6).

Enter matching quantities in the same order (e.g., 2 1 3).

*Repeat for other categories.*

When you finish ordering, a Total Bill is shown and a QR pops up.

Scan the QR with any UPI app → confirm payment → done!

# 🖼️ Demo (text)
*STARTERS
1. Garlic Bread -> ₹50
2. Veg Spring Rolls -> ₹40

```
Order starters? (Yes(y) / No(n): y

Serial nos: 1 2

Quantities (same order): 1 2

Garlic Bread x1 => ₹50

Veg Spring Rolls x2 => ₹80
```

=====================

Total Bill: ₹130

=====================

📲 Scan the displayed QR in any UPI app to pay.

*The file upi_qr.png is also saved in the same directory so you can reuse or share it.*

# 📚 What You’ll Learn
1. Creating and looping over nested lists/tuples.
2. Accepting and validating user input.
3. Generating dynamic strings with f‑strings.
4. Simple arithmetic for totals.
5. Using third‑party libraries (qrcode) to create images.
6. Opening images with the default OS viewer.

**Have fun coding and customizing your very own Python café! ☕🍰**
