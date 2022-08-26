const week = ["日", "月", "火", "水", "木", "金", "土"];//曜日を入れた配列を使う
const today = new Date();//現在の日付を取る

var showDate = new Date(today.getFullYear(), today.getMonth(), 1);
// 今月の１日を取得(月末だとずれる可能性があるため)
/*
Date(年,月,日,時,分,秒,ミリ秒)のかたちでミリ秒を指定できる。
日以降は省略可能で、その場合１日の0:00 0.000秒になる
*/

// 初期表示
window.onload = function () {
  showProcess(today, calendar);
  /*ShowProcessは処理モーダル（モーダルは操作するまで親ウィンドウを操作できなくする小ウィンドウ）を表示する関数
  
  */
};

//window.onloadはHTMLが読み込まれてすぐに実行される関数
// 前の月表示(＜ボタン)
function prev() {
  showDate.setMonth(showDate.getMonth() - 1);
  showProcess(showDate);
}

// 次の月表示(＞ボタン)
function next() {
  showDate.setMonth(showDate.getMonth() + 1);
  showProcess(showDate);
}

// カレンダー表示
function showProcess(date) {
  var year = date.getFullYear();
  var month = date.getMonth();//１月が０で返されるので+1する必要あり
  document.getElementById('header').innerHTML = year + "年 " + (month + 1) + "月";
  /*
  querySelectorはidでもclassでも指定して要素受け取れる
  #〜ならidで、.〜ならclassで持ってこれる
  ただしquerySelectorは１つ目の要素しか持ってこれない
  ただ遅いから、idならgetElementById使ったほうがいいらしい
  ということで改変しました
  */

  var calendar = createProcess(year, month);
  document.getElementById('calendar').innerHTML = calendar;
}

// カレンダー作成
function createProcess(year, month) {
  // 曜日
  var calendar = "<table><tr class='dayOfWeek'>";
  for (var i = 0; i < week.length; i++) {
    calendar += "<th>" + week[i] + "</th>";
  }
  calendar += "</tr>";

  var count = 0;
  var startDayOfWeek = new Date(year, month, 1).getDay();
  var endDate = new Date(year, month + 1, 0).getDate();
  var lastMonthEndDate = new Date(year, month, 0).getDate();
  var row = Math.ceil((startDayOfWeek + endDate) / week.length);

  // 1行ずつ設定
  for (var i = 0; i < row; i++) {
    calendar += "<tr>";
    // 1colum単位で設定
    for (var j = 0; j < week.length; j++) {
      if (i == 0 && j < startDayOfWeek) {
        // 1行目で1日まで先月の日付を設定
        calendar += "<td class='disabled'>" + (lastMonthEndDate - startDayOfWeek + j + 1) + "</td>";
      } else if (count >= endDate) {
        // 最終行で最終日以降、翌月の日付を設定
        count++;
        calendar += "<td class='disabled'>" + (count - endDate) + "</td>";
      } else {
        // 当月の日付を曜日に照らし合わせて設定
        count++;
        if (year == today.getFullYear()
          && month == (today.getMonth())
          && count == today.getDate()) {
          calendar += "<td class='today'>" + count + "</td>";
        } else {
          calendar += "<td>" + count + "</td>";
        }
      }
    }
    calendar += "</tr>";
  }
  return calendar;
}