# cyberNews Aggregator

CyberNews Aggregator is a Flask web application that fetches technology and cybersecurity-related news using the News API. It dynamically generates relevant images for each news update from Unsplash, providing a user-friendly interface for news consumption.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Support](#support)
- [Contributing](#contributing)

## Introduction

The project aims to provide a convenient platform for users to stay updated on technology and cybersecurity news. It leverages the News API to fetch news articles and dynamically generates relevant images from Unsplash for a visually appealing user experience.

## Features

- **News Fetching:** Retrieve latest news articles related to technology and cybersecurity.
- **Dynamic Image Generation:** Enhance news articles with dynamically generated relevant images.
- **Filtering Options:** Customize news feed by language, category, and search term.
- **Automatic Updates:** News updates are fetched automatically every 3 minutes.
- **User-Friendly Interface:** Intuitive web interface for easy news consumption.

## Requirements

Make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Flask
- Flask-CORS
- Requests
- Unsplashed (python-unsplash)

## Installation

1. **Setting up the Virtual Environment:**

      python -m venv venv
   
**Activate the virtual environment:**

**On Windows:**

venv\Scripts\activate

**On Unix or MacOS:**
 source venv/bin/activate

**Install Required Packages:**

    pip install Flask Flask-CORS requests python-unsplash

   **Configuration:**
        Obtain API keys from News API and Unsplash API.
        Replace 'YOUR_NEWS_API_KEY' and 'YOUR_UNSPLASH_ACCESS_KEY' in server.py with your actual API keys.

**Usage**

  **Run the Flask application:**

     python server.py

  **Access the Application:**
        Open your web browser and navigate to http://localhost:3000.
        Use language, category, and search filters to customize your news feed.

  **Automatic Updates:**
        News updates are fetched every 3 minutes.

**Troubleshooting**

    **API Key Errors:** Double-check API keys and ensure correct configuration.
    **Library Installation:** Ensure all required libraries are installed. Use pip install -r requirements.txt.

**Support**

For additional assistance or inquiries, please contact **benardmulwa508@gmail.com**.

**Contributing**

Contributions are welcome! Fork the repository and submit a pull request.

