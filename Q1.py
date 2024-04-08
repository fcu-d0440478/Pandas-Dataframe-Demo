import pandas as pd

detail = pd.read_excel(
    f"(DATA) 專業測驗.xlsx",
    sheet_name="detail",
    # index_col=0,
)

sales_info = pd.read_excel(
    f"(DATA) 專業測驗.xlsx",
    sheet_name="sales_info",
    # index_col=0,
)

detail = detail[detail.group != "Test"]
detail = detail[detail.date <= "2021-03-05"]
sales_info = sales_info[sales_info.date <= "2021-03-05"]
sales_info["bonus"] = 0
sales_info["pnl"] = 0
sales_info["volume"] = 0
sales_info["commission"] = 0
sales_info["deposit"] = 0

for index, row in detail.iterrows():
    login = row["login"]
    date = row["date"]
    deposit = row["deposit"]

    sales_info[sales_info["login"] == login]

    sales_index = (sales_info["login"] == login) & (sales_info["date"] == date)

    if deposit >= 3000:
        sales_info.loc[sales_index, "bonus"] += 1

    sales_info.loc[sales_index, "pnl"] += row["pnl"]
    sales_info.loc[sales_index, "volume"] += row["volume"]
    sales_info.loc[sales_index, "commission"] += row["commission"]
    sales_info.loc[sales_index, "deposit"] += row["deposit"]

sales_info = sales_info.sort_values(by="pnl", ascending=False)
sales_info["pnl_rank"] = sales_info["pnl"].rank(ascending=False)

print(sales_info[["date", "sales", "pnl", "volume", "commission", "deposit", "bonus"]])
