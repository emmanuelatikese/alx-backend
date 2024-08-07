import { expect } from 'chai';
import kue from 'kue';
import { createPushNotificationsJobs } from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create new jobs for each item in the array', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Hello, this is a test notification' },
      { phoneNumber: '0987654321', message: 'Another test notification' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_2');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_2');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
