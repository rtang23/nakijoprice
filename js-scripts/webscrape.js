const puppeteer = require("puppeteer");

async function scrapeProduct(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);

  // const [el] = await page.$('/html/body/div[2]/div/div/div/div[3]/div/div/div[1]/div/a/div[2]/div/div/div[1]')
  // const text = await el.getProperty('textContent')
  // const srcText = await text.jsonValue()

  selector = ".product-link";
  const cardLinks = await page.evaluate(selector => {
    let elements = Array.from(document.querySelectorAll(selector));
    let links = elements.map(element => {
      return element.href;
    });
    return links;
  }, selector);
  console.log({ cardLinks });

  browser.close();
}

// url = "https://www.nakijo.com.au/collections/dark-neostorm-dane"
url ="https://www.nakijo.com.au/collections/ots-tournament-pack-12-op12"
scrapeProduct(url);
