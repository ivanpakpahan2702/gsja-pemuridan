function Paging(
  PageNumber,
  PageSize,
  TotalRecords,
  ClassName,
  DisableClassName
) {
  var ReturnValue = "";
  var TotalPages = Math.ceil(TotalRecords / PageSize);

  if (+PageNumber > 1) {
    if (+PageNumber == 2) {
      ReturnValue =
        ReturnValue +
        "<li class='page-item'><a pn='" +
        (+PageNumber - 1) +
        "' class='page-link " +
        ClassName +
        "'>Sebelumnya</a></li>";
    } else {
      ReturnValue = ReturnValue + "<li class='page-item'><a pn='";
      ReturnValue =
        ReturnValue +
        (+PageNumber - 1) +
        "' class='page-link " +
        ClassName +
        "'>Sebelumnya</a></li>";
    }
  } else {
    ReturnValue =
      ReturnValue +
      "<li class='page-item " +
      DisableClassName +
      "'><a class='page-link'>Sebelumnya</a></li>";
  }

  if (+PageNumber - 3 > 1)
    ReturnValue =
      ReturnValue +
      "<li class='page-item'><a pn='1' class='page-link " +
      ClassName +
      "'>1</a></li><li class='page-item disabled dots'><a class='page-link disabled'>...</a></li>";

  for (var i = +PageNumber - 3; i <= +PageNumber; i++)
    if (i >= 1) {
      if (+PageNumber != i) {
        ReturnValue = ReturnValue + "<li class='page-item'><a pn='";
        ReturnValue =
          ReturnValue +
          i +
          "' class='page-link " +
          ClassName +
          "'>" +
          i +
          "</a></li>";
      } else {
        ReturnValue =
          ReturnValue +
          "<li class='page-item activePage disabled'><a class='page-link disabled'>" +
          i +
          "</a></li>";
      }
    }

  for (var i = +PageNumber + 1; i <= +PageNumber + 3; i++)
    if (i <= TotalPages) {
      if (+PageNumber != i) {
        ReturnValue = ReturnValue + "<li class='page-item'><a pn='";
        ReturnValue =
          ReturnValue +
          i +
          "' class='page-link " +
          ClassName +
          "'>" +
          i +
          "</a></li>";
      } else {
        ReturnValue =
          ReturnValue +
          "<li class='page-item activePage disabled'><a class='page-link disabled'>" +
          i +
          "</a></li>";
      }
    }

  if (+PageNumber + 3 < TotalPages) {
    ReturnValue =
      ReturnValue +
      "<li class='page-item disabled dots'><a class='page-link disabled'>...</a></li><li class='page-item'><a pn='";
    ReturnValue =
      ReturnValue +
      TotalPages +
      "' class='page-link " +
      ClassName +
      "'>" +
      TotalPages +
      "</a></li>";
  }

  if (+PageNumber < TotalPages) {
    ReturnValue = ReturnValue + "<li class='page-item'><a pn='";
    ReturnValue =
      ReturnValue +
      (+PageNumber + 1) +
      "' class='page-link " +
      ClassName +
      "'>Selanjutnya</a></li>";
  } else {
    ReturnValue =
      ReturnValue +
      "<li class='page-item " +
      DisableClassName +
      "'><a class='page-link'>Selanjutnya</a></li>";
  }

  return ReturnValue;
}
