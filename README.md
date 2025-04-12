# TrendSage_Al_Data_Analyst_Project

**TrendSage** is an intelligent assistant for data analysts. It loads your CSV files, runs exploratory data analysis (EDA), and allows you to ask questions in natural language using Gemini AI.

## Features

- Loads CSV files
- Auto-detects missing values, outliers, correlations
- Generates summary statistics and visualizations
- Gemini AI answers your data-related questions

## Setup

1. Clone the repo or unzip the folder
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file and insert your Gemini API key like this:
    ```
    GEMINI_API_KEY=your_gemini_api_key_here
    ```
4. Run the app:
    ```bash
    python main.py
    ```

## Example Questions

- "Which features are most correlated?"
- "Summarize key insights from the dataset."
- "Any outliers I should know about?"

## License

This project is 100% original and open-source. Free for academic and personal use.
