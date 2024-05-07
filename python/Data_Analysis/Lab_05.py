import pandas as pd

# Merge&Join

#Join or merge is a process that enables us to convert both two data sets by using common areas in different two data sets.

customers = {
    'Customer_Id': [1, 2, 3],
    'First_Name': ['okan', 'bukan', 'sukan'],
    'User_Name': ['resilient', 'rezilyent', 'rezilient']
}

orders = {
    'Order_Id': [1001, 1002, 1003, 1004, 1005],
    'Customer_Id': [1, 2, 3, 1, 4],
    'Order_Date': ['2023-07-01', '2023-06-06', '2023-07-12', '2023-07-23', '2023-07-07']
}

df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

print(df_customers)
print(df_orders)

#It brings datas as instrection set matched in both data set.

print(pd.merge(
    left=df_customers,
    right=df_orders,
    on='Customer_Id',
    how='inner'
))

#
print(pd.merge(
    left=df_customers,
    right=df_orders,
    on='Customer_Id',
    how='right'
))
