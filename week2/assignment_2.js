// === Task 2 ===
console.log("=== Task 2 ===");

function book(consultants, hour, duration, criteria) {
  let reservationTime = [
    {
      name: "John",
      hour: {
        9: true,
        10: true,
        11: true,
        12: true,
        13: true,
        14: true,
        15: true,
        16: true,
        17: true,
        18: true,
        19: true,
        20: true,
        21: true,
      },
    },
    {
      name: "Bob",
      hour: {
        9: true,
        10: true,
        11: true,
        12: true,
        13: true,
        14: true,
        15: true,
        16: true,
        17: true,
        18: true,
        19: true,
        20: true,
        21: true,
      },
    },
    {
      name: "Jenny",
      hour: {
        9: true,
        10: true,
        11: true,
        12: true,
        13: true,
        14: true,
        15: true,
        16: true,
        17: true,
        18: true,
        19: true,
        20: true,
        21: true,
      },
    },
  ];

  if (criteria === "rate") {
    consultants.sort((a, b) => b.rate - a.rate);
  }
  if (criteria === "price") {
    consultants.sort((a, b) => a.price - b.price);
  }
}
const consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];
book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

// === Task 3 ===
console.log("=== Task 3 ===");

function func(...data) {
  let compareArr = [];
  let uniqueCount = 0;
  //將資料放入物件中
  for (let x = 0; x < data.length; x++) {
    let charTocompare;
    if (data[x].length === 2 || data[x].length === 3) {
      charTocompare = data[x][1];
    } else {
      charTocompare = data[x][2];
    }
    compareArr.push({ name: data[x], char: charTocompare });
  }

  //物件資料互相比較
  for (let i = 0; i < compareArr.length; i++) {
    let count = 0;
    for (let j = 0; j < compareArr.length; j++) {
      if (compareArr[i].char === compareArr[j].char) {
        count++;
      }
    }
    if (count === 1) {
      uniqueCount++;
      return compareArr[i].name;
    }
  }
  if (uniqueCount === 0) {
    return "沒有";
  }
}
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安
console.log(func("彭大牆", "陳王明雅", "吳明"));
console.log(func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"));
console.log(func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"));
console.log(func("郭宣雅", "夏曼藍波安", "郭宣恆"));
// === Task 4 ===
console.log("=== Task 4 ===");

function getNumber(index) {
  let arr = [0];
  if (index === 0) {
    return 0;
  }
  for (let i = 1; i <= index; i++) {
    if (i % 3 === 0) {
      arr[i] = arr[i - 1] - 1;
    } else {
      arr[i] = arr[i - 1] + 4;
    }
  }
  return arr[index];
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
console.log(getNumber(1));
console.log(getNumber(5));
console.log(getNumber(10));
console.log(getNumber(30));
