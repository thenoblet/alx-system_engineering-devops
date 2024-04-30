# Define a class for configuring custom HTTP response header
class custom_http_response_header {

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Define a file resource for custom Nginx configuration
file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure  => running,
    enable  => true,
  }
}

# Apply the custom_http_response_header class to the node
include custom_http_response_header

