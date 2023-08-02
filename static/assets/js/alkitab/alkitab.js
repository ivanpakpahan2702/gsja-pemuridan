$(function () {
  $("#search_verse").click(function () {
    $("#bibleModal").modal("show");
    links =
      "/alkitab/cari?search_verse=" +
      document.getElementById("kitab_field").value +
      "-" +
      document.getElementById("pasal_input_field").value +
      "-" +
      document.getElementById("ayat_input_field").value;
    console.log(links);
    $.ajax({
      url:
        "/alkitab/cari?search_verse=" +
        document.getElementById("kitab_field").value +
        " " +
        document.getElementById("pasal_input_field").value +
        " " +
        document.getElementById("ayat_input_field").value,
      beforeSend: function () {
        $("#bibleModalTitle").html('');
        $("#bibleModalBody").html('');
        $("#spinner-kontak").show();
      },
      success: function (data) {
        $("#spinner-kontak").hide();
        $("#bibleModalTitle").html(data[0]);
        $("#bibleModalBody").html(data[1]);
        console.log(data);
      },
    });
  });
});
