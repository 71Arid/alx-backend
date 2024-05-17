function createPushNotificationsJobs(jobs, queue) {
  if (!jobs instanceof Array) {
    throw new Error('Jobs is not an array');
  }
  for (const item in jobs) {
    const job = queue.create('push_notification_code_3', jobs)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });
    job.on('complete', (_result) => {
      console.log(`Notification job ${job.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    })
    .on('progress', (progress, _data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    })
  }
}

export default createPushNotificationsJobs;
