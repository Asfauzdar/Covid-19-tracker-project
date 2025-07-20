import requests
import time
from datetime import datetime
import matplotlib.pyplot as plt

print("🎯 WELCOME TO THE COVID-19 TRACKER")
print(" ")

while True:
    country = input("🌍 Enter the country name you want to get the data for: ").strip()
    print(" ")
    time.sleep(1)

    url = f"https://disease.sh/v3/covid-19/countries/{country}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print(f"\n📊 COVID-19 STATS FOR {data['country'].upper()}:")
        time.sleep(1)
        print(" ")
        print(f"🧪 Total Cases   : {data['cases']:,}")
        time.sleep(1)
        print(" ")
        print(f"📈 Active Cases  : {data['active']:,}")
        time.sleep(1)
        print(" ")
        print(f"💚 Recovered     : {data['recovered']:,}")
        time.sleep(1)
        print(" ")
        print(f"⚰️ Deaths        : {data['deaths']:,}")
        time.sleep(1)

        # Format last updated time
        timestamp_ms = int(data['updated'])
        updt_time = datetime.fromtimestamp(timestamp_ms / 1000)
        print(f"\n🕒 Last Updated  : {updt_time.strftime('%A, %d %B %Y %I:%M:%S %p')}")
        print("\n")
        time.sleep(1)

        # Ask for bar graph
        while True:
            graph = input("📊 Do you want to see this in a bar graph? (yes/no): ").strip().lower()
            if graph == "yes":
                labels = ['Total Cases', 'Active', 'Recovered', 'Deaths']
                values = [data['cases'], data['active'], data['recovered'], data['deaths']]
                colors = ['skyblue', 'orange', 'limegreen', 'red']

                plt.figure(figsize=(8, 5))
                plt.bar(labels, values, color=colors)
                plt.title(f"COVID-19 STATS FOR {data['country'].upper()}")
                plt.ylabel("Number of Cases")
                plt.tight_layout()
                plt.show()
                break
            elif graph == "no":
                print("👍 No problem!\n")
                break
            else:
                print("⚠️ Please enter only 'yes' or 'no'.")

        # Ask to exit or continue 
        while True:
            exit_ = input("🔁 Do you want to check another country or exit? (more/exit): ").strip().lower()
            if exit_ == "exit":
                print("\n👋 BYE! STAY SAFE AND TAKE PROPER PRECAUTIONS! 🛡️")
                exit()
            elif exit_ == "more":
                print("\n🔄 Okay! Let's check another country.\n")
                break
            else:
                print("⚠️ Please type only 'more' to continue or 'exit' to quit.\n")

    except requests.exceptions.HTTPError:
        print("❌ Invalid country name or data not available.\nPlease try again.\n")
        time.sleep(1)
        continue

    except requests.exceptions.RequestException as e:
        print("🚫 Network error:", e)
        print("Please try again later.")
        break
