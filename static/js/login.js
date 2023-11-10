document.addEventListener("DOMContentLoaded", function (e) {
  var miForm = document.getElementById('loginForm');
  miForm.onsubmit = function (e) {
    e.preventDefault();
    const formData = new FormData(this);

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

        if (data.code) {
          // Si la respuesta contiene un error
          // console.error("Error en la solicitud:", data.code, data.error);

          // Aquí puedes mostrar una alerta en la página, por ejemplo:
          const errorAlert = document.getElementById('error-alert');
          errorAlert.style.display = 'block';
          errorAlert.textContent = data.error;
        } else {
          // Si la respuesta es exitosa
          localStorage.setItem('access_token', data.access_token);
          localStorage.setItem('user_id', data.user.id);
          localStorage.setItem('user_cedula', data.user.cedula);
          const token = localStorage.getItem('access_token');
          window.location.href = "/dashboard";

        }
      })
      .catch(error => {
        // console.error('Error en la solicitud:', error);
        // Opcional: Muestra un mensaje de error genérico en caso de un fallo en la solicitud
        const errorAlert = document.getElementById('error-alert');
        errorAlert.style.display = 'block';
        errorAlert.textContent = 'Hubo un error en la solicitud.';
      });
  }
});
