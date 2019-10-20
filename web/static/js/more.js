
// $(function(){ /* to make sure the script runs after page load */

//   $('a.read_more').click(function(event){ /* find all a.read_more elements and bind the following code to them */

//       event.preventDefault(); /* prevent the a from changing the url */
//       $(this).parents('.item').find('.more_text').show(); /* show the .more_text span */

//   });

// });



function myFunction(id) {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById(id);
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}

// function myFunc() {
//   var dots = document.getElementById("dots");
//   var moreText = document.getElementById('more_2');
//   var btnText = document.getElementById("myBtn");

//   if (dots.style.display === "none") {
//     dots.style.display = "inline";
//     btnText.innerHTML = "Read more";
//     moreText.style.display = "none";
//   } else {
//     dots.style.display = "none";
//     btnText.innerHTML = "Read less";
//     moreText.style.display = "inline";
//   }
// }