# Webassembly performance comparision

## Preparation

```sh
pip install playwright selenium
playwright install firefox

# + geckodriver and firefox browser for selenium
```

## Running

```sh
python -m http.server 8000 # serve `loop.wasm` file

# selenium
python run_selenium.py

# playwright
python run_playwright.py
```