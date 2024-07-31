import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () =>{
    console.log('Redis client connected to the server');
}).on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
})



client.hset('Cities', 'Portland', '50', print);
client.hset('Cities', 'Seattle', '80', print);
client.hset('Cities', 'New York', '20', print);
client.hset('Cities', 'Bogota', '20', print);
client.hset('Cities', 'Cali', '40', print);
client.hset('Cities', 'paris', '2', print);

client.hgetall('Cities', (err, data) => {
    if (err) throw err;
    console.log(data);
});
