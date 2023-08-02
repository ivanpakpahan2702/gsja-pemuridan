// ======================================================================================
// Preloader
$(window).load(function () {
  $(".loader").delay(2000).fadeOut("slow");
  $("#overlayer").delay(2000).fadeOut("slow");
});
// ======================================================================================
// Struktur Organisasi
$(document).ready(function () {
  $("#id01").click(function () {
    $("#ModalBagan").modal("show");
  });
});
// ======================================================================================
//Thumbnail Text Blog
// $(window).load(function () {
//   var myDiv = $(".body-thumb");
//   myDiv.text("..." + myDiv.text().substring(10, 200) + "...");
// });
// ======================================================================================
// Blog
$(function () {
  $("#category_blog").click(function () {
    val = document.getElementById("category_field").value.length;
    if (val > 0) {
      console.log(val);
      links =
        "/blog/kategori/" +
        document.getElementById("category_field").value +
        "/1";
      window.location.href =
        "/blog/kategori/" +
        document.getElementById("category_field").value +
        "/1";
      console.log("links : " + links);
    } else {
      Swal.fire({
        title: "Kesalahan",
        text: "Kategori Harus Dipilih",
        icon: "error",
        confirmButtonText: "Tutup",
      });
    }
  });
});
$(function () {
  $("#search_blog").click(function () {
    val = document.getElementById("blog_slug").value.length;
    if (val > 0) {
      console.log(val);
      links = "/blog/cari/" + document.getElementById("blog_slug").value + "/1";
      window.location.href =
        "/blog/cari/" + document.getElementById("blog_slug").value + "/1";
      console.log("links : " + links);
    } else {
      Swal.fire({
        title: "Kesalahan",
        text: "Kata Kunci Harus Dimasukkan",
        icon: "error",
        confirmButtonText: "Tutup",
      });
    }
  });
});
$(function () {
  $("#all_blog").click(function () {
    window.location.href = "/blog";
    console.log("links : " + links);
  });
});
// ======================================================================================
// Kontak
$(function () {
  $("#Kirim_Pesan").click(function () {
    val01 = document.getElementById("Full_Name").value.length;
    val02 = document.getElementById("Email").value.length;
    val03 = document.getElementById("Message").value.length;
    if (val01 > 0 && val02 > 0 && val03 > 0) {
      console.log(val01);
      console.log(val02);
      console.log(val03);
      $.ajax({
        url:
          "/kontak/kirim?nama=" +
          document.getElementById("Full_Name").value +
          "&email=" +
          document.getElementById("Email").value +
          "&message=" +
          document.getElementById("Message").value,
        timeout: 10000,
        beforeSend: function () {
          $("#spinner-kontak").show();
          $("#Kirim_Pesan").prop('disabled', true);
        },
        success: function (data) {
          $("#Full_Name").val("");
          $("#Email").val("");
          $("#Message").val("");
          $("#spinner-kontak").hide();
          $("#notif-modal").modal("show");
          $("#notif-modal-title").html(data[0]);
          $("#notif-modal-body").html(data[1]);
          console.log(data);
          $("#Kirim_Pesan").prop('disabled', false);
        },
        error: function (x, t, m) {
          if (t === "timeout") {
            Swal.fire({
              title: "Kesalahan",
              text: "Periksa koneksi internet",
              icon: "error",
              confirmButtonText: "Tutup",
            });
            $("#spinner-kontak").hide();
            $("#Kirim_Pesan").prop('disabled', false);
          } else {
            alert(t);
          }
        }
      });
    } else {
      Swal.fire({
        title: "Kesalahan",
        text: "Semua Formulir Wajib Diisi",
        icon: "error",
        confirmButtonText: "Tutup",
      });
    }
  });
});
// ======================================================================================
// Komentar
$(function () {
  $("#send-comment").click(function () {
    val01 = document.getElementById("comment-author").value.length;
    val02 = ckeditor.getData().length;
    if (val01 > 0 && val02 > 0) {
      console.log(val01);
      console.log(val02);
      console.log(document.getElementById("comment-author").value);
      console.log(ckeditor.getData());
      console.log(id_blog);
      $.ajax({
        url: "/komen/kirim",
        data: {
          "comment-author": document.getElementById("comment-author").value,
          "comment-editor": ckeditor.getData(),
          "posting-id": id_blog,
        },
        beforeSend: function () {
          $("#spinner-kontak").show();
        },
        success: function (data) {
          $("#comment-author").val("");
          ckeditor.setData("");
          $("#spinner-kontak").hide();
          $("#komen-notif-modal").modal("show");
          $("#komen-notif-modal-title").html(data[0]);
          $("#komen-notif-modal-body").html(data[1]);
          console.log(data);
        },
      });
    } else {
      // window.alert("Formulir Tidak Boleh Kosong");
      Swal.fire({
        title: "Kesalahan",
        text: "Semua Formulir Wajib Diisi",
        icon: "error",
        confirmButtonText: "Tutup",
      });
    }
  });
});
