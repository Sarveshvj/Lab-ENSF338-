import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def load_data():
    data = pd.read_json('internetdata.json')
    return data

def create_dataframe(data):
    col = ["country", "incomeperperson"]
    df = pd.DataFrame(data, columns=col)
    return df

def split_data(data):
    data = data.dropna(subset=["incomeperperson"])  
    group1 = data[data["incomeperperson"] < 10000]
    group2 = data[data["incomeperperson"] >= 10000]

    return group1, group2

def plot_histograms(group1, group2):
    plt.figure()
    plt.hist(group1["internetuserate"], bins=20)
    plt.title("Internet Use (Income < 10000)")
    plt.xlabel("Internet Use Rate")
    plt.ylabel("Number of Countries")
    plt.savefig("hist1.png")
    plt.close()

    plt.figure()
    plt.hist(group2["internetuserate"], bins=20)
    plt.title("Internet Use (Income >= 10000)")
    plt.xlabel("Internet Use Rate")
    plt.ylabel("Number of Countries")
    plt.savefig("hist2.png")
    plt.close()


def main():
    data = load_data()
    group1, group2 = split_data(data)
    plot_histograms(group1, group2)

main()
