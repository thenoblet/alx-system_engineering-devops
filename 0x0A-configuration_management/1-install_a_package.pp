# Puppet manifest to install flask from pip3

package { 'flask':
ensure 	 => '2.1.0', # Ensure Flask version 2.1.0 is installed
provider => 'pip3',  # Specify the package provider as pip3
}
