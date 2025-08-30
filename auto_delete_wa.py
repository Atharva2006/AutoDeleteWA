import asyncio
from patchright.async_api import async_playwright
import time


class wab:

    def __init__(self, url):
        self.url = url
        self.data = []
        self.page_n = 1
        self.browser = None
        self.page = None
        self.value = None

    async def browser_open(self):
        async with async_playwright() as p:
            self.browser = await p.chromium.launch_persistent_context(
            user_data_dir="./profile",
            executable_path="/usr/bin/chromium",
            channel="chrome",
            headless=False,
            no_viewport=True,
        )
            self.page = await self.browser.new_page()
            await self.page.goto(self.url)
            scan = input("login in whatsapp web. press enter when done")
            await asyncio.sleep(8)
            
            grp = input("enter your exact group/chat name (is case sensitive)")
            bomboclat = self.page.locator(f'span[title= "{grp}"]')
        

            await bomboclat.click()
            
            await asyncio.sleep(4)

            while True:
                yoo = self.page.locator('div.copyable-text[data-pre-plain-text*="Atharv"]:not(:has-text("You deleted this message"))')
                
                while True:
                    count = await yoo.count()
                    if count > 0:
                        lastmsg = yoo.nth(count - 1)
                        break
                await asyncio.sleep(20)

                await self.page.evaluate('window.scrollBy(0, -100)')
                
                print("foundit")
                await lastmsg.hover(position={"x": 10, "y": 10}, timeout=0)
                print("hover")

                menu_btn = self.page.locator('div[data-js-context-icon="true"][role="button"]')
                await menu_btn.click()
                await asyncio.sleep(2)
                

                deletems = self.page.locator("li[role='button'][data-animate-dropdown-item='true'][style*='opacity']")
                msgg = deletems.nth(await deletems.count()-1)
                print(await deletems.count())
                await msgg.click()
                await asyncio.sleep(1)


                await self.page.locator("button[title='Delete']").click()
                await asyncio.sleep(1)

                await self.page.locator('//button[.//div[text()="Delete for everyone"]]').click()
                await asyncio.sleep(2)


url = "https://web.whatsapp.com/"
asyncio.run(wab(url).browser_open())
