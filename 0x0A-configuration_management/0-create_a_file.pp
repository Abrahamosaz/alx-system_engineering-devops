# create a file /tmp

file {'school':
content => 'I love puppet',
group   => 'www-data',
mode    => '0744',
owner   => 'www-data',
path    => '/tmp/school',
}
