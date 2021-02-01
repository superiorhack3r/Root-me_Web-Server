<?php
    if (isset($_GET['page'])) 
    {
        $page = $_GET['page'];
    } 
    else 
    {
        $page = "home";
    }

    $file = "includes/" . $page . ".php";
    //injection:  ww', 'r') == true or system('shell') and strpos('1
    //==> "strpos('includes/', ww', 'r') == true or system('cat .passwd') and strpos('1.php', '..') === false";
    assert("strpos('$file', '..') === false") or die("Detected hacking attempt!");
    
?>

