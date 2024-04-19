# 0x0A. Configuration Management

This project focuses on configuration management using Puppet. Puppet is a powerful tool for automating the configuration of systems, ensuring consistency across multiple machines, and simplifying the management of complex infrastructures.

## Requirements

### General
- All files will be interpreted on Ubuntu 20.04 LTS.
- All files should end with a new line.
- A `README.md` file at the root of the folder of the project is mandatory.
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Your Puppet manifests files must end with the extension `.pp`.

## Project Structure

The project is structured as follows:

./
│
├── README.md
├── 0x0A-configuration_management/
│ ├── 0-create_a_file.pp
│ ├── 1-install_a_package.pp
│ ├── 2-execute_a_command.pp
│ └── ...



## Contents

1. **0-create_a_file.pp**: This manifest creates a file at the path `/tmp/school` with specific permissions, owner, group, and content. The file is set to have permissions `0744`, owned by the user `www-data`, and belonging to the group `www-data`. Additionally, the content of the file is set to "I love Puppet". This manifest is useful for setting up a file with predefined properties on a system managed by Puppet.

2. **1-install_a_package.pp**: This manifest demonstrates how to use Puppet to install a package on the target system. It showcases the simplicity and power of Puppet in managing software installations.

3. **2-execute_a_command.pp**: This manifest illustrates how Puppet can be used to execute commands on the target system. This is useful for performing tasks such as running scripts or executing one-time configuration commands.

## Usage

To use these Puppet manifests, follow these steps:

1. Ensure you have Puppet installed on your system. If not, you can install it by following the instructions provided by Puppet Labs.
   
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/thenoblet/0x0A-configuration_management.git

