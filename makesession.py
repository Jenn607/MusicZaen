from pyrogram import Client

API_KEY = int(input("11cba413-db8b-4256-83d1-957c65fae8e1: "))
API_HASH = input("eda35365e336d67a8354ce83813b9a73: ")
with Client(":memory:", api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
