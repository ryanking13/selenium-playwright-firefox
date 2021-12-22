import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

def run(driver):
    driver.execute_async_script("""
        (async () => {
            var callback = arguments[arguments.length - 1];
            WebAssembly.instantiateStreaming(fetch("loop.wasm"))
            .then(function(results) {
                let run_loop = results.instance.exports.run_loop;
                callback(run_loop(987_654_321_0n));
            })
        })()
    """)


options = Options()
options.add_argument("--headless")
firefox = Firefox(executable_path="geckodriver", options=options)
firefox.set_script_timeout(60)
firefox.get("http://localhost:8000")
try:
    st = time.time()
    run(firefox)
    ed = time.time()
    print(ed - st)
finally:
    firefox.quit()