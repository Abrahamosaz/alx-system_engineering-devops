# config ssh server for authentication to the remote server

file {'/home/abraham/.ssh/config':
  ensure => 'present',
  content => "IdentityFile ~/.ssh/school\nPasswordAthentication no",
} 
