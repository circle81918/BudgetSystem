
window.onload = function(){
    const submitButton = document.querySelector('#submit');
    submitButton.addEventListener('click', clickcb);
}


export default async function clickcb(){
    const date = document.querySelector('#date').value
    const budget = document.querySelector('#budget').value
    const messageBox = document.getElementById("messageBox")
    const budget_record = {date, budget}

    axios.post('/createBudget/', budget_record)
    .then(res=>{
        messageBox.innerHTML = res.data.message
    })
}