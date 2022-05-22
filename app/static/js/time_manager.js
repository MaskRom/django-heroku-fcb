document.getElementById("day_timetable_1st").innerHTML = day_timetable[0];
document.getElementById("day_timetable_2st").innerHTML = day_timetable[1];
document.getElementById("day_timetable_3st").innerHTML = day_timetable[2];

setInterval('showClock1()',1000);
function showClock1() {
var DWs = new Array('日','月','火','水','木','金','土');
var Now = new Date();
var YY = Now.getYear();
if (YY < 2000) { YY += 1900; }
var MM = Now.getMonth() + 1 ;
var DD = set0( Now.getDate() );
var DW = DWs[ Now.getDay() ];
var hh = set0( Now.getHours() );
var mm = set0( Now.getMinutes() );
var ss = set0( Now.getSeconds() );
var RTime1 = ' ' + YY + '.' + MM + '.' + DD + ' ' + DW + ' ' + hh + ':' + mm + ':' + ss + ' ';
var header_time = MM + '月' + DD + '日(' + DW + ')';
var now_mm = Now.getMinutes() + (60 * hh);
var default_timer = [540, 585, 595, 640, 650, 695, 705, 750, 800, 845, 855, 900, 1440];
var status = status_num(now_mm, default_timer, DW);
var hour = [
`次の時間：${day_timetable[0]}`,
"1時間目 第一部",
`次の時間：${day_timetable[0]}`,
"1時間目 第二部",
`次の時間：${day_timetable[1]}`,
"2時間目 第一部",
`次の時間：${day_timetable[1]}`,
"2時間目 第二部",
`次の時間：${day_timetable[2]}`,
"3時間目 第一部",
`次の時間：${day_timetable[2]}`,
"3時間目 第二部",
"　",
"　",
];
var subject = [
"授業開始前",
day_timetable[0],
"休み時間",
day_timetable[0],
"休み時間",
day_timetable[1],
"休み時間",
day_timetable[1],
"昼休み",
day_timetable[2],
"休み時間",
day_timetable[2],
"放課後",
"休日"
];
document.getElementById("Clock1").innerHTML = hour[status[0]];
document.getElementById("header_time").innerHTML = header_time;
document.getElementById("subject").innerHTML = subject[status[0]];
document.getElementById("now_st").innerHTML = hour[status[0]];
document.getElementById("timer_2").innerHTML = (status[1] - now_mm) + "分";
//console.log("現在時刻 : " + RTime1);
//console.log("経過時間 : " + now_mm);
}



function set0(num) {
var ret = num;
if( num < 10 ) { ret = "0" + num; }
else { ret = num; }
return ret;
}



function status_num(s, t, d) {
    var ret;
    if(d === "土" || d === "日"){ret = [13, s]; }
    else{
        for(let i = 0; i < t.length; i++) {
            if(s < t[i]){ret = [i, t[i]];break; }
        }
        if (s >= 900){ret = [12, s]; }
    }
    return ret;
}