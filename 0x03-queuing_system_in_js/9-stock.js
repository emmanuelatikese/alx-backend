import express from 'express';
import { createClient } from 'redis';
import util from 'util';

const app = express();
const PORT = 1245;
const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
}).on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

const listProducts = [
    { itemId: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { itemId: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { itemId: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { itemId: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

const getItemById = (id) => {
    return listProducts.find(product => product.itemId === parseInt(id));
};

const reserveStockById = (itemId, stock) => client.set(`item.${itemId}`, stock);

const getClient = util.promisify(client.get).bind(client);
const getCurrentReservedStockById = async (itemId) => {
    try {
        const ans = await getClient(`item.${itemId}`);
        return ans ? parseInt(ans) : null;
    } catch (error) {
        console.error(error);
        return null;
    }
};

app.use(express.json());


app.get('/list_products', (req, res) => {
    res.json(listProducts);
});


app.get('/list_products/:id', async (req, res) => {
    const itemId = parseInt(req.params.id);
    const product = getItemById(itemId);

    if (!product) {
        return res.status(404).json({ "status": "Product not found" });
    }

    const currentQuantity = await getCurrentReservedStockById(itemId);
    const availableQuantity = currentQuantity !== null ? currentQuantity : product.stock;

    res.json({
        itemId: product.itemId,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity: availableQuantity
    });
});

app.get('/reserve_product/:id', async (req, res) => {
    const itemId = parseInt(req.params.id);
    const product = getItemById(itemId);

    if (!product) {
        return res.status(404).json({ "status": "Product not found" });
    }

    const currentQuantity = await getCurrentReservedStockById(itemId);
    const availableQuantity = currentQuantity !== null ? currentQuantity : product.stock;

    if (availableQuantity <= 0) {
        return res.json({ "status": "Not enough stock available", "itemId": itemId });
    }

    await reserveStockById(itemId, availableQuantity - 1);
    res.json({ "status": "Reservation confirmed", "itemId": itemId });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
