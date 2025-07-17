'''
Performs the core analytics for your dashboard using the cleaned DataFrames (city_df, carrier_df, delay_df) 
— stuff like:

Top sectors
Demand prediction
Airline market share
Delay pattern detection
Forecasting future demand using ML

'''



import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class AnalysisEngine:
    def __init__(self,city_df,carrier_df,delay_df=None):# Initialize the analytics engine with preloaded DataFrames
        self.city_df = city_df
        self.carrier_df = carrier_df
        self.delay_df = delay_df

    def top_sectors(self): #  Finds the top 3 busiest air routes based on total passenger traffic.
        self.city_df["Passenger_count"] = self.city_df["PaxToCity2"] + self.city_df["PaxFromCity2"]
        grouped = self.city_df.groupby(["Origin","Destination"])
        sector_traffic  = grouped["Passenger_count"].sum().reset_index()
        sorted_sector_traffic = sector_traffic.sort_values(by="Passenger_count", ascending = False)
        top_3 = sorted_sector_traffic.head(3)

        return top_3
    
    def predict_demand(self, Origin, Destination, Year=None): #Returns past passenger data for a specific route (optionally filtered by year).
        self.city_df["Passenger_count"] = self.city_df["PaxToCity2"] + self.city_df["PaxFromCity2"]
        grouped = self.city_df.groupby(["Origin", "Destination", "Year"])
        grouped_sum = grouped["Passenger_count"].sum().reset_index()
        filtered_data = (grouped_sum["Origin"] == Origin) & (grouped_sum["Destination"] == Destination)
        route_data = grouped_sum[filtered_data]
        
        if Year:
            route_data = route_data[route_data["Year"] == Year]

        return route_data
    
    def airline_market_share(self): # Calculates yearly market share % for each airline to spot growth trends.
        self.carrier_df.columns = self.carrier_df.columns.str.strip()
        grouped = self.carrier_df.groupby(["Airline","Year"])["Passengers"].sum().reset_index()
        airline_data = grouped
        total_per_year = airline_data.groupby("Year")["Passengers"].sum().reset_index()
        total_per_year.rename(columns={"Passengers": "Total Passengers"}, inplace=True)
        merged = pd.merge(airline_data, total_per_year, on="Year")
        merged["Market Share (%)"] = (merged["Passengers"]/merged["Total Passengers"])*100

        result = merged.sort_values(by=["Year","Market Share (%)"], ascending=[True,False])

        return result
    
    def flight_delay_patterns(self, top_n = 5): # Shows top delayed airlines, routes, and most common delay reasons.
            df = self.delay_df.copy()
            df.columns = df.columns.str.strip()

            # Top Delayed Airlines
            airline_delays = (
                df.groupby("Airline")["Delay_Minutes"]
                .sum()
                .reset_index()
                .sort_values(by="Delay_Minutes", ascending=False)
                .head(top_n)
            )

            # Top Delayed Routes
            route_delays = (
                df.groupby(["Origin", "Destination"])["Delay_Minutes"]
                .sum()
                .reset_index()
                .sort_values(by="Delay_Minutes", ascending=False)
                .head(top_n)
            )

            # Top Delay Reasons (excluding 'None')
            reason_df = (
                df[df["Delay_Reason"] != "None"]
                .groupby("Delay_Reason")
                .size()
                .reset_index(name="Delay_Count")
                .sort_values(by="Delay_Count", ascending=False)
            )

            return airline_delays, route_delays, reason_df
    
    
    def forecast_demand(self, origin, destination, future_years=[2025, 2026]):#Predicts future passenger demand on a route using linear regression.
        self.city_df["Passenger_count"] = self.city_df["PaxToCity2"] + self.city_df["PaxFromCity2"]
        grouped = self.city_df.groupby(["Origin", "Destination", "Year"])["Passenger_count"].sum().reset_index()
        route_data = grouped[(grouped["Origin"] == origin) & (grouped["Destination"] == destination)]

        if route_data.empty:
            print("No historical data found for this route.")
            return None, None, None

        X = route_data["Year"].values.reshape(-1, 1)
        y = route_data["Passenger_count"].values
        model = LinearRegression()
        model.fit(X, y)

        future_X = np.array(future_years).reshape(-1, 1)
        future_preds = model.predict(future_X)

        predictions = pd.DataFrame({
            "Year": future_years,
            "Predicted_Passenger_Count": future_preds.astype(int)
        })

        return route_data, future_years, future_preds
