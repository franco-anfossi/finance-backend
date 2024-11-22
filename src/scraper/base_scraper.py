from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BaseScraper:
    def __init__(self, username: str, password: str, otp: str = None):
        self.username = username
        self.password = password
        self.otp = otp
        self.driver = None

    def setup_driver(self):
        """Configurar el navegador."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def close_driver(self):
        """Cerrar el navegador."""
        if self.driver:
            self.driver.quit()

    def login(self):
        """Este método debe ser implementado por cada banco."""
        raise NotImplementedError(
            "El método login debe ser implementado por el scraper específico."
        )

    def scrape_transactions(self):
        """Este método debe ser implementado por cada banco."""
        raise NotImplementedError(
            "El scrape_transactions debe ser ejecutarse por el scraper específico."
        )

    def run(self):
        """Este método ejecuta el scraper."""
        raise NotImplementedError(
            "El método run debe ser implementado por el scraper específico."
        )
