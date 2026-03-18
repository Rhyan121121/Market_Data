# Market Data

I created this project because I needed a shopping list while preparing for a beach trip.
Instead of writing everything by hand, I built a small terminal tool to register items in `.txt`, generate `.ods` spreadsheets, and export lists to image files.

## What it does today

- Create and edit shopping lists from the terminal
- Save data in `data/<list_name>.txt`
- Generate `.ods` spreadsheets using LibreOffice + UNO (`pyoo`)
- Remove items from existing lists
- Export `.ods` files to `.png`

## Acknowledgments

I used AI Claude to help me write the connection with `pyoo` and the LibreOffice UNO integration.

## Contributions

I'm open to receiving pull requests and contributions! Feel free to fork this project, make improvements, and submit your PRs. Any feedback or ideas are welcome!

## Requirements

- Python 3.14+
- LibreOffice installed (`soffice` available in PATH)
- Python dependency listed in `requirements.txt`

## Installation

### Using pip

Install dependencies:

```bash
pip install -r requirements.txt
```

### Using Poetry

If you have Poetry installed, run:

```bash
poetry install
```

## Run

### With Poetry

```bash
poetry run python main.py
```

### With pip

```bash
python main.py
```

## Future plans

In the future, I plan to make this project run in Office environments too, using `pandas` to improve file handling and compatibility.
