import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io
import geocoder
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x600")
        self.root.configure(bg="#2C3E50")

     
        self.api_key = "YOUR_API_KEY" 
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "http://api.openweathermap.org/data/2.5/forecast"

      
        self.setup_ui()

    def setup_ui(self):
       
        search_frame = tk.Frame(self.root, bg="#2C3E50")
        search_frame.pack(pady=20)

        self.city_entry = tk.Entry(search_frame, font=("Arial", 14), width=20)
        self.city_entry.pack(side=tk.LEFT, padx=10)
        self.city_entry.bind('<Return>', lambda event: self.get_weather())

        search_btn = tk.Button(search_frame, text="🔍", command=self.get_weather, font=("Arial", 12))
        search_btn.pack(side=tk.LEFT)

        gps_btn = tk.Button(search_frame, text="📍", command=self.get_gps_location, font=("Arial", 12))
        gps_btn.pack(side=tk.LEFT, padx=5)

      
        self.weather_frame = tk.Frame(self.root, bg="#2C3E50")
        self.weather_frame.pack(pady=20)

        self.city_label = tk.Label(self.weather_frame, text="Enter City", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="white")
        self.city_label.pack()

        self.icon_label = tk.Label(self.weather_frame, bg="#2C3E50")
        self.icon_label.pack()

        self.temp_label = tk.Label(self.weather_frame, text="--°C", font=("Helvetica", 48), bg="#2C3E50", fg="white")
        self.temp_label.pack()

        self.desc_label = tk.Label(self.weather_frame, text="---", font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1")
        self.desc_label.pack(pady=5)

       
        details_frame = tk.Frame(self.root, bg="#2C3E50")
        details_frame.pack(fill="x", padx=40)

        self.humidity_lbl = tk.Label(details_frame, text="Humidity: --%", bg="#2C3E50", fg="#BDC3C7")
        self.humidity_lbl.grid(row=0, column=0, sticky="w", padx=20)
        
        self.wind_lbl = tk.Label(details_frame, text="Wind: -- m/s", bg="#2C3E50", fg="#BDC3C7")
        self.wind_lbl.grid(row=0, column=1, sticky="e", padx=20)

    def get_gps_location(self):
        try:
          
            g = geocoder.ip('me')
            if g.city:
                self.city_entry.delete(0, tk.END)
                self.city_entry.insert(0, g.city)
                self.get_weather()
            else:
                messagebox.showerror("Error", "Could not detect location.")
        except Exception as e:
            messagebox.showerror("Error", f"GPS Error: {e}")

    def get_weather(self):
        city = self.city_entry.get()
        if not city: return

  
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()

            if data["cod"] == 200:
                self.update_ui(data)
            else:
                messagebox.showerror("Error", data.get("message", "City not found"))

        except Exception as e:
            messagebox.showerror("Error", f"Connection failed: {e}")

    def update_ui(self, data):
       
        city_name = f"{data['name']}, {data['sys']['country']}"
        temp = int(data['main']['temp'])
        description = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        self.city_label.config(text=city_name)
        self.temp_label.config(text=f"{temp}°C")
        self.desc_label.config(text=description)
        self.humidity_lbl.config(text=f"Humidity: {humidity}%")
        self.wind_lbl.config(text=f"Wind: {wind} m/s")

       
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        self.load_icon_from_url(icon_url)

    def load_icon_from_url(self, url):
        try:
            response = requests.get(url)
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            photo = ImageTk.PhotoImage(image)

           
            self.icon_label.config(image=photo)
            self.icon_label.image = photo 
        except Exception as e:
            print(f"Icon error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
