// 獲取當下日期
const today = new Date();
let currentYear = today.getFullYear();
let currentMonth = today.getMonth();

// 生成月曆
function generateCalendar() {
    const calendarElement = document.getElementById('calendar');
    const currentMonthElement = document.getElementById('currentMonth');
    // 獲取當下月份的第一天
    const firstDay = new Date(currentYear, currentMonth, 1);
    // 獲取當下月份的最後一天
    const lastDay = new Date(currentYear, currentMonth + 1, 0).getDate();
    // 清空月曆
    calendarElement.innerHTML = '';
    // 添加星期幾
    const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    for (let i = 0; i < weekdays.length; i++) {
        const weekdayElement = document.createElement('div');
        weekdayElement.className = 'calendar__day calendar__weekday';
        weekdayElement.textContent = weekdays[i];
        calendarElement.appendChild(weekdayElement);
    }
    // 獲取當下月份的第一天是星期幾
    const firstDayOfWeek = firstDay.getDay();
    // 添加空白格子，使日期對應正確的星期幾
    for (let i = 0; i < firstDayOfWeek; i++) {
        const emptyDayElement = document.createElement('div');
        emptyDayElement.className = 'calendar__day calendar__empty';
        calendarElement.appendChild(emptyDayElement);
    }
    // 添加日期
    for (let i = 1; i <= lastDay; i++) {
        const dayElement = document.createElement('div');
        dayElement.className = 'calendar__day';
        dayElement.textContent = i;
        // 為日期添加點擊事件
        dayElement.addEventListener('click', function() {
            const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
            const currentDayOfWeek = weekdays[new Date(currentYear, currentMonth, i).getDay()];
            const paddedMonth = String(currentMonth + 1).padStart(2, '0');
            const paddedDay = String(i).padStart(2, '0');
            const link = 'https://ahsnccu-cim.github.io/lib-AMS/history/' + currentYear + '-' + paddedMonth + '-' + paddedDay + '%20' + currentDayOfWeek +'.html';
            window.location.href = link;
        });
        if (
            i === today.getDate() &&
            currentMonth === today.getMonth() &&
            currentYear === today.getFullYear()
        ) {
            dayElement.classList.add('current-day');
        }
        calendarElement.appendChild(dayElement);
    }
    // 更新當下月份顯示
    const currentMonthText = new Intl.DateTimeFormat('en', { month: 'long' }).format(firstDay);
    currentMonthElement.textContent = currentMonthText + ' ' + currentYear;
}

// 切換到上一個月份
function previousMonth() {
    currentMonth--;
    if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
    }
    generateCalendar();
}

// 切換到下一個月份
function nextMonth() {
    currentMonth++;
    if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
    }
    generateCalendar();
}

// 返回今天日期
function goToToday() {
    currentYear = today.getFullYear();
    currentMonth = today.getMonth();
    generateCalendar();
}

// 初始化月曆
generateCalendar();