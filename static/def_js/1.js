console.log('--------js log start-------------------')
var files
$('input[type=file]').change(function(e){
files = e.target.files
console.log(files)
if(typeof files === 'undefined' || files.length==0   )
{
console.log('changed file empty return')
return
}

if(files[0].size > 307200){
       alert("File is too big!")
       files=null
       return
}

fn=files[0].name
$($(this).next()[0]).text(fn)
})

$('#sbt1').click(sbt1f)



function sbt1f(){console.log('1111111111111')

if(files === null || typeof files === 'undefined' || files.length==0 )
{
console.log('submit file empty return')
return
}


console.log(files)

    var data = new FormData();
    $.each(files, function(k,v)
    {
        data.append('file', v);

        console.log(v)
        console.log('######3')
    });

//console.log(data)

 $.ajax({
        url: 'data-analyst/upload-file',
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
                //submitForm(event, data);
                console.log('success uploaded!')
                $('#returntext').text(data.filename)
                $('#exampleModalCenter').modal('show')
                console.log(data.filename)
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