import json
import timeit

def main():
    with open("large-file.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    def change_size():
        for record in data:
            record["size"] = 42

    timer = timeit.Timer(change_size)
    results = timer.repeat(repeat=10, number=1)

    average = sum(results) / 10
    print("Average time over 10 runs:", average)

    data.reverse()
    with open("output.2.3.json", "w") as f:
        json.dump(data, f, indent=2)

main()