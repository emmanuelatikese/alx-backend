import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () =>{
    console.log('Redis client connected to the server');
}).on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});
client.SUBSCRIBE('holberton school channel');
client.on('message', (channel, message) =>{
    if (channel === 'holberton school channel'){
        if (message === 'KILL_SERVER'){
            client.UNSUBSCRIBE();
            client.QUIT();
        }
        console.log(message);
    }
})