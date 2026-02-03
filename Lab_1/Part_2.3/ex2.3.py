import json

def main():
    with open("large-file.json", "r", encoding="utf-8") as f:
        data = json.load(f)


    for record in data:
        record["size"] = 42

    data.reverse()
    with open("output.2.3.json", "w") as f:
        json.dump(data, f, indent=2)

main()