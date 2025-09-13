# Flipkart Automation Script

This Python script automates a complete user journey on Flipkart using Selenium. It logs in, searches for a smartphone, selects it, adds it to the cart, proceeds to checkout, selects a payment method, and navigates to the OTP page.

## ✅ Features
- Open Flipkart and log in using valid credentials.
- Search for "smartphone".
- Select the first product and add it to the cart.
- Proceed to checkout.
- Choose payment method.
- Navigate to OTP page and validate the presence.

## 📦 Requirements
- Python 3.8 or higher
- Google Chrome installed
- Internet connection

## 📂 Files
- `automation.py`: Automation script.
- `config.json`: Configuration file with credentials.
- `requirements.txt`: Required Python packages.
- `README.md`: Instructions and details.

## ⚙ Installation Steps

1. Clone the repository:
   ```bash
Create a virtual environment (optional):

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Add your Flipkart credentials in config.json:

{
  "username": "your_email_or_phone",
  "password": "your_password"
}


Run the script:

python automation.py
   git clone https://github.com/yourusername/flipkart-automation.git
   cd flipkart-automation
