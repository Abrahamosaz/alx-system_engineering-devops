# create a file

file {'tmp-file':
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I Love Puppet',
}
