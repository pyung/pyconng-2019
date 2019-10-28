window.addEventListener('load', function(){
  var day_2 =($('.day-2'))
  console.log(day_2)
  var day_3 =($('#day-3'))
  console.log(day_3)

  var day_4 =($('#day-4'))
  console.log(day_4)
  
  day_2.hide()  
  day_3.hide()
  day_4.hide()
});


$("#button_2").click(function(event){
  console.log("Clicked Button")
  var day_2_id =($('#day-2'))
  day_2_id.show()
  event.preventDefault()
})

$("#button_3").click(function(event){
  console.log("Clicked Button")
  var day_3_id =($('#day-3'))
  day_3_id.show()
  event.preventDefault()
})


$("#button_4").click(function(event){
  console.log("Clicked Button")
  var day_4_id =($('#day-4'))
  day_4_id.show()
  event.preventDefault()
})

