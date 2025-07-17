'''
This file creates a clean, user-friendly GUI dashboard for IndiGO Analytics.
Features:
- Top 3 busiest air sectors
- Passenger demand prediction
- Airline market share trends
- Delay pattern visualizations
- Forecasting future demand via ML
The GUI is built using Tkinter and connects to analysis & visualization modules.

⚠️ IMPORTANT: This application might take a few **seconds to load and respond** due to the 
use of **large real-world aviation datasets**. Please be patient while the data is being processed.
'''

from tkinter import *
from tkinter import ttk
from data_loader import DataLoader
from analysis_engine import AnalysisEngine
import visualization as viz 

# 1. Load & clean data from CSV files
loader = DataLoader(
    "D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/city.csv",
    "D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/carrier.csv",
    "D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/indian_flight_delays.csv"
)
loader.load_data()
loader.clean_data()

engine = AnalysisEngine(loader.city_df, loader.carrier_df, loader.delay_df) # 2. Initialize analysis engine with the cleaned data

def show_top_sectors(): # Display top 3 busiest sectors using passenger traffic.
    top3 = engine.top_sectors()
    print(top3)
    viz.plot_top_sectors(top3)

def show_demand_prediction(): # Open a sub-window to take route & year input, then plot predicted demand.
    def run_prediction():
        origin = origin_entry.get().upper().strip()
        destination = dest_entry.get().upper().strip()
        try:
            year = int(year_entry.get().strip())
        except ValueError:
            error_label.config(text="Invalid year. Use numbers only.")
            return

        result = engine.predict_demand(origin, destination, year)
        if not result.empty:
            viz.plot_demand_prediction(result, origin, destination)
            error_label.config(text="")
        else:
            error_label.config(text="No data found for that route + year.")

    # GUI
    pred_window = Toplevel(root)
    pred_window.title("Predict Demand")
    Label(pred_window, text="Origin City: (example: mumbai, delhi)").pack(pady=2)
    origin_entry = Entry(pred_window)
    origin_entry.pack(pady=2)

    Label(pred_window, text="Destination City: (example: mumbai, pune, delhi)").pack(pady=2)
    dest_entry = Entry(pred_window)
    dest_entry.pack(pady=2)

    Label(pred_window, text="Year:").pack(pady=2)
    year_entry = Entry(pred_window)
    year_entry.pack(pady=2)

    error_label = Label(pred_window, text="", fg="red")
    error_label.pack(pady=5)

    Button(pred_window, text="Predict", command=run_prediction).pack(pady=5)

def show_market_share(): # Analyze market share of airlines over years.
    share_df = engine.airline_market_share()
    print(share_df.head())
    viz.plot_market_share(share_df)

def show_flight_delays(): # Open sub-window to select between delay analysis types.
    def show_airlines():
        airlines, _, _ = engine.flight_delay_patterns()
        viz.plot_delay_analysis(airlines, None, None)

    def show_routes():
        _, routes, _ = engine.flight_delay_patterns()
        viz.plot_delay_analysis(None, routes, None)

    def show_reasons():
        _, _, reasons = engine.flight_delay_patterns()
        viz.plot_delay_analysis(None, None, reasons)

    # Sub-window for selecting delay type
    delay_window = Toplevel(root)
    delay_window.title("Choose Delay Analysis")
    Label(delay_window, text="Select Delay Category", font=("Helvetica", 14)).pack(pady=10)

    Button(delay_window, text="Top Delayed Airlines", command=show_airlines).pack(pady=5)
    Button(delay_window, text="Top Delayed Routes", command=show_routes).pack(pady=5)
    Button(delay_window, text="Common Delay Reasons", command=show_reasons).pack(pady=5)


def show_forecast():# Take future years input and forecast passenger demand on a route.
    def run_forecast():
        origin = origin_entry.get().upper().strip()
        destination = dest_entry.get().upper().strip()
        try:
            years = [int(y.strip()) for y in years_entry.get().split(',')]
        except ValueError:
            error_label.config(text="Invalid year format. Use commas, e.g. 2025,2026")
            return

        route_data, future_years, future_preds = engine.forecast_demand(origin, destination, years)
        if route_data is not None:
            viz.plot_forecast(route_data, future_years, future_preds, origin, destination)
        else:
            error_label.config(text="No historical data for this route.")

    # Create popup
    forecast_window = Toplevel(root)
    forecast_window.title("Forecast Demand Input")
    Label(forecast_window, text="Origin City: (example: mumbai, delhi)").pack(pady=2)
    origin_entry = Entry(forecast_window)
    origin_entry.pack(pady=2)

    Label(forecast_window, text="Destination City: (example: mumbai, pune, delhi)").pack(pady=2)
    dest_entry = Entry(forecast_window)
    dest_entry.pack(pady=2)

    Label(forecast_window, text="Years (comma separated):").pack(pady=2)
    years_entry = Entry(forecast_window)
    years_entry.pack(pady=2)

    error_label = Label(forecast_window, text="", fg="red")
    error_label.pack(pady=5)

    Button(forecast_window, text="Run Forecast", command=run_forecast).pack(pady=5)

# === GUI Layout ===

root = Tk()
root.title("IndiGO Analytics Dashboard")
root.geometry("600x500")
root.configure(bg="#f4f6fa")  

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 11), padding=10)
style.map("TButton", background=[("active", "#0052cc")])


header = Frame(root, bg="#003366")
header.pack(fill=X)
Label(header, text="✈ IndiGO Analytics", font=("Helvetica", 20, "bold"), fg="white", bg="#003366", pady=10).pack()


Label(root, text="Select an analysis to begin", font=("Segoe UI", 14), bg="#f4f6fa", fg="#333").pack(pady=20)


button_frame = Frame(root, bg="#f4f6fa")
button_frame.pack(pady=10)

ttk.Button(button_frame, text="📊  Top 3 Sectors", command=show_top_sectors, width=25).grid(row=0, column=0, padx=10, pady=10)
ttk.Button(button_frame, text="🔍  Predict Demand", command=show_demand_prediction, width=25).grid(row=1, column=0, padx=10, pady=10)
ttk.Button(button_frame, text="📈  Market Share", command=show_market_share, width=25).grid(row=2, column=0, padx=10, pady=10)
ttk.Button(button_frame, text="⏱️  Flight Delay Analysis", command=show_flight_delays, width=25).grid(row=3, column=0, padx=10, pady=10)
ttk.Button(button_frame, text="📅  Forecast Demand", command=show_forecast, width=25).grid(row=4, column=0, padx=10, pady=10)


Label(root, text="Powered by Team IndiGO Hackers 🚀", font=("Segoe UI", 9), bg="#f4f6fa", fg="#777").pack(side=BOTTOM, pady=10)

root.mainloop()
