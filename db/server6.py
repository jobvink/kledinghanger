import json
import requests

# 1231425363543
server = '84.105.147.0'
port = 8002
auth = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjAxZTczMTQ2NWQwNGNjNGIyOTczNDkwZDBmOTc2NmE1NWI1YmQxMDdjYTFkMDU4MDczN2Q2OWIwMmU4ZTIyNjc1YWE1NTkzYTZmNjViYzY1In0.eyJhdWQiOiIyIiwianRpIjoiMDFlNzMxNDY1ZDA0Y2M0YjI5NzM0OTBkMGY5NzY2YTU1YjViZDEwN2NhMWQwNTgwNzM3ZDY5YjAyZThlMjI2NzVhYTU1OTNhNmY2NWJjNjUiLCJpYXQiOjE0OTI4NTk3MDAsIm5iZiI6MTQ5Mjg1OTcwMCwiZXhwIjoxNTI0Mzk1NzAwLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.ynJNQHoC5Y6DYDmUfovo05gx4lTXJd61zrnuu1NHs4dykRH2jkLCoolLwHz-ubmFIINn5YZCOjaqqxQxFfWpBMNU1hSqfgomLPeW059SYb4_T6Hj-XtZgFfaOjKoYEwa0hWJI8kUaRtxK0TxPAhMTY02ENJd9D9m56_9WVfcp-av5FXe8RTYbEL2lni9-JAqc6ps6URfpslS5R53DKujDY0SPIu2rmdUvYLB-c_lLNdTjV-cMunp4eiNWiMJtxmj8dQf0qriSfqgExoZpIkJnWkS_XUp6AEDfj8-0go5Fpb5ySfquIyXIDqhg45OMLJX1PJQmMtsJoPLZWiNNZXTMGRSlrfzPIxxXHlayxAlzRn7epPoN-n22KxIFVwES8KJKnxlDhdVm6KdHQ10tg4RBTpaUkJZ6mUnGTFiQedQ9FwCceOkpsXfkK9eG8pk_ZXm31PPUVFcwbNMzM3-Qvugf8saSl05nROj-877bCf_8QInKTVVqcoqIKJOC0JgxukJBq_nUOhhsO2xa6Az68sUXOPcUwbv4zd7B_afAlIHD72xVa3mHRCtqz3BDYkkeCz9FwvT-IxBeehm2MdaOvesDzic5x-5oAqQUiKU3426EJ36y-S0kxRkyy01dUurnC2NOg8tk3u17kWjNU8M9JtmH7wdMLN9Zl0XKaIerI0RspE'}

data = {
    'rack': 1,
    'barcode': ['1234567891237', '5234567891238']
}

# response = requests.get('http://%s:%i/api/products/1234567891234' % (server, port), headers=auth)
response = requests.post('http://%s:%i/api/rack/attach' % (server, port), data=json.dumps(data), headers=auth)

print response.text
