# This manifest kills a process
exec {'kill process':
command => '/usr/bin/pkill -x killmenow',
}
