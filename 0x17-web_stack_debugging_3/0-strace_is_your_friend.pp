# Define the file path as a variable
$file_path = '/var/www/html/wp-settings.php'

# Ensure the file exists before making changes
file { $file_path:
  ensure => file,
}

# Use exec to replace 'phpp' with 'php' in the file
exec { 'replace_phpp_with_php':
  command     => "/usr/bin/sed -i 's/phpp/php/g' ${file_path}",
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => File[$file_path],
}
