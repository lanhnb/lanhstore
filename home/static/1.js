$(document).ready(function(){
  $("#search_icon").bind("click",(function(){
    $(".fas.fa-search").css({"font-size": "150%"});

    $(".search-tt").toggle();
  }));
});
$(document).ready(function(){
  $("#search_icon1").bind("click",(function(){
    $(".fas.fa-search").css({"font-size": "150%"});

    $(".search-tt").toggle();
  }));
});

// When the user scrolls down 20px from the top of the document, slide down the navbar
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
}
//End Hide menu
function color(color) {
  document.forms[0].q.style.background = color;
}
function loadTime(){
    const d = new Date();
    //document.getElementById("demo").innerHTML = 30- d.getDate();
    document.getElementById("deals_timer1_hr").innerHTML = 24-  d.getHours() + " hour";
    document.getElementById("deals_timer1_min").innerHTML = d.getMinutes() + " minute";
    document.getElementById("deals_timer1_sec").innerHTML = d.getSeconds() + " second";

    document.getElementById("deals_timer2_hr").innerHTML = 24- d.getHours()+ " hour";
    document.getElementById("deals_timer2_min").innerHTML = d.getMinutes() + " minute";
    document.getElementById("deals_timer2_sec").innerHTML = d.getSeconds() + " second";

    document.getElementById("deals_timer3_hr").innerHTML = 24- d.getHours()+ " hour";
    document.getElementById("deals_timer3_min").innerHTML = d.getMinutes() + " minute";
    document.getElementById("deals_timer3_sec").innerHTML = d.getSeconds() + " second";}


