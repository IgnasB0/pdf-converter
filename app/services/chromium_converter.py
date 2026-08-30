from playwright.async_api import async_playwright

class ChromiumConverter:

    async def create(self) -> None:
        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch()

    async def convert_to_pdf(self, html_content: str) -> bytes:
        page = await self._browser.new_page()
        try:
            await page.set_content(html_content)
            return await page.pdf()
        finally:
            await page.close()

    async def close(self) -> None:
        await self._browser.close()
        await self._playwright.stop()