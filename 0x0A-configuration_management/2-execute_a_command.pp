# kill a process with pill command

exec {'pkill':
  command => 'pkill -f killmenow',
  path    => 'usr/bin/:/usr/local/bin/:/bin/'
}
