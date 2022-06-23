from typing import Callable, Union

import pathlib
import json


def get_stock_ticker_from_file(file_path: pathlib.Path):
    parse_method = get_file_parse_method(file_path.suffix)
    return parse_method(file_path)


def get_file_parse_method(
    file_suffix: str,
) -> Callable[[pathlib.Path], Union[list, dict]]:
    if file_suffix == ".txt":
        return parse_txt_file
    elif file_suffix == ".json":
        return parse_json_file


def parse_json_file(file_path: pathlib.Path) -> dict:
    with file_path.open() as f:
        json_data: dict = json.load(f)
    return json_data


def parse_txt_file(file_path: pathlib.Path) -> list:
    with file_path.open() as f:
        tickers = f.read().splitlines()
    return tickers


def write_txt_file_from_tickers(tickers: list[str], file_path: pathlib.Path):
    with file_path.open("w") as f:
        map(lambda x: x + "\n", tickers)
        f.writelines(tickers)


def write_json_file_from_dict(dict: dict, file_path: pathlib.Path):
    with file_path.open("w") as f:
        json_data = json.dumps(dict)
        f.write(json_data)


if __name__ == "__main__":

    temp_dir = pathlib.Path(__file__).parent / "temp"
    temp_dir.mkdir(exist_ok=True)

    tickers = ["NVO"]
    data_dict = {"Danish": ["NVO"]}
    txt_file = temp_dir / "stocks.txt"
    json_file = temp_dir / "stocks.json"
    write_txt_file_from_tickers(tickers=tickers, file_path=txt_file)
    write_json_file_from_dict(dict=data_dict, file_path=json_file)

    txt_data = get_stock_ticker_from_file(txt_file)
    json_data = get_stock_ticker_from_file(json_file)

    print(
        f"Text data was {'Correctly' if tickers==txt_data else 'Wrongly'} written and read, {txt_data =}"
    )
    print(
        f"JSON data  was {'Correctly' if data_dict==json_data else 'Wrongly'} written and read, {json_data =}"
    )
