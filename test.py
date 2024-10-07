from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define path to your mitmproxy certificate

# Setup Chrome options
chrome_options = Options()
chrome_options.accept_untrusted_certs = True
chrome_options.add_argument('--proxy-server=http://localhost:8080')  # Proxy setup
# chrome_options.add_argument('--ignore-certificate-errors')  # Ignore certificate errors (optional)

# Initialize the WebDriver with the options
driver = webdriver.Chrome(options=chrome_options)

# Open a URL to test HTTPS
driver.get("https://example.com")

input()