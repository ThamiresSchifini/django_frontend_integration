    $(document).ready(function() {

     var deleteBtn = $('.delete-btn');                          // seleciona o elemento no jquery
     var searchBtn = $('#search-btn');                           // lupa
     var searchForm = $('#search-form');                        // form = submit

     $(deleteBtn).on('click', function(e) {         // função ativa quando botão é clicado e parâmetro 'evento', js sabe qual evento tá acontecendo, evento default ativar o botão de delete
        e.preventDefault();                                   // impede o delete
        var delLink = $(this).attr('href');                              // consigo ver a tarefa que o usuário deletou = this(esse botão), e pega atributo href de link
        var result = confirm('Quer deletar esta tarefa?');

        if(result) {
            window.location.href = delLink;
            console.log('funcionou')
        }
     });
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});