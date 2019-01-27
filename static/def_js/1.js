console.log('--------js log start-------------------')
var files
$('input[type=file]').change(function(e){
fn=e.target.files[0].name
$($(this).next()[0]).text(fn)
files = event.target.files
})

$('#sbt1').click(sbt1f)

function sbt1f(){console.log('1111111111111')


    var data = new FormData();
    $.each(files, function(key, value)
    {
        data.append(key, value);
    });

 $.ajax({
        url: 'submit.php?files',
        type: 'POST',
        data: data,
        cache: false,
        dataType: 'json',
        processData: false, // Don't process the files
        contentType: false, // Set content type to false as jQuery will tell the server its a query string request
        success: function(data, textStatus, jqXHR)
        {
            if(typeof data.error === 'undefined')
            {
                // Success so call function to process the form
                submitForm(event, data);
            }
            else
            {
                // Handle errors here
                console.log('ERRORS: ' + data.error);
            }
        },
        error: function(jqXHR, textStatus, errorThrown)
        {
            // Handle errors here
            console.log('ERRORS: ' + textStatus);
            // STOP LOADING SPINNER
        }
    })

}