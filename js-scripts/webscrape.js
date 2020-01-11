const puppeteer = require('puppeteer')

async function scrapeProduct(url) {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.goto(url)

    const [el] = await page.$x('/html/body/div[2]/div/div/div/div[3]/div/div/div[1]/div/a/div[2]/div/div/div[1]')
    const text = await el.getProperty('textContent')
    const srcText = await text.jsonValue()

    console.log({srcText})

    // const arr = await page.$x('/html/body/div[2]/div/div/div/div[3]/div/div/div[6]/div/a/div[2]/div/div/div[1]')
    // console.log({arr})
    // arr.forEach(async (x) => {
    //     const text = await x.getProperty('textContent')
    //     const srcText = await text.jsonValue()
    //     console.log({srcText})
    // })

    browser.close()
}

url = 'https://www.nakijo.com.au/collections/dark-neostorm-dane'
scrapeProduct(url)

