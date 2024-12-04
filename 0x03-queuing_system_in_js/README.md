# Queuing System in JS

This project implements a queuing system in JavaScript using Redis and Node.js. The project covers:

- Basic Redis operations
- Redis client usage in Node.js
- Redis publisher/subscriber
- Redis with Node.js for basic operations and async operations
- Kue as a queue system
- Building an Express app using Redis for storage
- Building an Express app with Redis and Queue system

## Requirements

- All code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All code should use ES6 with Babel
- All files should end with a new line
- A README.md file is mandatory
- Code should use the .js extension

## Setup

```bash
# Install dependencies
npm install

# Run development server
npm run dev [filename]

# Run tests
npm test
```

## Files

- `0-redis_client.js`: Basic Redis client
- `1-redis_op.js`: Redis basic operations
- `2-redis_op_async.js`: Redis async operations
- `4-redis_advanced_op.js`: Redis advanced operations
- `5-subscriber.js`: Redis subscriber
- `5-publisher.js`: Redis publisher
- `6-job_creator.js`: Kue job creator
- `6-job_processor.js`: Kue job processor
- `7-job_creator.js`: Track progress and errors with Kue
- `7-job_processor.js`: Process tracked jobs
- `8-job.js`: Job creation function
- `8-job.test.js`: Tests for job creation
- `9-stock.js`: Stock check with Redis
- `100-seat.js`: Seat reservation system
