import customtkinter as ctk
import requests
import tkinter.messagebox as msgbox
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define API Key and Base URL
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


# Function to get weather data
def get_weather():
    city = entry_city.get()  # Get city name from the entry box

    if not city:
        msgbox.showerror("Error", "Please enter a valid city name.")
        return

    # Build the URL and send the request
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=en"
    response = requests.get(url)

    # Check the response status
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        # Display the result on the label
        label_result.configure(text=f"Temperature: {temperature}°C\nDescription: {description}")
    else:
        label_result.configure(text="City not found or an error occurred.")


# Create the main application window
app = ctk.CTk(fg_color = "#37353E")
app.title("Weather Forecast")
app.geometry("600x600")
app.resizable(False, False)

# Create the main frame
frame = ctk.CTkFrame(master=app, fg_color = "#37353E")
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Main title label
label_tag = ctk.CTkLabel(frame, text="Weather Forecast", font=("Poppins", 40, "bold"), anchor="w", text_color="#D3DAD9")
label_tag.pack(fill="x", padx=20, pady=30)

# City entry label
label_city = ctk.CTkLabel(frame, text="Enter your city", font=("Poppins", 20), anchor="w", text_color="#D3DAD9")
label_city.pack(fill="x", padx=20, pady=5)

# City entry box
entry_city = ctk.CTkEntry(frame, width=480, fg_color = "#44444E", border_color="#D3DAD9", corner_radius=20, font=("Poppins", 13), height=35)
entry_city.pack(padx=20, pady=10, anchor="w")

# Get Weather button
button = ctk.CTkButton(frame, text="Get Weather", fg_color="#D3DAD9", hover_color="#D3DAD9", command=get_weather, text_color="#050505", font=("Poppins", 13, "bold"), corner_radius=20)
button.pack(padx=20, pady=30, anchor="w")

# Result label
label_result = ctk.CTkLabel(frame, text="", font=("Poppins", 20, "bold"), anchor="w")
label_result.pack(padx=20, pady=10, anchor="w")

app.mainloop()
