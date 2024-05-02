# Update package 
exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    => ['/usr/bin', '/bin'],
}

# Install the Nginx package 
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to add the custom HTTP header 
file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable  => true,
  require => Package['nginx'],
}
