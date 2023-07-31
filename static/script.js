
$('#otherCheckbox1').click(function() {
  $('#otherText1').toggle($('#otherCheckbox1').prop("checked"));
});

$('#otherCheckbox2').click(function() {
  $('#otherText2').toggle($('#otherCheckbox2').prop("checked"));
});

$('#otherCheckbox3').click(function() {
  $('#otherText3').toggle($('#otherCheckbox3').prop("checked"));
});

$('#otherCheckbox4').click(function() {
  $('#otherText4').toggle($('#otherCheckbox4').prop("checked"));
});

$('#otherCheckbox5').click(function() {
  $('#otherText5').toggle($('#otherCheckbox5').prop("checked"));
});

$('#otherCheckbox6').click(function() {
  $('#otherText6').toggle($('#otherCheckbox6').prop("checked"));
});

$('#otherCheckbox7').click(function() {
  $('#otherText7').toggle($('#otherCheckbox7').prop("checked"));
});

$(document).ready(function() {
  // Handle form submission
  $('#questionnaire').submit(function(event) {
    var isValid = true;

    // Iterate over each set of checkboxes (questions)
    $('[id^="checkbox"]').not('#checkboxGroupRiskFactors').each(function() {
      var checkboxes = $(this).find('input[type="checkbox"]');
      var isChecked = false;

      // Check if at least one checkbox is checked in the current set
      checkboxes.each(function() {
        if ($(this).prop('checked')) {
          isChecked = true;
          return false; // Exit the loop early
        }
      });

      // If no checkbox is checked, mark the set as invalid and show an error message
      if (!isChecked) {
        $(this).addClass('invalid');
        isValid = false;
      } else {
        $(this).removeClass('invalid');
      }
    });

    // Prevent form submission if any set of checkboxes is invalid
    if (!isValid) {
      event.preventDefault();
    }
  });

  // Show/hide the "Other" text input based on the "Other" checkbox selection
  $('[id^="otherCheckbox"]').change(function() {
    var otherTextId = $(this).attr('id').replace('otherCheckbox', 'otherText');
    $('#' + otherTextId).toggle(this.checked);
  });
});