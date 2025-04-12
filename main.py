
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
except Exception as e:
    print(f"Gemini configuration error: {e}")
    exit()

def load_dataset(path):
    try:
        df = pd.read_csv(path)
        print("CSV loaded successfully!")
        return df
    except Exception as e:
        print(f"Failed to load CSV: {e}")
        return None

def auto_eda(df):
    print("\n--- Basic Info ---")
    print(df.info())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    print("\n--- Descriptive Stats ---")
    print(df.describe())
    print("\n--- Correlation Matrix ---")
    print(df.corr(numeric_only=True))

def visualize(df):
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        print("\nGenerating pairplot for numeric features...")
        sns.pairplot(df[numeric_cols].dropna())
        plt.show()
    else:
        print("No numeric columns to visualize.")

def ask_gemini(df, question):
    try:
        sample = df.head(10).to_string(index=False)
        prompt = f"You are a data analyst. Based on the dataset sample below, answer this question:

{sample}

Question: {question}"
        response = model.generate_content([{"text": prompt}])
        return response.text.strip()
    except Exception as e:
        return f"Error with Gemini: {e}"

def main():
    path = input("Enter path to your CSV file: ")
    df = load_dataset(path)
    if df is None:
        return

    auto_eda(df)
    visualize(df)

    while True:
        question = input("\nAsk a question about this data (type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        answer = ask_gemini(df, question)
        print(f"\nGemini Insight:\n{answer}")

if __name__ == "__main__":
    main()
