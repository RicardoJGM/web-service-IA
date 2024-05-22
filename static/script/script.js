document.querySelector(".btnSpam").addEventListener("click", function() {
    var isSpam = Math.random() > 0.5; 
    var percentage = Math.floor(Math.random() * 100);
    var resultText = isSpam ? `Spam (Confianza: ${percentage}%)` : `No es spam (Confianza: ${percentage}%)`;
    document.getElementById('result').innerText = resultText;
});
