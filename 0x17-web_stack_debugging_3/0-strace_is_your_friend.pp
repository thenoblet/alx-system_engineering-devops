# Define the file path as a variable

$file_path = '/var/www/html/wp-settings.php'
file { $file_path:
  ensure => file,
}

exec { 'replace_phpp_with_php':
  command     => "sed -i 's/phpp/php/g' ${file_path}",
  path        => ['/bin', '/usr/bin', '/usr/sbin/'],
  refreshonly => true,
  require     => File[$file_path],
}
