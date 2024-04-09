// === Task 1 ===
console.log("=== Task 1 ===");
function findAndPrint(messages, currentStation) {
  let stationIndexMap = [
    "Xiaobitan",
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xindian City Hall",
    "Xindian",
  ];
  //用戶的地點轉換成索引數字
  function transformCurrentStation(currentStation) {
    for (let [index, stationName] of stationIndexMap.entries()) {
      if (stationName === currentStation) {
        return parseInt(index);
      }
    }
    return null;
  }

  function transformMessageData(messages, stationIndexMap) {
    let nameAndStationNewData = {};
    Object.entries(messages).forEach(([person, description]) => {
      for (let [index, stationName] of stationIndexMap.entries()) {
        if (description.includes(stationName)) {
          if (!nameAndStationNewData[person]) {
            nameAndStationNewData[person] = [];
          }
          nameAndStationNewData[person] = parseInt(index);
        }
      }
    });
    return nameAndStationNewData;
  }
  // console.log(transformMessageData(messages, stationIndexMap));

  let stationIndexNewData = transformCurrentStation(currentStation);
  let friendsNewData = transformMessageData(messages, stationIndexMap);
  let closestFriend = null;
  let minDistance = Infinity;
  for (let friend in friendsNewData) {
    let stationIndex = friendsNewData[friend];
    let distance = Math.abs(stationIndex - stationIndexNewData);
    if (stationIndex === 0) {
      distance = Math.abs(17 - stationIndexNewData) + 1;
    } else if (stationIndexNewData === 0) {
      distance = Math.abs(stationIndex - 17) + 1;
    } else if (stationIndex === 0 && stationIndexNewData === 0) {
      distance = 0;
    } else {
      distance = Math.abs(stationIndex - stationIndexNewData);
    }

    if (distance < minDistance) {
      minDistance = distance;
      closestFriend = friend;
    }
  }
  return closestFriend;
}
const messages = {
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Leslie: "I'm at home near Xiaobitan station.",
  Vivian: "I'm at Xindian station waiting for you.",
};

console.log(findAndPrint(messages, "Wanlong")); // print Mary
console.log(findAndPrint(messages, "Songshan")); // print Copper
console.log(findAndPrint(messages, "Qizhang")); // print Leslie
console.log(findAndPrint(messages, "Ximen")); // print Bob
console.log(findAndPrint(messages, "Xindian City Hall")); // print Vivian

// === Task 2 ===
console.log("=== Task 2 ===");

function book(consultants, hour, duration, criteria) {
  let sortedConsultants = [...consultants];

  //優先度、排序
  if (criteria === "rate") {
    sortedConsultants.sort((a, b) => b.rate - a.rate);
  }
  if (criteria === "price") {
    sortedConsultants.sort((a, b) => a.price - b.price);
  }

  for (let consultant of sortedConsultants) {
    /*let matchedConsultant = consultantAvailability.find(
      (person) => person.name === consultant.name
    );*/
    let matchedConsultant = dictionary[consultant.name];
    //console.log(matchedConsultant);
    let isAvailable = true;

    for (let i = hour; i < hour + duration; i++) {
      if (!matchedConsultant.hour[i]) {
        isAvailable = false;
        break;
      }
    }
    if (isAvailable) {
      for (let i = hour; i < hour + duration; i++) {
        matchedConsultant.hour[i] = false;
      }
      return consultant.name;
    }
  }
  return "No service";
}

const consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];
let consultantAvailability = consultants.map((consultant) => ({
  name: consultant.name,
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
}));
let dictionary = {};
for (let i = 0; i < consultantAvailability.length; i++) {
  dictionary[consultantAvailability[i].name] = consultantAvailability[i];
}

console.log(book(consultants, 15, 1, "price")); // Jenny
console.log(book(consultants, 11, 2, "price")); // Jenny
console.log(book(consultants, 10, 2, "price")); // John
console.log(book(consultants, 20, 2, "rate")); // John
console.log(book(consultants, 11, 1, "rate")); // Bob
console.log(book(consultants, 11, 2, "rate")); // No Service
console.log(book(consultants, 14, 3, "price")); // John

// === Task 3 ===
console.log("=== Task 3 ===");

function func(...data) {
  let compareArr = [];
  let uniqueCount = 0;
  //將資料放入陣列中
  for (let x = 0; x < data.length; x++) {
    let charTocompare;
    if (data[x].length === 2 || data[x].length === 3) {
      charTocompare = data[x][1];
    } else {
      charTocompare = data[x][2];
    }
    compareArr.push({ name: data[x], char: charTocompare });
  }

  //陣列資料互相比較
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
