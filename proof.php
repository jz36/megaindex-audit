<?php
header("Content-Type: text/html; charset=utf-8");  
$methods = array();
$methods[] = "reindex_site";
$methods[] = "get_index";
$method = $methods[1];
$sites = array();
$sites[] = "biksileev.ru";
$sites[] = "marvel-gold.ru";
$sites[] = "russouvenir.ru";
$sites[] = "blog.biksileev.ru";

    $arr["email"] = "dmitriy@biksileev.ru";
    $arr["password"] = "NokiaN9777";
    $arr["method"] = "add_project";
    $arr["project"] = $sites[0];
    $arr["lr"][] = "225";


 $array = array();
                            $array["method"] = $method;
                            $array["output"] = "json";
                            $array["mode"] = "site";
                            $array["login"] = "dmitriy@biksileev.ru";
                            $array["password"] = "NokiaN9777";
                            $array["url"] = urlencode($sites[3]);
                            $array["target"] = ''; // Необязательный параметр если пустой, вернет дату последней индексации
                            $array["version_id"] = "1";
                            $content = file_get_contents("http://api.megaindex.ru/?".http_build_query($array));    
                            $json = json_decode($content);  
 
if(!empty($json->error)){
    echo $json->error;
}
if($method == $methods[1]){
$table .= "<br><br>РЕЗУЛЬТАТ:";
$table .= "<table border=1>";
$table .= "<tr>";
$table .= "<th>page</th>";
$table .= "<th>level</th>"; 
$table .= "<th>status</th>"; 
$table .= "<th>keywords</th>"; 
$table .= "<th>description</th>"; 
$table .= "<th>title</th>";
$table .= "<th>h1</th>"; 
$table .= "<th>chars</th>"; 
$table .= "<th>wc</th>"; 
$table .= "<th>quality</th>"; 
$table .= "<th>uniq_content</th>"; 
$table .= "<th>count_ls_to</th>"; 
$table .= "<th>count_ls_from</th>"; 
$table .= "<th>count_vs_to</th>"; 
$table .= "<th>count_vs_from</th>";                    
$table .= "</tr>";
      
foreach($json as $array){
    $table .= "<tr>";
      
    $table .= "<td>";
        $table .= $array->page;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->level;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->status;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->keywords;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->description;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->title;
    $table .= "</td>";  
      
    $table .= "<td>";
        foreach($array->h1 as $key => $element){       
            $table .= $element.'<br>';
        }
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->chars;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->wc;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->quality;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->uniq_content;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->count_ls_to;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->count_ls_from;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->count_vs_to;
    $table .= "</td>";

    $table .= "<td>";
        $table .= $array->count_vs_from;
    $table .= "</td>";
      
    $table .= "</tr>";
}
$table .= "</table>";
echo $table;
}
elseif(!empty($json->report)){
    echo $json->report;
    exit;
}