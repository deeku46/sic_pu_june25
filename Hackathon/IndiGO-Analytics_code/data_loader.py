'''
Loads, cleans, and prepares three datasets:
- city.csv (route and passenger data)
- carrier.csv (airline performance data)
- delay.csv (flight delay statistics, optional)

'''


import pandas as pd

class DataLoader:
    def __init__(self, city_path, carrier_path, delay_path = None): # Initialize paths and DataFrame placeholders
        self.city_path = city_path
        self.carrier_path = carrier_path
        self.delay_path = delay_path
        self.city_df = None
        self.carrier_df = None
        self.delay_df = None

    def load_data(self): # Load city, delay and carrier datasets from CSV
        self.city_df = pd.read_csv("D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/city.csv")
        self.carrier_df = pd.read_csv("D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/carrier.csv")
        print("City data loaded successfully")
        print(self.city_df.head())
        print("Carrier data loaded successfully")
        print(self.carrier_df.head())

        if self.delay_path:
            self.delay_df = pd.read_csv(self.delay_path)
            print("Delay data loaded successfully")
            print(self.delay_df.head())


    def clean_data(self): # Clean .csv files: handle missing values, drop irrelevant columns, rename headers

        # Cleaning of city.csv

        print("Missing values in city data")
        print(self.city_df.isnull().sum())

        # Drop unnecessary freight/mail-related columns

        self.city_df.dropna(inplace=True)
        print("Cleaned city data, missing rows are dropped")

        self.city_df.drop(columns = ["FreightToCity2", "FreightFromCity2",
                                      "MailToCity2", "MailFromCity2"], inplace=True)
        
        print(self.city_df.columns)
        #  Rename columns for clarity and consistency

        self.city_df.rename(columns={"City1": "Origin",
                                    "City2": "Destination",
                                    "Passengers": "Passenger_Count"}, inplace=True)


        # Cleaning of carrier.csv

        print("Missing values in carrier data")
        print(self.carrier_df.isnull().sum())

        self.carrier_df.dropna(inplace=True)

        #  Drop aircraft/freight/cargo columns that aren't used in analysis

        self.carrier_df.drop(columns = ["Aircraft Hours", "Aircraft Kilometres", "Seat Kilometers",
                                        "Freight", "Mail", "Total Cargo",
                                        "Passenger Tonne Kilometer", "Mail Tonne Kilometer", "Freight Tonne Kilometer",
                                        "Total Tonne Kilometer", "Available Tonne Kilometer", "Weight Load Factor"], inplace=True)
        
         # Rename columns for consistency and better readability

        self.carrier_df.rename(columns={"Passenger Number": "Passengers",
                                        "Passenger Load Factor": "LoadFactor",
                                        "Passenger Kilometers": "PassengerKM",}, inplace=True)




if __name__ == "__main__":
    loader = DataLoader("D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/city.csv",
                        "D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/carrier.csv",
                        "D:/learning/sic_pu_june25/Hackathon/IndiGO-Analytics_datasets/indian_flight_delays.csv")
    loader.load_data()
    loader.clean_data()