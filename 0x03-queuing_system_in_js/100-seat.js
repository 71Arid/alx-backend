import kue from 'kue';
const redis = require('redis');
const util = require('util');
const express = require('express');

const app = express();
app.use(express.json());
const queue = kue.createQueue();
const client = redis.createClient('redis://127.0.0.1:6379');
let reservationEnabled = false; 
client.get = util.promisify(client.get);


function reserveSeat(number) {
  return client.set('available_seats', `${number}`);
}

async function getCurrentAvailableSeats() {
  try {
    const resp = await client.get('available_seats');
    return parseInt(resp);
  } catch(err) {
    console.error(err);
  }
}

app.get('/available_seats', async (_req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({"numberOfAvailableSeats":`${seats}`});
});

app.get('/reserve_seat', async (_req, res) => {
  if (!reservationEnabled) {
    res.json({"status": "Reservation are blocked"});
  }
  try {
    const job = queue.create('reserve_seat');
    job.on('complete', (_result) => {
      console.log(`Seat reservation job ${job.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    })
    job.save();
    res.json({ "status": "Reservation in process" });
  } catch(_err) {
    res.json({ "status": "Reservation failed" });
  }
});

app.get('/process', async (_req, res) => {
  res.json({ "status": "Queue processing" });
  try {
    queue.process('reserve_seat', async (_job, done) => {
      const current_seats = await getCurrentAvailableSeats();
      if (current_seats > 0) {
        reserveSeat(current_seats - 1);
        if (current_seats - 1 === 0) reservationEnabled = false;
        done();
      } else {
        done(new Error('Not enough seats available'));
      }
    })
  } catch(err) {
    done(err);
  }
});

app.listen(1245, () => {
  reserveSeat(50);
  reservationEnabled = true;
  console.log('App listening on port 1245');
});
