from datetime import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_scraper import BaseScraper


class SantanderScraper(BaseScraper):
    def login(self):
        """Autenticarse en el sitio de Santander."""
        try:
            self.driver.get("https://movil.santander.cl")

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "rut"))
            )
            rut_input = self.driver.find_element(By.ID, "rut")
            rut_input.send_keys(self.username)

            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "pass"))
            )
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.RETURN)

        except TimeoutException:
            print("Error al autenticarse en Santander.")

    def scrape_transactions(self):
        """Extraer transacciones desde la página de Santander."""
        transactions = []
        try:
            # Paso 1: Hacer clic en el botón inicial para acceder a las transacciones
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "box-product"))
            )
            product_button = self.driver.find_element(By.CLASS_NAME, "box-product")
            product_button.click()

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "tr.mat-row"))
            )
            rows = self.driver.find_elements(By.CSS_SELECTOR, "tr.mat-row")

            today = datetime.now().strftime("%d/%m")

            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                if len(cols) >= 5:
                    transaction_date = cols[0].text.strip()
                    if transaction_date == today:
                        transaction = {
                            "date": transaction_date,
                            "description": cols[2].text.strip(),
                            "amount_charge": cols[3].text.strip(),
                            "amount_payment": cols[4].text.strip(),
                            "balance": cols[5].text.strip(),
                        }
                        transactions.append(transaction)

        except TimeoutException:
            print("No se encontraron transacciones en Santander.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

        return transactions

    def run(self, username, password):
        self.username = username
        self.password = password
        self.setup_driver()
        self.login()
        transactions = self.scrape_transactions
        self.close_driver()
        return transactions


if __name__ == "__main__":
    scraper = SantanderScraper(username="21.129.535-K", password="9T^#fq4bk6")
    scraper.setup_driver()
    scraper.login()
    transactions = scraper.scrape_transactions()
    print(transactions)
    scraper.close_driver()
