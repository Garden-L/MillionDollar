const crypto = require('crypto');

const buf = Buffer.from('hello word', 'ascii');
console.log(buf);
console.log(buf.toString('hex'));
console.log(buf.toString('base64'));

console.log('-------------');

const random = crypto.randomBytes(12);
console.log(random);
console.log(random.toString('hex'));