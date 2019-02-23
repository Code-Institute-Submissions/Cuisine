//Javascript code that conditionally renders the dropdown field in the searh bar (in searchrecipes.html)
//When user chooses a search category (in the first dropdown field) the second dropdown is revealed, 
//with the search values matching the search field 


$(document).ready(function() {
    $(function() {
        $("#search_field").change(function() {
            var val = $(this).val();
            $("#hidden-until-clicked").children().hide()

            if (val === "author") {
                $("#author-input-field").toggle();

            }
            else if (val === "cooking_duration") {
                $("#cooking-duration-input-field").toggle();

            }
            else if (val === "cuisine_type") {
                $("#cuisine-type-input-field").toggle();

            }
            else if (val === "meal_type") {
                $("#meal-type-input-field").toggle();

            }
            else if (val === "serves") {
                $("#serves-input-field").toggle();

            }
        });
    });
});
