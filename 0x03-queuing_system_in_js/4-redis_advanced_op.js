import { createClient, print } from 'redis';
import { promisify } from 'util';

const PORT = 6379;
const redisUrl = `redis://127.0.0.1:${PORT}`;

const client = createClient(redisUrl);
client.hgetall = promisify(client.hgetall);

client.hset('HolbertonSchools', 'Portland', '50', print);
client.hset('HolbertonSchools', 'Seattle', '80', print);
client.hset('HolbertonSchools', 'New York', '20', print);
client.hset('HolbertonSchools', 'Bogota', '20', print);
client.hset('HolbertonSchools', 'Cali', '40', print);
client.hset('HolbertonSchools', 'Paris', '2', print);

client.hgetall('HolbertonSchools')
  .then((resp) => {
    console.log(resp);
  })
  .catch((err) => {
    console.error(err);
  });
