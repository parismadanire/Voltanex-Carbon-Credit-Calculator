from generator_data import get_generator
from etl.ons_collector import get_ons_energy
from etl.emission_factor import get_emission_factor
from etl.carbon_credit import calculate_carbon_credit
import json

# Define the CSV path
csv_path = "data/GERACAO_USINA-2_2025_06.csv"
usina_name = "Balbina"
month_filter = "2025-06"

# Get generator info
generator = get_generator(usina_name)

# Get real energy data
energy = get_ons_energy(csv_path, usina_name, month_filter)
if not energy:
    exit("No energy data found. Check plant name or file.")

# Emission factor
emission = get_emission_factor()

# Calculate carbon credit
credit = calculate_carbon_credit(generator, energy, emission)

# Save to JSON
with open("carbon_credit.json", "w") as f:
    json.dump(credit, f, indent=2)

print("Carbon credit created:")
print(json.dumps(credit, indent=2))




