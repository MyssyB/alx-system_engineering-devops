#This manifest installs a flask package using pip3

$deps = ['python3', 'python3-pip']
package {$deps:
ensure => 'installed',
}
exec {'install_flask':
command => '/usr/bin/pip3 install flask==2.1.0',
}

#class install_flask{
#package {'python3-pip':
#ensure => 'installed',
#}

#exec {'install_flask':
#command => '/usr/bin/pip3 install flask==2.1.0',
#unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
#require => Package['python3-pip']',
#}
#}

#include install_flask
