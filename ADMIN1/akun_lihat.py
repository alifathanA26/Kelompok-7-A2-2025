import json
import os
from prettytable import PrettyTable

def lihat_akun():
    if os.path.exists("akun.json"):
        with open("akun.json", "r") as f:
            data_akun = json.load(f)
    else:
        data_akun = {}

    if not data_akun:
        print("❌ Belum ada akun yang terdaftar.")
        return

    table = PrettyTable()
    table.field_names = ["Username", "Role"]
    for username, info in data_akun.items():
        table.add_row([username, info['role']])
    print("\n📋 Daftar Akun Terdaftar:")
    print(table)
