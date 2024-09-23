(function (win, doc) {
    'use strict';
    
    // Função para obter o valor do CSRF token dos cookies
    function getCookie(name) {
        let cookieValue = null;
        if (doc.cookie && doc.cookie !== '') {
            const cookies = doc.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Verifica se o cookie começa com o nome desejado
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    // Configurar o cabeçalho CSRF para todas as requisições AJAX
    function csrfSafeMethod(method) {
        // Métodos que não requerem CSRF
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    // Adiciona o CSRF token ao cabeçalho de requisições que precisam
    function setupCSRF(ajax) {
        if (!csrfSafeMethod(ajax.method) && !this.crossDomain) {
            ajax.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }

    // Confirmação de exclusão
    if (doc.querySelectorAll('.btnDel').length > 0) {
        const btnDel = doc.querySelectorAll('.btnDel');

        btnDel.forEach((button) => {
            button.addEventListener('click', (event) => {
                if (!confirm('Tem certeza que deseja apagar este dado?')) {
                    event.preventDefault();
                }
            });
        });
    }

    // Ajax do Form
    if (doc.querySelector('#form')) {
        let form = doc.querySelector('#form');
    
        form.addEventListener('submit', function(event) {
        event.preventDefault(); // Cancela o evento submit padrão do formulário
        sendForm(event);
        }, false);
    
        function sendForm(event) {
        let data = new FormData(form);
        let xhr = new XMLHttpRequest();
        xhr.open('POST', form.action, true);
        xhr.onload = function() {
            if (xhr.status === 200) {
            let result = doc.querySelector('#result');
            result.innerHTML = 'Operação realizada com sucesso!';
            result.classList.add('alert', 'alert-success');
            } else {
            let result = doc.querySelector('#result');
            result.innerHTML = 'Erro ao realizar a operação.';
            result.classList.add('alert', 'alert-danger');
            }
        };
        xhr.send(data);
        }
    }

})(window, document);
