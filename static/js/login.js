document.addEventListener("DOMContentLoaded", function (e) {

  var miForm = document.getElementById('loginForm');
  miForm.onsubmit = function (e) {
    e.preventDefault();
    const formData = new FormData(this); // Acceder a los elementos del formulario

    // Obtener los valores de los campos de entrada por su nombre
    const username = formData.get("username");
    const password = formData.get("password");

    fetch('/api-login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    })
      .then(response => response.json())
      .then(data => {
        console.log(data)

        localStorage.setItem('access_token', data.access_token);
        localStorage.setItem('user_id', data.user.id);
        localStorage.setItem('user_cedula', data.user.cedula);

        const token = localStorage.getItem('access_token');

        console.log(token)

        window.location.href = "/dashboard";
      });
  }
});