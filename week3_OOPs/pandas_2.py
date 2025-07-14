import pandas as pd
import os
import matplotlib.pyplot as plt

vehicles = [{"Brand":"Aston Martin", "Model":"DB9","Year":"2010","Price":"$ 400000"},
            {"Brand":"Koenigsegg", "Model":"Agera RS","Year":"2013","Price":"$ 5000000"},
            {"Brand":"Mclaren", "Model":"P1","Year":"2008","Price":"$ 4000000"}]

df = pd.DataFrame(vehicles)
df.to_csv("vehicles.csv", index=False)

if os.path.exists("vehicles.csv"):
    with open("vehicles.csv","r") as f:
        content = f.read()
        print(content)

df["Price"] = df["Price"].str.replace("$","").str.replace(" ","").astype(int)
plt.bar(df["Brand"], df["Price"])
plt.xlabel("Brand")
plt.ylabel("Price (USD)")
plt.title("Vehicle Prices by Brand")
plt.show()