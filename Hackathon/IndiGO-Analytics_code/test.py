from data_loader import DataLoader
from analysis_engine import AnalysisEngine
from visualization import (
    plot_delay_analysis,
    plot_forecast
)

# Load data
loader = DataLoader(
    "D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/city.csv",
    "D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/carrier.csv",
    "D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/indian_flight_delays.csv"
)

loader.load_data()
loader.clean_data()

# Initialize engine
engine = AnalysisEngine(loader.city_df, loader.carrier_df, loader.delay_df)

# Top Sectors
print("\n--- Top 3 Sectors by Passenger Traffic ---")
top3 = engine.top_sectors()
print(top3)

# Predict demand for a specific route and year
print("\n--- Passenger Trend (Specific Route & Year) ---")
demand_trend = engine.predict_demand("DELHI", "MUMBAI", 2021)
print(demand_trend)

# Airline Market Share
print("\n--- Airline Market Share Analysis ---")
share_df = engine.airline_market_share()
print(share_df.head(10))

# Flight Delay Patterns
print("\n--- Flight Delay Analysis ---")
airlines, routes, reasons = engine.flight_delay_patterns()
print("\nTop Delayed Airlines:\n", airlines)
print("\nMost Delayed Routes:\n", routes)
print("\nCommon Delay Reasons:\n", reasons)
plot_delay_analysis(airlines, routes, reasons)

# Forecasting Future Demand
print("\n--- Forecasting Future Demand for DELHI → MUMBAI ---")
route_data, future_years, future_preds = engine.forecast_demand("DELHI", "MUMBAI", [2025, 2026, 2027])
if route_data is not None:
    plot_forecast(route_data, future_years, future_preds, "DELHI", "MUMBAI")
