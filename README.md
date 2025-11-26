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

3.  **Crucially**, you must replace the placeholder API key in the `Weather_App.py` file with your own:

    ```python
    # Locate this line in BASIC_WETHER_APP.py and update it
    self.api_key = "YOUR_API_KEY"
    ```

-----

## ⚙️ How to Run

Execute the main Python script from your terminal:

```bash
python Weather_App.py
```

-----

## 🛠️ Project Structure

```
WeatherApp/
├── Weather_App.py  # Main application logic and UI
├── requirements.txt     # List of required Python packages
└── README.md            # Project documentation (this file)
```

-----

## 🤝 Contributing

Contributions are welcome\! Feel free to open an issue or submit a pull request if you find a bug or have a suggestion for improvement.


-----

## 👨‍💻 Author

  * **ANMOL INGLE** - [(https://github.com/anmolingle)]

<!-- end list -->
