import { createClient } from 'redis';
import { promisify } from 'util';

const PORT = 6379;
const redisUrl = `redis://127.0.0.1:${PORT}`;

const client = createClient(redisUrl)
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

client.unsubscribe = promisify(client.unsubscribe).bind(client);

client.subscribe('holberton school channel')

client.on('message', (channel, message) => {
  console.log(`${message}`);
  if (message === "KILL_SERVER") {
    client.unsubscribe('holberton school channel')
      .then(() => {
        client.quit();
      })
      .catch((err) => {
        console.error('Error unsubscribing:', err);
      });
  }
});
