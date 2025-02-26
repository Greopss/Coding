<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page Keren</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }
        body {
            background-color: #121212;
            color: white;
            text-align: center;
        }
        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .menu {
            position: absolute;
            top: 20px;
            right: 20px;
            cursor: pointer;
            font-size: 24px;
        }
        .nav {
            display: none;
            position: absolute;
            top: 50px;
            right: 20px;
            background: rgba(255, 255, 255, 0.1);
            padding: 10px;
            border-radius: 5px;
        }
        .nav a {
            display: block;
            color: white;
            text-decoration: none;
            padding: 5px 0;
        }
        .nav.show {
            display: block;
        }
    </style>
</head>
<body>
    <div class="menu" onclick="toggleMenu()">☰</div>
    <div class="nav" id="nav">
        <a href="#">Home</a>
        <a href="#">Tentang</a>
        <a href="#">Kontak</a>
    </div>
    <div class="container">
        <h1>Welcome to My Web</h1>
        <p>Ini adalah landing page simpel tapi keren.</p>
    </div>

    <script>
        function toggleMenu() {
            document.getElementById("nav").classList.toggle("show");
        }
    </script>
</body>
</html>
