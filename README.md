# Weather Forecast GUI Application 🌦️

A simple, clean, and modern desktop weather application built with Python and CustomTkinter. This application allows users to fetch and display the current weather conditions for any city around the world.

![App Screenshot](./apss.png)
*(Note: You should replace `screenshot.png` with an actual screenshot of your application.)*

## Description

This project is a straightforward graphical user interface (GUI) application that provides real-time weather data. Users can enter a city name, and the application will communicate with the OpenWeatherMap API to retrieve and display the current temperature and a short weather description.

The interface is designed to be intuitive and visually appealing, leveraging the modern widgets provided by the CustomTkinter library.

---

## ✨ Features

* **User-Friendly Interface:** Clean and simple UI that is easy to navigate.
* **Real-Time Data:** Fetches live weather data from the OpenWeatherMap API.
* **Global Coverage:** Get weather information for any city available in the OpenWeatherMap database.
* **Essential Information:** Displays the most important weather details: temperature in Celsius and a weather description (e.g., "clear sky," "light rain").
* **Error Handling:** Provides user-friendly feedback if the city is not found or if the input field is empty.
* **Secure API Key Management:** Uses a `.env` file to keep the API key secure and out of the source code.

---

## 🔧 Technologies Used

* **Python 3:** The core programming language.
* **CustomTkinter:** A modern Python UI library based on Tkinter, used for creating the graphical interface.
