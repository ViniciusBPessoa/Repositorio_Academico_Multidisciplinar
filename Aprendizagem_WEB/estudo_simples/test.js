function clicando(){
    var but_2 = document.getElementById('tue');
    var recebendo = "Link FODA PARA CARALHO";
    but_2.innerHTML = recebendo
}
function tuezin(){
    window.location.href = 'https://www.youtube.com/watch?v=TKqa-ZXGKYA';
}

var inicio = 0

while (inicio < 10) {
    document.write("</br>O valor é: " + inicio);
    inicio++;
}

var nome = '';

if (localStorage.nome == null) {
    localStorage.nome = prompt('Qual é o seu nome?');
}

nome = localStorage.nome;

document.getElementById("inicio").innerHTML = nome;

function adcionar(...numeros){
    let total = numeros.reduce((total, numero) => {
        let soma = total + numero;
        return soma;
    });
}

  