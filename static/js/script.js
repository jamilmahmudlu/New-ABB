document.addEventListener('DOMContentLoaded', () => {
    const fromamountElement = document.querySelector('.amount');
    const convertedamountElement = document.querySelector('.convertedamount');
    const fromcurrencyElement = document.querySelector('.fromcurrency');
    const tocurrencyElement = document.querySelector('.tocurrency');
    const resultElement = document.querySelector('.result');

    const countries = [
        { code: "USD", name: "United States Dollar" },
        { code: "AZN", name: "Azerbaijan Manat" },
        { code: "EUR", name: "Euro" },
        { code: "RUB", name: "Rubl" }
    ];

    // Show countries from array in select tags
    countries.forEach(country => {
        const option1 = document.createElement('option');
        const option2 = document.createElement('option');

        option1.value = option2.value = country.code;
        option1.textContent = option2.textContent = `${country.code} (${country.name})`;
        fromcurrencyElement.appendChild(option1);
        tocurrencyElement.appendChild(option2);
    });

    // Select default tags
    fromcurrencyElement.value = "USD";
    tocurrencyElement.value = "AZN";

    // Function to get exchange rate using API
    const getExchangeRate = async () => {
        const amount = parseFloat(fromamountElement.value);
        const fromcurrency = fromcurrencyElement.value;
        const tocurrency = tocurrencyElement.value;
        resultElement.textContent = "Fetching Exchange Rates....";

        try {
            const response = await fetch(`https://api.exchangerate-api.com/v4/latest/${fromcurrency}`);
            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();
            const conversionRate = data.rates[tocurrency];
            if (typeof conversionRate === 'undefined') {
                resultElement.textContent = "Exchange rate data is not available for the selected currency.";
                convertedamountElement.value = "";
            } else {
                const convertedamount = (amount * conversionRate).toFixed(2);
                convertedamountElement.value = convertedamount;
                resultElement.textContent = `${amount} ${fromcurrency} = ${convertedamount} ${tocurrency}`;
            }
        } catch (error) {
            resultElement.textContent = "Error while fetching exchange rate.";
        }
    };

    // Fetch exchange rate when user inputs the amount
    fromamountElement.addEventListener('input', getExchangeRate);
    fromcurrencyElement.addEventListener('change', getExchangeRate);
    tocurrencyElement.addEventListener('change', getExchangeRate);

    // Initial fetch to populate the converted amount
    getExchangeRate();
});
