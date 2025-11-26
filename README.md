# ☀️ Simple Weather App (Tkinter/OpenWeatherMap)

A simple, desktop-based weather application built using Python's **Tkinter** for the graphical user interface and the **OpenWeatherMap API** for fetching real-time weather data.


---

## ✨ Features

* **Real-time Weather:** Fetches current temperature, humidity, and wind speed.
* **City Search:** Look up weather by city name.
* **Auto-Detect Location:** Uses your IP address to detect your current city with the "📍" button.
* **Dynamic Icon:** Displays a relevant weather icon fetched from OpenWeatherMap.

---

## 🚀 Installation & Setup

### 1. Prerequisites

* Python 3.x installed on your system.

### 2. Clone the Repository

```bash
git clone https://github.com/anmolingle/OIBSIP_Python_Task6.git
cd OIBSIP_Python_Task6
````

### 3\. Install Dependencies

Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

### 4\. OpenWeatherMap API Key

This application requires an **API Key** from OpenWeatherMap.

1.  Sign up for a free account on [OpenWeatherMap](https://openweathermap.org/).

2.  Navigate to the API Keys tab to find or generate your key.

3.  **Crucially**, you must replace the placeholder API key in the `BASIC_WETHER_APP.py` file with your own:

    ```python
    # Locate this line in BASIC_WETHER_APP.py and update it
    self.api_key = "YOUR_PERSONAL_API_KEY_HERE"
    ```

-----

## ⚙️ How to Run

Execute the main Python script from your terminal:

```bash
python BASIC_WETHER_APP.py
```

-----

## 🛠️ Project Structure

```
WeatherApp/
├── BASIC_WETHER_APP.py  # Main application logic and UI
├── requirements.txt     # List of required Python packages
└── README.md            # Project documentation (this file)
```

-----

## 🤝 Contributing

Contributions are welcome\! Feel free to open an issue or submit a pull request if you find a bug or have a suggestion for improvement.

-----

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file (if you choose to add one) for details.

-----

## 👨‍💻 Author

  * **ANMOL INGLE** - [Link to your GitHub Profile]

<!-- end list -->

````

---

## ✅ Professional Steps Summary

1.  **Create a Repository** on GitHub (e.g., `Simple-Python-Weather-App`).
2.  **Create `requirements.txt`** and populate it with the dependencies.
3.  **Create `README.md`** and copy the suggested content above.
4.  **Create `.gitignore`** (Highly Recommended). A common Python one looks like this (you can find templates online):

    ```gitignore
    # .gitignore
    __pycache__/
    *.pyc
    # Virtual environment
    venv/
    .env
    ```

5.  **Commit and Push** the four files (`BASIC_WETHER_APP.py`, `requirements.txt`, `README.md`, and `.gitignore`) to your new GitHub repository.

Would you like me to draft a simple `LICENSE.md` (e.g., MIT License) for your project as well?
````
