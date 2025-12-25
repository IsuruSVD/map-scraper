## Google Maps Business Scraper

A free and open-source Python tool for scraping publicly available business information from Google Maps based on a business category and geographic area.
The project includes a simple web interface (Flask) to submit inputs and automatically generate CSV files.


## ✨ Features

- Scrape Google Maps without paid APIs

- Extract:

  1. Business name
  2. Phone number (if publicly available)
  3. Address

- Simple web interface (Flask)

- Automatic ChromeDriver handling (Selenium Manager)

- CSV output (Excel compatible)

- Configurable category and area

- Suitable for any country or business type



## 🛠 Tech Stack


- Python 3.10+

- Flask – Web interface

- Selenium (>= 4.10) – Browser automation

- Pandas – CSV generation

- Google Chrome (115+)


## 📁 Project Structure
```text
google-maps-business-scraper/
├── app.py
├── scraper.py
├── templates/
│   └── index.html
├── output/
├── requirements.txt
├── .gitignore
└── README.md
```


## ✅ Prerequisites

Before starting, make sure you have:

- Windows / Linux / macOS
- Internet connection
- Google Chrome installed



## 🚀 STEP-BY-STEP INSTALLATION GUIDE

### 1️⃣ Install Python

- Download Python

👉 https://www.python.org/downloads/

- Install Python 3.10 or newer

✔ During installation, CHECK:

```bash
☑ Add Python to PATH
```

- Verify installation

Open Command Prompt / Terminal:
```bash
python --version
```

Expected output:
```bash
Python 3.x.x
```

### 2️⃣ Clone the Repository

git clone https://github.com/your-username/google-maps-business-scraper.git

```bash
cd google-maps-business-scraper
```

Or download ZIP and extract it.

### 3️⃣ Create a Python Virtual Environment (Recommended)

Virtual environments keep dependencies isolated.

```bash
python -m venv venv
```

### 4️⃣ Activate the Virtual Environment

On Windows
```bash
venv\Scripts\activate
```

On macOS / Linux
```bash
source venv/bin/activate
```

You should see:
```bash
(venv)
```

### 5️⃣ Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 6️⃣ Install Required Libraries

```bash
pip install flask selenium pandas
```

Or using requirements.txt:

```bash
pip install -r requirements.txt
```

Required versions

- Selenium >= 4.10

- Pandas (latest)

- Flask (latest)

### 7️⃣ Google Chrome & Selenium Manager

- Install Google Chrome (version 115 or newer)
- No manual ChromeDriver download needed
- Selenium Manager automatically handles drivers

✔ Nothing else required

▶️ RUNNING THE APPLICATION

### 8️⃣ Start the Flask App

```bash
python app.py
```

You should see:

```bash
Running on http://127.0.0.1:5000
```

### 9️⃣ Open the Web Interface

Open your browser and go to:

`http://127.0.0.1:5000`

## 🔍 How to Use

- Enter a business category

`Example: computer shop, pharmacy, restaurant`

- Enter an area / location
  
`Example: Colombo, Kandy, Galle`

- Click Start Scraping

- Google Chrome will open and collect data

- CSV file will be saved in the output/ folder

## 📄 Output Example

output/

`computer_shop_Colombo.csv`

CSV columns:

- Shop Name
- Phone
- Address

## ⚠️ Notes & Limitations

- Only publicly visible data is collected
- Some businesses may not show phone numbers
- Scraping speed is intentionally slow to avoid blocking
- Do not run multiple instances simultaneously

## 📜 Disclaimer

This project is intended for educational, research, and directory-building purposes only.
Users are responsible for ensuring compliance with Google Maps Terms of Service and local regulations when using or distributing scraped data.



