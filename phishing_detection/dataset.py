from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from phishing_detection.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

import pandas as pd

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset_full.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
   data = pd.read_csv(input_path)
   data

if __name__ == "__main__":
    app()
