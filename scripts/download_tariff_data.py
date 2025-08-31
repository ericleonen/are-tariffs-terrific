import requests
from zipfile import ZipFile
from io import BytesIO
import os

def download_tariff_data(
    dir_to: str,
    min_year: int = 1997,
    max_year: int = 2025
):
    """
    Downloads USITC annual tariff data in the given year range into the given directory. Skips years when
    the directory has that year's data. Prints a warning if a year's data is not available.

    Parameters
    ----------
    dir_to: str
        The directory that will have all the downloaded data files, each named 'tariff_data_{year}.xlsx'.
    min_year: int, optional
        The earliest year to include in the donwloaded data. Defaults to 1997.
    max_year: int, optional
        The latest year to include in the downloaded data. Defaults to 2025.

    Returns
    -------
    None
    """
    print("Downloading USITC annual tariff data from {min_year}-{max_year}:")
  
    for year in range(min_year, max_year + 1):
        f_name = f"tariff_data_{year}.xlsx"
        f_path = os.path.join(dir_to, f_name)
      
        if os.path.exists(f_path):
            print("    > Skipping download of {year} data")
            continue
      
        print(f"    > Attempting to download {year} data: ", end=" ")

        try:
            url = f"https://www.usitc.gov/tariff_affairs/documents/tariff_data/tariff_data_{year}.zip"
            res = requests.get(url)
            res.raise_for_status()
          
            with ZipFile(BytesIO(res.content)) as z:
                for name in z.namelist():
                    if name.endswith(".xlsx"):
                        with z.open(name) as f_in:
                            raw_annual_tariff_data = f_in.read()
                        with open(f_path, "wb") as f_out:
                            f_out.write(raw_annual_tariff_data)
                        print(f"✅")
        except Exception as e:
            print("❌")
            print(f"An exception occurred: {e}")

if __name__ == "__main__":
    download_tariff_data("data/processed/tariff_data")
