# SCT_SD_04
🔍 Python script to scrape product data (name, price, rating, reviews, etc.) from Amazon and save it in a structured CSV format. Developed as Task 4 of SkillCraft Technology's Software Development Internship.

# 🛍️ Amazon Product Scraper

This repository contains the solution to **Task 04** of my **Software Development Internship at SkillCraft Technology**.  
The objective is to develop a Python script that scrapes product details from Amazon India and stores them in a structured CSV format.

## 📌 Task Description

> **TASK 04**  
Create a program that extracts product information, such as names, prices, and ratings, from an online e-commerce website and stores the data in a structured format like a CSV file.

## 🚀 Features

- 🔍 Searches Amazon.in for a given product term
- 📄 Extracts:
  - Product Name
  - Price
  - Rating
  - Number of Reviews
  - Product URL
  - Image URL
- 📂 Stores the results in a CSV file
- 📄 Scrapes the first 3 pages of search results

## 🧑‍💻 Technologies Used

- `Python`
- `Selenium`
- `Chrome WebDriver`
- `CSV module`
- `webdriver_manager`

## 📁 Output

The script generates a `.csv` file with product information based on your input. Example filename:
```
laptop_products.csv
```

## ⚙️ How to Run

1. **Install requirements**  
   ```bash
   pip install selenium webdriver-manager
   ```

2. **Run the script**  
   ```bash
   python amazon_scraper.py
   ```

3. **Enter your product name** when prompted.

> ✅ The data will be saved in a CSV file with the format: `<search_term>_products.csv`.

## 🔒 Note

- This script is intended for educational purposes only.
- Use it responsibly and respect the terms of service of the website.

## 📸 Screenshot

<img width="1919" height="1011" alt="image" src="https://github.com/user-attachments/assets/7f312b24-6a64-4db8-a28e-15f2328c2417" />


## 📌 Internship Credit

This project is a part of my **Software Development Internship** at **SkillCraft Technology**.

---

## 👤 Author

**Nadeemsaba**  
🔗 [GitHub Profile](https://github.com/Nadeemsaba)

---

## 📜 License

© 2025 Nadeemsaba  
This project is licensed under the MIT License.
