# Puppet manifest  that kills a process named killmenow

exec { 'killmenow':
command  => 'pkill -f killmenow',
onlyif   => '/usr/bin/pgrep -f killmenow',
provider => shell,
}
