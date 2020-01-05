const request = require("request");

// Build Request Input
let input = "Instant Fusion - OP04-EN002 - Ultimate Rare - Unlimited Edition";
let inputFormatted = input.replace(/\s/g, "-").replace(/(\-)+/g, "-");
let inputUrl = "http://www.nakijo.com.au/products/" + inputFormatted + ".js";
// let inputUrl = 'https://www.nakijo.com.au/collections/chaos-impact-chim'
let options = {
  url: inputUrl,
  headers: {
    "User-Agent":
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0"
  },
  method: "GET"
};

// HTTP Request - GET
request(options, (err, res, body) => {
  let json = JSON.parse(body);
  console.log("Inventory Quantity: " + json.variants[0].inventory_quantity); // Output Inventory Quantity
});

// request(options, (err, res, body) => {
//   // let json = JSON.parse(body)
//   console.log(body) 
// })
// // console.log('https://www.nakijo.com.au/collections/chaos-impact-chim')