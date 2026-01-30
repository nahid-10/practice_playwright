from playwright.async_api import async_playwright
import asyncio

async def open_browser():
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        
        await page.goto("https://www.udemy.com/")
        
        await asyncio.sleep(5)
        
        print(await page.title())
        
        await browser.close()
        print("Browser closed")

async def timer():
    for i in range(1, 6):
        print(f"Timer: {i} second passed")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(
        open_browser(),
        timer()
    )
asyncio.run(main())
