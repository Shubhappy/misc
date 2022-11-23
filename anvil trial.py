import pandas as pd
import anvil.tables as tables
from anvil.tables import app_tables
import plotly.express as px

import anvil.server
anvil.server.connect("CZQ554ZMBVHSL35MTUXJJ2VV-BIKRZ3UUKNRYSGZF")  # Make sure you replace this with your own Uplink key

def import_csv_data(file):
  with open(file, "r") as f:
    df = pd.read_csv(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.population.add_row(**d)

'''def import_excel_data(file):
  with open(file, "rb") as f:
    df = pd.read_excel(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.population.add_row(**d)'''

import_csv_data("Madhya Pradesh Population Data.csv")
#import_excel_data("colours.xlsx")

