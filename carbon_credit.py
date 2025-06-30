def calculate_carbon_credit(generator, energy, emission_factor):
    energy_kwh = energy["energy_kwh"]
    co2_avoided = (energy_kwh / 1000) * emission_factor  # MWh conversion

    return {
        "device_id": generator["device_id"],
        "month": energy["month"],
        "energy_kwh": energy_kwh,
        "co2_avoided_kg": round(co2_avoided, 2),
        "source": energy["source"],
        "owner_signed": False
    }
