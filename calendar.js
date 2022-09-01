const week = ["日", "月", "火", "水", "木", "金", "土"];//曜日を入れた配列を使う
const today = new Date();//現在の日付を取る

var showDate = new Date(today.getFullYear(), today.getMonth(), 1);
// 今月の１日を取得(月末だとずれる可能性があるため)
/*
Date(年,月,日,時,分,秒,ミリ秒)のかたちでミリ秒を指定できる。
日以降は省略可能で、その場合１日の0:00 0.000秒になる
*/
//APIで祝日を取得
const calendarId = 'ja.japanese#holiday@group.v.calendar.google.com'
const calendarApiUrl = 'https://www.googleapis.com/calendar/v3/calendars/'
const apiKey = 'APIキー'
 
/*function loadGoogleCalendarApi() {
  gapi.client.init({
    apiKey: apiKey,
  }).then(() => {
    return gapi.client.request({
      path: calendarApiUrl + encodeURIComponent(calendarId) + '/events'
    })
  }).then((res) => {
    const items = (res.result.items).reduce((a, c) => {
      a.push({date: c.start.date, summary: c.summary})
      return a
    }, []).sort((a, b) => {
      if (new Date(a.date) > new Date(b.date)) {
        return 1
      } else if (new Date(a.date) < new Date(b.date)) {
        return -1
      } else {
        return 0
      }
    })
    console.table(items)
  })
}
gapi.load('client', loadGoogleCalendarApi)*/

// 初期表示
window.onload = function () {
  //loadGoogleCalendarApi()
  showProcess(today, calendar);
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
function createProcess(year, month) {//カレンダーを作る関数
  var calendar = "<table><tr class='dayOfWeek'>";
  for (var i = 0; i < week.length; i++) {
    calendar += "<th>" + week[i] + "</th>";
  }
  calendar += "</tr>";//ここまでで表の見出しthタグとして曜日をかく

  var count = 0;//日付のカウント
  var startDayOfWeek = new Date(year, month, 1).getDay();//表示する月の1日の曜日
  var endDate = new Date(year, month + 1, 0).getDate();//表示する月の末日の曜日
  var lastMonthEndDate = new Date(year, month, 0).getDate();//表示する月の前の月の末日
  var row = Math.ceil((startDayOfWeek + endDate) / week.length);//カレンダーの行数

  // 1行ずつ設定
  for (var i = 0; i < row; i++) {
    calendar += "<tr>";//表のtrタグの始まりを作る。
    // 日付単位で設定
    for (var j = 0; j < week.length; j++) {
      if (i == 0 && j < startDayOfWeek) {
        // 1行目で1日まで先月の日付を設定(j<startDayOfWeekは１日の前までにするためにある)
        calendar += "<td class='disabled'>" + (lastMonthEndDate - startDayOfWeek + j + 1) + "</td>";
      } else if (count >= endDate) {
        // 最終行で最終日以降、翌月の日付を設定
        count++;
        calendar += "<td class='disabled'>" + (count - endDate) + "</td>";
      } else {
        // 当月の日付を曜日に照らし合わせて設定
        //今日かそうじゃないかで分けて入れる（色分けのため）
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