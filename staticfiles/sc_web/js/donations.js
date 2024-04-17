$(document).ready(function () {
    // Update total amount when the page loads
    updateTotalAmount();

    // Update total amount when a donation level button is clicked
    $('.give-donation-level-btn').on('click', function () {
        var amount = $(this).val();
        $('#give-amount').val(amount);
        updateTotalAmount();
    });

    // Update total amount when the custom amount changes
    $('#give-amount').on('input', function () {
        updateTotalAmount();
    });

    function updateTotalAmount() {
        var customAmount = parseFloat($('#give-amount').val()) || 0;
        $('.give-final-total-amount').text(' $' + customAmount.toFixed(2));
    }
});
