const elementoH1 = document.querySelector("h1");
console.log(elementoH1);
elementoH1.innerText = "Titulo H1";

const elementoUL = document.querySelector("ul");
console.log(elementoUL);
elementoUL.innerHTML = `
<li>Primeiro</li>
<li>Segundo</li>
<li>Terceiro</>
`


const elemLink = document.querySelector("a");
console.log(elemLink);
elemLink.innerText = "PROZ";

const elementoOL = document.querySelector("ol");
console.log(elementoOL)
elementoOL.innerHTML = `
<li><a href="https://pt-br.facebook.com/"> Facebook </a></li>
<li><a href="https://www.instagram.com/"> Instragram </a></li>
<li><a href="https://www.youtube.com/"> Youtube </a></li>
`