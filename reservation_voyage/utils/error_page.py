error_page = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Page inaccessible</title>
    <style>
        .container {
            font-family: sans-serif, Arial;
            padding: 30px 20px 20px 20px;
            background-color: #fff;
            border-radius: 8px;
        }
        
        h1 {
           font-size: 32px;
           color: black;
           font-weight: 400;
        }
        
        p {
            font-size: 14px;
            margin-bottom: 20px;
            line-height: 1.5;
        }
        
        a {
            all: unset;
            text-decoration: none;
            color: #00e;
            cursor: pointer;
        }
        a:hover {
            text-decoration: underline;
            text-underline-offset: 2px;
        }
        .contact-info {
            margin-top: 30px;
            font-size: 1em;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Page inaccessible</h1>
        <p>
            Nous sommes désolés, mais la page que vous essayez d'atteindre est actuellement inaccessible.
            Cela peut être dû à une maintenance technique ou à un problème temporaire.
        </p>
        <p>
            Veuillez réessayer plus tard ou retourner à la <a href="/">page d'accueil</a>.
        </p>
        <div class="contact-info">
            <p>
                Si le problème persiste, n'hésitez pas à nous contacter à l'adresse suivante :
                <a href="mailto:allovoyage@gmail.com">allovoyage@gmail.com</a>.
            </p>
        </div>
    </div>
</body>
</html>
"""
