document.getElementById('loginButton').addEventListener('click', function() {
    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;

    if (!login || !password) {
        showAlert('Proszę wypełnić wszystkie pola');
        return;
    }

    fetch('https://DORABANAbazaCIBUSanimae.com/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ login: login, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showAlert('Błędny login lub hasło');
        } else {
            console.log('Success:', data);
            localStorage.setItem('isLoggedIn', 'true'); // Set isLoggedIn to true
            window.location.href = 'profile.html'; // Redirect to profile page
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        showAlert('Błędny login lub hasło');
    });
});

function updateTopBar() {
    const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true'; // Retrieve isLoggedIn value
    const topBarButtons = document.getElementById('top-bar-buttons');
    topBarButtons.innerHTML = '';

    if (isLoggedIn) {
        topBarButtons.innerHTML += '<button onclick="location.href=\'profile.html\'">Profil</button>';
        topBarButtons.innerHTML += '<button onclick="location.href=\'logout.html\'">Wyloguj</button>';
        topBarButtons.innerHTML += '<button onclick="location.href=\'EkranWyszukiwania.html\'">Wyszukiwanie</button>';
    } else {
        topBarButtons.innerHTML += '<button onclick="location.href=\'about.html\'">O stronie</button>';
        topBarButtons.innerHTML += '<button onclick="location.href=\'EkranLogowania.html\'">Logowanie</button>';
    }
}

document.addEventListener('DOMContentLoaded', updateTopBar);

