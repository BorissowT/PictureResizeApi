function all_in_one{
Write-Output "YES";
cd .\kafka_container;
docker-compose up -d;
cd ..;
cd .\db_container;
docker-compose up -d;
cd ..;
cd .\api_container;
docker-compose up -d;
cd ..;
cd .\consumer_container;
docker-compose up -d;
cd ..;
}

$start = Read-Host 'Want to start all of parts of this application on this machine? (Y|N)';
while($start -ne 'Y' -and $start -ne 'N'){
$start = Read-Host 'Want to start all of parts of this application on this machine? (Y|N)';
}
if ($start -ieq 'Y'){
all_in_one;
}
elseif($start -ieq 'N'){
Write-Output "NO";
}
