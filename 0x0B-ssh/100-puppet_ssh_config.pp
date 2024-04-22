# Define a Puppet manifest for managing SSH client configuration

# Define the SSH client configuration file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Define the content for the SSH client configuration
$ssh_config_content = @(EOF)
  Host *
      IdentityFile ~/.ssh/school
      PubKeyAuthentication yes
      PasswordAuthentication no
EOF

# Ensure the SSH client configuration file exists and has the correct content
file { $ssh_config_file:
  ensure  => file,
  content => $ssh_config_content,
  mode    => '0644',
}
