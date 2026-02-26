import json, time

def LOADER(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"DataLoader file me error aa gya:- {e}")


