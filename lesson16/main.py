import pandas as pd
import json


def read_files():
    df_csv = pd.read_csv('internet_store_sales.csv')
    print("CSV данные:")
    print(df_csv.head())

    df_xlsx = pd.read_excel('internet_store_sales.xlsx')
    print("\nXLSX данные:")
    print(df_xlsx.head())

    with open('example.txt', 'r') as file:
        json_data = json.loads('[' + file.read() + ']')
    print("\nJSON данные:")
    print(json_data)

    return df_csv, df_xlsx, json_data


def write_files(df_csv, df_xlsx, json_data):
    df_csv.to_csv('new_sales.csv', index=False)

    df_xlsx.to_excel('new_sales.xlsx', index=False)

    with open('new_sales.json', 'w') as file:
        json.dump(json_data, file, indent=4)


def append_data(df):
    new_row = {
        'order_id': 999999,
        'customer_id': 1234,
        'order_date': '2024-12-31',
        'shipping_date': '2025-01-05',
        'order_status': 'Pending',
        'total_amount': 500.00
    }

    return df.append(new_row, ignore_index=True)


def delete_data(df):
    df = df[df['total_amount'] < 1000]
    return df


def main():
    df_csv, df_xlsx, json_data = read_files()
    df_csv = append_data(df_csv)
    df_csv = delete_data(df_csv)
    write_files(df_csv, df_xlsx, json_data)

    print("\nБазова статистика:")
    print(df_csv.describe())

    print("\nГрупування за статусом заказу:")
    print(df_csv.groupby('order_status')['total_amount'].sum())


if __name__ == "__main__":
    main()
