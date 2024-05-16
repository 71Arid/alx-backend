import { createClient } from 'redis';

const PORT = 6379;
const redisUrl = `redis://127.0.0.1:${PORT}`;

const client = createClient(redisUrl)
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'))
