# Carbon-Credit-Calculator
Carbon Credit Generator
This project simulates carbon credit tokenization using real energy generation data from Brazil’s ONS (Operador Nacional do Sistema Elétrico). It parses generation data from a monthly .csv file and calculates the estimated carbon credits produced, which can be further tokenized on Avalanche. In this project the most recent data is being used which is from the month of June 2025.

The dataset is too large to host on GitHub, so you'll need to download it manually.

1. Go to:
https://dados.ons.org.br/dataset/geracao-usina-2

Scroll down to the most recent month (in this case: "Geracao_Usina_2-2025-06")
Download the .csv file.

2. Create a local folder in your project root called data/ and move the file into it:

carbon_credit_project/
├── data/
│   └── geracao_usina_202506.csv

3. Setup & Installation
Clone this repo or copy files to your machine.

Create a virtual environment and install dependencies

Project Structure:

carbon_credit_project/

├── etl/
│   └── emission_factor.py  # Retrieves the emission factor
│   └── ons_collector.py    # Reads and filters ONS generation CSV
│   └── carbon_credit.py    # Calculates the carbon credit

├── main.py                # Main script to run calculation

├── data/                  # Folder where the ONS CSV is stored
│   └── geracao_usina_202506.csv

├── README.md
└── requirements.txt
