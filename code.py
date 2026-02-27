import requests
import pandas as pd


def fetch_crypto_data():
    
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
   
    params = {
        "vs_currency": "inr",        # Currency for prices (Indian Rupee)
        "order": "market_cap_desc", # Order by descending market cap
        "per_page": 10,             # Fetch only the top 10 cryptocurrencies
        "page": 1                   # Fetch data from the first page
    }
    
   
    response = requests.get(url, params=params)
    
   
    if response.status_code == 200:
        return response.json()  # Return the JSON response if successful
    else:
       
        raise Exception(f"Failed to fetch data: {response.status_code}")


def process_data(data):
    
    df = pd.DataFrame(data)
    
   
    df = df[["name",                
             "current_price",       
             "high_24h",            
             "low_24h",             
             "price_change_percentage_24h"]]  
    
    
    return df


def main():
    
    try:
        
        crypto_data = fetch_crypto_data()
        
        
        df = process_data(crypto_data)
        
       
        print("Top 10 Cryptocurrencies (by Market Cap):\n")
        print(df)
        
        
        print("\nTop 5 Gainers:")
        print(df.nlargest(5, "price_change_percentage_24h"))  # Find the top 5 cryptocurrencies with the highest gains
    except Exception as e:
       
        print(e)

# Entry point for the script
if __name__ == "__main__":
    main()
