
$mysql_root = 'DB_MYSQL_REMOTE_USER=root';
$mysql_pass = 'DB_MYSQL_PASS=12345';

$kafka_topic_name = 'KAFKA_TOPIC_NAME=topic_test';
$kafka_group_name = 'KAFKA_GROUP_NAME=my-group-id';

$credentials_output_flag = $false;

function fill_def_credentials {
$global:credentials_output_flag = $true;

$content = "{0}" -f $mysql_pass;
Out-File -Encoding utf8 -FilePath .\db_container\.env -InputObject $content ;

$content = "{0} `n{1} `n{2}" -f $mysql_pass, $mysql_root, $kafka_topic_name;
Out-File -Encoding utf8 -FilePath .\api_container\.env -InputObject $content ;

$content = "{0} `n{1} `n{2} `n{3}" -f $mysql_pass, $mysql_root, $kafka_topic_name, $kafka_group_name;
Out-File -Encoding utf8 -FilePath .\consumer_container\.env -InputObject $content;

}

function fill_manual_credentials{

$pass_var_secured = Read-Host -assecurestring "Please enter your data-base password";
$topic_name_var = Read-Host 'Enter kafka topic name (note, that you can add and delete new topics in control-center interface)';
$group_name_var = Read-Host 'Enter kafka-consumer group name';

$bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($pass_var_secured)
$pass_var = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)

$mysql_pass = "DB_MYSQL_PASS={0}" -f $pass_var;
$kafka_topic_name = "KAFKA_TOPIC_NAME={0}" -f $topic_name_var;
$kafka_group_name = "KAFKA_GROUP_NAME={0}" -f $group_name_var;

$content = "{0}" -f $mysql_pass;
Out-File -Encoding utf8 -FilePath .\db_container\.env -InputObject $content ;

$content = "{0} `n{1} `n{2}" -f $mysql_pass, $mysql_root, $kafka_topic_name;
Out-File -Encoding utf8 -FilePath .\api_container\.env -InputObject $content ;

$content = "{0} `n{1} `n{2} `n{3}" -f $mysql_pass, $mysql_root, $kafka_topic_name, $kafka_group_name;
Out-File -Encoding utf8 -FilePath .\consumer_container\.env -InputObject $content;
}

function fill_env_credentials {

$credentials_command = Read-Host  "Want to use default credentials? (Y|N)";
if ($credentials_command -ieq 'Y'){
fill_def_credentials;
}
elseif($credentials_command -ieq 'N'){
fill_manual_credentials;
}

}

function all_in_one{

Write-Output "YES";

fill_env_credentials;

#cd .\kafka_container;
#docker-compose up -d;
#cd ..;
#cd .\db_container;
#docker-compose up -d;
#cd ..;
#cd .\api_container;
#docker-compose up -d;
#cd ..;
#cd .\consumer_container;
#docker-compose up -d;
#cd ..;
}

#start
cls;
$start = Read-Host 'Want to start all parts of this application on this machine? (Y|N)';

while($start -ne 'Y' -and $start -ne 'N'){
$start = Read-Host 'Want to start all parts of this application on this machine? (Y|N)';
}

if ($start -ieq 'Y'){
all_in_one;
if($credentials_output_flag){
$output =  "`nYour credentials: `n{0} `n{1} `n{2} `n{3}"-f $mysql_pass, $mysql_root, $kafka_topic_name, $kafka_group_name;
Write-Output $output;
}
$end = Read-Host 'Press "enter" to close';
}

elseif($start -ieq 'N'){
Write-Output "NO";

}

