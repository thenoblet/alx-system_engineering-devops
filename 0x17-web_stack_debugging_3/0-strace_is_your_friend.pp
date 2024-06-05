# Puppet Manifest to replace 'phpp' with 'php' in wp-settings.php

$file_path='/var/www/html/wp-settings.php'
file { $file_path:
  ensure => file,
}

exec {'replace_phpp_with_php':
  path    => ['/bin/', '/usr/bin/', '/usr/sbin/'],
  command => "sed -i s/phpp/php/g ${file_path}",
  require => File[$file_path],
}
