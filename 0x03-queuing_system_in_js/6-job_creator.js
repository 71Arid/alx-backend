import kue from 'kue';

const queue = kue.createQueue();
const obj = { phoneNumber: '0723456789', message: 'This is me.....' }

const job = queue.create('push_notification_code', obj)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', (_result) => {
  console.log('Notification job created: JOB ID');
})
.on('failed', (_err) => {
  console.log('Notification job failed');
})
