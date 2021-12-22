import time
from playwright.sync_api import sync_playwright

def run(page):
    page.evaluate("""
        WebAssembly.instantiateStreaming(fetch("loop.wasm"))
        .then(function(results) {
            let run_loop = results.instance.exports.run_loop;
            run_loop(987_654_321_0n);
        })
    """)


with sync_playwright() as p:
    firefox = p.firefox.launch()
    page = firefox.new_page()
    page.goto("http://localhost:8000")
    st = time.time()
    run(page)
    ed = time.time()
    print(ed - st)