function resize_quantity(url) {
    fetch(url, {
        method: 'GET'
    }).then(response => response.json()).then(data => {
        document.getElementById('resize_quantity').innerHTML = data.quantity
    })
}

function resize_data(url) {
    fetch(url, {
        method: 'GET'
    }).then(response => response.json()).then(data => {
        document.getElementById('resize_data').innerHTML = data.data
    })
}

function resize_products(url) {
    fetch(url, {
        method: 'GET'
    }).then(response => response.json()).then(data => {
        document.getElementById('resize_products').innerHTML = data.product
    })
}

function random_color(qtd = 1) {
    var bg_color = []
    var bbg_color = []
    for (let i = 0; i < qtd; i++) {
        let r = Math.random() * 255
        let g = Math.random() * 255
        let b = Math.random() * 255
        bg_color.push(`rgb(${r}, ${g}, ${b}, ${0, 2})`)
        bbg_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    return [bg_color, bbg_color]
}

function generate_expenses() {
    const ctx = document.getElementById('despesas').getContext('2d');
    var color_expense = random_color(qtd = 12)
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Janeiro', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            datasets: [{
                label: 'Despesas',
                data: [12, 19, 3, 5, 2, 3, 5, 2, 3, 5, 2, 3],
                backgroundColor: color_expense[0],
                borderColor: color_expense[1],
                borderWidth: 1
            }]
        },
    });
}

function generate_revenue(url) {
    fetch(url, {
        method: 'GET',
    }).then(function (result) {
        return result.json();
    }).then(function (data) {

        const ctx = document.getElementById('faturamento').getContext('2d');
        var color_revenue = random_color(qtd = 12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                    datasets: [{
                    label: 'Faturamento',
                    data: data.data,
                    backgroundColor: color_revenue[1],
                    borderColor: color_revenue[1],
                    borderWidth: 1
                }]
            },
        });
    });
}

function best_product(url) {
    fetch(url, {
        method: 'GET',
    }).then(function (result) {
        return result.json();
    }).then(function (data) {

        const ctx = document.getElementById('quantidade').getContext('2d');
        var color_product = random_color(qtd = 4)
        const myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                    datasets: [{
                    label: 'Faturamento',
                    data: data.data,
                    backgroundColor: color_product[1],
                    borderColor: color_product[1],
                    borderWidth: 1
                }]
            },
        });
    });
}

function best_seller(url) {
    fetch(url, {
        method: 'GET',
    }).then(function (result) {
        return result.json();
    }).then(function (data) {

        const ctx = document.getElementById('funcionario').getContext('2d');
        var color_seller = random_color(qtd = 4)
        const myChart = new Chart(ctx, {
            type: 'polarArea',
            data: {
                labels: data.labels,
                    datasets: [{
                    data: data.data,
                    backgroundColor: color_seller[1],
                    borderColor: color_seller[1],
                    borderWidth: 1
                }]
            },
        });
    });
}