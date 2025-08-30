import asyncio
from patchright.async_api import async_playwright
import time
# import pandas as pd 

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
            # R = input("enter\n")
            await asyncio.sleep(8)
            # bomboclat = self.page.locator('span[title="Caffeinated Chaos"]')
            # bomboclat = self.page.locator('span[title="DYPIU UNOFFICIAL GROUP "]')
            bomboclat = self.page.locator('span[title="Test"]')
        

            await bomboclat.click()
            # p = input("enter\n")
            await asyncio.sleep(4)

            while True:
                yoo = self.page.locator('div.copyable-text[data-pre-plain-text*="Atharv"]:not(:has-text("You deleted this message"))')
                
                while True:
                    count = await yoo.count()
                    if count > 0:
                        lastmsg = yoo.nth(count - 1)
                        break
                # lastmsg = yoo.nth(await yoo.count()-1)

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
                await asyncio.sleep(1)



                # q = input("waiting\n")
                await asyncio.sleep(4)







                # await page.locator('img[alt="Sticker with no label"]').hover()














                
              




            

        
        

url = "https://web.whatsapp.com/"
asyncio.run(wab(url).browser_open())
