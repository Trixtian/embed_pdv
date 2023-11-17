window.addEventListener("load", function () {

    var reportContainer = document.getElementById("report-container");
    powerbi.bootstrap(reportContainer, { type: "report" });

    var models = window["powerbi-client"].models;
    var reportLoadConfig = {
        type: "report",
        tokenType: models.TokenType.Embed,
    };

    fetch('/getembedinfo', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        //   body: JSON.stringify({ username, password }),
    })
        .then(response => response.json())
        .then(data => {
            

            reportLoadConfig.accessToken = data.accessToken;

            // You can embed different reports as per your need
            reportLoadConfig.embedUrl = data.reportConfig[0].embedUrl;

            // Use the token expiry to regenerate Embed token for seamless end user experience
            // Refer https://aka.ms/RefreshEmbedToken
            tokenExpiry = data.tokenExpiry;

            // Embed Power BI report when Access token and Embed URL are available
            var report = powerbi.embed(reportContainer, reportLoadConfig);

        });

    // Peticion para obtener los CO
    const token = localStorage.getItem('access_token');
    const user_id = localStorage.getItem('user_id');

    fetch('/get-co-list', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token, user_id }),
    })
        .then(response => response.json())
        .then(data => {
            // Obtén el elemento select por su ID
            const select = document.getElementById("co");

            // Recorre el arreglo de opciones con forEach y crea elementos option
            data.forEach(function (opcion) {
                const option = document.createElement("option");
                option.value = opcion.f_id;  // El valor de la opción
                option.text = opcion.f_descripcion;   // El texto visible de la opción
                select.appendChild(option);  // Agrega la opción al select
            });

        });
});

// Obtener el elemento select
const select = document.getElementById("co");

// Agregar un listener onchange al select
select.addEventListener("change", function () {
    // Obtener el valor seleccionado
    const filterValue = select.value;
    const reportContainer = document.getElementById('report-container');
    const report = powerbi.get(reportContainer);

    report.setFilters([{
        $schema: "http://powerbi.com/product/schema#basic",
        target: {
            table: 'centros_operaciones',
            column: 'centro_operaciones'
        },
        operator: 'In',
        values: [filterValue]
    }]);

});

// Obtener el elemento select
const logout = document.getElementById("logout");
logout.addEventListener('click', function () {
    // Eliminar un valor de localStorage
    localStorage.removeItem('access_token');
    localStorage.removeItem('user_id');
    localStorage.removeItem('user_cedula');
    window.location.href = "/";
});