from db import *
from pprint import pprint


def main():
    print("######## Travel Records ########")

    while True:
        try:
            ch = int(
                input(
                    "Select your option:\n"
                    "1. All Tourist Details\n"
                    "2. All Travel Information\n"
                    "3. Most Expensive Travel Costs by City\n"
                    "4. Best Country to Visit\n"
                    "5. Exit\n"
                    "Enter option (1-5): "
                )
            )
            if ch == 1:
                tourist_details = fetch_all_tourist_details()
                print("All Tourist Details:")
                pprint(tourist_details)
            elif ch == 2:
                travel_info = fetch_all_travel_info()
                print("All Tourist Information:")
                pprint(travel_info)
            elif ch == 3:
                expensive_costs = expensive_travel_costs()
                print("Most Expensive Travel Costs by City:")
                pprint(expensive_costs)
            elif ch == 4:
                travel_info = get_travel_info_with_country()
                print("All Travel Information:")
                pprint(travel_info)
            elif ch == 5:
                best_country = best_country_to_visit()
                print("Best Country to Visit:")
                pprint(best_country)
            elif ch == 6:
                best_experiences = fetch_all_experiences()
                print("Best Experiences (Satisfaction Level = 5):")
                pprint(best_experiences)
            elif ch == 7:
                print("Exiting...")
                break
            else:
                print("Invalid option, please select a valid option (1-5).")

        except ValueError:
            print("Invalid input, please enter a number (1-5).")
        except Exception as e:
            print(f"An error occurred: {e}")

    CONN.close()
    print("PostgreSQL connection is closed.")


if __name__ == "__main__":
    main()
