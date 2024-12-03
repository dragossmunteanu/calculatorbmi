
# 📊 **BMI Calculator Flask App**

A web application built with Flask to calculate Body Mass Index (BMI) and provide personalized health recommendations based on lifestyle choices.

---

## 🚀 **Getting Started**

These instructions will help you get the project up and running locally.

### 🛠️ **Prerequisites**

Before you begin, make sure you have the following installed on your system:

- Python (3.7 or higher)
- pip (Python package installer)

### 🔧 **Installation Steps**

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/yourusername/bmi-flask-app.git
    cd bmi-flask-app
    ```

2. **Install dependencies**:

    Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
    ```

    Then install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. **Setup environment variables** for email configuration:

    Create a `.env` file in the root of the project and add your email credentials:

    ```bash
    EMAIL_ADDRESS=your-email@gmail.com
    EMAIL_PASSWORD=your-email-password
    ```

    > **Note:** It is essential to use environment variables to keep your email credentials secure! Don't hard-code sensitive information in your code.

---

## ⚙️ **How It Works**

### 1. **BMI Calculation**

- The app asks for the user’s **weight** (kg) and **height** (cm) to calculate the BMI.
- Based on the BMI value, the app categorizes the user into different BMI categories (e.g., Underweight, Normal weight, Overweight, Obesity).
- Health tips and recommendations are displayed based on the BMI category.

### 2. **Lifestyle Form**

After calculating the BMI, the app asks users for additional details such as:

- Water intake 💧
- Sleep duration 🛏️
- Exercise habits 🏃‍♂️

These answers are used to provide **personalized health recommendations**.

### 3. **Email Notifications**

- Once the lifestyle form is completed, the app sends an **email** to the user with health recommendations and tips based on their BMI and lifestyle.
  
> **Note:** The email is sent via **Gmail** using SMTP. Make sure your Gmail account allows less secure apps or configure it for secure access.

---

## 💻 **Usage**

1. **Run the Flask application**:

    In your terminal, navigate to the project folder and run the following command:

    ```bash
    python app.py
    ```

2. **Open the app in your browser**:

    Go to `http://127.0.0.1:5000` to access the BMI calculator.

---

## 🛠️ **Project Structure**

- **app.py** – The main Flask application file.
- **templates/** – Contains HTML files for the front-end views.
- **static/** – Holds static files like CSS, JavaScript, and images.
- **.env** – Stores environment variables for email credentials.

---

## 📩 **Sending Emails**

The application uses SMTP (Simple Mail Transfer Protocol) to send emails with the **recommendations** to the user.

**Important:** Use your Gmail account's credentials and allow access for less secure apps or configure secure authentication.

Example email sending setup in `app.py`:

```python
import smtplib
from email.mime.text import MIMEText

def send_email(recipient, message):
    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(os.getenv('EMAIL_ADDRESS'), os.getenv('EMAIL_PASSWORD'))
            msg = MIMEText(message)
            msg['Subject'] = 'Your Personalized Health Recommendations'
            msg['From'] = os.getenv('EMAIL_ADDRESS')
            msg['To'] = recipient
            server.sendmail(os.getenv('EMAIL_ADDRESS'), recipient, msg.as_string())
            print("Email sent successfully! 📧")
    except Exception as e:
        print(f"Error sending email: {e}")
```

---

## 🛡️ **Security Tips**

- Always store sensitive information like your **email password** in environment variables, not directly in the code.
- Consider using libraries like `dotenv` to manage environment variables.

---

## 🎨 **Styling and Responsiveness**

- The app is **mobile-friendly**, using responsive design techniques for a good user experience on all devices.
- The front-end design uses basic HTML and CSS for simplicity and clarity.

---

## 📍 **Possible Improvements**

- **Form Validation:** Add more validation checks for user input (e.g., ensure positive numbers for weight, height, and other inputs).
- **Error Handling:** Improve error messages and handling (e.g., if the email fails to send).
- **Styling:** Enhance the visual design of the app with advanced CSS or front-end frameworks like Bootstrap.

---

## 🏅 **Contributing**

Feel free to fork this repository and submit pull requests for any improvements or bug fixes! 😊

---


