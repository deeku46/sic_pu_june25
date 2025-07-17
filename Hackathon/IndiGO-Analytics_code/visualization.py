'''
This module handles all visualizations for the Indigo Analytics Dashboard.
Functions include:
- Delay analysis charts
- Forecasted passenger trends
- Market share trends over time
- Top air sector visualizations
- Predicted demand plotting
All graphs are built using matplotlib and seaborn (where needed) for clarity and insight.
'''

import matplotlib.pyplot as plt

def plot_delay_analysis(airlines_df=None, routes_df=None, reasons_df=None):
    '''
    Plots 3 delay-related visualizations:
    1. Bar chart of top delayed airlines
    2. Bar chart of top delayed routes
    3. Pie chart of delay reasons
    '''
    if airlines_df is not None:
        plt.figure(figsize=(12, 5))
        plt.bar(airlines_df["Airline"], airlines_df["Delay_Minutes"], color="skyblue")
        plt.title("Top Delayed Airlines")
        plt.xlabel("Airline")
        plt.ylabel("Total Delay Minutes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    if routes_df is not None:
        plt.figure(figsize=(12, 5))
        route_labels = routes_df["Origin"] + " → " + routes_df["Destination"]
        plt.bar(route_labels, routes_df["Delay_Minutes"], color="salmon")
        plt.title("Top Delayed Routes")
        plt.xlabel("Route")
        plt.ylabel("Total Delay Minutes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    if reasons_df is not None:
        plt.figure(figsize=(8, 8))
        plt.pie(
            reasons_df["Delay_Count"],
            labels=reasons_df["Delay_Reason"],
            autopct="%1.1f%%",
            startangle=140,
            colors=plt.cm.Pastel1.colors
        )
        plt.title("Common Delay Reasons")
        plt.tight_layout()
        plt.show()


def plot_forecast(route_data, future_years, future_preds, origin, destination):

# Plots actual passenger data vs forecasted predictions for a selected route.

    plt.figure(figsize=(10, 5))
    plt.plot(route_data["Year"], route_data["Passenger_count"], marker='o', label='Actual')
    plt.plot(future_years, future_preds, marker='x', linestyle='--', label='Forecast')
    plt.title(f"Passenger Forecast for {origin} → {destination}")
    plt.xlabel("Year")
    plt.ylabel("Passenger Count")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_market_share(market_share_df): #  Uses seaborn to show airline-wise market share % trend over years.
    import seaborn as sns
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=market_share_df, x="Year", y="Market Share (%)", hue="Airline", marker="o")
    plt.title("Airline Market Share Over Years")
    plt.ylabel("Market Share (%)")
    plt.xlabel("Year")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

def plot_top_sectors(top3_df): #  Plots the top 3 busiest air sectors (routes) based on passenger count.
    routes = top3_df["Origin"] + " → " + top3_df["Destination"]
    counts = top3_df["Passenger_count"]
    plt.figure(figsize=(8, 5))
    plt.bar(routes, counts, color="goldenrod")
    plt.title("Top 3 Busiest Air Sectors")
    plt.xlabel("Route")
    plt.ylabel("Total Passengers")
    plt.tight_layout()
    plt.show()

def plot_demand_prediction(result_df, origin, destination): # Plots bar graph of predicted demand per year for a given route.
    if result_df.empty:
        print("No data to plot.")
        return
    plt.figure(figsize=(6, 4))
    plt.bar(result_df["Year"].astype(str), result_df["Passenger_count"], color="mediumseagreen")
    plt.title(f"Predicted Demand: {origin} → {destination}")
    plt.xlabel("Year")
    plt.ylabel("Passenger Count")
    plt.tight_layout()
    plt.show()
