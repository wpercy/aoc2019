const start = 236491 
const end = 713787 

function check_value(v) {
  const parts = v.toString().split('');
  let hasDouble = false;

  for (let i=1; i<parts.length; i++) {
    const c = parts[i];
    if (Number(c) < Number(parts[i-1])) {
      return false;
    } else if (Number(c) == Number(parts[i-1])) {
      hasDouble = true;
    }
  };
  return hasDouble;
}

function check_value_2(v) {
  const parts = v.toString().split('');
  const counts = {};

  for (let i=1; i<parts.length; i++) {
    const c = parts[i];
    if (Number(c) < Number(parts[i-1])) {
      return false;
    } else if (Number(c) == Number(parts[i-1])) {
      counts[c] = counts[c] ? counts[c] + 1 : 1;
    }
  };
  return Object.values(counts).includes(1) 
}

let correct = 0;

for (let j=start; j<end; j++) {
    if (check_value(j)) {
      correct += 1;
    }
}

console.log(correct);
