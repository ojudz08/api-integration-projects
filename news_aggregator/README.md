<p align="right"><a href="https://github.com/ojudz08/api-integration-projects/tree/main">Back To Main Page</a></p>


<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">📰 NewsAPI Fetcher</h1>
</div>


<!-- ABOUT PROJECT -->
### ℹ️ About

A object-oriented Python script designed to fetch, process and save news articles as csv using the [NewsAPI service](https://newsapi.org/). Retrieves historical news using keyword and date and top headlines using country or category.


### 🚀 Features

- **Search Modes:** Toggle between "Everything" (keyword-based) and "Top Headlines" (category/country-based).
- **Professional Logging:** Tracks every execution in news_fetcher_logs.log with high-precision timestamps (AM/PM format).
- **Data Normalization:** Flattens complex JSON responses from NewsAPI into a structured CSV format.


### 📋 Requirements

- **Virtual Environment:** This project was created and tested in an isolated miniconda venv within VsCode. To setup your venv, go to this link [Set Up That Virtual Environment](https://medium.com/@ojelle.rogero/wait-how-did-i-set-up-that-virtual-environment-again-b8ff359d6477)
- **Python 3.13.9**
- **API Key:** Create your API key from [NewsAPI.org](https://newsapi.org/)


### 🛠️ Installation

- **Dependencies:** Run install.py. This will run all the python libraries from requirements.txt.

   ```python
   import subprocess, sys

   def setup():
      print("--- Starting Environment Setup ---\n")
      
      # Install pip requirements
      subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
      
      print("\n--- Setup Complete! Run 'python src/main.py' to start. ---")

   if __name__ == "__main__":
      setup()
   ```

- **Setup API Key in .env:** Make sure you have your free API key. Create a file named .env in the root directory and add your API key.

   ```
   NEWSAPI_API_KEY='your_actual_api_key_here'
   ```


### 📖 Usage
- Run the script from your terminal.
- **Dynamic Input**
   - **Keyword Search (mode 1):** Enter keyword search (e.g., 'gold') and a date range
   - **Top Headlines (moed 2):** Enter country code (e.g., us) and category (e.g., 'health')


### 📂 Output Files
All outputs are saved to the Current Working Directory (CWD) for easy access:
<table>
<tr>
   <th>FileName</th>
   <th>Description</th>
</tr>
<tr>
   <td>data/news_report.csv</td>
   <td>The fetched news articles containing Headlines, Author, Source and News URL.</td>
</tr>
<tr>
   <td>logs/news_fetcher_logs.log</td>
   <td>Detailed runtime logs with timestamps - success or error messages.</td>
</tr>
</table>


### ⚠️ API Constraints & Limitations

As this project is configured for the NewsAPI Developer Plan, the following limitations apply:

- **Pagination Cap:** The script is hard-coded to fetch a maximum of 5 pages. On the Developer Plan, NewsAPI restricts access to the first 100 results (20 articles per page × 5 pages).

- **Search History:** Keyword searches (get_everything) are limited to articles published within the last 30 days.

- **Request Rate:** The free tier allows for 100 requests per day. If you exceed this, the script will log a 429 Too Many Requests error. You will have to wait 12 hours for the next requests once you exceeded the limit.

- **Production Use:** Per NewsAPI terms, the Developer Plan is for development and testing only. A paid plan is required for commercial distribution.


### ⚖️ Disclaimer

This tool is intended for **development purposes only**. 
- **API Compliance:** Users must adhere to the [NewsAPI Terms of Use](https://newsapi.org/terms). 
- **Data Usage:** The developer is not responsible for how the fetched data is used or redistributed.
- **Plan Limits:** This script is optimized for the **Developer Plan**; results are subject to NewsAPI's 100-article limit and 30-day historical window.
- **Suggestions:** For any improvements or suggestions, please contact Ojelle Rogero-Casas - ojelle.rogero@gmail.com.
