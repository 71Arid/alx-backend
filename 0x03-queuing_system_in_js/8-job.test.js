import kue from 'kue';
import createPushNotificationsJobs from './8-job';
const chai = require('chai');
const sinon = require('sinon');
const expect = chai.expect;

const queue = kue.createQueue();
const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    }
];

describe('createPushNotificationsJobs', function() {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit()
  });

  it('displays an error if jobs not an array', function() {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });
  it('creates two jobs', function() {
    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
  })
});
