from pyrogram import Client

API_KEY = int(input("2fd358c2-cedc-4f46-aee9-a0b0bfdf0ca8: "))
API_HASH = input("eda35365e336d67a8354ce83813b9a73: ")
with Client(":memory:", api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
