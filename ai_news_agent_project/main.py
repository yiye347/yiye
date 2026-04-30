import subprocess
import pandas as pd
from ai_analyzer import analyze_text

print("Start crawling news...")

subprocess.run([
    "scrapy",
    "runspider",
    "spiders/news_spider.py",
    "-o",
    "news.csv"
])

print("Crawling finished")

df = pd.read_csv("news.csv")

analysis = []

for i, row in df.iterrows():
    title = row["title"]
    print("AI analyzing:", title)
    result = analyze_text(title)
    analysis.append(result)

df["ai_analysis"] = analysis

df.to_excel("data/result.xlsx", index=False)

print("Excel report generated: data/result.xlsx")
