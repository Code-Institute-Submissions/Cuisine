//Javascript code required to initialize javascript components from Materialize 0.100.2



$(document).ready(function() {
    $(".button-collapse").sideNav();
    $('select').material_select();
    $('#modal1').modal();
    $('#modal2').modal();
    $('#modal3').modal();
    $('#modal4').modal();
    $('.parallax').parallax();
    $('.dropdown-inner-button').dropdown({ hover: true });
    $(".dropdown-button").dropdown({ hover: true });
    $(".dropdown-button-authors").dropdown();
    $(".dropdown-button-cooking-durations").dropdown();
    $(".dropdown-button-cuisine-types").dropdown();
    $(".dropdown-button-meal-types").dropdown();
    $(".dropdown-button-serves").dropdown();
});
