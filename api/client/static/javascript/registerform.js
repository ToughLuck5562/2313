document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('register-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        var username = document.getElementById('register-form-username-input').value;

        fetch('https://ipinfo.io/json')
            .then(response => response.json())
            .then(ipInfo => {
                var userIP = ipInfo.ip;
                var data = { Username: username, UserIP: userIP };

                return fetch('https://bitnsfwofficial.vercel.app/register-account-api', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'X-Referer': 'bitnsfwoffical.vercel.app/register-account' },
                    body: JSON.stringify(data)
                });
            })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(error => { throw new Error(error); });
                }
                return response.json();
            })
            .then(result => {
                console.log('Success:', result);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});
