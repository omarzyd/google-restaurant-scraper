# 🍽️ Google Restaurant Scraper

A **Python Selenium script** that automates scraping restaurant details from **Google Search**, extracting:

- ✅ **Restaurant Name**
- ✅ **Address**
- ✅ **Rating**
- ✅ **Phone Number**
- ✅ **Cuisine Type**

This tool is useful for **food bloggers, market analysts, and business owners** looking to gather structured restaurant data.

---

## 📌 Features

### 🔹 Automated Google Search Scraping
- Uses **Selenium WebDriver** to interact with Google search results.
- Clicks each restaurant dynamically and extracts relevant details.

### 🔹 JavaScript-Based Data Extraction
- Leverages **JavaScript execution** instead of traditional XPath.
- Handles dynamically loaded content more effectively.

### 🔹 Duplicate-Free & Structured Output
- Stores extracted restaurant data in a **CSV file**.
- Ensures unique entries using a **set-based approach**.

---

## 🛠️ Installation

### **1️⃣ Install Dependencies**
Make sure you have Python **3.x** installed, then install the required packages:

```bash
pip install selenium webdriver-manager
