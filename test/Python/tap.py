import tkinter as tk
import requests


def get_weather():
    city = city_entry.get()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = str(round(data['main']['temp'] - 273.15, 1)) + '°C'
    weather_label.config(text=f'Weather: {weather}')
    temperature_label.config(text=f'Temperature: {temperature}')


root = tk.Tk()

city_label = tk.Label(root, text='City:')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

button = tk.Button(root, text='Get Weather', command=get_weather)
button.pack()

weather_label = tk.Label(root, text='')
weather_label.pack()

temperature_label = tk.Label(root, text='')
temperature_label.pack()

root.mainloop()
