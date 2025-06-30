import pandas as pd


def get_ons_energy(csv_path, usina_name, month_filter="2025-06"):
    # Load the CSV file with the correct delimiter
    try:
        print(f"Attempting to load file from: {csv_path}")
        df = pd.read_csv(csv_path, delimiter=";")  # Specify semicolon as the delimiter
        print("File loaded successfully.")
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at path: {csv_path}")
    
    # Strip and normalize column names
    df.columns = df.columns.str.strip().str.lower()
    print("Normalized columns:", df.columns)  # Debugging output
    
    # Check if 'din_instante' exists
    if "din_instante" not in df.columns:
        raise ValueError("Column 'din_instante' is missing from the CSV file.")
    
    # Convert 'din_instante' to datetime
    df["din_instante"] = pd.to_datetime(df["din_instante"], errors="coerce")
    if df["din_instante"].isnull().any():
        raise ValueError("Invalid or missing date values in 'din_instante' column.")
    
    # Extract the month from 'din_instante'
    df["month"] = df["din_instante"].dt.strftime("%Y-%m")
    
    # Filter the DataFrame based on the month and usina name
    filtered = df[
        (df["month"] == month_filter) &
        (df["nom_usina"].str.upper() == usina_name.upper())
    ]
    
    # Handle case where no data is found
    if filtered.empty:
        print("No data found for that plant and month.")
        return None
    
    # Calculate total energy in kWh
    total_mwh = filtered["val_geracao"].sum() * 24  # MW médios × 24 hours = MWh
    total_kwh = total_mwh * 1000  # Convert MWh to kWh
    
    # Return the result
    return {
        "month": month_filter,
        "energy_kwh": round(total_kwh, 2),
        "source": "ONS"
    }