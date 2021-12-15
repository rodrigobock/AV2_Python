$(function() {
    
    $.ajax({
        url: 'http://localhost:5000/listar_pessoas',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (pessoa) {
        for (var i in pessoa) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da pessoa
              '<td>' + pessoa[i].nome + '</td>' + 
              '<td>' + pessoa[i].email + '</td>' + 
              '<td>' + pessoa[i].cpf + '</td>' + 
              '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaPessoas').append(lin);
        }
    }
});