<?php

$new_style_template = TRUE;

include_once '../../includes/easyparliament/init.php';
include_once INCLUDESPATH . 'easyparliament/member.php';

$alert = new MySociety\TheyWorkForYou\AlertView\Standard($THEUSER);
$data = $alert->display();

MySociety\TheyWorkForYou\Renderer::output('alert/index', $data);
