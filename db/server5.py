import requests, json

# 1231425363543
server = '84.105.147.0'
port = 8002
auth = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjczODE4MjEzNzI2MTczYTExZDAyMDU3N2Q3ZTcwZTUyMmRlYzdjMzc2Yjk5NWY2ODUzZjYyMzYxYjcwOWE5MGExMDJmMDBiODhhOGNmODFlIn0.eyJhdWQiOiIxIiwianRpIjoiNzM4MTgyMTM3MjYxNzNhMTFkMDIwNTc3ZDdlNzBlNTIyZGVjN2MzNzZiOTk1ZjY4NTNmNjIzNjFiNzA5YTkwYTEwMmYwMGI4OGE4Y2Y4MWUiLCJpYXQiOjE0OTI1MTE1MDUsIm5iZiI6MTQ5MjUxMTUwNSwiZXhwIjoxNTI0MDQ3NTA1LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.FxBtbQp5OfFHtxL-FeBt36eFrqQ-GbiqJoVLYrwYju6jc384gPIaBiZPaQr-kJiZVaQkoHe50zeiI4TIKf9fjeAekUSf4crfCleQVNA6NWAFuGdmpXXphCAjs1NgYuiEW2IdVkoetQhA2frnZAzMuVITQqe4S_bR4Tst2R92HAANXyeY3FdzpE6hwTyRI1oEeBK9TwE52hJ7jfnwu9YJQ1ODNn9-DikaVkfHx7gwwdIDWf44EVAyzWRyFaMqdfRA3drks1XE2eDr8JOl3ym-K57UQ1b_gwIPjFA0SdbFxOha1EaYNcwjoVZd4pX8bbbP2KQX_xxbW9M__gpRkT7BHggOlvzYclP7a43bcp_cmaBHzUkTSlEFeULqJssRwx_Z8elkasyMHDtBs4hQIgracgxL-be27x2oXOP1lS9Qbgto4dQM3udBU80n_zxWhM0LoOhTLv-tLTz4iOZYdORI6yfz3hViWlnhnytmaM1wS8kqoTosqf8o2uE5ppE5juclfUpkj7ujH4eOSqX2tISmGhQ7fUnZLJtBigdlKMMhVgq5f8z0GjERzwngEDA3mrfNHc3QzlNmeCwNfzOa6VZcBs9MyKKRN95YlNNNz8g6HNcWhZS1NCqN8Q8e58xUpdHiDcwgZTKe10lhks0_Nq8Yb-LmyT7TtbgBlWDuGW0S0-w'}

data = {
    'rack': 1,
    'barcode': 2234567891237
}
response = requests.get('http://%s:%i/api/products/123  ' % (server, port), headers=auth)
try:
    if response.json()['status'] == 'faild':
        print 'faild'
except KeyError:
    pass

print response.text

