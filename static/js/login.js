// document.addEventListener('DOMContentLoaded', function () {
//     const loginForm = document.getElementById('login-form');
//     const message = document.getElementById('message');

//     loginForm.addEventListener('submit', function (e) {
//         e.preventDefault();
//         message.classList.add('hidden');

//         const usuario = document.getElementById('usuario').value;
//         const password = document.getElementById('password').value;

//         // Hacer una solicitud a la API con usuario y contraseña
//         fetch('https://olimpo.gentesplendor.com/api-trafico/login', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ usuario, password }),
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 // El inicio de sesión fue exitoso
//                 window.location.href = 'index.html'; // Redirigir a la página de inicio
//             } else {
//                 // Mostrar mensaje de error
//                 message.textContent = 'Inicio de sesión fallido. Verifica tus credenciales.';
//                 message.classList.remove('hidden');
//             }
//         })
//         .catch(error => {
//             // Mostrar mensaje de error en caso de fallo de la API
//             message.textContent = 'Ha ocurrido un error. Inténtalo de nuevo más tarde.';
//             message.classList.remove('hidden');
//         });
//     });
// });

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

        // // Obtén el elemento select por su ID
        // const select = document.getElementById("co");

        // // Recorre el arreglo de opciones con forEach y crea elementos option
        // data.forEach(function (opcion) {
        //   const option = document.createElement("option");
        //   option.value = opcion.f_id;  // El valor de la opción
        //   option.text = opcion.f_descripcion;   // El texto visible de la opción
        //   select.appendChild(option);  // Agrega la opción al select
        // });




      });


  }

});