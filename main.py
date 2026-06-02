from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "data.csv"
df=pd.read_csv(csv_path)
df["total_sales"]=df["price"]*df["quantity"]
grouped=df.groupby("product")["total_sales"].sum().reset_index()
print(grouped)
output_path = BASE_DIR / "sales_summary.xlsx"
grouped.to_excel(output_path, index=False)
print("Excel file created:", output_path)