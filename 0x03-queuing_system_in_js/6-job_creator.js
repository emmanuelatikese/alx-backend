import { createQueue} from 'kue';

const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '0983453',
  message: "Push Notification"
});

job.on('failed', () => {
  console.log('Notification job failed');
}).on('complete', () => {
  console.log('Notification job completed');
}).save((err) => {
  if (err) {
    console.error('Failed to create job:', err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});
