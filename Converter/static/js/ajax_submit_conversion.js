$(document).ready(function () {
    $(".submit-btn").click(function (event) {
        event.preventDefault();
        $('.error').text('');
        $.ajax({
            type: 'POST',
            url: window.page_data.convert,
            data: {
                'number': $('#id_number').val(),
                csrfmiddlewaretoken: window.page_data.csrf
            },
            dataType: "json",
            success: function (response) {
                console.log(response);
                if (response.success === true) {
                    $('#id_result').val(response.result);
                }
                else if (response.err_code === 'invalid_form') {
                    $('.error').text(response.err_msg['number']);
                    $('#id_result').val('');
                }
            },
        });
    });
});