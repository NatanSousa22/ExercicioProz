const titulo = document.createElement("h1");

titulo.id = "titulo";
titulo.innerText = "Loja de Jogos"

const body = document.querySelector("body");
body.appendChild(titulo);

const produto = document.createElement("div");
produto.innerHTML = `
    <div>
        <h2> Fight Games</h2>
        <p> Tekken 5 é um jogo de luta desenvolvido e publicado pela Namco em 2004 para Arcades, e em 2005 para PlayStation 2. É o sexto game da série Tekken, marcando o aniversário de dez anos desta última.</p>
        <p id="preco_jogo"> R$ 5.00</p>
    </div>
`

body.appendChild(produto)