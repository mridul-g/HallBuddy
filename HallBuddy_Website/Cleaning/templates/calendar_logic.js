<script>
    const calendar = document.getElementById('calendar');
let currentDate = new Date();
let firstDayOfMonth, lastDayOfMonth;

function createCalendar(month, year) {
calendar.innerHTML = ''; // Clear previous calendar

const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

firstDayOfMonth = new Date(year, month, 1);
lastDayOfMonth = new Date(year, month + 1, 0);
const daysInMonth = lastDayOfMonth.getDate();
const startingDay = firstDayOfMonth.getDay(); // Day of the week for the 1st day

const monthYearHeader = document.createElement('div');
monthYearHeader.classList.add('month');
monthYearHeader.innerHTML = `
<span class="month-navigation" onclick="prevMonth()">&#60;</span>
<span>${monthNames[month]} ${year}</span>
<span class="month-navigation" onclick="nextMonth()">&#62;</span>
`;
calendar.appendChild(monthYearHeader);

const daysContainer = document.createElement('div');
daysContainer.classList.add('days');
calendar.appendChild(daysContainer);

for (const dayName of dayNames) {
const dayNameCell = document.createElement('div');
dayNameCell.classList.add('day-name');
dayNameCell.textContent = dayName;
daysContainer.appendChild(dayNameCell);
}

for (let i = 0; i < startingDay; i++) {
const emptyCell = document.createElement('div');
emptyCell.classList.add('date');
daysContainer.appendChild(emptyCell);
}

for (let i = 1; i <= daysInMonth; i++) {
const dateDiv = document.createElement('div');
dateDiv.classList.add('date');
dateDiv.textContent = i;
dateDiv.addEventListener('click', () => askCleaningStatus(i, month, year));
daysContainer.appendChild(dateDiv);
}
}


// Inside askCleaningStatus function

function askCleaningStatus(day, month, year) {
const response = confirm(`Has the room been cleaned on ${day}-${month + 1}-${year}?`);
const dateDivIndex = day + firstDayOfMonth.getDay() - 1;
const dateDiv = calendar.querySelectorAll('.date')[dateDivIndex];

if (response) {
dateDiv.classList.remove('red');
dateDiv.classList.add('green');
} else {
dateDiv.classList.remove('green');
dateDiv.classList.add('red');
}
}

createCalendar(currentDate.getMonth(), currentDate.getFullYear());

// Function to switch to the previous month
function prevMonth() {
currentDate.setMonth(currentDate.getMonth() - 1);
createCalendar(currentDate.getMonth(), currentDate.getFullYear());
}

// Function to switch to the next month
function nextMonth() {
currentDate.setMonth(currentDate.getMonth() + 1);
createCalendar(currentDate.getMonth(), currentDate.getFullYear());
}
</script>