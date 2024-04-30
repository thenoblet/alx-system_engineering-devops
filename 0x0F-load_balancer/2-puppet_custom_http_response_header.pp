# Define a class for configuring custom HTTP response header
class custom_http_response_header {

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Define a file resource for custom Nginx configuration
  file { '/etc/nginx/conf.d/custom_response_headers.conf':
    ensure  => present,
    content => "add_header X-Served-By ${facts['hostname']};",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}

# Apply the custom_http_response_header class to the node
include custom_http_response_header

