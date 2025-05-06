# Casos de Prueba – GameZone

| ID   | Nombre del caso                    | Pasos                                                                 | Datos de prueba                           | Resultado esperado                             |
|------|------------------------------------|-----------------------------------------------------------------------|-------------------------------------------|------------------------------------------------|
| TC01 | Registro exitoso                   | 1. Ir a registro<br>2. Llenar formulario<br>3. Clic en 'Registrarse' | Correo: susana@mail.com<br>Pass: Susy1234 | Usuario registrado correctamente               |
| TC02 | Login con contraseña incorrecta    | 1. Ir a login<br>2. Ingresar datos<br>3. Clic en 'Iniciar sesión'    | Pass incorrecta                           | Error: "Contraseña incorrecta"                 |
| TC03 | Búsqueda de juego existente        | 1. Buscar "Mario Kart"                                               | Texto: Mario Kart                         | Juego aparece en los resultados                |
| TC04 | Agregar juego a favoritos          | 1. Buscar juego<br>2. Clic en favorito                               | -                                         | Juego se agrega y aparece en favoritos         |
| TC05 | Visualizar leaderboard             | 1. Ir a "Leaderboard"                                                | -                                         | Tabla de puntuaciones se muestra correctamente |
