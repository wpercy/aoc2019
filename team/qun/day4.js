const min = 246540;
const max = 787419;
let counter = 0;
let results = [];

for (let i = min; i <= max; i++) {
  const digits = i.toString().split("");
  const uniqueDigits = new Set(digits);

  if (digits.length === uniqueDigits.size) {
    continue;
  }

  const sortedStr = digits.sort((a, b) => a - b).join("");
  if (sortedStr === i.toString()) {
    counter++;
    results.push(i);
  }
}

console.log(`q1 result: ${counter}`);

function arrayToMap(list) {
  return list.reduce((prev, cur) => {
    if (prev[cur]) {
      prev[cur] = prev[cur] + 1;
    } else {
      prev[cur] = 1;
    }
    return prev;
  }, {});
}

const q2 = results.filter(num => {
  const digits = num.toString().split("");
  const map = arrayToMap(digits);
  return Object.values(map).some(count => count == "2");
});

console.log(`q2 result: ${q2.length}`);
