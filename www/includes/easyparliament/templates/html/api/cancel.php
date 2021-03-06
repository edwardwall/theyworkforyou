<section class="account-form">
    <h2>Cancel subscription</h2>

    <p>If you’re sure you wish to cancel your subscription at the end of its
    current month, please select the button below.</p>

    <form method="post" action="/api/cancel-plan">
        <?= \Volnix\CSRF\CSRF::getHiddenInputString() ?>
        <input name="cancel" type="submit" class="button alert" value="Cancel subscription">
    </form>
</section>
