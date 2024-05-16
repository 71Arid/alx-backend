import { createClient, print } from 'redis';

const PORT = 6379;
const redisUrl = `redis://127.0.0.1:${PORT}`;

const client = createClient(redisUrl)
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'))

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, resp) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(resp);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
