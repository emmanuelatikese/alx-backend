import express from 'express';
import { createClient } from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const PORT = 1245;
const redisClient = createClient();
const queue = kue.createQueue();


const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

let reservationEnabled = true;

const initializeSeats = async () => {
    await setAsync('available_seats', 50);
};

initializeSeats().catch(console.error);


const reserveSeat = async (number) => {
    await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
    try {
        const seats = await getAsync('available_seats');
        return seats;
    } catch (error) {
        console.error(error);
        return null;
    }
};


queue.process('reserve_seat', async (job, done) => {
    try {
        const availableSeats = await getCurrentAvailableSeats();
        const newSeats = parseInt(availableSeats) - 1;

        if (newSeats < 0) {
            done(new Error('Not enough seats available'));
        } else {
            await reserveSeat(newSeats);
            if (newSeats === 0) {
                reservationEnabled = false;
            }
            done();
        }
    } catch (error) {
        done(error);
    }
});

app.use(express.json());


app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat', {}).save((err) => {
        if (err) {
            return res.json({ status: 'Reservation failed' });
        }
        res.json({ status: 'Reservation in process' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (error) => {
        console.log(`Seat reservation job ${job.id} failed: ${error.message}`);
    });
});

app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });


    await new Promise((resolve) => {
        queue.process('reserve_seat', (job, done) => {
            resolve(done);
        });
    });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
