import { createClient, print } from 'redis';
import { promisify } from 'util';

const PORT = 6379;
const redisUrl = `redis://127.0.0.1:${PORT}`;

const client = createClient(redisUrl)
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

client.get = promisify(client.get);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName)
    .then((resp) => {
      console.log(resp);
    })
    .catch((err) => {
      console.error(err);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
