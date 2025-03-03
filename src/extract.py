from typing import Dict

import requests
from pandas import DataFrame, read_csv, read_json, to_datetime
import os

def temp() -> DataFrame:
    """Get the temperature data.
    Returns:
        DataFrame: A dataframe with the temperature data.
    """
    print("Directorio de trabajo actual:", os.getcwd())
    return read_csv("../data/temperature.csv")


def get_public_holidays(public_holidays_url: str, year: str) -> DataFrame:
    """Get the public holidays for the given year for Brazil.
    Args:
        public_holidays_url (str): url to the public holidays.
        year (str): The year to get the public holidays for.
    Raises:
        SystemExit: If the request fails.
    Returns:
        DataFrame: A dataframe with the public holidays.
    """

    # Definimos la URL para obtener los días festivos públicos del año dado.
    url = f"{public_holidays_url}/{year}/BR"

    try:
        # Realizamos la solicitud GET a la URL.
        response = requests.get(url)

        # Si la solicitud falla, lanzamos una excepción.
        response.raise_for_status()

        # Convertimos la respuesta a un DataFrame.
        df = DataFrame(response.json())

        # Eliminamos las columnas "types" y "counties".
        columns_to_drop = ["types", "counties"]
        df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

        # Convertimos la columna "date" a formato datetime.
        df["date"] = to_datetime(df["date"])

        return df

    except requests.exceptions.RequestException as e:
        # Si la solicitud falla, lanzamos una excepción de tipo SystemExit con el mensaje de error.
        print(f"Error al obtener los días festivos públicos del año {year}: {e}")
        raise SystemExit(1)

    # TODO: Implementa esta función.
    # Debes usar la biblioteca requests para obtener los días festivos públicos del año dado.
    # La URL es public_holidays_url/{year}/BR.
    # Debes eliminar las columnas "types" y "counties" del DataFrame.
    # Debes convertir la columna "date" a datetime.
    # Debes lanzar SystemExit si la solicitud falla. Investiga el método raise_for_status
    # de la biblioteca requests.


def extract(
    csv_folder: str, csv_table_mapping: Dict[str, str], public_holidays_url: str
) -> Dict[str, DataFrame]:
    """Extract the data from the csv files and load them into the dataframes.
    Args:
        csv_folder (str): The path to the csv's folder.
        csv_table_mapping (Dict[str, str]): The mapping of the csv file names to the
        table names.
        public_holidays_url (str): The url to the public holidays.
    Returns:
        Dict[str, DataFrame]: A dictionary with keys as the table names and values as
        the dataframes.
    """
    dataframes = {
        table_name: read_csv(f"{csv_folder}/{csv_file}")
        for csv_file, table_name in csv_table_mapping.items()
    }

    holidays = get_public_holidays(public_holidays_url, "2017")

    dataframes["public_holidays"] = holidays

    return dataframes
