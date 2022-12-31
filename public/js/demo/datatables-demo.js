$(document).ready(function() {
    var a = $('#dataTable').DataTable({
      searching:true,
      dom: "<'row'<'col-sm-12 col-md-5'l><'col-sm-12 col-md-1'B>>" +
      "<'row'<'col-sm-12'tr>>" +
      "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
      buttons: [
        {
            text: 'My button',
            action: function ( e, dt, node, config ) {
                alert( 'Button activated' );
            }
        },

    ]
    });

} );