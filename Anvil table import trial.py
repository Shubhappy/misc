import pandas as pd
import anvil.tables as tables
from anvil.tables import app_tables
import plotly.express as px

import anvil.server
anvil.server.connect("GYSLNWI3Z4V3CT6NPGUO6DKU-G2BT7WNDMLX6QA2L")  # Make sure you replace this with your own Uplink key

def import_table(file):
    df = pd.read_csv(file)
    app_tables.population
    
import_table("Madhya Pradesh Population Data.csv")