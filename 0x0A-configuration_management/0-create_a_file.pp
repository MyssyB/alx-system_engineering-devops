# This manifest creates a file in /tmp directory

file { '/tmp/school':
ensure  => 'file',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
