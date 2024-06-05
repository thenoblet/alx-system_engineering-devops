# Define the file path as a variable
$file_path = '/var/www/html/wp-settings.php'

# Ensure the file exists before making changes
file { $file_path:
  ensure => file,
}

# Perform the replacement of 'phpp' with 'php' using augeas
augeas { 'replace_phpp_with_php':
  incl    => $file_path,
  lens    => 'Text.lns',
  changes => [
    "set *[contains(text(), 'phpp')]/text[.='phpp'] 'php'",
  ],
}

