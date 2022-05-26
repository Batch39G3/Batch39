function add_row() {
    $rowno = $("#employee_table tr").length;
    $rowno = $rowno + 1;
    $("#employee_table tr:last").after("<tr id='row" + $rowno + "'><td><input type='text' name='name[]' placeholder='Enter Name'></td><td><input type='text' name='age[]' placeholder='Enter Age'></td><td><input type='text' name='job[]' placeholder='Enter Job'></td><td><input type='text' name='region[]' placeholder='Enter region'></td><td><input type='button' value='DELETE' onclick=delete_row('row" + $rowno + "')></td></tr>");
}

function delete_row(rowno) {
    $('#' + rowno).remove();
}