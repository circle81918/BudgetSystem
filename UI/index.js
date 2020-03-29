
window.onload = function(){
    const submitButton = document.querySelector('#submit');
    submitButton.addEventListener('click', clickcb);
}

async function clickcb(){
    
    const messageBox = document.getElementById("messageBox")
    messageBox.innerHTML = "Create Budget Success";
}