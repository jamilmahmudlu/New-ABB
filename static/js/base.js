function toggleDropdown() {
    var dropdown = document.getElementById("langDropdown");
    if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
    } else {
        dropdown.style.display = "block";
    }
}
var angleIcon = document.getElementById("angleIcon");

function toggleRotation() {
    angleIcon.classList.toggle("rotated");
}

document.querySelectorAll('.modalclose').forEach(item => {
    item.addEventListener('click', event => {
        const modalbox = item.parentElement.parentElement;
        modalbox.style.display = 'none';
    });
});


// document.addEventListener("DOMContentLoaded", function() {
//     var navbar = document.getElementById("navbar");
//     var sticky = navbar.offsetTop;

//     window.onscroll = function() {
//         if (window.pageYOffset > sticky) {
//             navbar.classList.add("sticky");
//         } else {
//             navbar.classList.remove("sticky");
//         }
//     };
// });




document.addEventListener('DOMContentLoaded', () => {
    const amount = document.getElementById('amount');
    const interest = document.getElementById('interest');
    const years = document.getElementById('years');
    
    const amountVal = document.getElementById('amount-val');
    const interestVal = document.getElementById('interest-val');
    const yearsVal = document.getElementById('years-val');

    const updateValues = () => {
        amountVal.textContent = amount.value;
        interestVal.textContent = interest.value;
        yearsVal.textContent = years.value;
        calculateResults();
    }

    const calculateResults = () => {
        const principal = parseFloat(amount.value);
        const monthlyInterest = parseFloat(interest.value * 0.01) / 12;
        const totalPayments = parseInt(years.value);

        const x = Math.pow(1 + monthlyInterest, totalPayments); //ayliq faizi toplam odeme sayisinin quvvetine yukseldirik
        const monthlyPayment = (principal * x * monthlyInterest) / (x - 1);//

        if (isFinite(monthlyPayment)) {
            document.getElementById('monthly-payment').innerText = monthlyPayment.toFixed(2); //yuvarlaqlasdirma
            document.getElementById('total-payment').innerText = (monthlyPayment * totalPayments).toFixed(2);
        } else {
            document.getElementById('monthly-payment').innerText = '0';
            document.getElementById('total-payment').innerText = '0';
        }
    }


    amount.addEventListener('input', updateValues);
    interest.addEventListener('input', updateValues);
    years.addEventListener('input', updateValues);

    updateValues();
});
function toggleCards() {
    const cards = document.querySelectorAll('.debet-card');
    const hiddenCards = document.querySelectorAll('.debet-card.hidden');
    const button = document.getElementById('toggle-button');
    
    if (hiddenCards.length > 0) {
        cards.forEach(card => card.classList.remove('hidden'));
        button.textContent = "Gizlət";
    } else {
        for (let i = 5; i < cards.length; i++) {
            cards[i].classList.add('hidden');
        }
        button.textContent = "Bütün kartlar";
    }
}

document.addEventListener('DOMContentLoaded', () => {
    toggleCards();
});

function hiddenCards() {
    const cards = document.querySelectorAll('.debet-card2');
    const hiddenCards = document.querySelectorAll('.debet-card2.hidden2');
    const button = document.getElementById('hidden-button');
    
    if (hiddenCards.length > 0) {
        cards.forEach(card => card.classList.remove('hidden2'));
        button.textContent = "Gizlət";
    } else {
        for (let i = 5; i < cards.length; i++) {
            cards[i].classList.add('hidden2');
        }
        button.textContent = "Bütün kartlar";
    }
}

document.addEventListener('DOMContentLoaded', () => {
    hiddenCards();
});
  
window.addEventListener("scroll", function() {
    var navbar1 = document.querySelector(".header1");
    var navbar2 = document.querySelector(".sticky-nav");
  
    if (window.scrollY > 0) {
      navbar1.classList.add("hidden");
      navbar2.style.marginTop = "-50px";

    } else {
      navbar1.classList.remove("hidden");
      navbar2.style.marginTop = "0";
    }
  });
  



var counter = 1;
setInterval(function(){
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if (counter > 6){
        counter = 1;
    }
}, 5000);

