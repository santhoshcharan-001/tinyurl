$(window).on("load", function () {
  $(".before-load").addClass("hide");
});
$(".only_form").submit(function (e) {
  e.preventDefault();
  $(".before-load").removeClass("hide");
  $.ajax({
    type: "GET",
    url: "/tiny/?q=" + $("#normal_url").val(),
    success: function (response) {
      $("input.given_response").val(response);
      $(".shorted-url-data").removeClass("hide");
      $(".before-load").addClass("hide");
      window.scrollBy(0, 1000);
    },
  });
});
function copy_text() {
  /* Get the text field */
  var copyText = document.getElementById("given_response");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  document.execCommand("copy");
}
