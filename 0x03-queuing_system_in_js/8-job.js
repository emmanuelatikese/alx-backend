const createPushNotificationsJobs = (jobs, queue) =>{
    if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
    jobs.forEach(job => {
    job =  queue.create('push_notification_code_2', job);
    job.on('complete', () =>{
            console.log('Notification job JOB_ID completed')
    })
    .on('progress', (progress) =>{
        console.log(`Notification job ${job.id} ${progress}% complete`)
    })
    .on('failed', (err) => {
        console.error(`Notification job ${job.id} failed: ${err.message}`);
    })
        .save((err) => console.log(`Notification job created: ${job.id}`));
    });
}