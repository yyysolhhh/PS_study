const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const [h,m] = input

const hour = h===0?(m-45 >= 0? 0:23):(m-45 >= 0? h:h-1)
const minuite = m-45 >= 0 ? m-45: 60+(m-45)

console.log(hour+" "+minuite);