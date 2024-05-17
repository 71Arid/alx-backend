const express = require('express');
const redis = require('redis');
const util = require('util');

const app = express();
const client = redis.createClient('redis://127.0.0.1:6379');
app.use(express.json());
client.get = util.promisify(client.get);

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById(id) {
  for (const item of listProducts) {
    if (item.Id === id) {
      return item;
    }
  }
}

function reserveStockById(itemId, stock) {
  return client.set(`item.${itemId}`, `${stock}`);
}

async function getCurrentReservedStockById(itemId) {
  try {
    const resp = await client.get(`item.${itemId}`);
    return parseInt(resp) || 0;
  } catch (err) {
    console.error(err);
    return 0;
  }
}

function handleProductNotFound(req, res, next) {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    return res.json({ status: "Product not found" });
  }
  next();
}

async function checkAvailableStock(req, res, next) {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  const reservedStock = await getCurrentReservedStockById(itemId);
  if (product.stock - reservedStock <= 0) {
    return res.json({ status: "Not enough stock available", itemId });
  }
  next();
}

app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map(product => ({
    itemId: product.Id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  }));
  res.json(formattedProducts);
})

app.get('/list_products/:itemId', handleProductNotFound, async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.stock - reservedStock || product.stock;
  res.json({
    itemId: product.Id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: currentQuantity
  });
});

app.get('/reserve_product/:itemId', handleProductNotFound, checkAvailableStock, async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  const reservedStock = await getCurrentReservedStockById(itemId) || 0;
  reserveStockById(itemId, reservedStock + 1);
  res.json({ status: "Reservation confirmed", itemId });
})

app.listen(1245, () => {
  console.log('Server started listening at port 1245');
});
