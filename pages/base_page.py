from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def highlight(self, selector: str, color: str = "red"):
        try:
            self.page.eval_on_selector(selector, f"""
                el => {{
                    el.style.boxShadow = '0 0 0 3px {color} inset';
                    setTimeout(() => el.style.boxShadow = '', 1000);
                }}
            """)
        except Exception as e:
            print(f"[WARN] Failed to highlight element: {selector} — {e}")

    def click_on_element(self, selector: str, timeout: int = 5000):
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            self.highlight(selector, "blue")
            self.page.click(selector)
        except PlaywrightTimeoutError:
            raise Exception(f"Element not found or not clickable: {selector}")

    def fill_text(self, selector: str, value: str, timeout: int = 5000):
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            self.highlight(selector, "green")
            self.page.fill(selector, value)
        except PlaywrightTimeoutError:
            raise Exception(f"Unable to fill field: {selector}")

    def get_text(self, selector: str) -> str:
        self.highlight(selector, "orange")
        return self.page.text_content(selector)

    def is_visible(self, selector: str) -> bool:
        try:
            return self.page.is_visible(selector)
        except PlaywrightTimeoutError:
            return False

    def wait_for_url(self, expected_url: str, timeout: int = 5000):
        try:
            self.page.wait_for_url(expected_url, timeout=timeout)
        except PlaywrightTimeoutError:
            raise Exception(f"Timeout waiting for URL: {expected_url}")

    def press_key(self, selector: str, key: str):
        self.highlight(selector, "purple")
        self.page.press(selector, key)

    def get_attribute(self, selector: str, attribute: str) -> str:
        self.highlight(selector, "yellow")
        return self.page.get_attribute(selector, attribute)

    def screenshot(self, path: str = "screenshot.png"):
        self.page.screenshot(path=path)

    def select_dropdown_option(self, selector: str, value: str = None, label: str = None, index: int = None):

        self.highlight(selector, "teal")

        if value:
            self.page.select_option(selector, value=value)
        elif label:
            self.page.select_option(selector, label=label)
        elif index is not None:
            self.page.select_option(selector, index=index)
        else:
            raise ValueError("You must provide either value, label, or index to select from dropdown.")


